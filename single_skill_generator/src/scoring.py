from __future__ import annotations

import math
from typing import Any


def evidence_score(row: dict[str, Any]) -> float:
    tier = row.get("evidence_tier")
    if tier == "gold":
        return 1.0
    if tier == "silver":
        return 0.7
    if tier == "curated" and row.get("evidence_validation") == "executed_tests":
        return 0.8
    return 0.0


def alignment_score(row: dict[str, Any]) -> float:
    return 1.0 if row.get("taco_family_alignment") is True else 0.0


def compute_quality_score(row: dict[str, Any]) -> float:
    return (
        0.35 * float(row.get("subtype_confidence") or 0)
        + 0.20 * float(row.get("pass_rate") or 0)
        + 0.15 * float(row.get("rule_confidence") or 0)
        + 0.15 * float(row.get("primary_solution_score") or 0)
        + 0.10 * evidence_score(row)
        + 0.05 * alignment_score(row)
    )


def compute_code_simplicity_score(row: dict[str, Any]) -> float:
    code = str(row.get("solution_code") or "")
    code_lines = len(code.splitlines())
    return 1.0 / math.log(code_lines + 2)


def _diversity_bonus(values: list[str], current: str) -> float:
    if not current:
        return 0.0
    seen = {v for v in values if v}
    if current in seen:
        return 0.0
    return 1.0 if len(seen) < 6 else 0.5


def compute_representative_score(
    row: dict[str, Any],
    *,
    selected_difficulties: list[str] | None = None,
    selected_sources: list[str] | None = None,
) -> float:
    qs = float(row.get("quality_score") or compute_quality_score(row))
    diff_bonus = _diversity_bonus(selected_difficulties or [], str(row.get("difficulty") or ""))
    src_bonus = _diversity_bonus(selected_sources or [], str(row.get("source") or ""))
    return (
        0.50 * qs
        + 0.20 * float(row.get("subtype_confidence") or 0)
        + 0.15 * compute_code_simplicity_score(row)
        + 0.10 * diff_bonus
        + 0.05 * src_bonus
    )
