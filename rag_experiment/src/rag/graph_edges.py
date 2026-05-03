"""Build edge tables for every edge type defined in graph_schema.

Each edge is a dict with keys:

    edge_type:  str
    src:        namespaced node id
    dst:        namespaced node id
    weight:     float (negative for conflict edges we store positive weight
                and let the retriever subtract it).
    source:     short provenance string ("rule", "stage_c", "pmi", ...)
    evidence:   list[str] of optional evidence markers
"""
from __future__ import annotations

import math
from collections import Counter
from typing import Any, Dict, Iterable, List, Sequence, Tuple

from .graph_schema import (
    EDGE_BUNDLE_CONTAINS_SKILL,
    EDGE_FAMILY_HAS_MECHANISM,
    EDGE_MECHANISM_CONFLICTS_MECHANISM,
    EDGE_PROTO_PROB_HAS_SIGNAL,
    EDGE_PROTO_PROB_SUPPORTS_SKILL,
    EDGE_PROTO_SOL_SUPPORTS_SKILL,
    EDGE_PROTO_SOL_USES_MECHANISM,
    EDGE_SKILL_CONFLICTS_SKILL,
    EDGE_SKILL_COOCCURS_SKILL,
    EDGE_SKILL_HAS_FAMILY,
    EDGE_SKILL_IMPLEMENTS_MECHANISM,
    EDGE_SKILL_TRIGGERED_BY_SIGNAL,
    FAMILY_MECHANISMS,
    MECHANISM_CONFLICT_PAIRS,
    SKILL_CONFLICT_PAIRS,
    family_node_id,
    mechanism_node_id,
    signal_node_id,
    skill_node_id,
)


def _edge(
    edge_type: str,
    src: str,
    dst: str,
    *,
    weight: float,
    source: str,
    evidence: Iterable[str] = (),
) -> Dict[str, Any]:
    return {
        "edge_type": edge_type,
        "src": src,
        "dst": dst,
        "weight": float(weight),
        "source": source,
        "evidence": list(evidence),
    }


# --------------------------------------------------------------------------- #
# Structural edges (skill/family/mechanism)
# --------------------------------------------------------------------------- #

