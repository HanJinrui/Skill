"""Glue between RAG pipeline and the Qwen code LLM.

Given a problem + `RAGContext`, returns `n` raw code samples along with the
retrieval trace (for later evaluation).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, replace
from typing import Any, Sequence

import numpy as np

from ..llm.base import CodeLLM
from ..logging_utils import get_logger
from ..rag.pipeline import RAGContext, build_generation_prompt, extract_query_from_problem
from ..rag.retrieve import RetrievalResult

LOG = get_logger(__name__)

_CODE_FENCE_RE = re.compile(r"```(?:python|py)?\s*\n(.*?)```", re.DOTALL | re.IGNORECASE)


def _effective_routing_confidence(schema: dict[str, Any]) -> float | None:
    """Prefer query_analyzer's routing_confidence; accept legacy router_confidence."""
    rc = schema.get("routing_confidence")
    if isinstance(rc, (int, float)):
        return float(rc)
    rc = schema.get("router_confidence")
    if isinstance(rc, (int, float)):
        return float(rc)
    return None


def _is_graph_rag_mode(mode: str) -> bool:
    return mode in {"graph", "graph_subtype_rag"}


def _skill_level(skill: dict[str, Any]) -> str:
    raw = str(skill.get("skill_level") or "").strip().lower()
    sid = str(skill.get("skill_id") or "")
    if raw:
        return raw
    if sid.startswith("subtype__"):
        return "subtype"
    if sid.startswith("family__"):
        return "family"
    if skill.get("scope") == "multi":
        return "bundle"
    return ""


def _is_subtype_skill(skill: dict[str, Any]) -> bool:
    return _skill_level(skill) == "subtype" or str(skill.get("skill_id") or "").startswith("subtype__")


def _is_family_skill(skill: dict[str, Any]) -> bool:
    return _skill_level(skill) == "family" or str(skill.get("skill_id") or "").startswith("family__")


def _skill_families(skill: dict[str, Any]) -> set[str]:
    fams = skill.get("families") or skill.get("family_set") or []
    out = {str(x).strip() for x in fams if isinstance(x, str) and str(x).strip()}
    fam = skill.get("family")
    if isinstance(fam, str) and fam.strip():
        out.add(fam.strip())
    return out


def _schema_cosine_at(schema: dict[str, Any], skill_index: int) -> float | None:
    cosl = schema.get("post_rerank_cosines") or []
    if not isinstance(cosl, list) or skill_index < 0 or skill_index >= len(cosl):
        return None
    try:
        return float(cosl[skill_index])
    except (TypeError, ValueError):
        return None


def _graph_hybrid_enabled(rag_ctx: RAGContext) -> bool:
    raw = getattr(rag_ctx, "graph_hybrid", None) or {}
    return isinstance(raw, dict) and bool(raw.get("enabled", False))


def _graph_hybrid_float(rag_ctx: RAGContext, key: str, default: float) -> float:
    raw = getattr(rag_ctx, "graph_hybrid", None) or {}
    if isinstance(raw, dict) and raw.get(key) is not None:
        try:
            return float(raw[key])
        except (TypeError, ValueError):
            return default
    return default


def _graph_hybrid_bool(rag_ctx: RAGContext, key: str, default: bool) -> bool:
    raw = getattr(rag_ctx, "graph_hybrid", None) or {}
    if isinstance(raw, dict) and raw.get(key) is not None:
        return bool(raw[key])
    return default


