from __future__ import annotations

from typing import Any

REQUIRED_ROW_FIELDS = [
    "problem_id",
    "solution_id",
    "solution_code",
    "problem_statement",
    "syntax_ok",
    "safe_exec_ok",
    "full_pass",
    "pass_rate",
    "algorithm_scope",
    "is_true_composition",
    "is_primary_solution",
    "primary_subtype",
    "detected_single_skill",
    "subtype_confidence",
    "evidence_tier",
    "rule_confidence",
    "primary_solution_score",
    "taco_family_alignment",
    "candidate_subtypes",
    "ast_features",
    "core_mechanism_summary",
    "subtype_rationale",
    "original_tags",
    "problem_families",
]

REQUIRED_SKILL_FIELDS = [
    "skill_id",
    "skill_name",
    "skill_type",
    "algorithm_family",
    "primary_subtype",
    "trigger_signals",
    "applicability_conditions",
    "non_applicability_conditions",
    "core_mechanism",
    "algorithm_steps",
    "code_template",
    "common_pitfalls",
    "retrieval_keywords",
]

SKILL_ID_PATTERN = r"^single\.[a-z0-9_]+\.v\d+$"


def missing_row_fields(row: dict[str, Any]) -> list[str]:
    return [f for f in REQUIRED_ROW_FIELDS if f not in row]


def skill_template() -> dict[str, Any]:
    return {
        "skill_id": "",
        "skill_name": "",
        "skill_type": "single_algorithm",
        "version": "v1",
        "status": "stable",
        "algorithm_family": "",
        "primary_subtype": "",
        "canonical_subtype": "",
        "alias_subtypes": [],
        "source_dataset": "TACO",
        "generation_method": "subtype_group_distillation",
        "trigger_signals": [],
        "applicability_conditions": [],
        "non_applicability_conditions": [],
        "core_mechanism": "",
        "algorithm_steps": [],
        "state_or_structure_design": "",
        "transition_or_decision_rule": "",
        "complexity_pattern": {"time": "", "space": "", "notes": ""},
        "code_template": "",
        "template_type": "executable_python",
        "implementation_notes": [],
        "common_pitfalls": [],
        "retrieval_keywords": [],
        "related_subtypes": {
            "similar": [],
            "prerequisite": [],
            "often_combined_with": [],
            "should_not_confuse_with": [],
        },
        "related_existing_subtypes": [],
        "related_future_subtypes": [],
        "representative_examples": [],
        "evidence": {
            "num_source_rows": 0,
            "num_representative_rows": 0,
            "evidence_tiers": {},
            "avg_subtype_confidence": 0.0,
            "source_problem_ids": [],
            "evidence_origin_counts": {},
        },
        "quality_control": {
            "schema_valid": False,
            "abstraction_check": "",
            "leakage_check": "",
            "consistency_check": "",
            "final_decision": "",
        },
    }
