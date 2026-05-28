from __future__ import annotations

from typing import Any

REQUIRED_SKILL_FIELDS = [
    "skill_id",
    "skill_name",
    "skill_type",
    "version",
    "status",
    "composition_signature",
    "composition_relation",
    "trigger_signals",
    "applicability_conditions",
    "non_applicability_conditions",
    "core_composition_mechanism",
    "why_multiple_algorithms_are_needed",
    "algorithm_flow",
    "state_interface",
    "composition_invariants",
    "correctness_argument_pattern",
    "complexity_pattern",
    "implementation_template",
    "common_pitfalls",
    "representative_examples",
    "evidence",
    "quality_control",
]

SKILL_ID_PATTERN = r"^multi\.[a-z0-9_]+(__[a-z0-9_]+)*\.v\d+$"
REQUIRED_REPRESENTATIVE_EXAMPLE_FIELDS = (
    "problem_id",
    "solution_id",
    "why_representative",
)


def skill_template() -> dict[str, Any]:
    return {
        "skill_id": "",
        "skill_name": "",
        "skill_type": "multi_algorithm",
        "version": "v1",
        "status": "stable",
        "source_dataset": "",
        "generation_method": "composition_signature_distillation",
        "composition_signature": [],
        "composition_families": [],
        "composition_relation": "",
        "trigger_signals": [],
        "applicability_conditions": [],
        "non_applicability_conditions": [],
        "core_composition_mechanism": "",
        "why_multiple_algorithms_are_needed": "",
        "algorithm_flow": [],
        "state_interface": {
            "input_state": "",
            "intermediate_state": "",
            "output_state": "",
            "handoff_description": "",
        },
        "composition_invariants": [],
        "correctness_argument_pattern": "",
        "complexity_pattern": {"time": "", "space": "", "dominant_factor": ""},
        "implementation_template": "",
        "implementation_notes": [],
        "common_pitfalls": [],
        "confusable_compositions": {"similar": [], "should_not_confuse_with": []},
        "representative_examples": [],
        "evidence": {},
        # Populated by skill_validator.py after generation, never by the LLM.
        "quality_control": {},
    }


def multi_skill_schema_json() -> str:
    import json

    return json.dumps(skill_template(), ensure_ascii=False, indent=2)
