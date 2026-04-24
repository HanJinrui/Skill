"""Rule layer: cheap, deterministic hints used to narrow candidates before LLM.

Two entry points:
  * `problem_candidate_families(problem)` – from text + original tags → ≤3 core families.
  * `solution_ast_features(code)` – lightweight AST/regex fingerprint of a reference solution.
Confidence/fusion logic uses both layers together with LLM outputs in stages B/C.
"""
from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from typing import Iterable

from .taxonomy import CORE_FAMILIES, CORE_FAMILY_SET, tags_to_core_families


# --- problem-side rules -----------------------------------------------------

_PROBLEM_PATTERNS: dict[str, tuple[str, ...]] = {
    "dynamic_programming": (
        r"\bmaximum\b.*\bsum\b", r"count.*ways", r"minimum\s+cost",
        r"longest\s+(common|increasing|palindromic)", r"\bsubsequence\b",
        r"mod(ulo)?\s*\d+", r"\bexactly\s+n\b",
    ),
    "greedy_algorithms": (
        r"\bminimum\s+number\b", r"\bmaximize\b", r"\bearliest\b",
        r"\bschedule\b", r"pair\s+up", r"\bintervals?\b.*\bnon-?overlap",
    ),
    "sorting": (
        r"\bsort(ed|ing)\b", r"in\s+ascending\s+order", r"in\s+non-?decreasing",
        r"\bkth\s+smallest\b",
    ),
    "bit_manipulation": (
        r"\bxor\b", r"\bor\b", r"\band\b.*\bbitwise\b", r"\bbit(s|mask)?\b",
        r"\b2\^n\b", r"\bsubsets?\s+of\s+size\b",
    ),
    "complete_search": (
        r"\benumerate\b", r"brute\s*force", r"\bpermutations?\b", r"\ball\s+possible\b",
        r"\bbacktrack\b", r"n\s*[<=]\s*2\s*0\b",
    ),
    "data_structures": (
        r"\bstack\b", r"\bqueue\b", r"\bdeque\b", r"\bheap\b", r"priority\s+queue",
        r"hash\s*map", r"union\s*find", r"\bdsu\b",
    ),
    "range_queries": (
        r"range\s+(sum|min|max|update|query)", r"segment\s+tree", r"fenwick",
        r"prefix\s+sum", r"difference\s+array", r"\bmo(?:'|’)?s\s+algorithm",
    ),
    "amortized_analysis": (
        r"two\s+pointers?", r"sliding\s+window", r"monotonic\s+(stack|queue|deque)",
    ),
}
_PROBLEM_REGEX: dict[str, list[re.Pattern[str]]] = {
    family: [re.compile(p, re.IGNORECASE) for p in patterns]
    for family, patterns in _PROBLEM_PATTERNS.items()
}


@dataclass(frozen=True)
class RuleCandidates:
    families: list[str]
    scores: dict[str, float]


def problem_candidate_families(
    problem_text: str,
    original_tags: Iterable[str],
    skill_types: Iterable[str] = (),
    max_candidates: int = 3,
) -> RuleCandidates:
    """Score the 8 core families by pattern match + original TACO tag hints."""
    text = problem_text or ""
    scores: dict[str, float] = {f: 0.0 for f in CORE_FAMILIES}
    tag_families = tags_to_core_families(list(original_tags) + list(skill_types))
    for family in tag_families:
        scores[family] += 2.0
    for family, patterns in _PROBLEM_REGEX.items():
        for pattern in patterns:
            if pattern.search(text):
                scores[family] += 0.5
    ranked = sorted(CORE_FAMILIES, key=lambda f: scores[f], reverse=True)
    picked = [f for f in ranked if scores[f] > 0][:max_candidates]
    if not picked:
        picked = [f for f in tag_families[:max_candidates]] or list(CORE_FAMILIES[:max_candidates])
    return RuleCandidates(families=picked, scores={f: scores[f] for f in picked})


# --- solution-side rules ----------------------------------------------------

@dataclass(frozen=True)
class AstFeatures:
    recursion: bool
    memoization: bool
    iterative_dp_table: bool
    segment_tree_like: bool
    fenwick_like: bool
    union_find_like: bool
    dfs_bfs: bool
    two_pointers: bool
    sliding_window: bool
    sort_call: bool
    heap_usage: bool
    bit_ops: bool
    closed_form: bool
    has_lru_cache: bool
    loops_max_depth: int
    tokens: list[str]

    def to_dict(self) -> dict[str, object]:
        return {
            "recursion": self.recursion,
            "memoization": self.memoization,
            "iterative_dp_table": self.iterative_dp_table,
            "segment_tree_like": self.segment_tree_like,
            "fenwick_like": self.fenwick_like,
            "union_find_like": self.union_find_like,
            "dfs_bfs": self.dfs_bfs,
            "two_pointers": self.two_pointers,
            "sliding_window": self.sliding_window,
            "sort_call": self.sort_call,
            "heap_usage": self.heap_usage,
            "bit_ops": self.bit_ops,
            "closed_form": self.closed_form,
            "has_lru_cache": self.has_lru_cache,
            "loops_max_depth": self.loops_max_depth,
        }


