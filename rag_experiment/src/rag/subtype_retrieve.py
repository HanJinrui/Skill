"""Conservative hierarchical retriever over Stage D v2 skills.

The path is intentionally simple and stable:

    query schema -> family filter -> subtype ranking -> optional bundle

It avoids graph propagation and reads `outputs/stage_d_v2/*` directly, which
makes it useful for quick smoke evaluation after Stage D v2 finishes.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from ..io_utils import load_jsonl
from ..logging_utils import get_logger
from ..settings import Settings
from .build_index import _tokenize
from .query_analyzer import analyze
from .retrieve import RetrievalResult

LOG = get_logger(__name__)


def _skill_text(skill: dict[str, Any]) -> str:
    parts: list[str] = []
    parts.append(str(skill.get("skill_name") or skill.get("skill_id") or ""))
    parts.append(" ".join(skill.get("families") or []))
    parts.append(str(skill.get("subtype") or ""))
    parts.append(str(skill.get("description") or ""))
    parts.extend(str(x) for x in (skill.get("trigger_signals") or []))
    parts.extend(str(x) for x in (skill.get("applicable_when") or []))
    parts.extend(str(x) for x in (skill.get("problem_signals") or []))
    parts.append(str(skill.get("core_idea") or ""))
    parts.extend(str(x) for x in (skill.get("template_strategy") or []))
    parts.append(str(skill.get("retrieval_text") or ""))
    return "\n".join(p for p in parts if p)


def _overlap_score(query_tokens: set[str], skill: dict[str, Any]) -> float:
    text_tokens = set(_tokenize(_skill_text(skill)))
    if not text_tokens or not query_tokens:
        return 0.0
    overlap = len(query_tokens & text_tokens)
    return overlap / max(8.0, len(query_tokens))


class SubtypeRetriever:
    def __init__(self, *, stage_d_v2_dir: Path) -> None:
        self.stage_d_v2_dir = stage_d_v2_dir
        self.subtype_skills = load_jsonl(stage_d_v2_dir / "subtype_skills.jsonl")
        self.family_skills = load_jsonl(stage_d_v2_dir / "family_skills.jsonl")
        self.router_skills = load_jsonl(stage_d_v2_dir / "router_skills.jsonl")
        self.bundle_skills = load_jsonl(stage_d_v2_dir / "bundles_or_compositions.jsonl")
        self.skills_by_id: dict[str, dict[str, Any]] = {}
        for row in self.subtype_skills + self.family_skills + self.router_skills + self.bundle_skills:
            sid = row.get("skill_id")
            if isinstance(sid, str):
                self.skills_by_id[sid] = row
        if not self.subtype_skills:
            raise FileNotFoundError(f"Stage D v2 subtype skills missing under {stage_d_v2_dir}")
        LOG.info(
            "SubtypeRetriever loaded: subtype=%d family=%d router=%d bundle=%d",
            len(self.subtype_skills),
            len(self.family_skills),
            len(self.router_skills),
            len(self.bundle_skills),
        )

    @classmethod
    def from_settings(cls, settings: Settings) -> "SubtypeRetriever":
        return cls(stage_d_v2_dir=settings.stage_dir("stage_d_v2"))

    def _rank_subtypes(
        self,
        *,
        problem_statement: str,
        candidate_families: list[str],
        mechanism_hints: list[str],
        top_k: int,
    ) -> list[tuple[dict[str, Any], float]]:
        query_tokens = set(_tokenize(problem_statement))
        pool = self.subtype_skills
        if candidate_families:
            cand = set(candidate_families)
            filtered = [s for s in pool if set(s.get("families") or []) & cand]
            if filtered:
                pool = filtered
        ranked: list[tuple[dict[str, Any], float]] = []
        for skill in pool:
            score = _overlap_score(query_tokens, skill)
            fams = set(skill.get("families") or [])
            if candidate_families and fams & set(candidate_families):
                score += 0.35
            skill_text = _skill_text(skill)
            for mech in mechanism_hints:
                if mech and mech in skill_text:
                    score += 0.25
            ranked.append((skill, score))
        ranked.sort(key=lambda item: (item[1], int(item[0].get("num_source_examples") or 0)), reverse=True)
        return ranked[: max(1, top_k)]

    def _pick_bundle(
        self,
        *,
        candidate_families: list[str],
        primary: dict[str, Any],
        problem_statement: str,
    ) -> tuple[dict[str, Any], float] | None:
        family_set = set(candidate_families)
        family_set.update(primary.get("families") or [])
        if len(family_set) < 2:
            return None
        query_tokens = set(_tokenize(problem_statement))
        candidates = []
        for bundle in self.bundle_skills:
            bfams = set(bundle.get("family_set") or bundle.get("families") or [])
            if len(bfams & family_set) >= 2:
                score = _overlap_score(query_tokens, bundle) + 0.15 * len(bfams & family_set)
                candidates.append((bundle, score))
        if not candidates:
            return None
        candidates.sort(key=lambda item: item[1], reverse=True)
        return candidates[0]

    def retrieve(self, query: str, *, top_k: int) -> RetrievalResult:
        schema = analyze(query)
        candidate_families = list(schema.candidate_families)
        subtype_ranked = self._rank_subtypes(
            problem_statement=query,
            candidate_families=candidate_families,
            mechanism_hints=list(schema.mechanism_hints),
            top_k=max(1, top_k),
        )
        if not subtype_ranked:
            return RetrievalResult([], [], [], [], [], method="subtype_rag", query_schema=schema.to_dict())

        primary, primary_score = subtype_ranked[0]
        skills = [primary]
        scores = [primary_score]
        skill_ids = [str(primary["skill_id"])]
        bundle_type = "primary_only"

        bundle = None
        if schema.is_multi_skill_likely or len(candidate_families) >= 2:
            bundle = self._pick_bundle(
                candidate_families=candidate_families,
                primary=primary,
                problem_statement=query,
            )
        if bundle is not None and len(skills) < max(1, top_k):
            bundle_skill, bundle_score = bundle
            skills.append(bundle_skill)
            scores.append(bundle_score)
            skill_ids.append(str(bundle_skill["skill_id"]))
            bundle_type = "primary_plus_bundle"

        evidence = [
            {
                "skill_id": primary.get("skill_id"),
                "why_selected": "top subtype after conservative family routing",
                "matched_signals": list(schema.signal_tags),
                "matched_mechanisms": list(schema.mechanism_hints),
                "prototype_evidence": (primary.get("representative_examples") or [])[:1],
            }
        ]
        return RetrievalResult(
            skill_ids=skill_ids,
            skills=skills,
            scores=scores,
            dense_ids=skill_ids[:top_k],
            bm25_ids=skill_ids[:top_k],
            method="subtype_rag",
            bundle_type=bundle_type,
            graph_evidence=evidence,
            matched_signals=list(schema.signal_tags),
            matched_mechanisms=list(schema.mechanism_hints),
            query_schema=schema.to_dict(),
        )
