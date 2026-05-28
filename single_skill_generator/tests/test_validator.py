from src.skill_validator import (
    score_skill,
    validate_no_leakage,
    validate_evidence_consistency,
    validate_normalized_skill_schema,
    validate_skill_schema,
)


def _minimal_skill():
    return {
        "skill_id": "single.dp_1d_state.v1",
        "skill_name": "One-dimensional DP",
        "skill_type": "single_algorithm",
        "algorithm_family": "dynamic_programming",
        "primary_subtype": "dp_1d_state",
        "trigger_signals": ["linear state"],
        "applicability_conditions": ["one dimension"],
        "non_applicability_conditions": ["two dimensions"],
        "core_mechanism": "Define dp[i] and transition from smaller states.",
        "algorithm_steps": ["init", "transition", "answer"],
        "state_or_structure_design": "dp array",
        "transition_or_decision_rule": "combine predecessors",
        "code_template": "def solve():\n    dp = [0] * n\n    return dp[-1]",
        "template_type": "executable_python",
        "common_pitfalls": ["wrong order"],
        "retrieval_keywords": ["dp", "1d"],
        "complexity_pattern": {"time": "O(n)", "space": "O(n)", "notes": ""},
        "related_subtypes": {
            "similar": [],
            "prerequisite": [],
            "often_combined_with": [],
            "should_not_confuse_with": [],
        },
        "canonical_subtype": "dp_1d_state",
        "alias_subtypes": [],
        "related_existing_subtypes": [],
        "related_future_subtypes": [],
    }


def test_validate_skill_schema_passes_minimal():
    ok, errs = validate_skill_schema(_minimal_skill())
    assert ok, errs


def test_validate_normalized_skill_schema_rejects_invalid_python_template():
    skill = _minimal_skill()
    skill["code_template"] = "def solve(...):\n    pass\n"
    ok, errs = validate_normalized_skill_schema(skill)
    assert not ok
    assert any("parse as Python" in error for error in errs)


def test_executable_template_rejects_explicit_placeholder_but_pseudocode_allows_it():
    skill = _minimal_skill()
    skill["code_template"] = "def solve(values):\n    result = ...\n    return result\n"
    ok, errs = validate_normalized_skill_schema(skill)
    assert not ok
    assert any("must not contain pass or ellipsis" in error for error in errs)
    skill["template_type"] = "pseudocode_python"
    ok, errs = validate_normalized_skill_schema(skill)
    assert ok, errs


def test_representative_example_count_must_match_evidence():
    skill = _minimal_skill()
    skill["representative_examples"] = [{"problem_id": "p1"}]
    skill["evidence"] = {"num_representative_rows": 5}
    ok, errs = validate_evidence_consistency(skill)
    assert not ok
    assert "5 != 1" in errs[0]


def test_validate_no_leakage_detects_long_copy():
    skill = _minimal_skill()
    repeated = " ".join(["leaktoken"] * 60)
    skill["core_mechanism"] = repeated
    row = {"problem_statement": repeated, "solution_code": "a = 1\nb = 2\n"}
    ok, issues = validate_no_leakage(skill, [row], {"validation": {"max_repeated_problem_tokens": 10}})
    assert not ok
    assert issues


def test_score_skill_computes_final():
    scores = score_skill(_minimal_skill(), {"abstraction_score": 0.9, "consistency_score": 0.9})
    assert scores["final_score"] >= 0.8
