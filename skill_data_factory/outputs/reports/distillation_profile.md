# Skill distillation profile

## single_algorithm

- primary_count: 763
- tier_counts: {'gold': 655, 'silver': 108}
- keys: {'dp_2d_state': 98, 'dp_1d_state': 94, 'sorting_custom_key': 92, 'search_backtracking': 82, 'greedy_exchange_argument': 71, 'search_permutation_enumeration': 46, 'greedy_sorting_order': 38, 'dp_counting_combinatorics': 37, 'search_branch_and_bound': 26, 'bit_binary_representation': 25, 'search_bitmask_enumeration': 17, 'search_dfs_bfs_graph': 15, 'sorting_binary_search_answer': 15, 'bit_xor_trick': 14, 'dp_tree': 13, 'ds_hash_map': 13, 'greedy_two_pointers': 10, 'dp_memoized_recursion': 10, 'ds_heap_priority_queue': 10, 'sorting_sweep_line': 6, 'dp_interval': 6, 'greedy_priority_queue': 5, 'amortized_two_pointers': 5, 'amortized_sliding_window': 4, 'dp_bitmask': 2, 'bit_set_operations': 2, 'dp_knapsack': 1, 'greedy_interval_scheduling': 1, 'bit_bitmask_dp': 1, 'ds_stack_monotonic': 1, 'ds_ordered_set': 1, 'ds_union_find': 1, 'ds_queue_deque': 1}

- pass3: {'track': 'single_algorithm', 'primary_in': 763, 'distillation_rows': 763, 'evidence_packets': 29, 'subtypes': 33}

- distillation_rows: 763
- evidence_packets: 29

## multi_algorithm

- primary_count: 260
- tier_counts: {'gold': 257, 'silver': 3}
- keys: {'greedy_algorithms+sorting': 80, 'data_structures+sorting': 23, 'amortized_analysis+sorting': 22, 'dynamic_programming+sorting': 21, 'complete_search+sorting': 13, 'data_structures+greedy_algorithms': 13, 'bit_manipulation+complete_search': 9, 'data_structures+dynamic_programming': 7, 'greedy_algorithms': 7, 'dynamic_programming+greedy_algorithms': 6, 'sorting': 5, 'data_structures+greedy_algorithms+sorting': 5, 'dynamic_programming': 4, 'amortized_analysis+greedy_algorithms+sorting': 4, 'data_structures': 4, 'amortized_analysis+data_structures': 4, 'amortized_analysis+dynamic_programming': 4, 'complete_search+dynamic_programming': 4, 'bit_manipulation+greedy_algorithms': 3, 'bit_manipulation+dynamic_programming': 3, 'amortized_analysis+greedy_algorithms': 3, 'complete_search+greedy_algorithms+sorting': 2, 'amortized_analysis+data_structures+sorting': 2, 'dynamic_programming+greedy_algorithms+sorting': 2, 'complete_search+greedy_algorithms': 2, 'amortized_analysis': 2, 'bit_manipulation+data_structures+greedy_algorithms': 1, 'data_structures+dynamic_programming+greedy_algorithms': 1, 'bit_manipulation+dynamic_programming+greedy_algorithms': 1, 'bit_manipulation+sorting': 1, 'complete_search': 1, 'data_structures+dynamic_programming+sorting': 1}

- pass3: {'track': 'multi_algorithm', 'packets': 7, 'rows': 260, 'composition_keys': 32}

- distillation_rows: 260
- evidence_packets: 7

## Pass1 route

```json
{
  "route_counts": {
    "single": 1042,
    "multi": 804,
    "quarantine": 0
  },
  "outputs": {
    "single_algorithm_problems": "/home/hjr/algo-skill-factory/skill_data_factory/outputs/single_algorithm/pass1_manifest/problems.jsonl",
    "single_algorithm_solutions": "/home/hjr/algo-skill-factory/skill_data_factory/outputs/single_algorithm/pass1_manifest/solutions.jsonl",
    "multi_algorithm_problems": "/home/hjr/algo-skill-factory/skill_data_factory/outputs/multi_algorithm/pass1_manifest/problems.jsonl",
    "multi_algorithm_solutions": "/home/hjr/algo-skill-factory/skill_data_factory/outputs/multi_algorithm/pass1_manifest/solutions.jsonl"
  }
}
```
