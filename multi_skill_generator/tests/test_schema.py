from src.schema import REQUIRED_SKILL_FIELDS, skill_template


def test_template_has_required():
    tmpl = skill_template()
    for f in REQUIRED_SKILL_FIELDS:
        assert f in tmpl
