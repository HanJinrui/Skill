"""Deterministic subtype taxonomy for verified solution labeling.

This layer refines the 8 family taxonomy into solution-level mechanisms. It is
intentionally rule-first: problem tags seed candidates, while solution AST/code
features anchor the final candidate ranking before any optional model rerank.
"""
from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from typing import Iterable, Mapping

from .rules import AstFeatures, solution_ast_features
from .taxonomy import CORE_FAMILIES, CORE_FAMILY_SET, canonicalize_tag, tags_to_core_families


@dataclass(frozen=True)
class SubtypeDefinition:
    subtype_id: str
    family: str
    aliases: tuple[str, ...]
    problem_tag_seeds: tuple[str, ...]
    solution_mechanism_seeds: tuple[str, ...]
    description: str

    def to_dict(self) -> dict[str, object]:
        payload = asdict(self)
        payload["aliases"] = list(self.aliases)
        payload["problem_tag_seeds"] = list(self.problem_tag_seeds)
        payload["solution_mechanism_seeds"] = list(self.solution_mechanism_seeds)
        return payload


SUBTYPE_DEFINITIONS: tuple[SubtypeDefinition, ...] = (
    SubtypeDefinition(
        "dp_1d_state",
        "dynamic_programming",
        ("1d dp", "linear dp", "one-dimensional dp"),
        ("dynamic programming", "dp", "linear dp", "states"),
        ("dp[", "prev", "curr", "rolling", "one dimension"),
        "Dynamic programming with a one-dimensional state or rolling array.",
    ),
    SubtypeDefinition(
        "dp_2d_state",
        "dynamic_programming",
        ("2d dp", "table dp", "matrix dp"),
        ("dynamic programming", "dp", "two-dimensional", "grid"),
        ("dp = [[", "dp[[", "table", "matrix", "for i", "for j"),
        "Dynamic programming over two explicit dimensions.",
    ),
    SubtypeDefinition(
        "dp_knapsack",
        "dynamic_programming",
        ("knapsack", "subset sum", "capacity dp"),
        ("knapsack", "subset sum", "capacity", "weight", "coin change"),
        ("capacity", "weight", "knapsack", "coins", "for w", "for weight"),
        "Knapsack, subset-sum, or capacity-constrained dynamic programming.",
    ),
    SubtypeDefinition(
        "dp_interval",
        "dynamic_programming",
        ("interval dp", "range dp"),
        ("interval", "range dynamic programming", "merge", "palindrome"),
        ("length", "for l", "for r", "interval", "split", "mid"),
        "Dynamic programming on intervals with length/order expansion.",
    ),
    SubtypeDefinition(
        "dp_tree",
        "dynamic_programming",
        ("tree dp", "dfs dp"),
        ("tree", "rooted tree", "subtree", "dynamic programming"),
        ("dfs", "children", "parent", "subtree", "tree dp"),
        "Dynamic programming whose state is attached to tree nodes or subtrees.",
    ),
    SubtypeDefinition(
        "dp_bitmask",
        "dynamic_programming",
        ("bitmask dp", "subset dp", "state compression"),
        ("bitmask", "subset", "state compression", "2^n"),
        ("mask", "1 <<", "1<<", "bitmask", "subset", "dp[mask"),
        "Dynamic programming over subsets or bitmask-compressed states.",
    ),
    SubtypeDefinition(
        "dp_memoized_recursion",
        "dynamic_programming",
        ("memoized dfs", "top-down dp", "cache recursion"),
        ("memoization", "top down", "recursive dp", "dynamic programming"),
        ("lru_cache", "@cache", "memo", "dfs", "recursion"),
        "Top-down dynamic programming implemented by recursion plus memoization.",
    ),
    SubtypeDefinition(
        "dp_counting_combinatorics",
        "dynamic_programming",
        ("counting dp", "combinatorics dp"),
        ("count ways", "number of ways", "modulo", "combinatorics"),
        ("mod", "ways", "comb", "factorial", "count"),
        "Counting or combinatorics dynamic programming, often modulo an integer.",
    ),
    SubtypeDefinition(
        "range_prefix_sum",
        "range_queries",
        ("prefix sum", "cumulative sum"),
        ("prefix sum", "range sum", "cumulative"),
        ("prefix", "accumulate", "partial_sum", "pre[", "sum["),
        "Static range aggregation with prefix sums.",
    ),
    SubtypeDefinition(
        "range_difference_array",
        "range_queries",
        ("difference array", "imos"),
        ("difference array", "range update", "imos"),
        ("diff", "difference", "+=", "-=", "imos"),
        "Range update accumulation through a difference array.",
    ),
    SubtypeDefinition(
        "range_fenwick_tree",
        "range_queries",
        ("fenwick tree", "binary indexed tree", "bit tree"),
        ("fenwick", "binary indexed tree", "bit"),
        ("lowbit", "i & -i", "fenwick", "bit.add", "bit.sum"),
        "Fenwick tree / binary indexed tree for online prefix queries and updates.",
    ),
    SubtypeDefinition(
        "range_segment_tree",
        "range_queries",
        ("segment tree", "lazy propagation"),
        ("segment tree", "lazy propagation", "range query"),
        ("segment", "segtree", "lazy", "tree = [", "build", "query", "update"),
        "Segment tree, possibly with lazy propagation, for range queries/updates.",
    ),
    SubtypeDefinition(
        "range_sparse_table",
        "range_queries",
        ("sparse table", "rmq"),
        ("sparse table", "rmq", "range minimum query"),
        ("sparse", "log", "st[", "rmq"),
        "Static idempotent range queries using a sparse table.",
    ),
    SubtypeDefinition(
        "range_sqrt_decomposition",
        "range_queries",
        ("sqrt decomposition", "block decomposition", "mo's algorithm"),
        ("sqrt decomposition", "block", "mo's algorithm", "offline queries"),
        ("sqrt", "block", "bucket", "mo", "queries.sort"),
        "Square-root/block decomposition, including Mo-style offline range queries.",
    ),
    SubtypeDefinition(
        "ds_hash_map",
        "data_structures",
        ("hash map", "dictionary", "counter"),
        ("hash", "map", "frequency", "counter"),
        ("dict", "defaultdict", "counter", "hashmap", "{}"),
        "Dictionary/hash-map based counting, lookup, or grouping.",
    ),
    SubtypeDefinition(
        "ds_heap_priority_queue",
        "data_structures",
        ("heap", "priority queue"),
        ("heap", "priority queue", "minimum", "maximum"),
        ("heapq", "heappush", "heappop", "priority"),
        "Heap or priority queue driven selection.",
    ),
    SubtypeDefinition(
        "ds_stack_monotonic",
        "data_structures",
        ("monotonic stack", "stack"),
        ("stack", "monotonic stack", "next greater", "next smaller"),
        ("stack", "while stack", "monotonic", "append", "pop"),
        "Stack-based processing, especially monotonic stack patterns.",
    ),
    SubtypeDefinition(
        "ds_queue_deque",
        "data_structures",
        ("queue", "deque"),
        ("queue", "deque", "breadth first"),
        ("deque", "popleft", "appendleft", "queue"),
        "Queue/deque data structure use, often for BFS or window maintenance.",
    ),
    SubtypeDefinition(
        "ds_union_find",
        "data_structures",
        ("union find", "dsu", "disjoint set"),
        ("union find", "dsu", "connected components"),
        ("parent", "find", "union", "rank", "size"),
        "Disjoint-set union / union-find connectivity maintenance.",
    ),
    SubtypeDefinition(
        "ds_ordered_set",
        "data_structures",
        ("ordered set", "balanced tree", "bisect list"),
        ("ordered set", "balanced tree", "predecessor", "successor"),
        ("bisect", "insort", "sortedlist", "order"),
        "Ordered set/list behavior for predecessor, successor, or rank queries.",
    ),
    SubtypeDefinition(
        "search_backtracking",
        "complete_search",
        ("backtracking", "recursive search"),
        ("backtracking", "all possible", "construct", "choices"),
        ("backtrack", "dfs", "used", "path", "recursion"),
        "Recursive backtracking through choices with pruning or restoration.",
    ),
    SubtypeDefinition(
        "search_dfs_bfs_graph",
        "complete_search",
        ("dfs", "bfs", "graph traversal"),
        ("dfs", "bfs", "graph", "grid", "connected"),
        ("dfs", "bfs", "deque", "visited", "graph", "adj"),
        "Graph or grid traversal using DFS/BFS.",
    ),
    SubtypeDefinition(
        "search_bitmask_enumeration",
        "complete_search",
        ("bitmask enumeration", "subset enumeration"),
        ("bitmask", "subset", "enumerate", "2^n"),
        ("mask", "1 <<", "range(1 <<", "subset"),
        "Complete enumeration of subsets or states via bitmasks.",
    ),
    SubtypeDefinition(
        "search_permutation_enumeration",
        "complete_search",
        ("permutation enumeration", "brute force permutations"),
        ("permutation", "arrangement", "all orders"),
        ("permutations", "itertools", "next_permutation", "used"),
        "Complete enumeration of permutations or orderings.",
    ),
    SubtypeDefinition(
        "search_branch_and_bound",
        "complete_search",
        ("branch and bound", "pruned search"),
        ("branch and bound", "pruning", "minimum search"),
        ("best", "bound", "prune", "if cost >=", "return"),
        "Exhaustive search with explicit pruning/bounds.",
    ),
    SubtypeDefinition(
        "bit_xor_trick",
        "bit_manipulation",
        ("xor trick", "xor basis", "parity xor"),
        ("xor", "exclusive or", "bitwise"),
        ("^", "xor", "basis", "bit_count"),
        "XOR-centered bit manipulation, parity, or basis-style reasoning.",
    ),
    SubtypeDefinition(
        "bit_bitmask_dp",
        "bit_manipulation",
        ("bitmask state", "mask transitions"),
        ("bitmask", "state compression", "subset"),
        ("mask", "1 <<", "dp[mask", "&", "|"),
        "Bitmask state manipulation; may overlap with bitmask DP.",
    ),
    SubtypeDefinition(
        "bit_set_operations",
        "bit_manipulation",
        ("set bits", "popcount", "bit count"),
        ("set bits", "popcount", "hamming"),
        ("bit_count", "bin(", "count('1')", "&=", "n &="),
        "Operations on set bits, popcount, or Hamming-like quantities.",
    ),
    SubtypeDefinition(
        "bit_binary_representation",
        "bit_manipulation",
        ("binary representation", "shifts"),
        ("binary", "bits", "powers of two"),
        ("<<", ">>", "bit_length", "binary"),
        "Reasoning over binary representation, shifts, or powers of two.",
    ),
    SubtypeDefinition(
        "greedy_sorting_order",
        "greedy_algorithms",
        ("sort and greedy", "greedy ordering"),
        ("greedy", "sort", "order", "maximize", "minimize"),
        ("sort", "sorted", "key=", "reverse", "greedy"),
        "Greedy decisions made after sorting by a useful order/key.",
    ),
    SubtypeDefinition(
        "greedy_interval_scheduling",
        "greedy_algorithms",
        ("interval scheduling", "activity selection"),
        ("interval", "schedule", "non-overlap", "earliest"),
        ("end", "start", "interval", "sort", "last"),
        "Greedy interval selection, scheduling, or coverage.",
    ),
    SubtypeDefinition(
        "greedy_exchange_argument",
        "greedy_algorithms",
        ("exchange greedy", "local optimal"),
        ("greedy", "exchange", "optimal", "minimum number"),
        ("if", "max", "min", "swap", "greedy"),
        "Greedy choice justified by an exchange/local optimality argument.",
    ),
    SubtypeDefinition(
        "greedy_priority_queue",
        "greedy_algorithms",
        ("heap greedy", "priority greedy"),
        ("greedy", "heap", "priority queue"),
        ("heapq", "heappush", "heappop", "while heap"),
        "Greedy process whose next action is chosen by a priority queue.",
    ),
    SubtypeDefinition(
        "greedy_two_pointers",
        "greedy_algorithms",
        ("two pointers greedy", "pairing greedy"),
        ("two pointers", "pair", "greedy", "sorted"),
        ("left", "right", "while", "sort"),
        "Greedy pairing or selection with two pointers.",
    ),
    SubtypeDefinition(
        "amortized_two_pointers",
        "amortized_analysis",
        ("two pointers", "linear scan"),
        ("two pointers", "amortized", "linear"),
        ("left", "right", "while", "two pointers"),
        "Two-pointer scan where each pointer advances monotonically.",
    ),
    SubtypeDefinition(
        "amortized_sliding_window",
        "amortized_analysis",
        ("sliding window", "window"),
        ("sliding window", "subarray", "substring", "at most"),
        ("window", "left", "right", "while", "counter"),
        "Sliding-window maintenance with amortized linear updates.",
    ),
    SubtypeDefinition(
        "amortized_monotonic_queue",
        "amortized_analysis",
        ("monotonic queue", "monotonic deque"),
        ("monotonic queue", "deque", "sliding maximum"),
        ("deque", "while", "popleft", "monotonic"),
        "Monotonic deque/queue with amortized pushes and pops.",
    ),
    SubtypeDefinition(
        "sorting_custom_key",
        "sorting",
        ("custom sort", "comparator", "key sort"),
        ("sorting", "custom order", "comparator"),
        ("sort", "sorted", "key=", "cmp_to_key", "lambda"),
        "Sorting with a custom key/comparator as the main mechanism.",
    ),
    SubtypeDefinition(
        "sorting_sweep_line",
        "sorting",
        ("sweep line", "events"),
        ("sweep line", "events", "intervals"),
        ("events", "sort", "sweep", "delta"),
        "Event sorting followed by sweep-line accumulation.",
    ),
    SubtypeDefinition(
        "sorting_binary_search_answer",
        "sorting",
        ("binary search answer", "sort plus binary search"),
        ("binary search", "answer", "sorted"),
        ("bisect", "lo", "hi", "mid", "while lo"),
        "Sorted data plus binary search or binary search on answer.",
    ),
)

