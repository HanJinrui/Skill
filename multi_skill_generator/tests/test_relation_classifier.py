from src.relation_classifier import classify_relation


def test_greedy_after_sort():
    assert (
        classify_relation(("sorting_custom_key", "greedy_sorting_order"))
        == "ordered_preprocessing_then_greedy"
    )


def test_binary_search_checker():
    assert (
        classify_relation(("sorting_binary_search_answer", "dp_1d_state"))
        == "answer_search_with_checker"
    )


def test_lookup_then_dp():
    assert (
        classify_relation(("sorting_binary_search_lookup", "dp_1d_state"))
        == "ordered_lookup_then_dp"
    )


def test_new_specific_relations_avoid_other_bucket():
    assert (
        classify_relation(("ds_hash_map", "sorting_custom_key"))
        == "hash_grouping_then_ordered_processing"
    )
    assert (
        classify_relation(("sorting_custom_key", "ds_hash_map"))
        == "ordered_processing_with_hash_index"
    )
    assert (
        classify_relation(("dp_1d_state", "amortized_two_pointers"))
        == "dp_with_amortized_pointer_optimization"
    )
    assert (
        classify_relation(("sorting_custom_key", "greedy_priority_queue"))
        == "sorted_sweep_with_priority_queue"
    )
