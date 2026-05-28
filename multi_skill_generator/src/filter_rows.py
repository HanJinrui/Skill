from __future__ import annotations

from collections import Counter
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
    if row.get("algorithm_scope") != fc.get("algorithm_scope", "multi"):
        return False
    subtypes = row.get("composition_subtypes") or []
    if len(subtypes) < 2:
        return False
    min_conf = float(fc.get("min_subtype_confidence", 0.90))
    if float(row.get("subtype_confidence") or 0) < min_conf:
        return False
    if not fc.get("allow_silver", True):
        if row.get("evidence_tier") != "gold":
            return False
    return True


def filter_rows(rows: list[dict[str, Any]], config: dict[str, Any]) -> list[dict[str, Any]]:
    return [r for r in rows if hard_filter(r, config)]


def build_filtering_report(
    rows: list[dict[str, Any]],
    filtered_rows: list[dict[str, Any]],
    config: dict[str, Any],
) -> dict[str, Any]:
    filtered_ids = {id(r) for r in filtered_rows}
    reject_reasons: Counter[str] = Counter()
    for row in rows:
        if id(row) in filtered_ids:
            continue
        if row.get("syntax_ok") is not True:
            reject_reasons["syntax_ok"] += 1
        elif row.get("safe_exec_ok") is not True:
            reject_reasons["safe_exec_ok"] += 1
        elif row.get("full_pass") is not True:
            reject_reasons["full_pass"] += 1
        elif float(row.get("pass_rate") or 0) != float(config.get("filter", {}).get("require_pass_rate", 1.0)):
            reject_reasons["pass_rate"] += 1
        elif row.get("algorithm_scope") != "multi":
            reject_reasons["algorithm_scope"] += 1
        elif len(row.get("composition_subtypes") or []) < 2:
            reject_reasons["composition_subtypes"] += 1
        elif float(row.get("subtype_confidence") or 0) < float(
            config.get("filter", {}).get("min_subtype_confidence", 0.90)
        ):
            reject_reasons["subtype_confidence"] += 1
        else:
            reject_reasons["other"] += 1

    return {
        "total_rows": len(rows),
        "hard_filtered_rows": len(filtered_rows),
        "rejected_rows": len(rows) - len(filtered_rows),
        "reject_reasons": dict(reject_reasons),
        "filter_config": config.get("filter", {}),
    }
