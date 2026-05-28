from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any


def group_by_primary_subtype(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        key = str(row.get("primary_subtype") or "")
        if key:
            groups[key].append(row)
    return dict(groups)


def classify_subtype_status(num_rows: int, config: dict[str, Any]) -> str:
    gc = config.get("grouping", config)
    stable_min = int(gc.get("stable_min_rows", 10))
    provisional_min = int(gc.get("provisional_min_rows", 5))
    if num_rows >= stable_min:
        return "stable"
    if num_rows >= provisional_min:
        return "provisional"
    return "hold"


def classify_evidence_status(rows: list[dict[str, Any]], config: dict[str, Any]) -> str:
    if not config.get("additional", {}).get("enabled", False):
        return classify_subtype_status(len(rows), config)
    verified_count = sum(1 for row in rows if row.get("evidence_origin") == "taco_verified")
    status = classify_subtype_status(verified_count, config)
    if status != "hold":
        return status
    allow_seed = config.get("grouping", {}).get("allow_seed_with_curated", False)
    min_rows = int(config.get("representative_selection", {}).get("min_examples_per_skill", 5))
    if allow_seed and len(rows) >= min_rows and any(row.get("evidence_origin") == "curated" for row in rows):
        return "seed"
    return "hold"


def summarize_groups(groups: dict[str, list[dict[str, Any]]], config: dict[str, Any]) -> dict[str, Any]:
    summary: dict[str, Any] = {}
    status_counts: Counter[str] = Counter()
    for subtype, rows in sorted(groups.items()):
        status = classify_evidence_status(rows, config)
        status_counts[status] += 1
        families = Counter(str(r.get("detected_single_skill") or "") for r in rows)
        tiers = Counter(str(r.get("evidence_tier") or "") for r in rows)
        summary[subtype] = {
            "num_rows": len(rows),
            "num_taco_verified_rows": sum(1 for row in rows if row.get("evidence_origin") == "taco_verified"),
            "status": status,
            "algorithm_family": families.most_common(1)[0][0] if families else "",
            "evidence_tiers": dict(tiers),
            "avg_subtype_confidence": round(
                sum(float(r.get("subtype_confidence") or 0) for r in rows) / max(len(rows), 1),
                4,
            ),
        }
    return {
        "subtype_summary": summary,
        "num_primary_subtypes": len(groups),
        "num_stable_subtypes": status_counts.get("stable", 0),
        "num_provisional_subtypes": status_counts.get("provisional", 0),
        "num_hold_subtypes": status_counts.get("hold", 0),
    }
