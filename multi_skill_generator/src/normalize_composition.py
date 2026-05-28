from __future__ import annotations

import re
from typing import Any

BINARY_SEARCH_ANSWER = "sorting_binary_search_answer"
BINARY_SEARCH_LOOKUP = "sorting_binary_search_lookup"
LOOKUP_SIGNALS = (
    "binary search per query",
    "binary searches per query",
    "binary search for predecessor",
    "binary search on sorted",
    "predecessor index",
    "nearest position",
    "lower_bound",
    "upper_bound",
    "bisect",
    "earliest index",
)
ANSWER_SEARCH_SIGNALS = (
    "binary search on answer",
    "binary search answer",
    "binary search on max",
    "binary search for minimal",
    "binary search for maximum",
    "maximum feasible",
    "minimum feasible",
    "feasibility checker",
    "checks if",
    "check if",
)


def extract_subtype_names(row: dict[str, Any]) -> list[str]:
    names: list[str] = []
    for item in row.get("composition_subtypes") or []:
        if isinstance(item, dict):
            st = str(item.get("subtype") or "").strip()
            if st:
                names.append(st)
        elif isinstance(item, str) and item.strip():
            names.append(item.strip())
    return names


def extract_subtype_roles(row: dict[str, Any]) -> dict[str, str]:
    roles: dict[str, str] = {}
    for item in row.get("composition_subtypes") or []:
        if isinstance(item, dict):
            st = str(item.get("subtype") or "").strip()
            role = str(item.get("role") or "").strip()
            if st:
                roles[st] = role
    return roles


def normalize_composition_order(row: dict[str, Any]) -> list[str]:
    raw = row.get("composition_order") or row.get("primary_composition_subtypes") or []
    if not isinstance(raw, list):
        return []
    return [str(x).strip() for x in raw if str(x).strip()]


def classify_binary_search_subtype(row: dict[str, Any]) -> str:
    """Separate value/position lookup from parametric search on an answer."""
    text = " ".join(
        [
            str(row.get("core_composition_summary") or ""),
            " ".join(
                str(item.get("role") or "")
                for item in row.get("composition_subtypes") or []
                if isinstance(item, dict)
            ),
            str(row.get("solution_code") or "")[:4000],
        ]
    ).lower()
    if any(signal in text for signal in ANSWER_SEARCH_SIGNALS):
        return BINARY_SEARCH_ANSWER
    if any(signal in text for signal in LOOKUP_SIGNALS):
        return BINARY_SEARCH_LOOKUP
    if re.search(r"\b(?:bisect_left|bisect_right|lower_bound|upper_bound)\b", text):
        return BINARY_SEARCH_LOOKUP
    return BINARY_SEARCH_ANSWER


def _rewrite_binary_search_labels(row: dict[str, Any]) -> dict[str, Any]:
    out = dict(row)
    subtype = classify_binary_search_subtype(row)
    for field in ("composition_order", "primary_composition_subtypes"):
        raw = out.get(field)
        if isinstance(raw, list):
            out[field] = [subtype if item == BINARY_SEARCH_ANSWER else item for item in raw]
    raw_subtypes = out.get("composition_subtypes")
    if isinstance(raw_subtypes, list):
        rewritten: list[Any] = []
        for item in raw_subtypes:
            if isinstance(item, dict) and item.get("subtype") == BINARY_SEARCH_ANSWER:
                item = {**item, "subtype": subtype}
            elif item == BINARY_SEARCH_ANSWER:
                item = subtype
            rewritten.append(item)
        out["composition_subtypes"] = rewritten
    return out


def build_composition_signature(row: dict[str, Any]) -> tuple[str, ...]:
    order = row.get("normalized_composition_order")
    if order is None:
        order = normalize_composition_order(row)
    return tuple(order)


def normalize_row(row: dict[str, Any]) -> dict[str, Any]:
    out = _rewrite_binary_search_labels(row)
    out["composition_subtype_names"] = extract_subtype_names(out)
    out["composition_roles"] = extract_subtype_roles(out)
    order = normalize_composition_order(out)
    out["normalized_composition_order"] = order
    out["composition_signature"] = list(build_composition_signature(out))
    families = row.get("composition_families") or []
    if isinstance(families, list):
        out["composition_families_normalized"] = [str(f) for f in families]
    else:
        out["composition_families_normalized"] = []
    return out
