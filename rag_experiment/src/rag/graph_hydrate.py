"""Hydrate a bundle + per-skill graph evidence into the final payload.

The hydrator is the *only* component that knows how the downstream
generator wants the retrieved skills formatted. It is kept separate so
we can extend the prompt format without touching the retrieval core.

Per-skill evidence is always produced so the retriever can attach it to
`RetrievalResult.graph_evidence` even if the generator ultimately only
renders the core skill card.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Sequence, Set

from .graph_schema import (
    EDGE_PROTO_PROB_SUPPORTS_SKILL,
    EDGE_PROTO_SOL_SUPPORTS_SKILL,
    EDGE_PROTO_SOL_USES_MECHANISM,
    EDGE_SKILL_IMPLEMENTS_MECHANISM,
    EDGE_SKILL_TRIGGERED_BY_SIGNAL,
    mechanism_node_id,
    parse_node_id,
    signal_node_id,
    skill_node_id,
)


@dataclass
class SkillEvidence:
    skill_id: str
    why_selected: str = ""
    matched_signals: List[str] = field(default_factory=list)
    matched_mechanisms: List[str] = field(default_factory=list)
    supporting_prototypes: List[str] = field(default_factory=list)
    prototype_evidence: List[Dict[str, str]] = field(default_factory=list)
    core_idea: str = ""
    template_strategy: List[str] = field(default_factory=list)
    pitfalls: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "skill_id": self.skill_id,
            "why_selected": self.why_selected,
            "matched_signals": list(self.matched_signals),
            "matched_mechanisms": list(self.matched_mechanisms),
            "supporting_prototypes": list(self.supporting_prototypes),
            "prototype_evidence": list(self.prototype_evidence),
            "core_idea": self.core_idea,
            "template_strategy": list(self.template_strategy),
            "pitfalls": list(self.pitfalls),
        }


def _index_edges_by_src(
    edges_by_type: Dict[str, List[tuple]],
    edge_type: str,
) -> Dict[str, List[tuple]]:
    idx: Dict[str, List[tuple]] = defaultdict(list)
    for src, dst, w in edges_by_type.get(edge_type, ()):
        idx[src].append((dst, w))
    return idx


def _index_edges_by_dst(
    edges_by_type: Dict[str, List[tuple]],
    edge_type: str,
) -> Dict[str, List[tuple]]:
    idx: Dict[str, List[tuple]] = defaultdict(list)
    for src, dst, w in edges_by_type.get(edge_type, ()):
        idx[dst].append((src, w))
    return idx


def hydrate_skill(
    *,
    skill_id: str,
    skill_card: Dict[str, Any],
    schema_signals: Set[str],
    schema_mechanisms: Set[str],
    edges_by_type: Dict[str, List[tuple]],
    proto_nodes_by_id: Dict[str, Dict[str, Any]],
    score: float,
    max_prototypes: int = 1,
) -> SkillEvidence:
    snid = skill_node_id(skill_id)

    # --- Matched signals (schema ∩ skill's triggered_by signals)
    skill_signals: Set[str] = set()
    for dst, _ in _index_edges_by_src(edges_by_type, EDGE_SKILL_TRIGGERED_BY_SIGNAL).get(snid, ()):
        ns, raw = parse_node_id(dst)
        if ns == "signal":
            skill_signals.add(raw)
    matched_signals = sorted(skill_signals & schema_signals) or sorted(skill_signals)[:3]

    # --- Matched mechanisms
    skill_mechs: Set[str] = set()
    for dst, _ in _index_edges_by_src(edges_by_type, EDGE_SKILL_IMPLEMENTS_MECHANISM).get(snid, ()):
        ns, raw = parse_node_id(dst)
        if ns == "mechanism":
            skill_mechs.add(raw)
    matched_mechanisms = sorted(skill_mechs & schema_mechanisms) or sorted(skill_mechs)[:3]

    # --- Supporting prototypes (problem & solution)
    proto_problem_ids: List[tuple] = []  # (node_id, weight)
    for src, w in _index_edges_by_dst(edges_by_type, EDGE_PROTO_PROB_SUPPORTS_SKILL).get(snid, ()):
        proto_problem_ids.append((src, w))
    proto_problem_ids.sort(key=lambda x: x[1], reverse=True)

    proto_solution_ids: List[tuple] = []
    for src, w in _index_edges_by_dst(edges_by_type, EDGE_PROTO_SOL_SUPPORTS_SKILL).get(snid, ()):
        proto_solution_ids.append((src, w))
    proto_solution_ids.sort(key=lambda x: x[1], reverse=True)

    prototype_evidence: List[Dict[str, str]] = []
    supporting: List[str] = []
    for src, _ in proto_solution_ids[:max_prototypes]:
        supporting.append(src)
        node = proto_nodes_by_id.get(src) or {}
        prototype_evidence.append({
            "kind": "solution",
            "prototype_id": node.get("prototype_solution_id") or src,
            "problem_id": node.get("problem_id") or "",
            "core_mechanism_summary": (node.get("core_mechanism_summary") or "")[:300],
        })
    for src, _ in proto_problem_ids[:max_prototypes]:
        supporting.append(src)
        node = proto_nodes_by_id.get(src) or {}
        prototype_evidence.append({
            "kind": "problem",
            "prototype_id": node.get("prototype_problem_id") or src,
            "problem_id": node.get("problem_id") or "",
            "problem_summary": (node.get("problem_summary") or "")[:300],
        })

    why_parts: List[str] = []
    if matched_signals:
        why_parts.append("matched signals: " + ", ".join(matched_signals[:4]))
    if matched_mechanisms:
        why_parts.append("matched mechanisms: " + ", ".join(matched_mechanisms[:4]))
    if prototype_evidence:
        why_parts.append(f"{len(prototype_evidence)} prototype example(s)")
    why = "; ".join(why_parts) or f"ranked by graph score={score:.3f}"

    return SkillEvidence(
        skill_id=skill_id,
        why_selected=why,
        matched_signals=matched_signals,
        matched_mechanisms=matched_mechanisms,
        supporting_prototypes=supporting,
        prototype_evidence=prototype_evidence,
        core_idea=str(skill_card.get("core_idea") or ""),
        template_strategy=list(skill_card.get("template_strategy") or []),
        pitfalls=list(skill_card.get("common_pitfalls") or []),
    )


def hydrate_bundle(
    *,
    ordered_skill_ids: Sequence[str],
    scores: Dict[str, float],
    skills_by_id: Dict[str, Dict[str, Any]],
    schema_signals: Iterable[str],
    schema_mechanisms: Iterable[str],
    edges_by_type: Dict[str, List[tuple]],
    proto_nodes_by_id: Dict[str, Dict[str, Any]],
    max_prototypes_per_skill: int = 1,
) -> List[SkillEvidence]:
    schema_sig_set = set(schema_signals)
    schema_mech_set = set(schema_mechanisms)
    out: List[SkillEvidence] = []
    for sid in ordered_skill_ids:
        card = skills_by_id.get(sid) or {}
        out.append(hydrate_skill(
            skill_id=sid,
            skill_card=card,
            schema_signals=schema_sig_set,
            schema_mechanisms=schema_mech_set,
            edges_by_type=edges_by_type,
            proto_nodes_by_id=proto_nodes_by_id,
            score=scores.get(sid, 0.0),
            max_prototypes=max_prototypes_per_skill,
        ))
    return out