def solution_ast_features(code: str) -> AstFeatures:
    tokens: list[str] = []
    recursion = False
    memoization = False
    iterative_dp_table = False
    dfs_bfs = False
    two_pointers = False
    sliding_window = False
    sort_call = False
    heap_usage = False
    bit_ops = False
    has_lru_cache = False
    segment_tree_like = False
    fenwick_like = False
    union_find_like = False
    loops_max_depth = 0
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return AstFeatures(
            recursion=False, memoization=False, iterative_dp_table=False,
            segment_tree_like=False, fenwick_like=False, union_find_like=False,
            dfs_bfs=False, two_pointers=False, sliding_window=False,
            sort_call=False, heap_usage=False, bit_ops=False,
            closed_form=False, has_lru_cache=False, loops_max_depth=0, tokens=[],
        )

    func_names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_names.add(node.name)
            for dec in node.decorator_list:
                s = ast.unparse(dec) if hasattr(ast, "unparse") else ""
                if "lru_cache" in s or "cache" in s:
                    has_lru_cache = True
                    memoization = True

    class LoopDepth(ast.NodeVisitor):
        def __init__(self) -> None:
            self.depth = 0
            self.max_depth = 0

        def visit_For(self, node: ast.For) -> None:
            self.depth += 1
            self.max_depth = max(self.max_depth, self.depth)
            self.generic_visit(node)
            self.depth -= 1

        def visit_While(self, node: ast.While) -> None:
            self.depth += 1
            self.max_depth = max(self.max_depth, self.depth)
            self.generic_visit(node)
            self.depth -= 1

    ld = LoopDepth()
    ld.visit(tree)
    loops_max_depth = ld.max_depth

    text = code.lower()
    if re.search(r"\bdef\s+(\w+)\b", text):
        for name in func_names:
            if re.search(rf"\b{name}\s*\(", text.replace(f"def {name}", "", 1)):
                recursion = True
                break
    if "@lru_cache" in code or "functools.lru_cache" in code or "@cache" in code:
        has_lru_cache = True
        memoization = True
    if re.search(r"\b(dp|f|memo|cache)\s*\[", code):
        iterative_dp_table = True
    if re.search(r"\bsegment_?tree\b|\btree\s*=\s*\[\s*0\s*\]\s*\*\s*\(?4\s*\*", code, re.I):
        segment_tree_like = True
    if re.search(r"\blowbit\b|i\s*&\s*-i", code):
        fenwick_like = True
    if re.search(r"\bparent\s*\[", code) and re.search(r"\bfind\s*\(", code):
        union_find_like = True
    if re.search(r"\bdeque\b|collections\.deque|from\s+collections\s+import\s+deque", code):
        dfs_bfs = True
    if re.search(r"heapq\.|heappush|heappop", code):
        heap_usage = True
    if re.search(r"\bsorted\s*\(|\.sort\s*\(", code):
        sort_call = True
    if re.search(r"[&|^]|<<|>>|bit_length\(", code):
        bit_ops = True
    if re.search(r"\bl\s*=\s*0\b.*\br\s*=", code, re.S) or re.search(r"left\s*=\s*0.*right", code, re.S):
        two_pointers = True
    if "while" in text and re.search(r"while\s+.*:\s*\n\s*.*\bmax\(|\bmin\(", code):
        sliding_window = True

    closed_form = (
        loops_max_depth <= 1
        and not iterative_dp_table
        and not recursion
        and not dfs_bfs
        and not sort_call
        and bool(re.search(r"\*\*|pow\s*\(|//\s*\d", code))
    )
    tokens = [
        t for t in [
            "recursion" if recursion else None,
            "memoization" if memoization else None,
            "dp_table" if iterative_dp_table else None,
            "segment_tree" if segment_tree_like else None,
            "fenwick" if fenwick_like else None,
            "union_find" if union_find_like else None,
            "bfs_dfs" if dfs_bfs else None,
            "two_pointers" if two_pointers else None,
            "sliding_window" if sliding_window else None,
            "sort" if sort_call else None,
            "heap" if heap_usage else None,
            "bit_ops" if bit_ops else None,
            "closed_form" if closed_form else None,
        ]
        if t
    ]
    return AstFeatures(
        recursion=recursion, memoization=memoization, iterative_dp_table=iterative_dp_table,
        segment_tree_like=segment_tree_like, fenwick_like=fenwick_like, union_find_like=union_find_like,
        dfs_bfs=dfs_bfs, two_pointers=two_pointers, sliding_window=sliding_window,
        sort_call=sort_call, heap_usage=heap_usage, bit_ops=bit_ops,
        closed_form=closed_form, has_lru_cache=has_lru_cache,
        loops_max_depth=loops_max_depth, tokens=tokens,
    )


def ast_to_family_hints(features: AstFeatures) -> list[str]:
    """Suggest which of the 8 core families this solution likely belongs to."""
    hints: list[str] = []
    if features.memoization or features.iterative_dp_table:
        hints.append("dynamic_programming")
    if features.segment_tree_like or features.fenwick_like:
        hints.append("range_queries")
    if features.union_find_like or features.heap_usage:
        hints.append("data_structures")
    if features.dfs_bfs or features.recursion:
        hints.append("complete_search")
    if features.two_pointers or features.sliding_window:
        hints.append("amortized_analysis")
    if features.sort_call:
        hints.append("sorting")
    if features.bit_ops:
        hints.append("bit_manipulation")
    if features.closed_form:
        hints.append("dynamic_programming")  # counting closed forms are often DP-derived
    uniq: list[str] = []
    for h in hints:
        if h in CORE_FAMILY_SET and h not in uniq:
            uniq.append(h)
    return uniq or ["complete_search"]
