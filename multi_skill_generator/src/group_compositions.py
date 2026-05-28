from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any

CLASSIC_COMPOSITIONS: set[tuple[str, ...]] = {
    ("sorting_custom_key", "greedy_sorting_order"),
    ("sorting_custom_key", "greedy_two_pointers"),
    ("sorting_custom_key", "amortized_two_pointers"),
    ("sorting_binary_search_answer", "greedy_sorting_order"),
    ("sorting_binary_search_answer", "greedy_two_pointers"),
    ("sorting_binary_search_answer", "dp_1d_state"),
    ("ds_heap_priority_queue", "greedy_priority_queue"),
    ("sorting_custom_key", "ds_heap_priority_queue", "greedy_priority_queue"),
    ("dp_2d_state", "dp_interval"),
    ("dp_interval", "dp_1d_state"),
    ("search_bitmask_enumeration", "dp_bitmask"),
}


def group_by_composition_signature(
    rows: list[dict[str, Any]],
) -> dict[tuple[str, ...], list[dict[str, Any]]]:
    groups: dict[tuple[str, ...], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        sig = tuple(row.get("composition_signature") or row.get("normalized_composition_order") or [])
        if len(sig) >= 2:
            groups[sig].append(row)
    return dict(groups)


def is_classic_composition(signature: tuple[str, ...]) -> bool:
    return signature in CLASSIC_COMPOSITIONS


def classify_composition_status(
    num_rows: int,
    signature: tuple[str, ...],
    config: dict[str, Any],
) -> str:
    gc = config.get("grouping", config)
    stable_min = int(gc.get("stable_min_rows", 5))
    provisional_min = int(gc.get("provisional_min_rows", 3))
    classic_min = int(gc.get("classic_min_rows", 2))

    if num_rows >= stable_min:
        return "stable"
    if num_rows >= provisional_min:
        return "provisional"
    if is_classic_composition(signature) and num_rows >= classic_min:
        return "provisional_classic"
    return "hold"


def summarize_composition_groups(
    groups: dict[tuple[str, ...], list[dict[str, Any]]],
    config: dict[str, Any],
) -> dict[str, Any]:
    summary: dict[str, Any] = {}
    status_counts: Counter[str] = Counter()
    for sig, rows in sorted(groups.items(), key=lambda x: -len(x[1])):
        status = classify_composition_status(len(rows), sig, config)
        status_counts[status] += 1
        sig_str = " -> ".join(sig)
        summary[sig_str] = {
            "composition_signature": list(sig),
            "num_rows": len(rows),
            "status": status,
            "avg_subtype_confidence": round(
                sum(float(r.get("subtype_confidence") or 0) for r in rows) / max(len(rows), 1),
                4,
            ),
        }
    top = sorted(
        [(list(k), len(v)) for k, v in groups.items()],
        key=lambda x: -x[1],
    )[:20]
    return {
        "group_summary": summary,
        "num_composition_signatures": len(groups),
        "num_stable": status_counts.get("stable", 0),
        "num_provisional": status_counts.get("provisional", 0),
        "num_provisional_classic": status_counts.get("provisional_classic", 0),
        "num_hold": status_counts.get("hold", 0),
        "top_composition_signatures": [{"signature": s, "count": c} for s, c in top],
    }