SUBTYPE_BY_ID: dict[str, SubtypeDefinition] = {
    item.subtype_id: item for item in SUBTYPE_DEFINITIONS
}
SUBTYPES_BY_FAMILY: dict[str, tuple[SubtypeDefinition, ...]] = {
    family: tuple(item for item in SUBTYPE_DEFINITIONS if item.family == family)
    for family in CORE_FAMILIES
}


def all_subtypes() -> list[dict[str, object]]:
    return [item.to_dict() for item in SUBTYPE_DEFINITIONS]


def get_subtype(subtype_id: str) -> SubtypeDefinition | None:
    return SUBTYPE_BY_ID.get(subtype_id)


def subtypes_for_family(family: str) -> tuple[SubtypeDefinition, ...]:
    return SUBTYPES_BY_FAMILY.get(family, ())


def infer_candidate_subtypes_from_problem(
    problem_statement: str,
    original_skill_types: Iterable[str] = (),
    original_tags: Iterable[str] = (),
    candidate_families: Iterable[str] = (),
    *,
    max_candidates: int = 10,
) -> list[dict[str, object]]:
    """Infer subtype candidates from weak problem-level signals."""
    text = _normalize_text(problem_statement)
    tag_values = [canonicalize_tag(str(t)) for t in list(original_skill_types) + list(original_tags)]
    tag_blob = " ".join(tag_values).replace("_", " ")
    family_seeds = _clean_families(candidate_families) or tags_to_core_families(tag_values)
    scores: dict[str, float] = {}
    sources: dict[str, list[str]] = {}

    for subtype in SUBTYPE_DEFINITIONS:
        score = 0.0
        src: list[str] = []
        if subtype.family in family_seeds:
            score += 1.0
            src.append(f"problem_family:{subtype.family}")
        for seed in subtype.problem_tag_seeds + subtype.aliases:
            normalized_seed = _normalize_text(seed)
            if not normalized_seed:
                continue
            if normalized_seed in tag_blob:
                score += 2.0
                src.append(f"tag_seed:{seed}")
            if normalized_seed in text:
                score += 0.45
                src.append(f"text_seed:{seed}")
        semantic_bonus = _problem_semantic_bonus(subtype.subtype_id, text)
        if semantic_bonus:
            score += semantic_bonus
            src.append(f"semantic:{subtype.subtype_id}")
        if score > 0:
            scores[subtype.subtype_id] = score
            sources[subtype.subtype_id] = src

    return _rank_candidates(scores, sources, max_candidates=max_candidates)


