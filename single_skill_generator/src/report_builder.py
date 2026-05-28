from __future__ import annotations

from collections import Counter
from typing import Any

from .group_rows import classify_evidence_status, summarize_groups
from .schema import missing_row_fields


def build_filtering_report(
    rows: list[dict[str, Any]],
    hard_filtered: list[dict[str, Any]],
    generation_filtered: list[dict[str, Any]],
    config: dict[str, Any],
) -> dict[str, Any]:
    missing_counts: Counter[str] = Counter()
    for row in rows:
        for field in missing_row_fields(row):
            missing_counts[field] += 1

    return {
        "total_rows": len(rows),
        "hard_filtered_rows": len(hard_filtered),
        "generation_filtered_rows": len(generation_filtered),
        "filter_config": config.get("filter", {}),
        "missing_field_counts": dict(missing_counts),
        "evidence_tier_distribution": dict(
            Counter(str(r.get("evidence_tier") or "") for r in generation_filtered)
        ),
        "primary_subtype_distribution": dict(
            Counter(str(r.get("primary_subtype") or "") for r in generation_filtered)
        ),
    }


def build_grouping_report(groups: dict[str, list[dict[str, Any]]], config: dict[str, Any]) -> dict[str, Any]:
    return summarize_groups(groups, config)


def build_generation_report(
    *,
    input_file: str,
    total_rows: int,
    hard_filtered_rows: int,
    generation_filtered_rows: int,
    config: dict[str, Any],
    groups: dict[str, list[dict[str, Any]]],
    skills: list[dict[str, Any]],
    held_subtypes: list[str] | None = None,
) -> dict[str, Any]:
    group_summary = summarize_groups(groups, config)
    accepted = []
    revised = []
    rejected = []
    for sk in skills:
        sid = sk.get("skill_id", "")
        decision = (sk.get("quality_control") or {}).get("final_decision", "")
        if decision == "accept":
            accepted.append(sid)
        elif decision == "revise":
            revised.append(sid)
        else:
            rejected.append(sid)

    stable_skills = sum(
        1 for sk in skills if sk.get("status") == "stable" and (sk.get("quality_control") or {}).get("final_decision") == "accept"
    )
    provisional_skills = sum(
        1
        for sk in skills
        if sk.get("status") == "provisional" and (sk.get("quality_control") or {}).get("final_decision") == "accept"
    )
    seed_skills = sum(
        1
        for sk in skills
        if sk.get("status") == "seed" and (sk.get("quality_control") or {}).get("final_decision") == "accept"
    )

    held = held_subtypes or [
        st for st, rows in groups.items() if classify_evidence_status(rows, config) == "hold"
    ]

    return {
        "input_file": input_file,
        "total_rows": total_rows,
        "hard_filtered_rows": hard_filtered_rows,
        "generation_filtered_rows": generation_filtered_rows,
        "filter_config": config.get("filter", {}),
        "num_primary_subtypes": group_summary["num_primary_subtypes"],
        "num_generated_skills": len(skills),
        "num_stable_skills": stable_skills,
        "num_provisional_skills": provisional_skills,
        "num_seed_skills": seed_skills,
        "num_hold_subtypes": group_summary["num_hold_subtypes"],
        "subtype_summary": group_summary["subtype_summary"],
        "accepted_skills": accepted,
        "revised_skills": revised,
        "rejected_skills": rejected,
        "held_subtypes": held,
    }
