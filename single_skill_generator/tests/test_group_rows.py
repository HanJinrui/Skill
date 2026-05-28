from src.group_rows import classify_evidence_status, classify_subtype_status, group_by_primary_subtype


CONFIG = {"grouping": {"stable_min_rows": 10, "provisional_min_rows": 5}}


def test_group_by_primary_subtype():
    rows = [
        {"primary_subtype": "dp_1d_state"},
        {"primary_subtype": "dp_2d_state"},
        {"primary_subtype": "dp_1d_state"},
    ]
    groups = group_by_primary_subtype(rows)
    assert len(groups) == 2
    assert len(groups["dp_1d_state"]) == 2


def test_classify_subtype_status():
    assert classify_subtype_status(12, CONFIG) == "stable"
    assert classify_subtype_status(7, CONFIG) == "provisional"
    assert classify_subtype_status(3, CONFIG) == "hold"


def test_additional_curated_rows_are_seed_not_stable():
    config = {
        **CONFIG,
        "additional": {"enabled": True},
        "representative_selection": {"min_examples_per_skill": 5},
        "grouping": {**CONFIG["grouping"], "allow_seed_with_curated": True},
    }
    rows = [{"evidence_origin": "curated"} for _ in range(5)]
    assert classify_evidence_status(rows, config) == "seed"