def _graph_hybrid_skill_allowed(
    *,
    retrieved: RetrievalResult,
    skill_index: int,
    rag_ctx: RAGContext,
    scope: str | None,
) -> tuple[bool, str]:
    schema = dict(getattr(retrieved, "query_schema", {}) or {})
    if skill_index < 0 or skill_index >= len(retrieved.skills):
        return False, "missing_skill"
    if "no_matching_subtype_candidate" in set(schema.get("graph_risk_flags") or []):
        return False, "no_matching_subtype_candidate"
    skill = retrieved.skills[skill_index]
    is_subtype = _is_subtype_skill(skill)
    is_family_aux = (
        skill_index > 0
        and _graph_hybrid_bool(rag_ctx, "allow_family_aux", False)
        and _is_family_skill(skill)
    )
    if skill_index == 0 and not is_subtype:
        return False, f"non_subtype_primary:{_skill_level(skill) or 'unknown'}"
    if not is_subtype and not is_family_aux:
        return False, f"non_subtype_skill:{_skill_level(skill) or 'unknown'}"

    cand_fams = [str(x).strip() for x in (schema.get("candidate_families") or []) if str(x).strip()]
    cand_set = set(cand_fams)
    skill_fams = _skill_families(skill)
    if is_subtype and cand_set and not (skill_fams & cand_set):
        return False, "subtype_family_mismatch"
    if is_family_aux and cand_set and not (skill_fams & cand_set):
        return False, "family_aux_mismatch"
    strict_multi = str(scope or "").strip().lower() == "multi" or bool(schema.get("is_multi_skill_likely"))
    strict_primary = _graph_hybrid_bool(rag_ctx, "strict_primary_family_for_multi", True)
    if (
        strict_primary
        and is_subtype
        and strict_multi
        and len(cand_fams) > 1
        and cand_fams[0] not in skill_fams
    ):
        return False, "multi_not_primary_family"

    min_router = _graph_hybrid_float(rag_ctx, "min_router_confidence", 0.38)
    min_margin = _graph_hybrid_float(rag_ctx, "min_score_margin_graph", 0.08)
    min_rel = _graph_hybrid_float(rag_ctx, "min_score_relative_graph", 0.20)
    min_cos = _graph_hybrid_float(rag_ctx, "min_dense_relevance_cosine", 0.50)

    rc = _effective_routing_confidence(schema)
    if rc is not None and rc < min_router:
        return False, f"low_router:{rc:.4f}<{min_router:.4f}"
    margin = float(schema.get("score_margin") or 0.0)
    if margin < min_margin:
        return False, f"low_margin:{margin:.4f}<{min_margin:.4f}"
    rel = float(schema.get("score_relative") or 0.0)
    if rel < min_rel:
        return False, f"low_relative:{rel:.4f}<{min_rel:.4f}"
    cos = _schema_cosine_at(schema, skill_index)
    if cos is None:
        return False, "missing_dense_cosine"
    if cos < min_cos:
        return False, f"low_dense:{cos:.4f}<{min_cos:.4f}"
    return True, "ok"


def _skill_format_tier_for_index(
    schema: dict[str, Any],
    skill_index: int,
    rag_ctx: RAGContext,
) -> str:
    """Shorter skill cards when dense problem↔skill cosine is below configured cutoffs."""
    cosl = schema.get("post_rerank_cosines") or []
    if not isinstance(cosl, list) or skill_index < 0 or skill_index >= len(cosl):
        return "full"
    try:
        c = float(cosl[skill_index])
    except (TypeError, ValueError):
        return "full"
    if rag_ctx.skill_cosine_minimal_below > 0.0 and c < rag_ctx.skill_cosine_minimal_below:
        return "minimal"
    if rag_ctx.skill_cosine_compact_below > 0.0 and c < rag_ctx.skill_cosine_compact_below:
        return "compact"
    return "full"


def _difficulty_gate_overrides(rag_ctx: RAGContext, difficulty_bucket: str | None) -> dict[str, Any]:
    raw = getattr(rag_ctx, "gates_by_difficulty", None) or {}
    if not difficulty_bucket or not isinstance(raw, dict):
        return {}
    key = str(difficulty_bucket).strip().lower()
    ent = raw.get(key)
    return dict(ent) if isinstance(ent, dict) else {}


