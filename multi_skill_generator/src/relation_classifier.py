from __future__ import annotations

from typing import Any

COMPOSITION_RELATIONS = [
    "ordered_preprocessing_then_greedy",
    "ordered_scan_then_two_pointers",
    "answer_search_with_checker",
    "preprocessing_then_dp",
    "dp_table_then_interval_optimization",
    "data_structure_accelerated_greedy",
    "sorted_sweep_with_data_structure",
    "sorted_sweep_with_priority_queue",
    "hash_grouping_then_ordered_processing",
    "ordered_processing_with_hash_index",
    "dp_with_amortized_pointer_optimization",
    "ordered_preprocessing_then_binary_search",
    "ordered_lookup_then_dp",
    "enumeration_with_bitmask_state",
    "search_with_memoized_dp",
    "multi_stage_dynamic_programming",
    "other_composition",
]

RELATION_DESCRIPTIONS = {
    "ordered_preprocessing_then_greedy": "Sort/preprocess to expose order, then greedy along that order.",
    "ordered_scan_then_two_pointers": "Sorted scan enables two-pointer or amortized pointer moves.",
    "answer_search_with_checker": "Binary search on answer with feasibility checker.",
    "preprocessing_then_dp": "Sorting or ordering reduces DP state space or order.",
    "dp_table_then_interval_optimization": "Table DP feeds interval or 1D optimization.",
    "data_structure_accelerated_greedy": "Heap/hash/set accelerates greedy decisions.",
    "sorted_sweep_with_data_structure": "Sweep line with dynamic structure maintenance.",
    "sorted_sweep_with_priority_queue": "Sorted event processing maintains active choices in a priority queue.",
    "hash_grouping_then_ordered_processing": "Hash grouping then ordered greedy/scan.",
    "ordered_processing_with_hash_index": "Sorted processing constructs or queries a hash-based index.",
    "dp_with_amortized_pointer_optimization": "One-dimensional DP uses monotone pointer progress to avoid repeated transitions.",
    "ordered_preprocessing_then_binary_search": "Ordered preprocessing enables repeated binary lookup or subsequent parametric search.",
    "ordered_lookup_then_dp": "Binary lookup on ordered positions provides DP predecessor or transition boundaries.",
    "enumeration_with_bitmask_state": "Bitmask enumeration combined with DP state.",
    "search_with_memoized_dp": "Search layer with memoized DP.",
    "multi_stage_dynamic_programming": "Multiple DP stages in sequence.",
    "other_composition": "Other multi-algorithm collaboration pattern.",
}


def classify_relation(signature: tuple[str, ...], rows: list[dict[str, Any]] | None = None) -> str:
    del rows
    s = list(signature)

    if s and s[0] == "sorting_binary_search_answer":
        return "answer_search_with_checker"

    if s == ["sorting_binary_search_lookup", "dp_1d_state"]:
        return "ordered_lookup_then_dp"

    if s == ["sorting_custom_key", "sorting_binary_search_lookup"] or s == [
        "sorting_custom_key",
        "sorting_binary_search_answer",
    ]:
        return "ordered_preprocessing_then_binary_search"

    if s == ["dp_1d_state", "amortized_two_pointers"]:
        return "dp_with_amortized_pointer_optimization"

    if s == ["ds_hash_map", "sorting_custom_key"]:
        return "hash_grouping_then_ordered_processing"

    if s == ["sorting_custom_key", "ds_hash_map"]:
        return "ordered_processing_with_hash_index"

    if s == ["greedy_sorting_order", "greedy_two_pointers"]:
        return "ordered_scan_then_two_pointers"

    if (
        "sorting_custom_key" in s
        and "greedy_priority_queue" in s
        and ("ds_heap_priority_queue" in s or len(s) == 2)
    ):
        return "sorted_sweep_with_priority_queue"

    if "sorting_custom_key" in s and any(
        x in s for x in ("greedy_sorting_order", "greedy_exchange_argument")
    ):
        return "ordered_preprocessing_then_greedy"

    if "sorting_custom_key" in s and any(
        x in s
        for x in ("greedy_two_pointers", "amortized_two_pointers", "amortized_sliding_window")
    ):
        return "ordered_scan_then_two_pointers"

    if "sorting_custom_key" in s and any(x.startswith("dp_") for x in s):
        return "preprocessing_then_dp"

    if s == ["dp_2d_state", "dp_interval"] or s == ["dp_interval", "dp_1d_state"]:
        return "dp_table_then_interval_optimization"

    if any(x.startswith("ds_") for x in s) and any(x.startswith("greedy_") for x in s):
        return "data_structure_accelerated_greedy"

    if "sorting_sweep_line" in s and any(x.startswith("ds_") for x in s):
        return "sorted_sweep_with_data_structure"

    if "ds_hash_map" in s and any(x.startswith("greedy_") for x in s):
        return "hash_grouping_then_ordered_processing"

    if any(
        x in s
        for x in ("search_bitmask_enumeration", "bit_binary_representation", "bit_xor_trick")
    ) and any(x.startswith("dp_") for x in s):
        return "enumeration_with_bitmask_state"

    if len([x for x in s if x.startswith("dp_")]) >= 2:
        return "multi_stage_dynamic_programming"

    return "other_composition"


def get_relation_description(relation: str) -> str:
    return RELATION_DESCRIPTIONS.get(relation, RELATION_DESCRIPTIONS["other_composition"])