def infer_candidate_subtypes_from_solution(
    solution_code: str,
    ast_features: AstFeatures | Mapping[str, object] | None = None,
    mechanism_summary: str = "",
    family_filter: Iterable[str] = (),
    *,
    max_candidates: int = 10,
) -> list[dict[str, object]]:
    """Infer subtype candidates from solution code and AST features."""
    features = _ensure_features(solution_code, ast_features)
    code_text = _normalize_text(solution_code)
    summary_text = _normalize_text(mechanism_summary)
    families = _clean_families(family_filter)
    scores: dict[str, float] = {}
    sources: dict[str, list[str]] = {}

    for subtype in SUBTYPE_DEFINITIONS:
        if families and subtype.family not in families:
            continue
        score = 0.0
        src: list[str] = []
        for seed in subtype.solution_mechanism_seeds + subtype.aliases:
            normalized_seed = _normalize_text(seed)
            if not normalized_seed:
                continue
            if normalized_seed in code_text:
                score += 0.75
                src.append(f"code_seed:{seed}")
            if normalized_seed in summary_text:
                score += 0.6
                src.append(f"summary_seed:{seed}")
        feature_bonus, feature_sources = _solution_feature_bonus(subtype.subtype_id, features, solution_code)
        if feature_bonus:
            score += feature_bonus
            src.extend(feature_sources)
        if subtype.family in families:
            score += 0.35
            src.append(f"family_filter:{subtype.family}")
        if score > 0:
            scores[subtype.subtype_id] = score
            sources[subtype.subtype_id] = src

    if not scores and families:
        for family in families:
            for subtype in subtypes_for_family(family)[:2]:
                scores[subtype.subtype_id] = 0.5
                sources[subtype.subtype_id] = [f"fallback_family:{family}"]

    return _rank_candidates(scores, sources, max_candidates=max_candidates)


