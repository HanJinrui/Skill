"""Heterogeneous skill-graph schema + rule-based vocabularies.

This module is the single source of truth for:

* node and edge type names,
* namespaced node-id helpers,
* mechanism vocabulary (+ family → mechanism mapping),
* signal vocabulary (with surface-form patterns),
* conflict priors between skills / mechanisms.

Everything here is rule-based so the offline graph build can run without any
online LLM call. All mappings are conservative by design: when evidence is
weak we prefer fewer / weaker edges rather than noisy ones.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, FrozenSet, List, Tuple


# --------------------------------------------------------------------------- #
# Node & edge type constants
# --------------------------------------------------------------------------- #

NODE_SKILL = "skill"
NODE_FAMILY = "family"
NODE_MECHANISM = "mechanism"
NODE_SIGNAL = "signal"
NODE_PROTO_PROBLEM = "prototype_problem"
NODE_PROTO_SOLUTION = "prototype_solution"

# Bundle skills are physically stored as skill nodes with scope=="multi"; we
# keep a logical alias so code that specifically wants "bundle" semantics can
# branch on it without creating a parallel node table.
NODE_BUNDLE_SKILL = "bundle_skill"

NODE_TYPES: Tuple[str, ...] = (
    NODE_SKILL,
    NODE_FAMILY,
    NODE_MECHANISM,
    NODE_SIGNAL,
    NODE_PROTO_PROBLEM,
    NODE_PROTO_SOLUTION,
)

EDGE_SKILL_HAS_FAMILY = "skill_has_family"
EDGE_FAMILY_HAS_MECHANISM = "family_has_mechanism"
EDGE_SKILL_IMPLEMENTS_MECHANISM = "skill_implements_mechanism"
EDGE_SKILL_TRIGGERED_BY_SIGNAL = "skill_triggered_by_signal"
EDGE_PROTO_PROB_SUPPORTS_SKILL = "prototype_problem_supports_skill"
EDGE_PROTO_SOL_SUPPORTS_SKILL = "prototype_solution_supports_skill"
EDGE_PROTO_PROB_HAS_SIGNAL = "prototype_problem_has_signal"
EDGE_PROTO_SOL_USES_MECHANISM = "prototype_solution_uses_mechanism"
EDGE_BUNDLE_CONTAINS_SKILL = "bundle_contains_skill"
EDGE_SKILL_COOCCURS_SKILL = "skill_cooccurs_skill"
EDGE_SKILL_CONFLICTS_SKILL = "skill_conflicts_skill"
EDGE_MECHANISM_CONFLICTS_MECHANISM = "mechanism_conflicts_mechanism"

POSITIVE_EDGES: Tuple[str, ...] = (
    EDGE_SKILL_HAS_FAMILY,
    EDGE_FAMILY_HAS_MECHANISM,
    EDGE_SKILL_IMPLEMENTS_MECHANISM,
    EDGE_SKILL_TRIGGERED_BY_SIGNAL,
    EDGE_PROTO_PROB_SUPPORTS_SKILL,
    EDGE_PROTO_SOL_SUPPORTS_SKILL,
    EDGE_PROTO_PROB_HAS_SIGNAL,
    EDGE_PROTO_SOL_USES_MECHANISM,
    EDGE_BUNDLE_CONTAINS_SKILL,
    EDGE_SKILL_COOCCURS_SKILL,
)
NEGATIVE_EDGES: Tuple[str, ...] = (
    EDGE_SKILL_CONFLICTS_SKILL,
    EDGE_MECHANISM_CONFLICTS_MECHANISM,
)


# --------------------------------------------------------------------------- #
# Namespaced node-id helpers
# --------------------------------------------------------------------------- #

def skill_node_id(skill_id: str) -> str:
    return f"skill::{skill_id}"


def family_node_id(family_id: str) -> str:
    return f"family::{family_id}"


def mechanism_node_id(mech_id: str) -> str:
    return f"mechanism::{mech_id}"


def signal_node_id(signal_id: str) -> str:
    return f"signal::{signal_id}"


def prototype_problem_node_id(prototype_id: str) -> str:
    return f"proto_prob::{prototype_id}"


def prototype_solution_node_id(prototype_id: str) -> str:
    return f"proto_sol::{prototype_id}"


def parse_node_id(node_id: str) -> Tuple[str, str]:
    """Return (namespace, raw_id) for a namespaced node id."""
    if "::" not in node_id:
        return ("", node_id)
    ns, raw = node_id.split("::", 1)
    return ns, raw


# --------------------------------------------------------------------------- #
# Mechanism vocabulary
# --------------------------------------------------------------------------- #

@dataclass(frozen=True)
class MechanismSpec:
    mechanism_id: str
    families: Tuple[str, ...]
    aliases: Tuple[str, ...]
    description: str


MECHANISMS: Tuple[MechanismSpec, ...] = (
    # amortized / two-pointer family
    MechanismSpec("sliding_window", ("amortized_analysis",),
                  ("sliding window", "window expansion", "two pointer window"),
                  "Maintain a valid moving window with amortized O(n) pointer movement."),
    MechanismSpec("two_pointers", ("amortized_analysis",),
                  ("two pointers", "two-pointer", "left right pointer"),
                  "Coordinate a left/right or fast/slow pointer pair in linear time."),
    MechanismSpec("monotonic_stack", ("amortized_analysis", "data_structures"),
                  ("monotonic stack", "stack of monotone"),
                  "Maintain a monotone stack to answer nearest-greater / previous-less queries."),
    MechanismSpec("monotonic_queue", ("amortized_analysis", "data_structures"),
                  ("monotonic deque", "sliding window maximum"),
                  "Maintain a monotone deque for sliding-window extrema."),

    # bit manipulation
    MechanismSpec("bitmask_enumeration", ("bit_manipulation", "complete_search"),
                  ("bitmask", "subset mask"),
                  "Enumerate subsets via their integer bitmask."),
    MechanismSpec("bitmask_dp", ("bit_manipulation", "dynamic_programming"),
                  ("bitmask dp", "dp on subsets"),
                  "Dynamic programming indexed by subset bitmasks."),
    MechanismSpec("xor_tricks", ("bit_manipulation",),
                  ("xor", "parity", "xor prefix"),
                  "Use xor / parity identities to cancel duplicates or collapse information."),
    MechanismSpec("shift_ops", ("bit_manipulation",),
                  ("shift", "bit shift", "bit set"),
                  "Directly manipulate bits via shifts, AND, OR."),

    # complete search
    MechanismSpec("backtracking", ("complete_search",),
                  ("backtrack", "recursive search"),
                  "Recursive enumeration with feasibility rollback."),
    MechanismSpec("dfs_enumeration", ("complete_search",),
                  ("dfs", "depth first search"),
                  "Depth-first enumeration of a state / tree / graph."),
    MechanismSpec("bfs_enumeration", ("complete_search",),
                  ("bfs", "breadth first search"),
                  "Breadth-first enumeration / shortest-edges search."),
    MechanismSpec("branch_and_bound", ("complete_search",),
                  ("branch and bound", "prune"),
                  "Exhaustive search guided by bounds and pruning."),

    # data structures
    MechanismSpec("heap_maintenance", ("data_structures",),
                  ("heap", "priority queue", "min-heap", "max-heap"),
                  "Maintain a heap / priority queue for order-statistics."),
    MechanismSpec("union_find", ("data_structures",),
                  ("union find", "disjoint set", "dsu"),
                  "Union-find with path compression / union by rank."),
    MechanismSpec("hash_lookup", ("data_structures",),
                  ("hash map", "dictionary", "frequency map"),
                  "Use a hash map for O(1) lookup / counting."),
    MechanismSpec("stack_simulation", ("data_structures",),
                  ("stack", "lifo"),
                  "Use a stack to simulate nested structure or last-in-first-out flow."),
    MechanismSpec("queue_simulation", ("data_structures",),
                  ("queue", "fifo"),
                  "Use a queue for first-in-first-out scheduling."),
    MechanismSpec("balanced_bst", ("data_structures",),
                  ("sorted set", "balanced tree", "treap"),
                  "Maintain an ordered set with O(log n) insert / erase / order."),

    # dynamic programming
    MechanismSpec("state_transition_dp", ("dynamic_programming",),
                  ("dp transition", "recurrence"),
                  "Classic DP with a forward / backward state recurrence."),
    MechanismSpec("dp_on_indices", ("dynamic_programming",),
                  ("dp over prefix", "dp[i]"),
                  "One- or two-index DP over sequence positions."),
    MechanismSpec("dp_on_subsets", ("dynamic_programming", "bit_manipulation"),
                  ("subset dp",),
                  "DP whose state is a subset mask (bitmask DP)."),
    MechanismSpec("dp_on_tree", ("dynamic_programming",),
                  ("tree dp",),
                  "DP over tree rooted state (dp on subtree)."),
    MechanismSpec("knapsack", ("dynamic_programming",),
                  ("knapsack", "0/1 knapsack", "unbounded knapsack"),
                  "Classic capacity / value knapsack DP."),
    MechanismSpec("digit_dp", ("dynamic_programming",),
                  ("digit dp",),
                  "DP by digit position with tight / not-tight state."),
    MechanismSpec("interval_dp", ("dynamic_programming",),
                  ("interval dp", "range dp"),
                  "DP where state is an interval [l, r]."),

    # greedy
    MechanismSpec("sort_then_greedy", ("greedy_algorithms", "sorting"),
                  ("sort and greedy", "sort then scan"),
                  "Sort by an informative key, then a linear greedy pass."),
    MechanismSpec("exchange_argument", ("greedy_algorithms",),
                  ("exchange argument",),
                  "Prove greedy correctness by a pairwise exchange argument."),
    MechanismSpec("priority_greedy", ("greedy_algorithms", "data_structures"),
                  ("priority queue greedy", "heap-based greedy"),
                  "Greedy driven by a priority-queue selection."),
    MechanismSpec("scanning_greedy", ("greedy_algorithms",),
                  ("scan and commit",),
                  "Single left-to-right scan making irrevocable local choices."),

    # range queries
    MechanismSpec("prefix_sum", ("range_queries",),
                  ("prefix sum", "cumulative sum"),
                  "Precompute cumulative sums for O(1) range aggregates."),
    MechanismSpec("difference_array", ("range_queries",),
                  ("difference array", "delta array"),
                  "Range update via delta array + prefix sum reconstruction."),
    MechanismSpec("fenwick_tree", ("range_queries", "data_structures"),
                  ("fenwick", "bit tree", "binary indexed tree"),
                  "Fenwick / BIT for point update + prefix / range sum."),
    MechanismSpec("segment_tree", ("range_queries", "data_structures"),
                  ("segment tree", "seg tree", "lazy propagation"),
                  "Segment tree (with lazy propagation) for range ops."),
    MechanismSpec("sparse_table", ("range_queries",),
                  ("sparse table", "rmq sparse"),
                  "Static sparse table for idempotent range queries (min/max/gcd)."),
    MechanismSpec("offline_queries", ("range_queries",),
                  ("offline queries", "sort queries"),
                  "Reorder queries offline to exploit monotone scan / sweep."),
    MechanismSpec("mo_algorithm", ("range_queries",),
                  ("mo's algorithm", "sqrt decomposition queries"),
                  "Mo's offline sqrt-decomposition for range queries."),

    # sorting
    MechanismSpec("comparator_sort", ("sorting",),
                  ("custom comparator", "sort by"),
                  "Sort items by a carefully chosen composite key."),
    MechanismSpec("coordinate_compression", ("sorting", "range_queries"),
                  ("coordinate compression", "rank"),
                  "Map large distinct values to dense ranks."),
    MechanismSpec("counting_sort", ("sorting",),
                  ("counting sort", "bucket"),
                  "Counting / bucket sort for small-value universes."),
)

MECHANISM_BY_ID: Dict[str, MechanismSpec] = {m.mechanism_id: m for m in MECHANISMS}

FAMILY_MECHANISMS: Dict[str, Tuple[str, ...]] = {}
for _m in MECHANISMS:
    for _fam in _m.families:
        FAMILY_MECHANISMS.setdefault(_fam, ())
        FAMILY_MECHANISMS[_fam] = FAMILY_MECHANISMS[_fam] + (_m.mechanism_id,)


def mechanism_surface_patterns() -> Dict[str, List[re.Pattern]]:
    """Return regex patterns per mechanism id (compiled, case-insensitive)."""
    out: Dict[str, List[re.Pattern]] = {}
    for m in MECHANISMS:
        pats = []
        for alias in (m.mechanism_id, *m.aliases):
            escaped = re.escape(alias.replace("_", " "))
            # Allow either underscore or space form to match.
            pats.append(re.compile(rf"\b{escaped.replace(' ', '[ _-]+')}\b", re.IGNORECASE))
        out[m.mechanism_id] = pats
    return out


# --------------------------------------------------------------------------- #
# Signal vocabulary
# --------------------------------------------------------------------------- #

@dataclass(frozen=True)
class SignalSpec:
    signal_id: str
    category: str  # operation | constraint | shape | goal | keyword
    surface_forms: Tuple[str, ...]  # regex-safe literal strings
    linked_mechanisms: Tuple[str, ...] = ()


# NOTE: Signal patterns are matched case-insensitively against the problem
# statement / skill text. We intentionally use *loose* literal fragments plus
# a few constraint regexes below.
SIGNALS: Tuple[SignalSpec, ...] = (
    # operation
    SignalSpec("range_query", "operation",
               ("range query", "interval query", "query range", "query sum", "query on interval", "sum over range"),
               ("prefix_sum", "fenwick_tree", "segment_tree", "sparse_table")),
    SignalSpec("point_update", "operation",
               ("point update", "update position", "update index", "update a_i"),
               ("fenwick_tree", "segment_tree")),
    SignalSpec("range_update", "operation",
               ("range update", "add to interval", "update interval", "apply on range"),
               ("difference_array", "segment_tree")),
    SignalSpec("many_range_queries", "operation",
               ("q queries", "many queries", "answer q queries", "multiple queries"),
               ("fenwick_tree", "segment_tree", "prefix_sum", "offline_queries")),
    SignalSpec("subarray", "operation",
               ("subarray", "contiguous subarray", "window", "sub-array"),
               ("sliding_window", "two_pointers", "prefix_sum")),
    SignalSpec("substring", "operation",
               ("substring", "contiguous substring", "smallest window"),
               ("sliding_window", "two_pointers")),
    SignalSpec("sort_action", "operation",
               ("sort the", "sorted order", "after sorting", "sort them"),
               ("sort_then_greedy", "comparator_sort")),
    SignalSpec("enumerate_subsets", "operation",
               ("all subsets", "2^n", "enumerate subsets"),
               ("bitmask_enumeration", "bitmask_dp")),
    SignalSpec("enumerate_permutations", "operation",
               ("all permutations", "n!", "permutation"),
               ("backtracking",)),
    SignalSpec("search_action", "operation",
               ("search for", "find a", "reachable", "shortest path"),
               ("bfs_enumeration", "dfs_enumeration")),

    # constraint (category is important for complexity gating)
    SignalSpec("n_le_20", "constraint",
               ("n <= 20", "n ≤ 20", "n<=20", "n = 20"),
               ("bitmask_enumeration", "bitmask_dp", "backtracking")),
    SignalSpec("n_le_100", "constraint",
               ("n <= 100", "n ≤ 100"),
               ("interval_dp", "dp_on_indices")),
    SignalSpec("n_le_1000", "constraint",
               ("n <= 1000", "n ≤ 1000", "n <= 10^3"),
               ("dp_on_indices", "interval_dp")),
    SignalSpec("n_le_1e5", "constraint",
               ("n <= 10^5", "n ≤ 10^5", "1 <= n <= 10^5", "n<=100000"),
               ("sliding_window", "prefix_sum", "fenwick_tree", "segment_tree")),
    SignalSpec("n_le_2e5", "constraint",
               ("n <= 2*10^5", "n ≤ 2·10^5", "n <= 200000", "n ≤ 200000"),
               ("fenwick_tree", "segment_tree")),
    SignalSpec("n_le_1e6", "constraint",
               ("n <= 10^6", "n ≤ 10^6"),
               ("prefix_sum", "counting_sort")),
    SignalSpec("q_large", "constraint",
               ("q <= 10^5", "q ≤ 10^5", "q <= 2*10^5", "q queries"),
               ("fenwick_tree", "segment_tree", "offline_queries")),
    SignalSpec("small_alphabet", "constraint",
               ("26 letters", "lowercase letters", "ascii 256", "o(26)"),
               ("hash_lookup", "counting_sort")),

    # shape
    SignalSpec("array_input", "shape",
               ("array of", "given an array", "given n integers", "integers a1", "sequence of integers"),
               ()),
    SignalSpec("string_input", "shape",
               ("string s", "given a string", "substring", "characters of the string"),
               ()),
    SignalSpec("tree_input", "shape",
               ("tree with", "rooted tree", "n-1 edges", "a tree"),
               ("dp_on_tree",)),
    SignalSpec("graph_input", "shape",
               ("graph with", "directed graph", "undirected graph", "vertices and edges"),
               ("bfs_enumeration", "dfs_enumeration", "union_find")),
    SignalSpec("matrix_input", "shape",
               ("n by m", "grid of", "matrix of", "2d array"),
               ()),
    SignalSpec("interval_list_input", "shape",
               ("intervals", "segments on a line", "list of ranges"),
               ("sort_then_greedy", "segment_tree")),

    # goal
    SignalSpec("minimize", "goal",
               ("minimum", "smallest", "minimize", "shortest"),
               ()),
    SignalSpec("maximize", "goal",
               ("maximum", "largest", "maximize", "longest"),
               ()),
    SignalSpec("count_ways", "goal",
               ("count the number of", "how many ways", "number of ways", "modulo 10^9"),
               ("state_transition_dp", "dp_on_indices")),
    SignalSpec("feasibility", "goal",
               ("determine whether", "is it possible", "yes or no", "possible to"),
               ()),
    SignalSpec("construct", "goal",
               ("construct", "output any", "print any valid"),
               ()),
    SignalSpec("kth_element", "goal",
               ("k-th smallest", "kth largest", "kth smallest"),
               ("heap_maintenance", "balanced_bst")),

    # keyword
    SignalSpec("xor_keyword", "keyword",
               ("xor", "exclusive or", "parity"),
               ("xor_tricks",)),
    SignalSpec("bitmask_keyword", "keyword",
               ("bitmask", "mask", "subset bit"),
               ("bitmask_enumeration", "bitmask_dp")),
    SignalSpec("prefix_keyword", "keyword",
               ("prefix sum", "cumulative", "running total"),
               ("prefix_sum",)),
    SignalSpec("mod_keyword", "keyword",
               ("modulo 10^9", "mod 998244353", "answer modulo"),
               ("state_transition_dp",)),
    SignalSpec("dp_keyword", "keyword",
               ("dp", "dynamic programming", "recurrence"),
               ("state_transition_dp",)),
    SignalSpec("greedy_keyword", "keyword",
               ("greedy",),
               ("sort_then_greedy", "scanning_greedy")),
)

SIGNAL_BY_ID: Dict[str, SignalSpec] = {s.signal_id: s for s in SIGNALS}


def _compile_signal_pattern(form: str) -> re.Pattern:
    # Escape then relax whitespace / punctuation differences.
    escaped = re.escape(form).replace(r"\ ", r"\s+")
    return re.compile(escaped, re.IGNORECASE)


def signal_surface_patterns() -> Dict[str, List[re.Pattern]]:
    return {s.signal_id: [_compile_signal_pattern(f) for f in s.surface_forms] for s in SIGNALS}


# Some constraint signals also need regex (loose form like "n <= 2·10^5").
CONSTRAINT_REGEXES: Tuple[Tuple[str, re.Pattern], ...] = (
    ("n_le_20", re.compile(r"\bn\s*[≤<]=?\s*(?:20)\b")),
    ("n_le_100", re.compile(r"\bn\s*[≤<]=?\s*100\b")),
    ("n_le_1000", re.compile(r"\bn\s*[≤<]=?\s*(?:1000|10\^?3)\b")),
    ("n_le_1e5", re.compile(r"\bn\s*[≤<]=?\s*(?:100000|10\^?5)\b")),
    ("n_le_2e5", re.compile(r"\bn\s*[≤<]=?\s*(?:2\s*[·\*x]\s*10\^?5|2\s*[·\*]\s*10\^5|200000)\b")),
    ("n_le_1e6", re.compile(r"\bn\s*[≤<]=?\s*(?:1000000|10\^?6)\b")),
    ("q_large", re.compile(r"\bq\s*[≤<]=?\s*(?:10\^?5|100000|2\s*[·\*x]\s*10\^?5)\b")),
)


# --------------------------------------------------------------------------- #
# Conflict priors (weights intentionally modest; small data sets)
# --------------------------------------------------------------------------- #

# (skill_id_a, skill_id_b, weight) — weight is how strongly we penalise the pair.
SKILL_CONFLICT_PAIRS: Tuple[Tuple[str, str, float], ...] = (
    ("sorting", "greedy_algorithms", 0.05),
    ("complete_search", "dynamic_programming", 0.05),
    ("data_structures", "range_queries", 0.05),
)

# (mech_a, mech_b, weight)
MECHANISM_CONFLICT_PAIRS: Tuple[Tuple[str, str, float], ...] = (
    ("segment_tree", "sliding_window", 0.20),
    ("bitmask_enumeration", "scanning_greedy", 0.20),
    ("fenwick_tree", "prefix_sum", 0.10),  # only meaningful when updates needed
    ("segment_tree", "prefix_sum", 0.10),
)


# --------------------------------------------------------------------------- #
# Core family list (kept in sync with taxonomy.py)
# --------------------------------------------------------------------------- #

CORE_FAMILIES: FrozenSet[str] = frozenset((
    "amortized_analysis",
    "bit_manipulation",
    "complete_search",
    "data_structures",
    "dynamic_programming",
    "greedy_algorithms",
    "range_queries",
    "sorting",
))