def _problem_top_skill_cosine(
    rag_ctx: RAGContext,
    problem_statement: str,
    retrieved: RetrievalResult,
) -> float | None:
    """Cosine similarity between problem text and top skill summary (normalized BGE)."""
    enc = getattr(rag_ctx.retriever, "_encode", None)
    if not callable(enc) or not retrieved.skills:
        return None
    q = extract_query_from_problem(problem_statement)
    qv = enc(q)
    if qv is None or getattr(qv, "size", 1) == 0:
        return None
    sk = retrieved.skills[0]
    parts = [
        str(sk.get("skill_name") or ""),
        str(sk.get("core_idea") or ""),
        " ".join((sk.get("applicable_when") or [])[:4]),
    ]
    stext = " ".join(p for p in parts if p).strip()[:2500]
    if not stext:
        return None
    sv = enc(stext)
    if sv is None or getattr(sv, "size", 1) == 0:
        return None
    return float(np.dot(np.asarray(qv, dtype=np.float64).ravel(), np.asarray(sv, dtype=np.float64).ravel()))


def _reorder_retrieval_for_router_families(
    retrieved: RetrievalResult,
    cand_fams: list[str],
) -> RetrievalResult:
    """If rank-1 skill families miss router candidate_families, promote first matching skill."""
    cand_set = {str(x).strip() for x in cand_fams if isinstance(x, str) and str(x).strip()}
    if not cand_set or not retrieved.skills:
        return retrieved
    skills = list(retrieved.skills)
    ids = list(retrieved.skill_ids)
    scores = list(retrieved.scores)
    for j, skill in enumerate(skills):
        s_fam = set(skill.get("families") or []) | set(skill.get("family_set") or [])
        if s_fam and (s_fam & cand_set):
            if j == 0:
                return retrieved
            order = [j] + [k for k in range(len(skills)) if k != j]
            new_skills = [skills[k] for k in order]
            new_ids = [ids[k] for k in order] if len(ids) == len(skills) else ids
            new_scores = [scores[k] for k in order] if len(scores) == len(skills) else scores
            new_schema = dict(getattr(retrieved, "query_schema", {}) or {})
            pcs = list(new_schema.get("post_rerank_cosines") or [])
            if pcs and len(pcs) == len(skills) and len(new_ids) == len(new_skills):
                sid_to_cos = {str(ids[k]): float(pcs[k]) for k in range(len(skills))}
                new_schema["post_rerank_cosines"] = [
                    sid_to_cos.get(str(sk.get("skill_id")), 0.0) for sk in new_skills
                ]
                if new_schema["post_rerank_cosines"]:
                    new_schema["post_rerank_top1_cosine"] = float(
                        new_schema["post_rerank_cosines"][0]
                    )
            reord_ev: list[dict[str, Any]] = []
            old_ev = list(getattr(retrieved, "graph_evidence", []) or [])
            for sk in new_skills:
                sid = str(sk.get("skill_id") or "")
                hit = next(
                    (e for e in old_ev if str(e.get("skill_id") or "") == sid),
                    None,
                )
                if hit is None:
                    reord_ev = []
                    break
                reord_ev.append(hit)
            use_ev = reord_ev if len(reord_ev) == len(new_skills) else old_ev
            return replace(
                retrieved,
                skills=new_skills,
                skill_ids=new_ids,
                scores=new_scores,
                query_schema=new_schema,
                graph_evidence=use_ev,
            )
    return retrieved


def extract_python_code(text: str) -> str:
    """Return the code inside the first ```python``` fence; fallback to trimmed text."""
    if not text:
        return ""
    m = _CODE_FENCE_RE.search(text)
    if m:
        return m.group(1).strip()
    # tolerate models that forget the fence
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = stripped.strip("`").strip()
        if stripped.lower().startswith("python"):
            stripped = stripped[6:].lstrip()
    return stripped


