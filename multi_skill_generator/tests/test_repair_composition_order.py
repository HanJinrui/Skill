from src.repair_composition_order import check_order_consistency, repair_order_by_rules


def test_check_complete():
    row = {
        "composition_subtypes": [{"subtype": "a"}, {"subtype": "b"}],
        "composition_order": ["a", "b"],
    }
    assert check_order_consistency(row)["complete"] is True


def test_repair_binary_search_outer():
    row = {
        "composition_subtypes": [
            {"subtype": "sorting_binary_search_answer"},
            {"subtype": "greedy_sorting_order"},
        ],
        "composition_order": ["greedy_sorting_order", "sorting_binary_search_answer"],
        "core_composition_summary": "binary search on answer with greedy check",
        "solution_code": "bisect",
    }
    repair = repair_order_by_rules(row)
    assert repair["decision"] == "repair"
    assert repair["repaired_composition_order"][0] == "sorting_binary_search_answer"
