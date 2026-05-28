from src.normalize_composition import (
    build_composition_signature,
    extract_subtype_names,
    normalize_row,
)


def test_extract_subtype_names():
    row = {
        "composition_subtypes": [
            {"subtype": "sorting_custom_key", "role": "sort"},
            {"subtype": "greedy_sorting_order", "role": "greedy"},
        ]
    }
    assert extract_subtype_names(row) == ["sorting_custom_key", "greedy_sorting_order"]


def test_build_signature_ordered():
    row = {
        "composition_subtypes": [
            {"subtype": "a"},
            {"subtype": "b"},
        ],
        "composition_order": ["a", "b"],
    }
    assert build_composition_signature(normalize_row(row)) == ("a", "b")


def test_binary_lookup_is_split_from_answer_search():
    row = {
        "composition_subtypes": [
            {"subtype": "sorting_binary_search_answer", "role": "find predecessor index"},
            {"subtype": "dp_1d_state", "role": "dp transition"},
        ],
        "composition_order": ["sorting_binary_search_answer", "dp_1d_state"],
        "core_composition_summary": "Binary search on sorted coordinates to find predecessor index, then DP.",
    }
    assert normalize_row(row)["composition_signature"] == [
        "sorting_binary_search_lookup",
        "dp_1d_state",
    ]


def test_binary_answer_search_remains_answer_search():
    row = {
        "composition_subtypes": [
            {"subtype": "sorting_binary_search_answer"},
            {"subtype": "dp_1d_state"},
        ],
        "composition_order": ["sorting_binary_search_answer", "dp_1d_state"],
        "core_composition_summary": "Binary search on answer; DP checks if the threshold is feasible.",
    }
    assert normalize_row(row)["composition_signature"][0] == "sorting_binary_search_answer"


def test_binary_answer_phrase_without_on_remains_answer_search():
    row = {
        "composition_subtypes": [{"subtype": "sorting_binary_search_answer"}],
        "composition_order": ["sorting_binary_search_answer"],
        "core_composition_summary": "Sort values, then binary search answer to find a threshold rank.",
    }
    assert normalize_row(row)["composition_signature"][0] == "sorting_binary_search_answer"
