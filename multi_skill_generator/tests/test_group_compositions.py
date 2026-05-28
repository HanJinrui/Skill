from src.group_compositions import classify_composition_status, is_classic_composition


def test_classic_provisional():
    sig = ("sorting_custom_key", "greedy_sorting_order")
    assert is_classic_composition(sig)
    config = {"grouping": {"stable_min_rows": 5, "provisional_min_rows": 3, "classic_min_rows": 2}}
    assert classify_composition_status(2, sig, config) == "provisional_classic"


def test_hold():
    config = {"grouping": {"stable_min_rows": 5, "provisional_min_rows": 3, "classic_min_rows": 2}}
    assert classify_composition_status(1, ("x", "y"), config) == "hold"