def build_skill_family_edges(skill_nodes: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for s in skill_nodes:
        sid = s["skill_id"]
        for fam in s.get("families") or []:
            out.append(_edge(
                EDGE_SKILL_HAS_FAMILY,
                skill_node_id(sid), family_node_id(fam),
                weight=1.0, source="skill_card",
            ))
    return out


def build_family_mechanism_edges() -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for fam, mechs in FAMILY_MECHANISMS.items():
        for mech in mechs:
            out.append(_edge(
                EDGE_FAMILY_HAS_MECHANISM,
                family_node_id(fam), mechanism_node_id(mech),
                weight=1.0, source="rule",
            ))
    return out


def build_skill_mechanism_edges(skill_nodes: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """skill → mechanism edges.

    Explicitly mentioned mechanisms get full weight; family-implied ones
    get a weaker default weight. This keeps the offline graph meaningful
    even when a skill card has sparse natural language.
    """
    out: List[Dict[str, Any]] = []
    for s in skill_nodes:
        sid = s["skill_id"]
        explicit = set(s.get("facets", {}).get("mechanism_tags") or [])
        families = s.get("families") or []
        family_implied: set[str] = set()
        for fam in families:
            family_implied.update(FAMILY_MECHANISMS.get(fam, ()))
        for mech in explicit:
            out.append(_edge(
                EDGE_SKILL_IMPLEMENTS_MECHANISM,
                skill_node_id(sid), mechanism_node_id(mech),
                weight=1.0, source="facet_extract",
                evidence=["skill_text"],
            ))
        # Stage D v2 skills already carry subtype-specific text. Avoid adding
        # every family-default mechanism because it makes weak routing look
        # falsely precise.
        if not s.get("skill_level"):
            for mech in family_implied - explicit:
                out.append(_edge(
                    EDGE_SKILL_IMPLEMENTS_MECHANISM,
                    skill_node_id(sid), mechanism_node_id(mech),
                    weight=0.4, source="family_prior",
                    evidence=["family_default"],
                ))
    return out


def build_skill_signal_edges(skill_nodes: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for s in skill_nodes:
        sid = s["skill_id"]
        for sig in s.get("facets", {}).get("signal_tags") or []:
            out.append(_edge(
                EDGE_SKILL_TRIGGERED_BY_SIGNAL,
                skill_node_id(sid), signal_node_id(sig),
                weight=0.8, source="facet_extract",
            ))
    return out


# --------------------------------------------------------------------------- #
# Prototype edges
# --------------------------------------------------------------------------- #

def build_prototype_problem_edges(
    proto_problems: Sequence[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for p in proto_problems:
        pp_node = p["node_id"]
        sid = p["skill_id"]
        out.append(_edge(
            EDGE_PROTO_PROB_SUPPORTS_SKILL,
            pp_node, skill_node_id(sid),
            weight=1.0, source="stage_a+b",
        ))
        for sig in p.get("signals") or []:
            out.append(_edge(
                EDGE_PROTO_PROB_HAS_SIGNAL,
                pp_node, signal_node_id(sig),
                weight=0.8, source="facet_extract",
            ))
    return out


def build_prototype_solution_edges(
    proto_solutions: Sequence[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for s in proto_solutions:
        ps_node = s["node_id"]
        sid = s["skill_id"]
        # Weight from consistency / label source / LLM confidence.
        w = 0.8
        if s.get("consistency_type") == "consistent":
            w += 0.3
        if s.get("label_source") == "glm_ast_fused":
            w += 0.1
        w += 0.2 * min(1.0, float(s.get("llm_confidence") or 0.0))
        out.append(_edge(
            EDGE_PROTO_SOL_SUPPORTS_SKILL,
            ps_node, skill_node_id(sid),
            weight=min(w, 1.4), source="stage_c",
        ))
        for mech in s.get("mechanism_tags") or []:
            out.append(_edge(
                EDGE_PROTO_SOL_USES_MECHANISM,
                ps_node, mechanism_node_id(mech),
                weight=1.0, source="ast+text",
            ))
    return out


# --------------------------------------------------------------------------- #
# Bundle / cooccur / conflict edges
# --------------------------------------------------------------------------- #

def build_bundle_contains_edges(
    skill_nodes: Sequence[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """For every multi-skill card, create bundle_contains_skill edges to
    the corresponding single-skill cards (if those exist in the index)."""
    from ..taxonomy import skill_id_for_single

    sid_set = {s["skill_id"] for s in skill_nodes}
    subtype_by_family: Dict[str, List[str]] = {}
    for s in skill_nodes:
        if s.get("skill_level") == "subtype":
            for fam in s.get("families") or []:
                subtype_by_family.setdefault(fam, []).append(s["skill_id"])
    out: List[Dict[str, Any]] = []
    for s in skill_nodes:
        if s.get("scope") != "multi" and s.get("skill_level") != "bundle":
            continue
        bundle_sid = s["skill_id"]
        for fam in s.get("families") or []:
            part_ids = [skill_id_for_single(fam), f"family__{fam}"] + subtype_by_family.get(fam, [])[:4]
            for part_sid in part_ids:
                if part_sid == bundle_sid or part_sid not in sid_set:
                    continue
                out.append(_edge(
                    EDGE_BUNDLE_CONTAINS_SKILL,
                    skill_node_id(bundle_sid), skill_node_id(part_sid),
                    weight=1.0 if part_sid.startswith("family__") else 0.6,
                    source="skill_card",
                ))
    return out


def build_skill_cooccur_edges(
    *,
    skill_nodes: Sequence[Dict[str, Any]],
    problem_labels: Sequence[Dict[str, Any]],
    solutions: Sequence[Dict[str, Any]],
    composition_rows: Sequence[Dict[str, Any]] | None = None,
    min_cooccur: int = 2,
) -> List[Dict[str, Any]]:
    """skill_cooccurs_skill: normalized PMI over single-skill cooccurrences.

    We pool cooccurrences from both Stage B (problem-level) and Stage C
    (solution-level) signals. Edges are emitted symmetrically (src < dst
    alphabetically) at the `single-skill` granularity.
    """
    from ..taxonomy import skill_id_for_single

    sid_set = {s["skill_id"] for s in skill_nodes}

    # Each observation is a set of distinct families.
    observations: List[Tuple[str, ...]] = []
    if composition_rows is not None:
        for row in composition_rows:
            fams = [f for f in (row.get("family_set") or row.get("candidate_families") or [])
                    if f in FAMILY_MECHANISMS]
            if len(set(fams)) >= 2:
                observations.append(tuple(sorted(set(fams))))
    else:
        for row in problem_labels:
            fams = [f for f in (row.get("normalized_multi_skills") or [])
                    if f in FAMILY_MECHANISMS]
            if len(set(fams)) >= 2:
                observations.append(tuple(sorted(set(fams))))
        for row in solutions:
            fams = [f for f in (row.get("detected_multi_skills") or [])
                    if f in FAMILY_MECHANISMS]
            if len(set(fams)) >= 2:
                observations.append(tuple(sorted(set(fams))))

    if not observations:
        return []

    family_counts: Counter = Counter()
    pair_counts: Counter = Counter()
    total = len(observations)
    for fams in observations:
        for f in fams:
            family_counts[f] += 1
        for i in range(len(fams)):
            for j in range(i + 1, len(fams)):
                pair_counts[(fams[i], fams[j])] += 1

    out: List[Dict[str, Any]] = []
    for (fa, fb), c in pair_counts.items():
        if c < min_cooccur:
            continue
        p_a = family_counts[fa] / total
        p_b = family_counts[fb] / total
        p_ab = c / total
        if p_a <= 0 or p_b <= 0:
            continue
        pmi = math.log(max(p_ab, 1e-9) / (p_a * p_b))
        # Map (−∞, +∞) → (0, 1] via sigmoid for nicer weight.
        weight = 1.0 / (1.0 + math.exp(-pmi))
        sid_a = f"family__{fa}" if f"family__{fa}" in sid_set else skill_id_for_single(fa)
        sid_b = f"family__{fb}" if f"family__{fb}" in sid_set else skill_id_for_single(fb)
        if sid_a not in sid_set or sid_b not in sid_set:
            continue
        out.append(_edge(
            EDGE_SKILL_COOCCURS_SKILL,
            skill_node_id(sid_a), skill_node_id(sid_b),
            weight=round(weight, 4), source="pmi",
            evidence=[f"cooccur={c}", f"pa={p_a:.3f}", f"pb={p_b:.3f}"],
        ))
        # Symmetric edge so propagation in both directions works naturally.
        out.append(_edge(
            EDGE_SKILL_COOCCURS_SKILL,
            skill_node_id(sid_b), skill_node_id(sid_a),
            weight=round(weight, 4), source="pmi",
            evidence=[f"cooccur={c}"],
        ))
    return out


def build_skill_conflict_edges(skill_nodes: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Prior conflict edges at the skill level (single-skill id pairs)."""
    sid_set = {s["skill_id"] for s in skill_nodes}
    out: List[Dict[str, Any]] = []
    for a, b, w in SKILL_CONFLICT_PAIRS:
        if a in sid_set and b in sid_set:
            out.append(_edge(
                EDGE_SKILL_CONFLICTS_SKILL,
                skill_node_id(a), skill_node_id(b),
                weight=w, source="rule_prior",
            ))
            out.append(_edge(
                EDGE_SKILL_CONFLICTS_SKILL,
                skill_node_id(b), skill_node_id(a),
                weight=w, source="rule_prior",
            ))
    return out


def build_mechanism_conflict_edges() -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for a, b, w in MECHANISM_CONFLICT_PAIRS:
        out.append(_edge(
            EDGE_MECHANISM_CONFLICTS_MECHANISM,
            mechanism_node_id(a), mechanism_node_id(b),
            weight=w, source="rule_prior",
        ))
        out.append(_edge(
            EDGE_MECHANISM_CONFLICTS_MECHANISM,
            mechanism_node_id(b), mechanism_node_id(a),
            weight=w, source="rule_prior",
        ))
    return out
