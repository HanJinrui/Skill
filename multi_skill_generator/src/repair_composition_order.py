from __future__ import annotations

from typing import Any

from .normalize_composition import (
    extract_subtype_names,
    normalize_composition_order,
    normalize_row,
)
from .scoring import compute_order_completeness_score

SORTING_PREFIXES = (
    "sorting_custom_key",
    "sorting_sweep_line",
    "sorting_binary_search_answer",
    "sorting_binary_search_lookup",
)

BINARY_SEARCH_OUTER = "sorting_binary_search_answer"
CHECKER_SUFFIXES = (
    "greedy_sorting_order",
    "greedy_two_pointers",
    "dp_1d_state",
    "greedy_exchange_argument",
    "amortized_two_pointers",
)

DS_TYPES = (
    "ds_heap_priority_queue",
    "ds_hash_map",
    "ds_ordered_set",
    "ds_union_find",
)

DP_CHAIN = [
    ("dp_2d_state", "dp_interval"),
    ("dp_interval", "dp_1d_state"),
    ("dp_2d_state", "dp_interval", "dp_1d_state"),
]


def check_order_consistency(row: dict[str, Any]) -> dict[str, Any]:
    subtype_names = extract_subtype_names(row)
    order = normalize_composition_order(row)
    return {
        "length_match": len(order) == len(subtype_names),
        "set_match": set(order) == set(subtype_names),
        "missing_subtypes": list(set(subtype_names) - set(order)),
        "extra_order_items": list(set(order) - set(subtype_names)),
        "complete": set(order) == set(subtype_names) and len(order) == len(subtype_names),
    }


def _text_signals(row: dict[str, Any]) -> str:
    parts = [
        str(row.get("core_composition_summary") or ""),
        str(row.get("solution_code") or "")[:4000],
    ]
    return " ".join(parts).lower()


def _rule_sorting_first(names: set[str], order: list[str]) -> list[str] | None:
    missing = names - set(order)
    sorting_missing = [s for s in missing if s in SORTING_PREFIXES]
    if not sorting_missing:
        return None
    text = _text_signals(row if isinstance(row, dict) else {})
    if not any(k in text for k in ("sort", "sorted", "key", "order", "binary search", "check")):
        return None
    repaired = list(order)
    for s in sorted(sorting_missing, key=lambda x: SORTING_PREFIXES.index(x) if x in SORTING_PREFIXES else 99):
        repaired.insert(0, s)
    for n in names:
        if n not in repaired:
            repaired.append(n)
    return repaired


def repair_order_by_rules(row: dict[str, Any]) -> dict[str, Any]:
    names = extract_subtype_names(row)
    name_set = set(names)
    order = normalize_composition_order(row)
    check = check_order_consistency(row)
    result = {
        "decision": "valid",
        "original_composition_order": list(order),
        "repaired_composition_order": list(order),
        "reason": "order already consistent",
        "confidence": 1.0,
        "method": "none",
    }
    text = _text_signals(row)

    # Rule 2: binary search answer outer (also when order is complete but wrong)
    if BINARY_SEARCH_OUTER in name_set:
        others = [n for n in names if n != BINARY_SEARCH_OUTER]
        checker = [n for n in others if n in CHECKER_SUFFIXES]
        if checker and (not order or order[0] != BINARY_SEARCH_OUTER):
            repaired = [BINARY_SEARCH_OUTER] + [n for n in names if n != BINARY_SEARCH_OUTER]
            return {
                "decision": "repair",
                "original_composition_order": list(order),
                "repaired_composition_order": repaired,
                "reason": "binary search on answer is outer framework",
                "confidence": 0.9,
                "method": "rule_binary_search_outer",
            }

    if check["complete"]:
        return result

    # Rule 4: DP chains
    names_tuple = tuple(names)
    for chain in DP_CHAIN:
        if set(chain) == name_set:
            return {
                "decision": "repair",
                "original_composition_order": list(order),
                "repaired_composition_order": list(chain),
                "reason": "known DP pipeline order",
                "confidence": 0.92,
                "method": "rule_dp_chain",
            }

    # Rule 3: data structure between sort and greedy
    ds_in = [n for n in names if n in DS_TYPES]
    if ds_in and "sorting_custom_key" in name_set:
        greedy = [n for n in names if n.startswith("greedy_")]
        if greedy:
            repaired = ["sorting_custom_key"]
            for d in ds_in:
                if d not in repaired:
                    repaired.append(d)
            for g in greedy:
                if g not in repaired:
                    repaired.append(g)
            for n in names:
                if n not in repaired:
                    repaired.append(n)
            if repaired != order:
                return {
                    "decision": "repair",
                    "original_composition_order": list(order),
                    "repaired_composition_order": repaired,
                    "reason": "data structure as intermediate layer",
                    "confidence": 0.85,
                    "method": "rule_ds_layer",
                }

    # Rule 1: sorting prefix
    missing = name_set - set(order)
    sorting_missing = [s for s in missing if s in SORTING_PREFIXES]
    if sorting_missing and any(
        k in text for k in ("sort", "sorted", "key", "order", "binary search")
    ):
        repaired = []
        for s in SORTING_PREFIXES:
            if s in name_set:
                repaired.append(s)
        for n in names:
            if n not in repaired:
                repaired.append(n)
        return {
            "decision": "repair",
            "original_composition_order": list(order),
            "repaired_composition_order": repaired,
            "reason": "sorting as preprocessing",
            "confidence": 0.88,
            "method": "rule_sorting_first",
        }

    # Missing order entirely: use composition_subtypes order
    if not order and names:
        return {
            "decision": "repair",
            "original_composition_order": [],
            "repaired_composition_order": list(names),
            "reason": "filled from composition_subtypes declaration order",
            "confidence": 0.75,
            "method": "rule_subtype_order",
        }

    # Append missing at end
    if missing and len(order) > 0:
        repaired = list(order) + [m for m in names if m not in order]
        if set(repaired) == name_set:
            return {
                "decision": "repair",
                "original_composition_order": list(order),
                "repaired_composition_order": repaired,
                "reason": "appended missing subtypes",
                "confidence": 0.7,
                "method": "rule_append_missing",
            }

    result["decision"] = "reject"
    result["reason"] = "could not repair order with rules"
    result["confidence"] = 0.3
    return result