@dataclass
class GenerationTrace:
    retrieved_skill_ids: list[str]
    retrieved_skills: list[dict[str, Any]]
    retrieval_scores: list[float]
    retrieval_method: str
    dense_ids: list[str]
    bm25_ids: list[str]
    raw_completions: list[str]
    extracted_codes: list[str]
    # Graph-specific trace fields (empty in flat mode).
    bundle_type: str = ""
    graph_evidence: list[dict[str, Any]] | None = None
    seed_ids: dict[str, list[str]] | None = None
    supporting_prototypes: list[str] | None = None
    matched_signals: list[str] | None = None
    matched_mechanisms: list[str] | None = None
    query_schema: dict[str, Any] | None = None
    fallback_to_no_rag: bool = False
    fallback_reason: str = ""
    dense_relevance_cosine: float | None = None
    dense_gate_bare_sample0: bool = False
    sample_prompt_modes: list[str] | None = None
    sample_skill_indices: list[int | None] | None = None
    sample_retrieved_skill_ids: list[list[str]] | None = None
    sample_retrieved_skills: list[list[dict[str, Any]]] | None = None
    sample_retrieval_scores: list[list[float]] | None = None
    graph_risk_flags: list[str] | None = None
    selected_skill_level: str = ""
    pre_rerank_skill_ids: list[str] | None = None
    post_rerank_skill_ids: list[str] | None = None