def _rank_candidates(
    scores: Mapping[str, float],
    sources: Mapping[str, list[str]],
    *,
    max_candidates: int,
) -> list[dict[str, object]]:
    ranked = sorted(
        scores,
        key=lambda subtype_id: (
            scores[subtype_id],
            -list(SUBTYPE_BY_ID).index(subtype_id),
        ),
        reverse=True,
    )
    out: list[dict[str, object]] = []
    for subtype_id in ranked[:max_candidates]:
        subtype = SUBTYPE_BY_ID[subtype_id]
        out.append(
            {
                "subtype_id": subtype.subtype_id,
                "family": subtype.family,
                "score": round(float(scores[subtype_id]), 4),
                "sources": list(dict.fromkeys(sources.get(subtype_id, [])))[:8],
                "description": subtype.description,
            }
        )
    return out


def _clean_families(values: Iterable[str]) -> list[str]:
    out: list[str] = []
    for value in values or []:
        if value in CORE_FAMILY_SET and value not in out:
            out.append(value)
    return out


def _normalize_text(value: object) -> str:
    if value is None:
        return ""
    text = str(value).lower().replace("_", " ").replace("-", " ")
    text = re.sub(r"[^a-z0-9<>=+*/&|^.'()\\[\\] ]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _ensure_features(
    solution_code: str,
    ast_features: AstFeatures | Mapping[str, object] | None,
) -> AstFeatures:
    if isinstance(ast_features, AstFeatures):
        return ast_features
    if isinstance(ast_features, Mapping):
        return AstFeatures(
            recursion=bool(ast_features.get("recursion")),
            memoization=bool(ast_features.get("memoization")),
            iterative_dp_table=bool(ast_features.get("iterative_dp_table")),
            segment_tree_like=bool(ast_features.get("segment_tree_like")),
            fenwick_like=bool(ast_features.get("fenwick_like")),
            union_find_like=bool(ast_features.get("union_find_like")),
            dfs_bfs=bool(ast_features.get("dfs_bfs")),
            two_pointers=bool(ast_features.get("two_pointers")),
            sliding_window=bool(ast_features.get("sliding_window")),
            sort_call=bool(ast_features.get("sort_call")),
            heap_usage=bool(ast_features.get("heap_usage")),
            bit_ops=bool(ast_features.get("bit_ops")),
            closed_form=bool(ast_features.get("closed_form")),
            has_lru_cache=bool(ast_features.get("has_lru_cache")),
            loops_max_depth=int(ast_features.get("loops_max_depth") or 0),
            tokens=list(ast_features.get("tokens") or []),
        )
    return solution_ast_features(solution_code)