def build_repair_prompt(row: dict[str, Any], config: dict[str, Any]) -> str:
    from pathlib import Path

    root = Path(config.get("_project_root", "."))
    tmpl = (root / "prompts" / "repair_composition_order.md").read_text(encoding="utf-8")
    import json

    payload = {
        "composition_subtypes": row.get("composition_subtypes"),
        "composition_order": row.get("composition_order"),
        "core_composition_summary": row.get("core_composition_summary"),
        "solution_code_excerpt": str(row.get("solution_code") or "")[:3000],
    }
    return tmpl.replace("{{row_json}}", json.dumps(payload, ensure_ascii=False, indent=2))


def repair_order_by_llm(row: dict[str, Any], llm_client: Any, config: dict[str, Any]) -> dict[str, Any]:
    prompt = build_repair_prompt(row, config)
    out = llm_client.generate_json(
        prompt,
        cache_key={"task": "repair_order", "problem_id": row.get("problem_id")},
        routing_key=str(row.get("problem_id") or ""),
    )
    out["method"] = "llm"
    return out


def repair_composition_orders(
    rows: list[dict[str, Any]],
    config: dict[str, Any],
    *,
    llm_client: Any | None = None,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rc = config.get("composition_order_repair", config)
    enable_rules = bool(rc.get("enable_rule_repair", True))
    enable_llm = bool(rc.get("enable_llm_repair", False))
    min_llm_conf = float(rc.get("min_llm_repair_confidence", 0.80))

    repaired_rows: list[dict[str, Any]] = []
    manual_review: list[dict[str, Any]] = []
    repair_log: list[dict[str, Any]] = []

    for row in rows:
        r = dict(row)
        if enable_rules:
            repair = repair_order_by_rules(r)
        else:
            repair = check_order_consistency(r)
            repair = {
                "decision": "valid" if repair["complete"] else "reject",
                "repaired_composition_order": normalize_composition_order(r),
                "confidence": 1.0 if repair["complete"] else 0.0,
            }

        if repair.get("decision") == "repair":
            r["composition_order"] = repair["repaired_composition_order"]
            r["order_repaired"] = True
            r["order_repair_meta"] = repair
            repaired_rows.append(
                {
                    "problem_id": r.get("problem_id"),
                    "solution_id": r.get("solution_id"),
                    **repair,
                }
            )
        elif repair.get("decision") == "valid":
            r["order_repaired"] = False
        elif enable_llm and llm_client is not None and repair.get("decision") != "valid":
            llm_repair = repair_order_by_llm(r, llm_client, config)
            conf = float(llm_repair.get("confidence") or 0)
            if llm_repair.get("decision") == "repair" and conf >= min_llm_conf:
                r["composition_order"] = llm_repair.get("repaired_composition_order", [])
                r["order_repaired"] = True
                r["order_repair_meta"] = llm_repair
                repaired_rows.append({"problem_id": r.get("problem_id"), **llm_repair})
            elif conf < min_llm_conf:
                manual_review.append({**r, "repair_meta": llm_repair})
                continue
            else:
                manual_review.append({**r, "repair_meta": repair})
                continue
        else:
            manual_review.append({**r, "repair_meta": repair})
            continue

        r = normalize_row(r)
        if compute_order_completeness_score(r) < 1.0 and config.get("filter", {}).get(
            "require_complete_order", True
        ):
            manual_review.append(r)
            continue
        repair_log.append(r)

    return repair_log, manual_review
