"""Glue between RAG pipeline and the Qwen code LLM.

Given a problem + `RAGContext`, returns `n` raw code samples along with the
retrieval trace (for later evaluation).
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from ..llm.base import CodeLLM
from ..logging_utils import get_logger
from ..rag.pipeline import RAGContext, build_generation_prompt

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


def generate_with_rag(
    *,
    code_llm: CodeLLM,
    rag_ctx: RAGContext,
    problem_statement: str,
    n_samples: int,
    seed_base: int = 0,
    first_sample_temperature: float | None = None,
    first_sample_top_p: float | None = None,
) -> GenerationTrace:
    retrieved = rag_ctx.retrieve(problem_statement)
    fallback_to_no_rag = False
    fallback_reason = ""
    if retrieved:
        schema = dict(getattr(retrieved, "query_schema", {}) or {})
        cand_fams = list(schema.get("candidate_families") or [])
        is_graph = _is_graph_rag_mode(rag_ctx.mode)

        if not cand_fams:
            fallback_to_no_rag = True
            fallback_reason = "empty_candidate_families"
        else:
            rc = _effective_routing_confidence(schema)
            if (
                rag_ctx.min_router_confidence > 0.0
                and rc is not None
                and rc < rag_ctx.min_router_confidence
            ):
                fallback_to_no_rag = True
                fallback_reason = f"low_routing_confidence:{rc:.4f}<{rag_ctx.min_router_confidence:.4f}"

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
                    rag_ctx.min_score_margin_graph > 0.0
                    and margin < rag_ctx.min_score_margin_graph
                ):
                    fallback_to_no_rag = True
                    fallback_reason = (
                        f"low_graph_score_margin:{margin:.4f}<{rag_ctx.min_score_margin_graph:.4f}"
                    )
                elif (
                    rag_ctx.min_score_relative_graph > 0.0
                    and rel < rag_ctx.min_score_relative_graph
                ):
                    fallback_to_no_rag = True
                    fallback_reason = (
                        f"low_graph_score_relative:{rel:.4f}<{rag_ctx.min_score_relative_graph:.4f}"
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
    system, user = build_generation_prompt(
        problem_statement=problem_statement,
        retrieved=retrieved,
        max_skill_tokens=rag_ctx.max_skill_tokens,
        tokenizer=rag_ctx.tokenizer,
    )
    # Per-sample seeding so each of the n generations explores a different mode.
    completions: list[str] = []
    for i in range(n_samples):
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
    return GenerationTrace(
        retrieved_skill_ids=list(retrieved.skill_ids) if retrieved else [],
        retrieved_skills=list(retrieved.skills) if retrieved else [],
        retrieval_scores=list(retrieved.scores) if retrieved else [],
        retrieval_method=(retrieved.method if retrieved else "disabled"),
        dense_ids=list(retrieved.dense_ids) if retrieved else [],
        bm25_ids=list(retrieved.bm25_ids) if retrieved else [],
        raw_completions=completions,
        extracted_codes=extracted,
        bundle_type=getattr(retrieved, "bundle_type", "") if retrieved else "",
        graph_evidence=list(getattr(retrieved, "graph_evidence", []) or []) if retrieved else [],
        seed_ids=dict(getattr(retrieved, "seed_ids", {}) or {}) if retrieved else {},
        supporting_prototypes=list(getattr(retrieved, "supporting_prototypes", []) or []) if retrieved else [],
        matched_signals=list(getattr(retrieved, "matched_signals", []) or []) if retrieved else [],
        matched_mechanisms=list(getattr(retrieved, "matched_mechanisms", []) or []) if retrieved else [],
        query_schema=dict(getattr(retrieved, "query_schema", {}) or {}) if retrieved else {},
        fallback_to_no_rag=fallback_to_no_rag,
        fallback_reason=fallback_reason,
    )
