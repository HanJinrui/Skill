from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Iterable

from schema import canonicalize_family_name


@dataclass(frozen=True)
class SubtypeRule:
    subtype_name: str
    trigger_tags: tuple[str, ...]


TAG_ALIASES = {
    "binary_indexed_tree": "fenwick_tree",
    "graph_theory": "graph_algorithms",
    "matrix": "matrices",
    "mo_s_algorithm": "mos_algorithm",
    "mo_algorithm": "mos_algorithm",
    "prefix_sums": "prefix_sum",
    "probability_theory": "probability",
    "segment_trees_revisited": "segment_tree",
    "shortest_path": "shortest_paths",
    "string_matching": "string_algorithms",
    "union_find_set": "union_find",
}

GENERIC_TAGS = frozenset({"ad_hoc"})
GRAPH_TAGS = (
    "flows_and_cuts",
    "graph_algorithms",
    "graph_traversal",
    "shortest_paths",
    "spanning_trees",
    "strong_connectivity",
    "union_find",
)
TREE_TAGS = ("tree_algorithms", "tree_queries")
STRING_TAGS = ("string_algorithms",)
MATRIX_TAGS = ("matrices",)
NUMERIC_TAGS = (
    "combinatorics",
    "high_precision",
    "mathematics",
    "number_theory",
    "polynomials_and_generating_functions",
    "probability",
)
RANGE_DATA_STRUCTURE_TAGS = (
    "blocking",
    "difference_array",
    "fenwick_tree",
    "mos_algorithm",
    "prefix_sum",
    "segment_tree",
    "square_root_algorithms",
)
COMPOSITE_SPECIALIZED_TAGS = (
    "binary_search",
    "bit_manipulation",
    "blocking",
    "difference_array",
    "divide_and_conquer",
    "fenwick_tree",
    "fundamentals",
    "game_theory",
    "implementation",
    "prefix_sum",
    "segment_tree",
    "square_root_algorithms",
    "state_compression",
    "two_pointers",
)

SINGLE_FAMILY_RULES: dict[str, tuple[SubtypeRule, ...]] = {
    "amortized_analysis": (
        SubtypeRule("string_amortized", STRING_TAGS),
        SubtypeRule("graph_amortized", GRAPH_TAGS),
        SubtypeRule("numeric_amortized", NUMERIC_TAGS),
        SubtypeRule("implementation_amortized", ("implementation",)),
    ),
    "bit_manipulation": (
        SubtypeRule("state_compression_bitmasking", ("state_compression",)),
        SubtypeRule("graph_bitmasking", GRAPH_TAGS + TREE_TAGS),
        SubtypeRule("string_bitmasking", STRING_TAGS),
        SubtypeRule("game_bitmasking", ("game_theory",)),
        SubtypeRule("numeric_bitmasking", NUMERIC_TAGS),
        SubtypeRule("divide_and_conquer_bitmasking", ("divide_and_conquer",)),
        SubtypeRule("fundamental_bit_manipulation", ("fundamentals",)),
    ),
    "complete_search": (
        SubtypeRule("state_compression_search", ("state_compression",)),
        SubtypeRule("backtracking_search", ("backtracking",)),
        SubtypeRule("heuristic_search", ("heuristic_search",)),
        SubtypeRule("graph_search", GRAPH_TAGS),
        SubtypeRule("tree_search", TREE_TAGS),
        SubtypeRule("geometry_search", ("computational_geometry", "geometry")),
        SubtypeRule("string_search", STRING_TAGS),
        SubtypeRule("enumerative_math_search", NUMERIC_TAGS),
        SubtypeRule("constructive_search", ("constructive_algorithms",)),
        SubtypeRule("implementation_search", ("implementation",)),
    ),
    "data_structures": (
        SubtypeRule("segment_tree_structures", ("segment_tree",)),
        SubtypeRule("fenwick_tree_structures", ("fenwick_tree",)),
        SubtypeRule("union_find_structures", ("union_find",)),
        SubtypeRule("hash_structures", ("hash",)),
        SubtypeRule("tree_data_structures", TREE_TAGS),
        SubtypeRule("graph_data_structures", GRAPH_TAGS),
        SubtypeRule("string_data_structures", STRING_TAGS),
        SubtypeRule("matrix_data_structures", MATRIX_TAGS),
        SubtypeRule("numeric_data_structures", NUMERIC_TAGS),
        SubtypeRule("fundamental_data_structures", ("fundamentals",)),
        SubtypeRule("implementation_data_structures", ("implementation",)),
    ),
    "dynamic_programming": (
        SubtypeRule("state_compression_dp", ("state_compression",)),
        SubtypeRule("bitmask_dp", ("bit_manipulation",)),
        SubtypeRule("prefix_sum_dp", ("difference_array", "prefix_sum")),
        SubtypeRule("tree_dp", TREE_TAGS + ("spanning_trees",)),
        SubtypeRule("graph_dp", GRAPH_TAGS),
        SubtypeRule("string_dp", STRING_TAGS),
        SubtypeRule("game_dp", ("game_theory",)),
        SubtypeRule("probabilistic_dp", ("probability",)),
        SubtypeRule("matrix_dp", MATRIX_TAGS),
        SubtypeRule("counting_dp", ("combinatorics",)),
        SubtypeRule("numeric_dp", ("high_precision", "mathematics", "number_theory")),
        SubtypeRule("divide_and_conquer_dp", ("divide_and_conquer",)),
        SubtypeRule("binary_search_dp", ("binary_search",)),
        SubtypeRule("implementation_dp", ("implementation",)),
    ),
    "greedy_algorithms": (
        SubtypeRule("binary_search_greedy", ("binary_search",)),
        SubtypeRule("two_pointer_greedy", ("two_pointers",)),
        SubtypeRule("graph_greedy", GRAPH_TAGS),
        SubtypeRule("tree_greedy", TREE_TAGS),
        SubtypeRule("string_greedy", STRING_TAGS),
        SubtypeRule("game_greedy", ("game_theory",)),
        SubtypeRule("numeric_greedy", NUMERIC_TAGS),
        SubtypeRule("constructive_greedy", ("constructive_algorithms",)),
        SubtypeRule("implementation_greedy", ("implementation",)),
    ),
    "range_queries": (
        SubtypeRule("segment_tree_queries", ("segment_tree",)),
        SubtypeRule("fenwick_tree_queries", ("fenwick_tree",)),
        SubtypeRule("offline_range_queries", ("blocking", "mos_algorithm", "square_root_algorithms")),
        SubtypeRule("prefix_range_queries", ("difference_array", "prefix_sum")),
        SubtypeRule("tree_range_queries", TREE_TAGS),
        SubtypeRule("geometric_range_queries", ("computational_geometry", "geometry", "sweep_line_algorithms")),
        SubtypeRule("graph_range_queries", GRAPH_TAGS),
        SubtypeRule("numeric_range_queries", NUMERIC_TAGS),
    ),
    "sorting": (
        SubtypeRule("geometry_sorting", ("computational_geometry", "geometry")),
        SubtypeRule("graph_sorting", GRAPH_TAGS),
        SubtypeRule("string_sorting", STRING_TAGS),
        SubtypeRule("numeric_sorting", NUMERIC_TAGS),
        SubtypeRule("constructive_sorting", ("constructive_algorithms",)),
        SubtypeRule("implementation_sorting", ("implementation",)),
    ),
}

