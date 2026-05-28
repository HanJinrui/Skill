from __future__ import annotations

import math
from typing import Any

from .normalize_composition import extract_subtype_names, normalize_composition_order


def evidence_score(row: dict[str, Any]) -> float:
    tier = row.get("evidence_tier")
    if tier == "gold":
        return 1.0
    if tier == "silver":
        return 0.7
    return 0.5


def compute_order_completeness_score(row: dict[str, Any]) -> float:
    names = extract_subtype_names(row)
    order = normalize_composition_order(row)
    if not names:
        return 0.0
    if set(order) == set(names) and len(order) == len(names):
        return 1.0
    return 0.5


def compute_quality_score(row: dict[str, Any]) -> float:
    order_score = compute_order_completeness_score(row)
    return (
        0.30 * float(row.get("subtype_confidence") or 0)
        + 0.20 * float(row.get("pass_rate") or 0)
        + 0.15 * float(row.get("rule_confidence") or 0)
        + 0.15 * float(row.get("primary_solution_score") or 0)
        + 0.10 * evidence_score(row)
        + 0.10 * order_score
    )


def compute_code_simplicity_score(row: dict[str, Any]) -> float:
    code = str(row.get("solution_code") or "")
    return 1.0 / math.log(len(code.splitlines()) + 2)


def compute_role_detail_score(row: dict[str, Any]) -> float:
    subtypes = row.get("composition_subtypes") or []
    if not subtypes:
        return 0.0
    counts = []
    for item in subtypes:
        if isinstance(item, dict):
            role = str(item.get("role") or "")
            counts.append(len(role.split()))
    if not counts:
        return 0.0
    return min(1.0, sum(counts) / len(counts) / 20)


def compute_summary_detail_score(row: dict[str, Any]) -> float:
    summary = str(row.get("core_composition_summary") or "")
    return min(1.0, len(summary.split()) / 80)


def compute_representative_score(
    row: dict[str, Any],
    *,
    selected_families: list[str] | None = None,
) -> float:
    qs = float(row.get("quality_score") or compute_quality_score(row))
    order_score = compute_order_completeness_score(row)
    diversity = 0.0
    fam = str(row.get("composition_key") or "")
    if selected_families is not None and fam and fam not in selected_families:
        diversity = 1.0 if len({f for f in selected_families if f}) < 6 else 0.5
    return (
        0.40 * qs
        + 0.20 * order_score
        + 0.15 * compute_role_detail_score(row)
        + 0.10 * compute_summary_detail_score(row)
        + 0.10 * compute_code_simplicity_score(row)
        + 0.05 * diversity
    )
