"""Typed constrained propagation on the heterogeneous skill graph.

We intentionally do *not* use a generic PPR implementation. Different
edge types mean different things, and the design document lists an
explicit priority:

    prototype_solution_supports_skill  >
    skill_implements_mechanism         >
    skill_triggered_by_signal          >
    prototype_problem_supports_skill   >
    skill_cooccurs_skill               >
    bundle_contains_skill

Each iteration we compute:

    score[v] = alpha * seed[v]
             + (1 - alpha) * sum_r lambda_r * sum_{u->v in r} w(u,v) * score_t(u)
             - delta * conflict_penalty(v)

where `lambda_r` comes from config. `conflict_penalty(v)` sums the
current score of skills that appear on the other end of a negative edge
from `v`, weighted by the edge weight — it represents "if rival
mechanisms are already highly ranked, this skill should lose a bit of
score".
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Sequence, Tuple

from .graph_schema import (
    EDGE_BUNDLE_CONTAINS_SKILL,
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
    parse_node_id,
    signal_node_id,
    mechanism_node_id,
    family_node_id,
    skill_node_id,
)

GENERIC_PROPAGATION_SIGNALS = frozenset({"maximize", "minimize", "construct"})


@dataclass
class GraphSlice:
    """A thin representation of the graph for in-RAM propagation."""
    # edges_by_type[type] -> list of (src, dst, weight)
    edges_by_type: Dict[str, List[Tuple[str, str, float]]] = field(default_factory=dict)
    # node_type -> set of node_ids
    nodes_by_type: Dict[str, set] = field(default_factory=dict)
    # fast lookup: skill_node_id -> raw skill_id
    skill_ids: List[str] = field(default_factory=list)

    def add_edge(self, etype: str, src: str, dst: str, weight: float) -> None:
        self.edges_by_type.setdefault(etype, []).append((src, dst, weight))


def build_slice(
    *,
    skill_nodes: Sequence[Dict[str, Any]],
    proto_problem_nodes: Sequence[Dict[str, Any]],
    proto_solution_nodes: Sequence[Dict[str, Any]],
    family_nodes: Sequence[Dict[str, Any]],
    mechanism_nodes: Sequence[Dict[str, Any]],
    signal_nodes: Sequence[Dict[str, Any]],
    edges: Sequence[Dict[str, Any]],
) -> GraphSlice:
    g = GraphSlice()
    g.nodes_by_type["skill"] = {n["node_id"] for n in skill_nodes}
    g.nodes_by_type["family"] = {n["node_id"] for n in family_nodes}
    g.nodes_by_type["mechanism"] = {n["node_id"] for n in mechanism_nodes}
    g.nodes_by_type["signal"] = {n["node_id"] for n in signal_nodes}
    g.nodes_by_type["prototype_problem"] = {n["node_id"] for n in proto_problem_nodes}
    g.nodes_by_type["prototype_solution"] = {n["node_id"] for n in proto_solution_nodes}
    g.skill_ids = [n["skill_id"] for n in skill_nodes]
    for e in edges:
        g.add_edge(e["edge_type"], e["src"], e["dst"], float(e.get("weight") or 0.0))
    return g


# --------------------------------------------------------------------------- #
# Seed → per-skill initial scores
# --------------------------------------------------------------------------- #

def distribute_seeds_to_skills(
    *,
    seed_scores_by_view: Dict[str, Dict[str, float]],
    graph: GraphSlice,
    edge_weights: Dict[str, float],
) -> Dict[str, float]:
    """Convert view-level seed scores into initial skill-level scores.

    * skill_master seeds are already skill nodes → copy directly.
    * prototype_problem seeds push score to their supported skill via
      prototype_problem_supports_skill edges.
    * prototype_solution seeds push score similarly, weighted higher.
    * signal_view seeds are skill nodes → copy.
    """
    skill_score: Dict[str, float] = defaultdict(float)

    for nid, sc in (seed_scores_by_view.get("skill_master") or {}).items():
        skill_score[nid] += sc
    for nid, sc in (seed_scores_by_view.get("signal_view") or {}).items():
        skill_score[nid] += 0.25 * sc  # signal-view is keyword-dense; keep it weak.

    # Prototype → skill via support edges.
    w_prob = edge_weights.get(EDGE_PROTO_PROB_SUPPORTS_SKILL, 0.8)
    w_sol = edge_weights.get(EDGE_PROTO_SOL_SUPPORTS_SKILL, 1.2)
    prob_seed = seed_scores_by_view.get("prototype_problem") or {}
    sol_seed = seed_scores_by_view.get("prototype_solution") or {}
    for src, dst, w in graph.edges_by_type.get(EDGE_PROTO_PROB_SUPPORTS_SKILL, ()):
        if src in prob_seed:
            skill_score[dst] += prob_seed[src] * w * w_prob
    for src, dst, w in graph.edges_by_type.get(EDGE_PROTO_SOL_SUPPORTS_SKILL, ()):
        if src in sol_seed:
            skill_score[dst] += sol_seed[src] * w * w_sol

    return dict(skill_score)


# --------------------------------------------------------------------------- #
# Facet pre-filter / soft boost
# --------------------------------------------------------------------------- #

def facet_boost(
    *,
    base_scores: Dict[str, float],
    skill_nodes_by_id: Dict[str, Dict[str, Any]],
    candidate_families: Sequence[str],
) -> Dict[str, float]:
    """Softly boost skills whose families overlap candidate_families.

    We don't hard-filter: tiny index, and a bad family prediction should
    not cause a zero-hit result.
    """
    if not candidate_families:
        return dict(base_scores)
    cand = set(candidate_families)
    out: Dict[str, float] = {}
    for nid, sc in base_scores.items():
        # nid is "skill::<sid>"
        ns, sid = parse_node_id(nid)
        if ns != "skill":
            out[nid] = sc
            continue
        skill = skill_nodes_by_id.get(sid, {})
        fams = set(skill.get("families") or [])
        if fams & cand:
            out[nid] = sc * 1.25 + 0.05  # boost matched families
        else:
            out[nid] = sc * 0.75  # light demotion (never zero)
    return out


# --------------------------------------------------------------------------- #
# Typed propagation
# --------------------------------------------------------------------------- #

def propagate(
    *,
    graph: GraphSlice,
    seed_skill_scores: Dict[str, float],
    seed_signal_scores: Dict[str, float] | None,
    seed_mechanism_scores: Dict[str, float] | None,
    edge_weights: Dict[str, float],
    alpha: float,
    steps: int,
    conflict_penalty: float,
    schema_signals: Sequence[str] = (),
    schema_mechanisms: Sequence[str] = (),
) -> Dict[str, float]:
    """Run typed propagation for `steps` iterations. Returns score per node.

    We maintain a score map over `skill` and `mechanism` / `signal`
    nodes. Propagation paths that matter in practice:

        prototype_solution --supports-->  skill   (initial seed)
        prototype_problem  --supports-->  skill   (initial seed)
        signal  <--triggered_by--  skill          (skill gets pulled
                                                    in by matched signals)
        mechanism <--implements--  skill          (skill pulled in by
                                                    matched mechanisms)
        skill <--cooccurs--> skill                (light synergy)
        bundle --contains--> skill                (bundle → component)
    """
    scores: Dict[str, float] = defaultdict(float)
    scores.update(seed_skill_scores)

    # Expose schema signals / mechanisms as first-class node scores so
    # propagation from them into skills has mass to carry.
    strong_schema_signals = [sig_id for sig_id in schema_signals if sig_id not in GENERIC_PROPAGATION_SIGNALS]
    strong_schema_mechanisms = [mech_id for mech_id in schema_mechanisms if mech_id]

    for sig_id in strong_schema_signals:
        nid = signal_node_id(sig_id)
        scores[nid] = max(scores[nid], 1.0)
    for mech_id in strong_schema_mechanisms:
        nid = mechanism_node_id(mech_id)
        scores[nid] = max(scores[nid], 1.0)
    if seed_signal_scores:
        for nid, sc in seed_signal_scores.items():
            scores[nid] = max(scores[nid], sc)
    if seed_mechanism_scores:
        for nid, sc in seed_mechanism_scores.items():
            scores[nid] = max(scores[nid], sc)

    initial = dict(scores)

    w = edge_weights
    # Which edge types drive mass INTO skills (and in what direction)?
    # Every entry is (edge_type, direction, lambda). direction="in" means
    # we use src→dst edges where dst is the target; direction="out" means
    # we reverse. For signal-triggered edges the graph stores
    # skill→signal, so to pull skills from signals we traverse reverse.
    skill_inflows: List[Tuple[str, str, float]] = [
        (EDGE_SKILL_IMPLEMENTS_MECHANISM, "reverse",
         w.get(EDGE_SKILL_IMPLEMENTS_MECHANISM, 1.0)),
        (EDGE_SKILL_TRIGGERED_BY_SIGNAL, "reverse",
         w.get(EDGE_SKILL_TRIGGERED_BY_SIGNAL, 0.9)),
        (EDGE_PROTO_PROB_SUPPORTS_SKILL, "forward",
         w.get(EDGE_PROTO_PROB_SUPPORTS_SKILL, 0.8)),
        (EDGE_PROTO_SOL_SUPPORTS_SKILL, "forward",
         w.get(EDGE_PROTO_SOL_SUPPORTS_SKILL, 1.2)),
        (EDGE_SKILL_COOCCURS_SKILL, "forward",
         w.get(EDGE_SKILL_COOCCURS_SKILL, 0.5)),
        (EDGE_BUNDLE_CONTAINS_SKILL, "forward",
         w.get(EDGE_BUNDLE_CONTAINS_SKILL, 0.6)),
    ]

    # Mechanism inflows (so signals can activate mechanisms → skills).
    mechanism_inflows: List[Tuple[str, str, float]] = [
        # family → mechanism (forward), weak
        (EDGE_PROTO_SOL_USES_MECHANISM, "forward", 0.6),
    ]
    # Signal inflows (prototype_problem → signal provides weak mass).
    signal_inflows: List[Tuple[str, str, float]] = [
        (EDGE_PROTO_PROB_HAS_SIGNAL, "forward", 0.4),
    ]

    def _accumulate_inflow(plans: Sequence[Tuple[str, str, float]]) -> Dict[str, float]:
        incoming: Dict[str, float] = defaultdict(float)
        for etype, direction, lam in plans:
            for src, dst, ew in graph.edges_by_type.get(etype, ()):
                if direction == "forward":
                    incoming[dst] += lam * ew * scores.get(src, 0.0)
                else:  # reverse
                    incoming[src] += lam * ew * scores.get(dst, 0.0)
        return incoming

    for _ in range(max(1, int(steps))):
        incoming_skill = _accumulate_inflow(skill_inflows)
        incoming_mech = _accumulate_inflow(mechanism_inflows)
        incoming_sig = _accumulate_inflow(signal_inflows)

        new_scores: Dict[str, float] = defaultdict(float)

        # Update skill nodes
        for nid in graph.nodes_by_type.get("skill", ()):
            base = alpha * initial.get(nid, 0.0) + (1.0 - alpha) * incoming_skill.get(nid, 0.0)
            new_scores[nid] = base

        # Mechanism / signal nodes update too, so propagation continues next step.
        for nid in graph.nodes_by_type.get("mechanism", ()):
            base = alpha * initial.get(nid, 0.0) + (1.0 - alpha) * incoming_mech.get(nid, 0.0)
            if base > 0:
                new_scores[nid] = base
        for nid in graph.nodes_by_type.get("signal", ()):
            base = alpha * initial.get(nid, 0.0) + (1.0 - alpha) * incoming_sig.get(nid, 0.0)
            if base > 0:
                new_scores[nid] = base

        # Apply conflict penalty at the skill level.
        if conflict_penalty > 0:
            for src, dst, ew in graph.edges_by_type.get(EDGE_SKILL_CONFLICTS_SKILL, ()):
                new_scores[dst] -= conflict_penalty * ew * scores.get(src, 0.0)
            # Mechanism conflict leaks back into skills via skill_implements_mechanism.
            # Track mechanism-level penalty then push down to skills.
            mech_penalty: Dict[str, float] = defaultdict(float)
            for src, dst, ew in graph.edges_by_type.get(EDGE_MECHANISM_CONFLICTS_MECHANISM, ()):
                mech_penalty[dst] += conflict_penalty * ew * scores.get(src, 0.0)
            if mech_penalty:
                for src_s, dst_m, ew in graph.edges_by_type.get(EDGE_SKILL_IMPLEMENTS_MECHANISM, ()):
                    if dst_m in mech_penalty:
                        new_scores[src_s] -= 0.5 * mech_penalty[dst_m] * ew

        # Keep non-skill mass from the previous iteration so mechanism/signal
        # scores don't decay faster than skills.
        for nid in list(scores.keys()):
            if nid not in new_scores:
                ns, _ = parse_node_id(nid)
                if ns in ("signal", "mechanism"):
                    new_scores[nid] = 0.5 * scores[nid]

        scores = dict(new_scores)

    # Clip negatives to 0.
    return {nid: max(0.0, sc) for nid, sc in scores.items()}