def _problem_semantic_bonus(subtype_id: str, text: str) -> float:
    checks: dict[str, tuple[str, ...]] = {
        "dp_counting_combinatorics": ("number of ways", "count the", "modulo", "10 9 + 7"),
        "dp_interval": ("palindrome", "substring", "interval", "merge"),
        "dp_tree": ("tree", "subtree", "root"),
        "dp_bitmask": ("2 n", "2^n", "subset", "bitmask"),
        "range_prefix_sum": ("sum of", "range sum", "subarray sum"),
        "range_segment_tree": ("range query", "range update", "minimum on a range", "maximum on a range"),
        "range_sqrt_decomposition": ("offline queries", "mo s algorithm", "block"),
        "ds_union_find": ("connect", "components", "disjoint"),
        "ds_heap_priority_queue": ("smallest", "largest", "priority"),
        "search_backtracking": ("all possible", "construct", "valid configuration"),
        "search_permutation_enumeration": ("permutation", "arrangement"),
        "bit_xor_trick": ("xor", "exclusive or"),
        "greedy_interval_scheduling": ("interval", "schedule", "non overlap"),
        "amortized_sliding_window": ("substring", "subarray", "at most"),
        "sorting_sweep_line": ("events", "sweep", "interval"),
    }
    return 0.65 if any(seed in text for seed in checks.get(subtype_id, ())) else 0.0