def generate_with_rag(
    *,
    code_llm: CodeLLM,
    rag_ctx: RAGContext,
    problem_statement: str,
    n_samples: int,
    seed_base: int = 0,
    first_sample_temperature: float | None = None,
    first_sample_top_p: float | None = None,
    later_sample_temperature: float | None = None,
    later_sample_top_p: float | None = None,
    per_sample_skill_index: bool = False,
    per_sample_skill_max_index: int | None = None,
    fn_name: str | None = None,
    family_hints: Sequence[str] | None = None,
    difficulty_bucket: str | None = None,
    retrieve_top_k_override: int | None = None,
    scope: str | None = None,
) -> GenerationTrace:
    dgo = _difficulty_gate_overrides(rag_ctx, difficulty_bucket)
    min_router = (
        float(dgo["min_router_confidence"])
        if "min_router_confidence" in dgo
        else rag_ctx.min_router_confidence
    )
    min_margin = (
        float(dgo["min_score_margin_graph"])
        if "min_score_margin_graph" in dgo
        else rag_ctx.min_score_margin_graph
    )
    min_rel = (
        float(dgo["min_score_relative_graph"])
        if "min_score_relative_graph" in dgo
        else rag_ctx.min_score_relative_graph
    )
    min_dense = (
        float(dgo["min_dense_relevance_cosine"])
        if "min_dense_relevance_cosine" in dgo
        else rag_ctx.min_dense_relevance_cosine
    )
    max_skill_budget = rag_ctx.max_skill_tokens
    if dgo.get("max_skill_tokens") is not None:
        try:
            max_skill_budget = max(32, int(float(dgo["max_skill_tokens"])))
        except (TypeError, ValueError):
            max_skill_budget = rag_ctx.max_skill_tokens

    retrieved = rag_ctx.retrieve(
        problem_statement,
        family_hints=family_hints,
        top_k_override=retrieve_top_k_override,
    )
    retrieval_trace = retrieved
    fallback_to_no_rag = False
    fallback_reason = ""
    if retrieved:
        if rag_ctx.try_alternate_skill_on_family_mismatch:
            _sch = dict(getattr(retrieved, "query_schema", {}) or {})
            _cf = list(_sch.get("candidate_families") or [])
            if _cf:
                retrieved = _reorder_retrieval_for_router_families(retrieved, _cf)
        retrieval_trace = retrieved
        schema = dict(getattr(retrieved, "query_schema", {}) or {})
        cand_fams = list(schema.get("candidate_families") or [])
        is_graph = _is_graph_rag_mode(rag_ctx.mode)

        if not retrieved.skills:
            fallback_to_no_rag = True
            fallback_reason = "empty_retrieved_skills"
        elif not cand_fams:
            fallback_to_no_rag = True
            fallback_reason = "empty_candidate_families"
        else:
            rc = _effective_routing_confidence(schema)
            if (
                min_router > 0.0
                and rc is not None
                and rc < min_router
            ):
                fallback_to_no_rag = True
                fallback_reason = f"low_routing_confidence:{rc:.4f}<{min_router:.4f}"

            if not fallback_to_no_rag and retrieved.skills:
                top_skill = retrieved.skills[0]
                skill_fams = set(top_skill.get("families") or []) | set(top_skill.get("family_set") or [])
                cand_set = set(cand_fams)
                if skill_fams and cand_set and not (skill_fams & cand_set):
                    fallback_to_no_rag = True
                    fallback_reason = (
                        f"family_mismatch:skill={sorted(skill_fams)} vs cand={sorted(cand_set)}"
                    )

            if not fallback_to_no_rag and is_graph:
                margin = float(schema.get("score_margin") or 0.0)
                rel = float(schema.get("score_relative") or 0.0)
                if (
                    min_margin > 0.0
                    and margin < min_margin
                ):
                    fallback_to_no_rag = True
                    fallback_reason = (
                        f"low_graph_score_margin:{margin:.4f}<{min_margin:.4f}"
                    )
                elif (
                    min_rel > 0.0
                    and rel < min_rel
                ):
                    fallback_to_no_rag = True
                    fallback_reason = (
                        f"low_graph_score_relative:{rel:.4f}<{min_rel:.4f}"
                    )

            if not fallback_to_no_rag and not is_graph:
                top_score = float((retrieved.scores or [0.0])[0] or 0.0)
                very_low_threshold = rag_ctx.min_retrieval_score * float(
                    rag_ctx.very_low_score_ratio or 0.6
                )
                if rag_ctx.min_retrieval_score > 0.0 and top_score < rag_ctx.min_retrieval_score:
                    fallback_to_no_rag = True
                    fallback_reason = (
                        f"low_retrieval_score:{top_score:.4f}<{rag_ctx.min_retrieval_score:.4f}"
                    )
                elif rag_ctx.min_retrieval_score > 0.0 and top_score < very_low_threshold:
                    fallback_to_no_rag = True
                    fallback_reason = (
                        f"very_low_retrieval_score:{top_score:.4f}<{very_low_threshold:.4f}"
                    )
    if fallback_to_no_rag:
        LOG.info("RAG fallback to no-rag prompt: %s", fallback_reason)
        retrieved = None

    dense_cos: float | None = None
    dense_gate_bare = False
    if retrieved is not None and min_dense > 0.0:
        sch_dense = dict(getattr(retrieved, "query_schema", {}) or {})
        pr = sch_dense.get("post_rerank_top1_cosine")
        pcs = sch_dense.get("post_rerank_cosines") or []
        if isinstance(pr, (int, float)) and isinstance(pcs, list) and len(pcs) > 0:
            dense_cos = float(pr)
        else:
            dense_cos = _problem_top_skill_cosine(rag_ctx, problem_statement, retrieved)
        if dense_cos is not None and dense_cos < min_dense:
            if rag_ctx.bare_sample0_on_dense_gate_fail:
                dense_gate_bare = True
                LOG.info(
                    "Dense relevance gate (bare sample0): cos=%.4f < %.4f — r1+ keep skills",
                    dense_cos,
                    min_dense,
                )
            else:
                fallback_to_no_rag = True
                fallback_reason = (
                    f"low_dense_relevance:{dense_cos:.4f}<{min_dense:.4f}"
                )
                LOG.info("RAG fallback to no-rag prompt: %s", fallback_reason)
                retrieved = None

    def _one_prompt(skill_index: int, eff_retrieved: RetrievalResult | None) -> tuple[str, str]:
        tier = "full"
        if eff_retrieved is not None:
            sch = dict(getattr(eff_retrieved, "query_schema", {}) or {})
            tier = _skill_format_tier_for_index(sch, skill_index, rag_ctx)
        return build_generation_prompt(
            problem_statement=problem_statement,
            retrieved=eff_retrieved,
            max_skill_tokens=max_skill_budget,
            tokenizer=rag_ctx.tokenizer,
            skill_index=skill_index,
            skill_format_tier=tier,
            fn_name=fn_name,
        )

    multi_skill_prompts = bool(
        per_sample_skill_index and retrieved and retrieved.skills and len(retrieved.skills) > 1
    )
    hybrid_enabled = bool(retrieved and _is_graph_rag_mode(rag_ctx.mode) and _graph_hybrid_enabled(rag_ctx))
    hybrid_sample0_bare = bool(hybrid_enabled and _graph_hybrid_bool(rag_ctx, "sample0_bare", False))
    completions: list[str] = []
    sample_prompt_modes: list[str] = []
    sample_skill_indices: list[int | None] = []
    sample_retrieved_skill_ids: list[list[str]] = []
    sample_retrieved_skills: list[list[dict[str, Any]]] = []
    sample_retrieval_scores: list[list[float]] = []

    def _sample_payload(eff_retrieved: RetrievalResult | None, skill_index: int | None) -> None:
        if eff_retrieved is None or skill_index is None:
            sample_retrieved_skill_ids.append([])
            sample_retrieved_skills.append([])
            sample_retrieval_scores.append([])
            return
        if skill_index < 0 or skill_index >= len(eff_retrieved.skills):
            sample_retrieved_skill_ids.append([])
            sample_retrieved_skills.append([])
            sample_retrieval_scores.append([])
            return
        ids = list(eff_retrieved.skill_ids)
        scores = list(eff_retrieved.scores)
        sid = ids[skill_index] if skill_index < len(ids) else str(eff_retrieved.skills[skill_index].get("skill_id") or "")
        score = float(scores[skill_index]) if skill_index < len(scores) else 0.0
        sample_retrieved_skill_ids.append([sid] if sid else [])
        sample_retrieved_skills.append([eff_retrieved.skills[skill_index]])
        sample_retrieval_scores.append([score])

    def _hybrid_max_skill_index(eff_retrieved: RetrievalResult) -> int:
        max_i = len(eff_retrieved.skills) - 1
        if per_sample_skill_max_index is not None:
            try:
                max_i = min(max_i, max(0, int(per_sample_skill_max_index)))
            except (TypeError, ValueError):
                pass
        return max_i

    def _choose_graph_hybrid_skill(start_index: int) -> tuple[int | None, str]:
        if retrieved is None or not retrieved.skills:
            return None, "missing_skill"
        max_i = _hybrid_max_skill_index(retrieved)
        if start_index > max_i:
            return None, "missing_skill"
        reasons: list[str] = []
        for cand_i in range(max(0, start_index), max_i + 1):
            ok, reason = _graph_hybrid_skill_allowed(
                retrieved=retrieved,
                skill_index=cand_i,
                rag_ctx=rag_ctx,
                scope=scope,
            )
            if ok:
                return cand_i, "ok"
            reasons.append(reason if start_index == max_i else f"{cand_i}:{reason}")
        return None, ";".join(reasons[:3]) if reasons else "no_allowed_skill"

    for i in range(n_samples):
        eff_retrieved = None if (dense_gate_bare and i == 0) else retrieved
        sk_i: int | None = 0 if eff_retrieved is not None else None
        mode = "rag_primary" if eff_retrieved is not None else "bare_no_rag"
        if dense_gate_bare and i == 0:
            mode = "bare_dense_gate_sample0"
        if hybrid_enabled and retrieved is not None:
            if hybrid_sample0_bare and i == 0:
                eff_retrieved = None
                sk_i = None
                mode = "bare_graph_hybrid_sample0"
            elif i in (0, 1):
                ok, reason = _graph_hybrid_skill_allowed(
                    retrieved=retrieved,
                    skill_index=0,
                    rag_ctx=rag_ctx,
                    scope=scope,
                )
                if ok:
                    eff_retrieved = retrieved
                    sk_i = 0
                    mode = "graph_hybrid_primary"
                else:
                    eff_retrieved = None
                    sk_i = None
                    mode = f"bare_graph_hybrid_primary:{reason}"
            elif i == 2:
                chosen_i, reason = _choose_graph_hybrid_skill(1)
                if chosen_i is not None:
                    eff_retrieved = retrieved
                    sk_i = chosen_i
                    second_level = _skill_level(retrieved.skills[chosen_i]) or "skill"
                    mode = f"graph_hybrid_second_{second_level}"
                else:
                    eff_retrieved = None
                    sk_i = None
                    mode = f"bare_graph_hybrid_second:{reason}"
            else:
                eff_retrieved = None
                sk_i = None
                mode = "bare_graph_hybrid_extra_sample"
        elif multi_skill_prompts and eff_retrieved:
            skills = eff_retrieved.skills
            sk_i = min(i, len(skills) - 1)
            if per_sample_skill_max_index is not None:
                sk_i = min(sk_i, max(0, int(per_sample_skill_max_index)))
            system, user = _one_prompt(sk_i, eff_retrieved)
            mode = f"rag_skill_index_{sk_i}"
        else:
            system, user = _one_prompt(sk_i or 0, eff_retrieved)
        if hybrid_enabled:
            system, user = _one_prompt(sk_i or 0, eff_retrieved)
        sample_prompt_modes.append(mode)
        sample_skill_indices.append(sk_i)
        _sample_payload(eff_retrieved, sk_i)
        temperature = None
        top_p = None
        # Match no_rag: only the first sample uses conservative temperature/top_p
        # when provided; later samples use model defaults (better PASS@3 diversity).
        # Fallback runs must stay distribution-aligned with no_rag so aggregate
        # PASS@k stays comparable to the baseline.
        use_conservative = i == 0
        if use_conservative and first_sample_temperature is not None:
            temperature = float(first_sample_temperature)
            top_p = float(first_sample_top_p) if first_sample_top_p is not None else None
        elif (
            not use_conservative
            and later_sample_temperature is not None
        ):
            temperature = float(later_sample_temperature)
            top_p = float(later_sample_top_p) if later_sample_top_p is not None else None
        outputs = code_llm.generate(
            system=system,
            user=user,
            temperature=temperature,
            top_p=top_p,
            max_new_tokens=None,
            n=1,
            stop=None,
            seed=seed_base + i,
        )
        completions.append(outputs[0] if outputs else "")
    extracted = [extract_python_code(c) for c in completions]
    trace_source = retrieval_trace
    trace_schema = dict(getattr(trace_source, "query_schema", {}) or {}) if trace_source else {}
    return GenerationTrace(
        retrieved_skill_ids=list(trace_source.skill_ids) if trace_source else [],
        retrieved_skills=list(trace_source.skills) if trace_source else [],
        retrieval_scores=list(trace_source.scores) if trace_source else [],
        retrieval_method=(trace_source.method if trace_source else "disabled"),
        dense_ids=list(trace_source.dense_ids) if trace_source else [],
        bm25_ids=list(trace_source.bm25_ids) if trace_source else [],
        raw_completions=completions,
        extracted_codes=extracted,
        bundle_type=getattr(trace_source, "bundle_type", "") if trace_source else "",
        graph_evidence=list(getattr(trace_source, "graph_evidence", []) or []) if trace_source else [],
        seed_ids=dict(getattr(trace_source, "seed_ids", {}) or {}) if trace_source else {},
        supporting_prototypes=list(getattr(trace_source, "supporting_prototypes", []) or []) if trace_source else [],
        matched_signals=list(getattr(trace_source, "matched_signals", []) or []) if trace_source else [],
        matched_mechanisms=list(getattr(trace_source, "matched_mechanisms", []) or []) if trace_source else [],
        query_schema=trace_schema,
        fallback_to_no_rag=fallback_to_no_rag,
        fallback_reason=fallback_reason,
        dense_relevance_cosine=dense_cos,
        dense_gate_bare_sample0=dense_gate_bare,
        sample_prompt_modes=sample_prompt_modes,
        sample_skill_indices=sample_skill_indices,
        sample_retrieved_skill_ids=sample_retrieved_skill_ids,
        sample_retrieved_skills=sample_retrieved_skills,
        sample_retrieval_scores=sample_retrieval_scores,
        graph_risk_flags=list(trace_schema.get("graph_risk_flags") or []),
        selected_skill_level=str(trace_schema.get("selected_skill_level") or ""),
        pre_rerank_skill_ids=list(trace_schema.get("pre_rerank_skill_ids") or []),
        post_rerank_skill_ids=list(trace_schema.get("post_rerank_skill_ids") or []),
    )
