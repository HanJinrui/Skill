from __future__ import annotations

from typing import Any

from .scoring import compute_quality_score, compute_representative_score


def build_representative_sample(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "problem_id": row.get("problem_id"),
        "solution_id": row.get("solution_id"),
        "quality_score": round(float(row.get("quality_score") or 0), 4),
        "subtype_confidence": row.get("subtype_confidence"),
        "evidence_tier": row.get("evidence_tier"),
        "core_mechanism_summary": row.get("core_mechanism_summary"),
        "subtype_rationale": row.get("subtype_rationale"),
        "difficulty": row.get("difficulty"),
        "source": row.get("source"),
    }


def select_representative_rows(
    rows: list[dict[str, Any]],
    config: dict[str, Any] | None = None,
    *,
    max_examples: int | None = None,
    min_examples: int | None = None,
) -> list[dict[str, Any]]:
    rc = (config or {}).get("representative_selection", config or {})
    max_n = max_examples if max_examples is not None else int(rc.get("max_examples_per_skill", 8))
    min_n = min_examples if min_examples is not None else int(rc.get("min_examples_per_skill", 5))
    prefer_gold = bool(rc.get("prefer_gold", True))
    max_code_lines = int(rc.get("max_code_lines_soft", 160))

    enriched: list[dict[str, Any]] = []
    for row in rows:
        r = dict(row)
        r["quality_score"] = compute_quality_score(r)
        enriched.append(r)

    if prefer_gold:
        gold = [r for r in enriched if r.get("evidence_tier") == "gold"]
        if len(gold) >= min_n:
            enriched = gold

    enriched.sort(
        key=lambda r: (
            -float(r.get("quality_score") or 0),
            -float(r.get("subtype_confidence") or 0),
            len(str(r.get("solution_code") or "").splitlines()),
        )
    )

    selected: list[dict[str, Any]] = []
    difficulties: list[str] = []
    sources: list[str] = []

    for row in enriched:
        if len(selected) >= max_n:
            break
        code_lines = len(str(row.get("solution_code") or "").splitlines())
        if len(selected) >= min_n and code_lines > max_code_lines:
            continue
        rep_score = compute_representative_score(
            row,
            selected_difficulties=difficulties,
            selected_sources=sources,
        )
        row = dict(row)
        row["representative_score"] = rep_score
        selected.append(row)
        difficulties.append(str(row.get("difficulty") or ""))
        sources.append(str(row.get("source") or ""))

    if len(selected) < min_n:
        selected = enriched[: min(max_n, len(enriched))]

    selected.sort(key=lambda r: -float(r.get("representative_score") or r.get("quality_score") or 0))
    return selected[:max_n]
