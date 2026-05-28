from src.skill_validator import validate_order_consistency, validate_representative_examples


def test_order_consistency():
    skill = {
        "composition_signature": ["a", "b"],
        "algorithm_flow": [
            {"step": 1, "algorithm": "a", "role": "r", "input": "i", "output": "o", "handoff_to_next": "h"},
            {"step": 2, "algorithm": "b", "role": "r", "input": "i", "output": "o"},
        ],
    }
    ok, errs = validate_order_consistency(skill, ["a", "b"])
    assert ok and not errs


def test_representative_examples_reject_strings_and_missing_fields():
    ok, errs = validate_representative_examples({"representative_examples": ["p1"]})
    assert not ok
    assert "must be object" in errs[0]

    ok, errs = validate_representative_examples(
        {"representative_examples": [{"problem_id": "p1", "solution_id": "s1"}]}
    )
    assert not ok
    assert any("why_representative" in err for err in errs)
