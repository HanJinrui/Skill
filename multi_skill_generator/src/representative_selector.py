from __future__ import annotations

import re
from typing import Any

from .scoring import compute_quality_score, compute_representative_score


def build_solution_code_excerpt(row: dict[str, Any], config: dict[str, Any]) -> str:
    rc = config.get("representative_selection", config)
    max_lines = int(rc.get("max_code_excerpt_lines", 120))
    code = str(row.get("solution_code") or "")
    lines = code.splitlines()

    def _score_line(line: str) -> int:
        low = line.lower()
        score = 0
        if re.match(r"\s*def\s+solve", low):
            score += 10
        for kw in (
            "sort",
            "heap",
            "bisect",
            "binary",
            "dp",
            "while",
            "for ",
            "greedy",
            "union",
            "fenwick",
            "segment",
        ):
            if kw in low:
                score += 2
        if line.strip().startswith("#"):
            score -= 1
        return score

    if len(lines) <= max_lines:
        return code

    ranked = sorted(range(len(lines)), key=lambda i: -_score_line(lines[i]))
    keep = sorted(ranked[:max_lines])
    return "\n".join(lines[i] for i in keep)


def build_representative_sample(row: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    excerpt = build_solution_code_excerpt(row, config)
    return {
        "problem_id": row.get("problem_id"),
        "solution_id": row.get("solution_id"),
        "source_dataset": row.get("source_dataset", "TACO"),
        "source_language": row.get("source_language"),
        "verification_source": row.get("verification_source", "taco-verified"),
        "source_problem_fingerprint": row.get("source_problem_fingerprint"),
        "problem_statement": str(row.get("problem_statement") or "")[:500],
        "composition_order": row.get("normalized_composition_order") or row.get("composition_order"),
        "composition_subtypes": row.get("composition_subtypes"),
        "core_composition_summary": row.get("core_composition_summary"),
        "solution_code_excerpt": excerpt,
        "why_representative": str(row.get("core_composition_summary") or "")[:300],
    }


def select_representative_rows(
    rows: list[dict[str, Any]],
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    rc = config.get("representative_selection", config)
    max_n = int(rc.get("max_examples_per_skill", 8))
    min_n = int(rc.get("min_examples_per_skill", 3))
    max_code = int(rc.get("max_code_lines_soft", 160))
    prefer_complete = bool(rc.get("prefer_complete_order", True))
    prefer_unrepaired = bool(rc.get("prefer_unrepaired_order", True))

    enriched: list[dict[str, Any]] = []
    for row in rows:
        r = dict(row)
        r["quality_score"] = compute_quality_score(r)
        enriched.append(r)

    if prefer_complete:
        complete = [r for r in enriched if r.get("order_repaired") is not True]
        if prefer_unrepaired and len(complete) >= min_n:
            enriched = complete
        else:
            from .scoring import compute_order_completeness_score

            good = [r for r in enriched if compute_order_completeness_score(r) >= 1.0]
            if len(good) >= min_n:
                enriched = good

    enriched.sort(
        key=lambda r: (
            -float(r.get("representative_score") or compute_representative_score(r)),
            -float(r.get("quality_score") or 0),
            len(str(r.get("solution_code") or "").splitlines()),
        )
    )

    selected: list[dict[str, Any]] = []
    families_seen: list[str] = []

    for row in enriched:
        if len(selected) >= max_n:
            break
        if len(selected) >= min_n and len(str(row.get("solution_code") or "").splitlines()) > max_code:
            continue
        rs = compute_representative_score(row, selected_families=families_seen)
        row = dict(row)
        row["representative_score"] = rs
        selected.append(row)
        families_seen.append(str(row.get("composition_key") or ""))

    if len(selected) < min_n:
        selected = enriched[: min(max_n, len(enriched))]

    selected.sort(key=lambda r: -float(r.get("representative_score") or 0))
    return selected[:max_n]
