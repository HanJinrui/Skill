"""Rule-based Query Schema extraction for online graph retrieval.

Input:  raw problem statement (optionally augmented by an external summary).
Output: a `QuerySchema` structure the graph retriever understands.

Design targets:

* Works without any LLM.
* Deterministic.
* Reuses the exact same facet extractor the offline build uses, so the
  "signals" the retriever matches against the graph are produced by the
  same rules that wrote the graph.
* Also produces an explicit list of candidate families (by scoring all
  core families against the problem text with a bag of keyword votes).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Dict, List, Sequence, Tuple

from .facet_extract import FacetBundle, explicit_signal_tags, extract_from_text
from .graph_schema import CORE_FAMILIES


# Each family has a bag of positive keyword patterns.
_FAMILY_KEYWORDS: Dict[str, Tuple[str, ...]] = {
    "amortized_analysis": (
        r"sliding\s+window", r"two\s+pointers?", r"monotonic\s+(?:stack|queue|deque)",
        r"substring", r"subarray\b", r"amortized",
    ),
    "bit_manipulation": (
        r"\bxor\b", r"\bbitmask\b", r"\bparity\b", r"\bbitwise\b",
        r"bit\s+ops", r"bits\s+of",
    ),
    "complete_search": (
        r"\bbacktrack", r"\benumerate", r"all\s+subsets", r"all\s+permutations",
        r"brute\s+force", r"\b2\^n\b", r"n\s*[≤<]=?\s*20",
    ),
    "data_structures": (
        r"\bheap\b", r"\bpriority\s+queue\b", r"\bstack\b", r"\bqueue\b",
        r"\bunion[\-\s]?find\b", r"\bhash\s*map\b", r"\bdsu\b",
    ),
    "dynamic_programming": (
        r"\bdp\b", r"dynamic\s+programming", r"\brecurrence\b",
        r"count\s+the\s+number\s+of", r"\bminimum\s+cost\b", r"optimal\s+value",
    ),
    "greedy_algorithms": (
        r"\bgreedy\b", r"sort\s+and\s+pick", r"sort\s+them",
        r"exchange\s+argument", r"local\s+(?:choice|minimum|maximum)",
    ),
    "range_queries": (
        r"\bprefix\s+sum\b", r"\bfenwick\b", r"\bbit\s+tree\b", r"segment\s+tree",
        r"range\s+(?:query|queries|sum|update|add|min|max)",
        r"\bq\s+queries\b", r"many\s+queries", r"difference\s+array",
    ),
    "sorting": (
        r"\bsort\b", r"sort\s+by", r"coordinate\s+compression",
        r"\bascending\b", r"\bdescending\b", r"sorted\s+order",
    ),
}
_FAMILY_KEYWORD_PATTERNS: Dict[str, List[re.Pattern]] = {
    fam: [re.compile(p, re.IGNORECASE) for p in pats]
    for fam, pats in _FAMILY_KEYWORDS.items()
}


@dataclass
class QuerySchema:
    raw_problem_text: str
    candidate_families: List[str] = field(default_factory=list)
    input_shapes: List[str] = field(default_factory=list)
    operation_tags: List[str] = field(default_factory=list)
    goal_tags: List[str] = field(default_factory=list)
    constraint_tags: List[str] = field(default_factory=list)
    signal_tags: List[str] = field(default_factory=list)
    mechanism_hints: List[str] = field(default_factory=list)
    keywords: List[str] = field(default_factory=list)
    is_multi_skill_likely: bool = False
    family_scores: Dict[str, float] = field(default_factory=dict)
    routing_confidence: float = 0.0

    def to_dict(self) -> Dict[str, object]:
        return {
            "raw_problem_text": self.raw_problem_text[:4000],
            "candidate_families": list(self.candidate_families),
            "input_shapes": list(self.input_shapes),
            "operation_tags": list(self.operation_tags),
            "goal_tags": list(self.goal_tags),
            "constraint_tags": list(self.constraint_tags),
            "signal_tags": list(self.signal_tags),
            "mechanism_hints": list(self.mechanism_hints),
            "keywords": list(self.keywords),
            "is_multi_skill_likely": self.is_multi_skill_likely,
            "family_scores": dict(self.family_scores),
            "routing_confidence": float(self.routing_confidence),
        }


def _score_families(text: str) -> Dict[str, float]:
    scores: Dict[str, float] = {f: 0.0 for f in CORE_FAMILIES}
    for fam, pats in _FAMILY_KEYWORD_PATTERNS.items():
        for pat in pats:
            if pat.search(text):
                scores[fam] += 1.0
    return scores


_KEYWORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9_]{2,}")
_STOPWORDS = {
    "the", "and", "for", "with", "that", "from", "this", "into", "when",
    "then", "have", "will", "you", "are", "but", "not", "print", "output",
    "input", "also", "given", "each", "all", "any", "some", "such", "case",
    "cases", "times", "time",
}


def _extract_keywords(text: str, limit: int = 12) -> List[str]:
    counts: Dict[str, int] = {}
    for tok in _KEYWORD_RE.findall(text.lower()):
        if tok in _STOPWORDS or len(tok) < 3:
            continue
        counts[tok] = counts.get(tok, 0) + 1
    return [t for t, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:limit]]


def _is_multi_skill_likely(family_scores: Dict[str, float], facets: FacetBundle) -> bool:
    strong = [fam for fam, s in family_scores.items() if s >= 2.0]
    if len(strong) >= 2:
        return True
    # Heuristic: presence of both "sort/greedy" + range-query-ish signals → likely multi.
    ops = set(facets.operation_tags)
    fams = set(strong)
    if {"sort_action"} & ops and {"range_query", "many_range_queries"} & ops:
        return True
    if {"sorting", "greedy_algorithms"} & fams and {"range_queries", "data_structures"} & fams:
        return True
    return False


def analyze(
    problem_text: str,
    *,
    extra_text: Sequence[str] = (),
    top_family_limit: int = 3,
) -> QuerySchema:
    """Analyse a problem statement into a Query Schema. Rule-based, no LLM."""
    blob = problem_text or ""
    if extra_text:
        blob = blob + "\n" + "\n".join(extra_text)

    family_scores = _score_families(blob)
    # Top families with a minimal evidence threshold.
    ranked_scores = [(fam, s) for fam, s in sorted(family_scores.items(), key=lambda kv: (-kv[1], kv[0]))
                     if s > 0]
    top_score = ranked_scores[0][1] if ranked_scores else 0.0
    # Conservative routing: weak evidence should remain uncertain instead of
    # opening all families and letting graph propagation amplify noise.
    if top_score >= 2.0:
        candidate_families = [fam for fam, s in ranked_scores if s >= max(1.0, top_score - 1.0)][:top_family_limit]
    elif top_score >= 1.0:
        candidate_families = [ranked_scores[0][0]]
    else:
        candidate_families = []
    routing_confidence = min(1.0, top_score / 3.0)

    facets = extract_from_text(blob, family_hint=candidate_families, include_family_implied=False)
    multi = _is_multi_skill_likely(family_scores, facets)
    strong_signals = list(explicit_signal_tags(facets))
    explicit_mechanisms = list(facets.mechanism_tags)

    return QuerySchema(
        raw_problem_text=problem_text or "",
        candidate_families=candidate_families,
        input_shapes=list(facets.input_shape_tags),
        operation_tags=list(facets.operation_tags),
        goal_tags=list(facets.goal_tags),
        constraint_tags=[
            s for s in facets.signal_tags
            if s.startswith("n_le_") or s in ("q_large", "small_alphabet")
        ],
        signal_tags=strong_signals,
        mechanism_hints=explicit_mechanisms,
        keywords=_extract_keywords(blob),
        is_multi_skill_likely=multi,
        family_scores={k: float(v) for k, v in family_scores.items() if v > 0},
        routing_confidence=routing_confidence,
    )
