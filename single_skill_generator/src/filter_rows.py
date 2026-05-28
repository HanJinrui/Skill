from __future__ import annotations

from typing import Any


def hard_filter(row: dict[str, Any], config: dict[str, Any]) -> bool:
    fc = config.get("filter", config)
    if fc.get("require_syntax_ok", True) and row.get("syntax_ok") is not True:
        return False
    if fc.get("require_safe_exec_ok", True) and row.get("safe_exec_ok") is not True:
        return False
    if fc.get("require_full_pass", True) and row.get("full_pass") is not True:
        return False
    req_rate = fc.get("require_pass_rate", 1.0)
    if float(row.get("pass_rate") or 0) != float(req_rate):
        return False
    if row.get("algorithm_scope") != fc.get("algorithm_scope", "single"):
        return False
    if fc.get("require_true_composition_false", True) and row.get("is_true_composition") is not False:
        return False
    if fc.get("require_primary_solution", True) and row.get("is_primary_solution") is not True:
        return False
    is_curated = row.get("evidence_origin") == "curated"
    curated_ok = (
        fc.get("allow_curated_evidence", False)
        and is_curated
        and row.get("evidence_validation") == "executed_tests"
    )
    if fc.get("require_taco_family_alignment", True) and not curated_ok and row.get("taco_family_alignment") is not True:
        return False
    if not row.get("primary_subtype"):
        return False
    if not row.get("detected_single_skill"):
        return False
    return True


def generation_filter(row: dict[str, Any], config: dict[str, Any]) -> bool:
    if not hard_filter(row, config):
        return False
    fc = config.get("filter", config)
    accepted_tiers = fc.get("accepted_evidence_tiers")
    tier = fc.get("evidence_tier")
    if accepted_tiers and row.get("evidence_tier") not in set(accepted_tiers):
        return False
    if not accepted_tiers and tier and row.get("evidence_tier") != tier:
        return False
    min_conf = float(fc.get("min_subtype_confidence", 0.85))
    if float(row.get("subtype_confidence") or 0) < min_conf:
        return False
    return True


def filter_rows(
    rows: list[dict[str, Any]],
    config: dict[str, Any],
    *,
    use_generation_filter: bool = True,
) -> list[dict[str, Any]]:
    fn = generation_filter if use_generation_filter else hard_filter
    return [r for r in rows if fn(r, config)]