FALLBACK_SUBTYPES = {
    "amortized_analysis": "general_amortized",
    "bit_manipulation": "general_bit_manipulation",
    "complete_search": "general_complete_search",
    "data_structures": "general_data_structures",
    "dynamic_programming": "general_dp",
    "greedy_algorithms": "general_greedy",
    "range_queries": "general_range_queries",
    "sorting": "general_sorting",
}


def normalize_taco_tag(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")
    return TAG_ALIASES.get(normalized, normalized)


def normalize_taco_tags(raw_tags: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    normalized_tags: list[str] = []
    for raw_tag in raw_tags:
        if not isinstance(raw_tag, str):
            continue
        normalized = normalize_taco_tag(raw_tag)
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        normalized_tags.append(normalized)
    return normalized_tags


def build_canonical_single_family_subtype(
    family_name: str,
    normalized_tags: Iterable[str],
) -> str:
    family_name = canonicalize_family_name(family_name)
    tag_list = normalize_taco_tags(normalized_tags)
    usable_tags = {
        tag
        for tag in tag_list
        if tag != family_name and tag not in GENERIC_TAGS
    }
    for rule in SINGLE_FAMILY_RULES.get(family_name, ()):
        if usable_tags.intersection(rule.trigger_tags):
            return rule.subtype_name
    return FALLBACK_SUBTYPES.get(family_name, family_name)


def build_family_combo_name(family_names: Iterable[str]) -> str:
    return "__".join(canonicalize_family_name(family_name) for family_name in family_names)


def build_canonical_composite_subtype(
    family_names: Iterable[str],
    normalized_tags: Iterable[str],
) -> str:
    family_names = [canonicalize_family_name(family_name) for family_name in family_names]
    family_tag_set = set(family_names)
    usable_tags = {
        tag
        for tag in normalize_taco_tags(normalized_tags)
        if tag not in GENERIC_TAGS and tag not in family_tag_set
    }
    if "segment_tree" in usable_tags:
        return "segment_tree"
    if "fenwick_tree" in usable_tags:
        return "fenwick_tree"
    if usable_tags.intersection({"prefix_sum", "difference_array"}):
        return "prefix_range"
    if usable_tags.intersection({"blocking", "mos_algorithm", "square_root_algorithms"}):
        return "offline_range"
    if "state_compression" in usable_tags:
        return "state_compression"
    if "bit_manipulation" in usable_tags:
        return "bitmask"
    if "binary_search" in usable_tags:
        return "binary_search"
    if "two_pointers" in usable_tags:
        return "two_pointers"
    if usable_tags.intersection(TREE_TAGS):
        return "tree"
    if usable_tags.intersection(GRAPH_TAGS):
        return "graph"
    if usable_tags.intersection(STRING_TAGS):
        return "string"
    if usable_tags.intersection({"computational_geometry", "geometry", "sweep_line_algorithms"}):
        return "geometry"
    if usable_tags.intersection(MATRIX_TAGS):
        return "matrix"
    if "game_theory" in usable_tags:
        return "game"
    if usable_tags.intersection(NUMERIC_TAGS):
        return "numeric"
    if "constructive_algorithms" in usable_tags:
        return "constructive"
    if "implementation" in usable_tags:
        return "implementation"
    if "fundamentals" in usable_tags:
        return "fundamental"
    if "divide_and_conquer" in usable_tags:
        return "divide_and_conquer"
    return "general"
