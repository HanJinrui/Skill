"""Rule-based facet extraction.

Given a blob of text (problem statement, skill card text, or solution
summary) we return the union of signal / mechanism / shape / operation /
goal / constraint / negative tags that the text plausibly triggers.

The same module is used during:

* offline graph build — to derive standardized facets on top of existing
  skill cards (without rebuilding Stage D),
* offline prototype build — to label prototype problem / solution nodes,
* online query analysis — to fill the Query Schema used by the graph
  retriever.

Everything here is rule-based and deterministic.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Sequence, Tuple

from .graph_schema import (
    CONSTRAINT_REGEXES,
    FAMILY_MECHANISMS,
    MECHANISM_BY_ID,
    SIGNAL_BY_ID,
    mechanism_surface_patterns,
    signal_surface_patterns,
)


@dataclass(frozen=True)
class FacetBundle:
    """Standardized facet tags derived from arbitrary text."""
    mechanism_tags: Tuple[str, ...] = field(default_factory=tuple)
    signal_tags: Tuple[str, ...] = field(default_factory=tuple)
    input_shape_tags: Tuple[str, ...] = field(default_factory=tuple)
    operation_tags: Tuple[str, ...] = field(default_factory=tuple)
    goal_tags: Tuple[str, ...] = field(default_factory=tuple)
    complexity_tags: Tuple[str, ...] = field(default_factory=tuple)
    negative_tags: Tuple[str, ...] = field(default_factory=tuple)
    keyword_tags: Tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> Dict[str, List[str]]:
        return {
            "mechanism_tags": list(self.mechanism_tags),
            "signal_tags": list(self.signal_tags),
            "input_shape_tags": list(self.input_shape_tags),
            "operation_tags": list(self.operation_tags),
            "goal_tags": list(self.goal_tags),
            "complexity_tags": list(self.complexity_tags),
            "negative_tags": list(self.negative_tags),
            "keyword_tags": list(self.keyword_tags),
        }


# Complexity regexes — used to infer a coarse complexity_tag for skill cards.
import re
_COMPLEXITY_PATTERNS: Tuple[Tuple[str, re.Pattern], ...] = (
    ("o_1", re.compile(r"\bO\(\s*1\s*\)", re.IGNORECASE)),
    ("o_logn", re.compile(r"\bO\(\s*log\s*n?\s*\)", re.IGNORECASE)),
    ("o_n", re.compile(r"\bO\(\s*n\s*\)", re.IGNORECASE)),
    ("o_nlogn", re.compile(r"\bO\(\s*n\s*\*?\s*log\s*n?\s*\)", re.IGNORECASE)),
    ("o_n_sqrt_n", re.compile(r"\bO\(\s*n\s*\*?\s*sqrt", re.IGNORECASE)),
    ("o_n_squared", re.compile(r"\bO\(\s*n\s*\^?\s*2\s*\)", re.IGNORECASE)),
    ("exponential", re.compile(r"\bO\(\s*2\s*\^\s*n\s*\)|\bO\(\s*n!\s*\)", re.IGNORECASE)),
)

# Negative-tag priors: if a skill explicitly mentions these, we record them so
# bundle assembly / propagation can avoid them (e.g. "prefix sum is
# insufficient under updates" → skill says that).
_NEGATIVE_MARKERS: Tuple[Tuple[str, re.Pattern], ...] = (
    ("avoid_prefix_under_updates",
     re.compile(r"prefix\s+sum[^.]*insufficient|prefix\s+sum[^.]*under\s+update", re.IGNORECASE)),
    ("avoid_nested_quadratic",
     re.compile(r"O\(\s*n\s*[*·]?\s*q\s*\)\s+will\s+time\s+out|nested\s+O\(n\^?2\)", re.IGNORECASE)),
)


_MECH_PATTERNS = mechanism_surface_patterns()
_SIG_PATTERNS = signal_surface_patterns()


def _dedup(seq: Iterable[str]) -> Tuple[str, ...]:
    seen: set[str] = set()
    out: List[str] = []
    for item in seq:
        if item and item not in seen:
            seen.add(item)
            out.append(item)
    return tuple(out)


def extract_from_text(
    text: str,
    *,
    family_hint: Sequence[str] | None = None,
) -> FacetBundle:
    """Derive facet tags from an arbitrary text blob.

    `family_hint` (if provided) is used to softly expand the set of
    candidate mechanisms — even mechanisms whose surface form doesn't
    appear explicitly become allowed if their family matches a hint. This
    is how we map a skill like `single__dynamic_programming` (which might
    have a sparse `core_idea`) to `state_transition_dp`, `dp_on_indices`,
    etc. without hallucinating.
    """
    text = text or ""
    lower = text.lower()

    # --- Mechanisms
    mechanisms: List[str] = []
    for mech_id, pats in _MECH_PATTERNS.items():
        if any(p.search(text) for p in pats):
            mechanisms.append(mech_id)

    if family_hint:
        for fam in family_hint:
            for mech_id in FAMILY_MECHANISMS.get(fam, ()):
                if mech_id not in mechanisms:
                    # Keep as a "family-implied" mechanism but don't mix into
                    # the primary explicit list — store separately so caller
                    # can decide. Simplest: append after explicit matches.
                    mechanisms.append(mech_id)

    # --- Signals (mixed category)
    signal_ids: List[str] = []
    for sig_id, pats in _SIG_PATTERNS.items():
        if any(p.search(text) for p in pats):
            signal_ids.append(sig_id)
    for sig_id, pat in CONSTRAINT_REGEXES:
        if pat.search(lower):
            signal_ids.append(sig_id)

    # --- Partition signals by category.
    shapes: List[str] = []
    operations: List[str] = []
    goals: List[str] = []
    constraints: List[str] = []
    keywords: List[str] = []
    for sid in signal_ids:
        spec = SIGNAL_BY_ID.get(sid)
        if not spec:
            continue
        if spec.category == "shape":
            shapes.append(sid)
        elif spec.category == "operation":
            operations.append(sid)
        elif spec.category == "goal":
            goals.append(sid)
        elif spec.category == "constraint":
            constraints.append(sid)
        elif spec.category == "keyword":
            keywords.append(sid)

    # --- Complexity tags
    complexity: List[str] = []
    for name, pat in _COMPLEXITY_PATTERNS:
        if pat.search(text):
            complexity.append(name)

    # --- Negative markers
    negatives: List[str] = []
    for name, pat in _NEGATIVE_MARKERS:
        if pat.search(text):
            negatives.append(name)

    return FacetBundle(
        mechanism_tags=_dedup(mechanisms),
        signal_tags=_dedup(signal_ids),
        input_shape_tags=_dedup(shapes),
        operation_tags=_dedup(operations),
        goal_tags=_dedup(goals),
        complexity_tags=_dedup(complexity),
        negative_tags=_dedup(negatives),
        keyword_tags=_dedup(keywords),
    )


def extract_skill_facets(skill: Dict[str, Any]) -> FacetBundle:
    """Extract facet tags for a Stage D skill card.

    We stitch together `skill_name / families / applicable_when /
    problem_signals / core_idea / template_strategy / common_pitfalls /
    complexity_pattern / retrieval_text` and run the generic extractor
    with `family_hint = skill["families"]`.
    """
    parts: List[str] = []
    parts.append(str(skill.get("skill_name") or ""))
    parts.append(", ".join(skill.get("families") or []))
    parts.append(str(skill.get("core_idea") or ""))
    parts.extend(str(x) for x in (skill.get("applicable_when") or []))
    parts.extend(str(x) for x in (skill.get("problem_signals") or []))
    parts.extend(str(x) for x in (skill.get("template_strategy") or []))
    parts.extend(str(x) for x in (skill.get("common_pitfalls") or []))
    parts.append(str(skill.get("complexity_pattern") or ""))
    parts.append(str(skill.get("retrieval_text") or ""))
    text = "\n".join(p for p in parts if p)
    return extract_from_text(text, family_hint=list(skill.get("families") or []))


def extract_problem_facets(problem: Dict[str, Any], *, label: Dict[str, Any] | None = None) -> FacetBundle:
    """Extract facets from a (problem, stage-B-label) pair."""
    parts: List[str] = []
    parts.append(str(problem.get("problem_statement") or ""))
    if label:
        parts.append(str(label.get("problem_summary") or ""))
        parts.extend(str(s) for s in (label.get("signals") or []))
        parts.extend(str(s) for s in (label.get("original_tags") or []))
    text = "\n".join(p for p in parts if p)
    # For a problem, we don't yet know the "right" family — but Stage B
    # gives us a set of `rule_candidates` we can pass as a soft hint.
    fam_hint: List[str] = []
    if label:
        fam_hint.extend([f for f in (label.get("rule_candidates") or []) if isinstance(f, str)])
    return extract_from_text(text, family_hint=fam_hint or None)


def extract_solution_facets(solution: Dict[str, Any]) -> FacetBundle:
    """Extract facets from a Stage C consistent/partial solution row.

    AST features give us a *much* more reliable mechanism hint than raw
    text, so we translate them first and then augment with a text scan.
    """
    ast = solution.get("ast_features") or {}
    mechanisms: List[str] = []
    if ast.get("sliding_window"):
        mechanisms.append("sliding_window")
    if ast.get("two_pointers"):
        mechanisms.append("two_pointers")
    if ast.get("segment_tree_like"):
        mechanisms.append("segment_tree")
    if ast.get("fenwick_like"):
        mechanisms.append("fenwick_tree")
    if ast.get("union_find_like"):
        mechanisms.append("union_find")
    if ast.get("dfs_bfs"):
        mechanisms.append("dfs_enumeration")
    if ast.get("heap_usage"):
        mechanisms.append("heap_maintenance")
    if ast.get("bit_ops"):
        mechanisms.append("shift_ops")
    if ast.get("iterative_dp_table") or ast.get("memoization"):
        mechanisms.append("state_transition_dp")
    if ast.get("sort_call"):
        mechanisms.append("comparator_sort")
    if ast.get("recursion"):
        mechanisms.append("backtracking")

    # Always scan the textual parts as well.
    text_parts: List[str] = []
    for hint in solution.get("ast_hints") or []:
        text_parts.append(str(hint))
    text_parts.append(str(solution.get("core_mechanism_summary") or ""))
    text_parts.append(str(solution.get("explanation") or ""))
    text_parts.append(str(solution.get("solution_code") or "")[:800])
    text_blob = "\n".join(p for p in text_parts if p)
    fam_hint = list(solution.get("detected_multi_skills") or [])
    text_bundle = extract_from_text(text_blob, family_hint=fam_hint or None)

    return FacetBundle(
        mechanism_tags=_dedup(list(mechanisms) + list(text_bundle.mechanism_tags)),
        signal_tags=text_bundle.signal_tags,
        input_shape_tags=text_bundle.input_shape_tags,
        operation_tags=text_bundle.operation_tags,
        goal_tags=text_bundle.goal_tags,
        complexity_tags=text_bundle.complexity_tags,
        negative_tags=text_bundle.negative_tags,
        keyword_tags=text_bundle.keyword_tags,
    )


def top_mechanism_from_facets(
    facets: FacetBundle,
    families: Sequence[str],
    limit: int = 6,
) -> List[str]:
    """Rank mechanisms for a skill by: (explicit, family-matched, by-order)."""
    fam_set = set(families or [])
    scored: List[Tuple[int, int, str]] = []
    for idx, mech_id in enumerate(facets.mechanism_tags):
        spec = MECHANISM_BY_ID.get(mech_id)
        if spec is None:
            continue
        fam_match = 1 if any(f in fam_set for f in spec.families) else 0
        scored.append((-fam_match, idx, mech_id))  # family-first, then input order
    scored.sort()
    return [m for _, _, m in scored[:limit]]