def _solution_feature_bonus(
    subtype_id: str,
    features: AstFeatures,
    solution_code: str,
) -> tuple[float, list[str]]:
    text = solution_code.lower()
    bonus = 0.0
    sources: list[str] = []

    def add(value: float, source: str) -> None:
        nonlocal bonus
        bonus += value
        sources.append(source)

    if subtype_id == "dp_memoized_recursion" and (features.memoization or features.has_lru_cache) and features.recursion:
        add(2.4, "ast:memoized_recursion")
    if subtype_id == "dp_2d_state" and features.iterative_dp_table and ("[[" in solution_code or features.loops_max_depth >= 2):
        add(1.8, "ast:2d_dp_table")
    if subtype_id == "dp_1d_state" and features.iterative_dp_table and "[[" not in solution_code:
        add(1.2, "ast:1d_dp_table")
    if subtype_id == "dp_knapsack" and re.search(r"capacity|weight|coin|amount|knapsack", text):
        add(1.5, "code:knapsack_terms")
    if subtype_id == "dp_interval" and re.search(r"for\s+\w+\s+in\s+range\(.*length|interval|split", text):
        add(1.2, "code:interval_loop")
    if subtype_id == "dp_tree" and features.dfs_bfs and re.search(r"tree|children|subtree|parent", text):
        add(1.1, "code:tree_dfs")
    if subtype_id in {"dp_bitmask", "bit_bitmask_dp", "search_bitmask_enumeration"} and re.search(r"1\s*<<|mask|bitmask", text):
        add(1.7, "code:bitmask")
    if subtype_id == "range_fenwick_tree" and features.fenwick_like:
        add(2.6, "ast:fenwick")
    if subtype_id == "range_segment_tree" and features.segment_tree_like:
        add(2.6, "ast:segment_tree")
    if subtype_id == "range_prefix_sum" and re.search(r"prefix|accumulate|pre\s*=", text):
        add(1.4, "code:prefix_sum")
    if subtype_id == "range_difference_array" and re.search(r"\bdiff\b|difference", text):
        add(1.3, "code:difference_array")
    if subtype_id == "range_sparse_table" and re.search(r"\bst\b|\bsparse\b|rmq", text) and "log" in text:
        add(1.3, "code:sparse_table")
    if subtype_id == "range_sqrt_decomposition" and re.search(r"sqrt|block|bucket|mo", text):
        add(1.2, "code:sqrt_block")
    if subtype_id == "ds_union_find" and features.union_find_like:
        add(2.5, "ast:union_find")
    if subtype_id == "ds_heap_priority_queue" and features.heap_usage:
        add(2.3, "ast:heap")
    if subtype_id == "ds_queue_deque" and features.dfs_bfs and "deque" in text:
        add(1.7, "ast:deque")
    if subtype_id == "ds_hash_map" and re.search(r"defaultdict|counter|dict\(|\{\}", text):
        add(1.4, "code:hash_map")
    if subtype_id == "ds_stack_monotonic" and re.search(r"stack", text):
        add(1.2, "code:stack")
    if subtype_id == "ds_ordered_set" and re.search(r"bisect|sortedlist|insort", text):
        add(1.5, "code:ordered_set")
    if subtype_id == "search_dfs_bfs_graph" and features.dfs_bfs:
        add(1.8, "ast:dfs_bfs")
    if subtype_id == "search_backtracking" and features.recursion and re.search(r"used|path|backtrack", text):
        add(1.5, "code:backtracking")
    if subtype_id == "search_permutation_enumeration" and re.search(r"permutations|itertools", text):
        add(1.6, "code:permutations")
    if subtype_id == "search_branch_and_bound" and re.search(r"prune|bound|best", text):
        add(1.1, "code:branch_bound")
    if subtype_id == "bit_xor_trick" and re.search(r"\^|xor", text):
        add(1.8, "code:xor")
    if subtype_id == "bit_set_operations" and re.search(r"bit_count|count\('1'\)|popcount", text):
        add(1.7, "code:popcount")
    if subtype_id == "bit_binary_representation" and re.search(r"<<|>>|bit_length", text):
        add(1.5, "code:binary_ops")
    if subtype_id in {"greedy_sorting_order", "sorting_custom_key"} and features.sort_call:
        add(1.3, "ast:sort")
    if subtype_id == "greedy_priority_queue" and features.heap_usage:
        add(1.6, "ast:heap_greedy")
    if subtype_id in {"greedy_two_pointers", "amortized_two_pointers"} and features.two_pointers:
        add(1.7, "ast:two_pointers")
    if subtype_id == "amortized_sliding_window" and features.sliding_window:
        add(1.8, "ast:sliding_window")
    if subtype_id == "amortized_monotonic_queue" and "deque" in text and re.search(r"while .*pop", text, re.S):
        add(1.5, "code:monotonic_queue")
    if subtype_id == "sorting_sweep_line" and features.sort_call and re.search(r"event|delta|sweep", text):
        add(1.5, "code:sweep_line")
    if subtype_id == "sorting_binary_search_answer" and re.search(r"bisect|while\s+\w+\s*<\s*\w+|mid\s*=", text):
        add(1.3, "code:binary_search")

    return bonus, sources
