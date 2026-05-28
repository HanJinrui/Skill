from src.filter_rows import hard_filter


def test_hard_filter_multi():
    config = {"filter": {"min_subtype_confidence": 0.9, "algorithm_scope": "multi"}}
    row = {
        "syntax_ok": True,
        "safe_exec_ok": True,
        "full_pass": True,
        "pass_rate": 1.0,
        "algorithm_scope": "multi",
        "composition_subtypes": [{"subtype": "a"}, {"subtype": "b"}],
        "subtype_confidence": 0.95,
    }
    assert hard_filter(row, config) is True


def test_hard_filter_rejects_single():
    config = {"filter": {"min_subtype_confidence": 0.9}}
    row = {
        "syntax_ok": True,
        "safe_exec_ok": True,
        "full_pass": True,
        "pass_rate": 1.0,
        "algorithm_scope": "single",
        "composition_subtypes": [{"subtype": "a"}, {"subtype": "b"}],
        "subtype_confidence": 0.95,
    }
    assert hard_filter(row, config) is False
