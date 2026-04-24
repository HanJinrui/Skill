"""Canonical algorithm-family taxonomy used by the RAG experiment.

This layer sits on top of the parent project's `taco_taxonomy` module: it maps
a normalized TACO tag (or skill_type) to the 8 core families we experiment
with. The module is intentionally self-contained so the RAG subsystem can run
without importing the parent's heavier validation stack.
"""
from __future__ import annotations

from typing import Iterable

CORE_FAMILIES: tuple[str, ...] = (
    "amortized_analysis",
    "bit_manipulation",
    "complete_search",
    "data_structures",
    "dynamic_programming",
    "greedy_algorithms",
    "range_queries",
    "sorting",
)
CORE_FAMILY_SET = frozenset(CORE_FAMILIES)


TAG_ALIASES: dict[str, str] = {
    "greedy": "greedy_algorithms",
    "greedy_algorithm": "greedy_algorithms",
    "dp": "dynamic_programming",
    "dynamic programming": "dynamic_programming",
    "brute_force": "complete_search",
    "brute force": "complete_search",
    "enumeration": "complete_search",
    "bfs": "complete_search",
    "dfs": "complete_search",
    "bitmask": "bit_manipulation",
    "bit": "bit_manipulation",
    "segment_tree": "range_queries",
    "segment_trees": "range_queries",
    "fenwick_tree": "range_queries",
    "binary_indexed_tree": "range_queries",
    "prefix_sum": "range_queries",
    "prefix_sums": "range_queries",
    "difference_array": "range_queries",
    "data structure": "data_structures",
    "hash": "data_structures",
    "stack": "data_structures",
    "queue": "data_structures",
    "priority_queue": "data_structures",
    "sort": "sorting",
    "sortings": "sorting",
}


TAG_TO_FAMILY: dict[str, str] = {
    "dynamic_programming": "dynamic_programming",
    "greedy_algorithms": "greedy_algorithms",
    "bit_manipulation": "bit_manipulation",
    "sorting": "sorting",
    "data_structures": "data_structures",
    "range_queries": "range_queries",
    "amortized_analysis": "amortized_analysis",
    "complete_search": "complete_search",
    "backtracking": "complete_search",
    "two_pointers": "amortized_analysis",
    "two pointers": "amortized_analysis",
    "segment_tree": "range_queries",
    "fenwick_tree": "range_queries",
    "prefix_sum": "range_queries",
    "difference_array": "range_queries",
    "mos_algorithm": "range_queries",
    "blocking": "range_queries",
    "square_root_algorithms": "range_queries",
    "hash": "data_structures",
    "heap": "data_structures",
    "stack": "data_structures",
    "queue": "data_structures",
    "union_find": "data_structures",
}


def canonicalize_tag(raw: str) -> str:
    if not isinstance(raw, str):
        return ""
    value = raw.strip().lower().replace("-", "_").replace(" ", "_")
    return TAG_ALIASES.get(value, value)


def tags_to_core_families(tags: Iterable[str]) -> list[str]:
    """Map a list of raw tags to the subset of the 8 core families they imply."""
    seen: set[str] = set()
    ordered: list[str] = []
    for tag in tags:
        canonical = canonicalize_tag(tag)
        if not canonical:
            continue
        family = TAG_TO_FAMILY.get(canonical)
        if family is None and canonical in CORE_FAMILY_SET:
            family = canonical
        if family and family in CORE_FAMILY_SET and family not in seen:
            seen.add(family)
            ordered.append(family)
    return ordered


def skill_id_for_single(family: str) -> str:
    return family


def skill_id_for_multi(families: Iterable[str]) -> str:
    parts = sorted({f for f in families if f in CORE_FAMILY_SET})
    return "__".join(parts)
