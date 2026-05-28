from __future__ import annotations

from collections import Counter
from typing import Any

from .filter_rows import build_filtering_report
from .group_compositions import summarize_composition_groups
from .relation_classifier import COMPOSITION_RELATIONS
from .scoring import compute_quality_score


def build_normalization_report(rows: list[dict[str, Any]]) -> dict[str, Any]:
    repaired = sum(1 for r in rows if r.get("order_repaired"))
    complete = sum(
        1
        for r in rows
        if len(r.get("composition_signature") or []) >= 2
        and r.get("composition_signature")
    )
    return {
        "total_normalized_rows": len(rows),
        "repaired_order_rows": repaired,
        "rows_with_signature": complete,
    }


def build_grouping_report(groups: dict[tuple[str, ...], list[dict[str, Any]]], config: dict) -> dict:
    return summarize_composition_groups(groups, config)


def build_relation_report(generation_inputs: list[dict[str, Any]]) -> dict[str, Any]:
    dist = Counter(gi.get("composition_relation") or "unknown" for gi in generation_inputs)
    return {
        "relation_distribution": dict(dist),
        "known_relations": COMPOSITION_RELATIONS,
    }


def build_evidence_map(
    skills: list[dict[str, Any]],
    generation_inputs: list[dict[str, Any]],
) -> dict[str, Any]:
    gi_by_id = {gi.get("skill_id"): gi for gi in generation_inputs}
    evidence_map: dict[str, Any] = {}

    for skill in skills:
        sid = str(skill.get("skill_id") or "")
        gi = gi_by_id.get(sid)
        if not gi:
            sig = skill.get("composition_signature") or []
            gi = next(
                (g for g in generation_inputs if g.get("composition_signature") == sig),
                None,
            )
        if not gi:
            continue
        all_rows = gi.get("all_source_rows") or []
        reps = gi.get("representative_samples") or []
        evidence_map[sid] = {
            "composition_signature": gi.get("composition_signature"),
            "composition_relation": gi.get("composition_relation"),
            "status": gi.get("status"),
            "all_source_rows": [
                {
                    "problem_id": r.get("problem_id"),
                    "solution_id": r.get("solution_id"),
                    "source_dataset": r.get("source_dataset", "TACO"),
                    "source_language": r.get("source_language"),
                    "verification_source": r.get("verification_source", "taco-verified"),
                    "source_problem_fingerprint": r.get("source_problem_fingerprint"),
                    "quality_score": round(
                        float(r.get("quality_score") or compute_quality_score(r)), 4
                    ),
                    "subtype_confidence": r.get("subtype_confidence"),
                    "composition_order": r.get("normalized_composition_order")
                    or r.get("composition_order"),
                    "order_repaired": bool(r.get("order_repaired")),
                }
                for r in all_rows
            ],
            "representative_rows": [
                {
                    "problem_id": s.get("problem_id"),
                    "solution_id": s.get("solution_id"),
                    "source_dataset": s.get("source_dataset", "TACO"),
                    "source_language": s.get("source_language"),
                    "representative_score": s.get("representative_score"),
                    "core_composition_summary": s.get("core_composition_summary"),
                    "why_representative": s.get("why_representative"),
                }
                for s in reps
            ],
        }
    return evidence_map


def build_generation_report(
    *,
    input_file: str,
    total_rows: int,
    hard_filtered_rows: int,
    valid_order_rows: int,
    repaired_order_rows: int,
    manual_review_rows: int,
    config: dict[str, Any],
    groups: dict[tuple[str, ...], list[dict[str, Any]]],
    generation_inputs: list[dict[str, Any]],
    skills: list[dict[str, Any]],
) -> dict[str, Any]:
    group_summary = summarize_composition_groups(groups, config)
    accepted = [s for s in skills if (s.get("quality_control") or {}).get("final_decision") == "accept"]
    review_required = [
        s
        for s in skills
        if (s.get("quality_control") or {}).get("final_decision") == "provisional_review_required"
    ]
    revised = [s for s in skills if (s.get("quality_control") or {}).get("final_decision") == "revise"]
    rejected = [s for s in skills if (s.get("quality_control") or {}).get("final_decision") == "reject"]

    status_counts = Counter(s.get("status") for s in accepted + review_required)
    dataset_counts = Counter(
        str(row.get("source_dataset") or "TACO")
        for gi in generation_inputs
        for row in (gi.get("all_source_rows") or [])
    )

    return {
        "input_file": input_file,
        "total_rows": total_rows,
        "hard_filtered_rows": hard_filtered_rows,
        "valid_order_rows": valid_order_rows,
        "repaired_order_rows": repaired_order_rows,
        "manual_review_rows": manual_review_rows,
        "num_composition_signatures": len(groups),
        "num_generation_inputs": len(generation_inputs),
        "num_generated_skills": len(skills),
        "num_stable_skills": status_counts.get("stable", 0),
        "num_provisional_skills": status_counts.get("provisional", 0),
        "num_provisional_classic_skills": status_counts.get("provisional_classic", 0),
        "num_hold_compositions": group_summary.get("num_hold", 0),
        "top_composition_signatures": group_summary.get("top_composition_signatures", []),
        "relation_distribution": build_relation_report(generation_inputs).get(
            "relation_distribution", {}
        ),
        "accepted_skills": [s.get("skill_id") for s in accepted],
        "provisional_review_required_skills": [s.get("skill_id") for s in review_required],
        "revised_skills": [s.get("skill_id") for s in revised],
        "rejected_skills": [s.get("skill_id") for s in rejected],
        "filter_config": config.get("filter", {}),
        "validation_summary": {
            "accepted": len(accepted),
            "provisional_review_required": len(review_required),
            "revised": len(revised),
            "rejected": len(rejected),
        },
        "generation_evidence_source_dataset_counts": dict(dataset_counts),
    }


__all__ = [
    "build_filtering_report",
    "build_normalization_report",
    "build_grouping_report",
    "build_relation_report",
    "build_evidence_map",
    "build_generation_report",
]
