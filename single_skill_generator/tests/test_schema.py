from src.schema import missing_row_fields, skill_template


def test_skill_template_has_required_keys():
    tmpl = skill_template()
    assert tmpl["skill_type"] == "single_algorithm"
    assert "evidence" in tmpl
    assert "quality_control" in tmpl


def test_missing_row_fields():
    row = {"problem_id": "p1"}
    missing = missing_row_fields(row)
    assert "solution_code" in missing
    assert "primary_subtype" in missing
