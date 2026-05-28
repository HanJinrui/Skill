"""Rule-based subtype candidates (not final labels)."""
from __future__ import annotations

from typing import Any

from sdf.shared import bootstrap  # noqa: F401

from src.rules import solution_ast_features
from src.subtype_taxonomy import (
    get_subtype,
    infer_candidate_subtypes_from_problem,
    infer_candidate_subtypes_from_solution,
)
from src.taxonomy import CORE_FAMILIES


def _ordered_unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for x in items:
        if x and x not in seen:
            seen.add(x)
            out.append(x)
    return out


def merge_subtype_candidates(
    problem_candidates: list[dict[str, Any]],
    solution_candidates: list[dict[str, Any]],
    *,
    family_filter: list[str],
) -> list[dict[str, Any]]:
    scores: dict[str, float] = {}
    meta: dict[str, dict[str, Any]] = {}
    for src in (problem_candidates, solution_candidates):
        for item in src:
            sid = str(item.get("subtype_id") or "")
            if not sid:
                continue
            if family_filter and str(item.get("family") or "") not in family_filter:
                continue
            scores[sid] = scores.get(sid, 0.0) + float(item.get("score") or 0.0)
            prev = meta.get(sid) or dict(item)
            prev["subtype_id"] = sid
            meta[sid] = prev
    ranked = sorted(scores.keys(), key=lambda k: (-scores[k], k))
    out: list[dict[str, Any]] = []
    for sid in ranked[:10]:
        row = dict(meta[sid])
        row["score"] = scores[sid]
        out.append(row)
    return out


def build_rule_candidates(row: dict[str, Any]) -> dict[str, Any]:
    problem_statement = row.get("problem_statement") or ""
    code = row.get("solution_code") or ""
    problem_families = list(row.get("problem_families") or row.get("candidate_families") or [])
    ast_features = solution_ast_features(code)
    from src.rules import ast_to_family_hints

    ast_hints = ast_to_family_hints(ast_features)
    if row.get("open_family_candidates"):
        family_filter = list(CORE_FAMILIES)
    else:
        family_filter = _ordered_unique(problem_families + list(row.get("solution_family_hints") or []) + ast_hints)

    problem_candidates = infer_candidate_subtypes_from_problem(
        problem_statement,
        row.get("original_skill_types") or [],
        row.get("original_tags") or [],
        family_filter if row.get("open_family_candidates") else problem_families,
        max_candidates=10,
    )
    solution_candidates = infer_candidate_subtypes_from_solution(
        code,
        ast_features,
        family_filter=family_filter,
        max_candidates=10,
    )
    merged = merge_subtype_candidates(problem_candidates, solution_candidates, family_filter=family_filter)
    if not merged:
        fallback_family = problem_families[0] if problem_families else "complete_search"
        merged = [
            {
                "subtype_id": "search_backtracking",
                "family": fallback_family,
                "score": 0.25,
                "description": "fallback",
                "sources": ["fallback"],
            }
        ]
    top = merged[0]
    return {
        "candidate_subtypes": merged,
        "rule_top_subtype": str(top.get("subtype_id") or ""),
        "rule_confidence": min(0.95, 0.25 + float(top.get("score") or 0.0) / 20.0),
        "ast_features": ast_features.to_dict() if hasattr(ast_features, "to_dict") else {},
    }


def rule_mechanism_scope_hint(candidates: list[dict[str, Any]], *, gap: float, multi_min_score: float) -> str:
    """Return single | multi | ambiguous from rule scores only."""
    if len(candidates) < 2:
        return "single"
    top = float(candidates[0].get("score") or 0.0)
    second = float(candidates[1].get("score") or 0.0)
    fam0 = str(candidates[0].get("family") or "")
    fam1 = str(candidates[1].get("family") or "")
    if top - second >= gap and fam0 == fam1:
        return "single"
    if top >= multi_min_score and second >= multi_min_score and fam0 != fam1:
        return "multi"
    if top - second >= gap:
        return "single"
    return "ambiguous"
