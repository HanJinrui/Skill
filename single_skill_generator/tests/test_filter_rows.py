from src.filter_rows import generation_filter, hard_filter


def _row(**kwargs):
    base = {
        "syntax_ok": True,
        "safe_exec_ok": True,
        "full_pass": True,
        "pass_rate": 1.0,
        "algorithm_scope": "single",
        "is_true_composition": False,
        "is_primary_solution": True,
        "taco_family_alignment": True,
        "primary_subtype": "dp_1d_state",
        "detected_single_skill": "dynamic_programming",
        "evidence_tier": "gold",
        "subtype_confidence": 0.9,
    }
    base.update(kwargs)
    return base


CONFIG = {
    "filter": {
        "evidence_tier": "gold",
        "min_subtype_confidence": 0.85,
    }
}


def test_hard_filter_accepts_valid_row():
    assert hard_filter(_row(), CONFIG) is True


def test_hard_filter_rejects_composition():
    assert hard_filter(_row(is_true_composition=True), CONFIG) is False


def test_generation_filter_requires_gold_and_confidence():
    assert generation_filter(_row(), CONFIG) is True
    assert generation_filter(_row(evidence_tier="silver"), CONFIG) is False
    assert generation_filter(_row(subtype_confidence=0.5), CONFIG) is False


def test_generation_filter_accepts_executed_curated_when_enabled():
    config = {
        "filter": {
            "accepted_evidence_tiers": ["gold", "curated"],
            "allow_curated_evidence": True,
            "min_subtype_confidence": 0.85,
        }
    }
    row = _row(
        taco_family_alignment=False,
        evidence_tier="curated",
        evidence_origin="curated",
        evidence_validation="executed_tests",
    )
    assert generation_filter(row, config) is True
