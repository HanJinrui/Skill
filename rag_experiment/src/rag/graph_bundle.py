"""Bundle assembly: turn propagated skill scores into a small, sensible
set of skills to show the generator.

We always return:

* 1 primary skill,
* 0..max_aux auxiliary skills,
* optionally 1 bundle skill if the primary's family set is contained in
  an existing multi-skill card and the schema suggests multi-skill.

Constraints:

* Auxiliary skills must not strongly conflict with the primary.
* Auxiliary skills must not be exact duplicates (same family set) of the
  primary unless they are bundle cards.
* Bundle size is capped by `max_bundle_size`.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Sequence, Set, Tuple

from .graph_schema import (
    EDGE_BUNDLE_CONTAINS_SKILL,
    EDGE_SKILL_CONFLICTS_SKILL,
    parse_node_id,
    skill_node_id,
)


@dataclass
class Bundle:
    primary_skill_id: str
    auxiliary_skill_ids: List[str] = field(default_factory=list)
    bundle_skill_id: str | None = None
    scores: Dict[str, float] = field(default_factory=dict)
    ordered_skill_ids: List[str] = field(default_factory=list)
    bundle_type: str = "primary_only"


def _score_for_skill(scores: Dict[str, float], skill_id: str) -> float:
    return scores.get(skill_node_id(skill_id), 0.0)


def _find_bundle_candidates(
    skills_by_id: Dict[str, Dict[str, Any]],
    member_families: Set[str],
) -> List[str]:
    """Return existing multi-skill cards whose family set matches or is a
    superset of `member_families`."""
    out: List[str] = []
    for sid, s in skills_by_id.items():
        if s.get("scope") == "multi" or s.get("skill_level") == "bundle":
            fams = set(s.get("family_set") or s.get("families") or [])
        else:
            continue
        if fams and member_families.issubset(fams):
            out.append(sid)
    return out


def _conflict_map(edges_by_type: Dict[str, List[Tuple[str, str, float]]]) -> Dict[str, Dict[str, float]]:
    """Return skill_id -> {other_skill_id: weight}."""
    out: Dict[str, Dict[str, float]] = {}
    for src, dst, w in edges_by_type.get(EDGE_SKILL_CONFLICTS_SKILL, ()):
        _, sa = parse_node_id(src)
        _, sb = parse_node_id(dst)
        if not sa or not sb:
            continue
        out.setdefault(sa, {})[sb] = max(out.get(sa, {}).get(sb, 0.0), w)
    return out


def assemble_bundle(
    *,
    scores: Dict[str, float],
    skills_by_id: Dict[str, Dict[str, Any]],
    edges_by_type: Dict[str, List[Tuple[str, str, float]]],
    is_multi_skill_likely: bool,
    max_bundle_size: int = 3,
    max_aux: int = 2,
    conflict_threshold: float = 0.1,
) -> Bundle:
    """Pick a small, consistent skill set.

    Selection strategy:

    1. Split candidate skills into singles vs bundles. For the primary
       we prefer the highest-scoring *single* (most stable interpretation
       on small data); bundles can only become primary if they beat any
       single by a large margin.
    2. Greedy-add auxiliaries that are: (a) non-redundant, (b) not
       strongly conflicting with the primary, (c) family-disjoint from
       the primary (or at least partly so).
    3. If multi-skill is plausible and a bundle card exists whose family
       set covers primary + auxiliaries, attach it.
    """
    ranked: List[Tuple[str, float, Dict[str, Any]]] = []
    for sid, skill in skills_by_id.items():
        sc = _score_for_skill(scores, sid)
        if sc <= 0:
            continue
        ranked.append((sid, sc, skill))
    ranked.sort(key=lambda x: x[1], reverse=True)

    if not ranked:
        return Bundle(primary_skill_id="", ordered_skill_ids=[])

    # Pick the primary (prefer highest-scoring single).
    primary_sid = None
    primary_score = 0.0
    best_single = next(
        ((sid, sc, s) for sid, sc, s in ranked if s.get("skill_level") == "subtype"),
        None,
    )
    if best_single is None:
        best_single = next(
            ((sid, sc, s) for sid, sc, s in ranked if s.get("scope") != "multi" and s.get("skill_level") != "bundle"),
            None,
        )
    best_any = ranked[0]
    if best_single is None:
        primary_sid, primary_score, _ = best_any
    else:
        single_sid, single_sc, _ = best_single
        any_sid, any_sc, any_skill = best_any
        # Only let a bundle take primary if it's much better than the top single.
        if (any_skill.get("scope") == "multi" or any_skill.get("skill_level") == "bundle") and any_sc >= single_sc * 1.4:
            primary_sid, primary_score = any_sid, any_sc
        else:
            primary_sid, primary_score = single_sid, single_sc

    primary_skill = skills_by_id.get(primary_sid, {})
    primary_families = set(primary_skill.get("families") or [])

    conflicts = _conflict_map(edges_by_type)
    conflicting_with_primary = conflicts.get(primary_sid, {})

    # Pick auxiliaries.
    aux_sids: List[str] = []
    aux_family_union: Set[str] = set(primary_families)
    for sid, sc, skill in ranked:
        if sid == primary_sid:
            continue
        if skill.get("scope") == "multi" or skill.get("skill_level") == "bundle":
            continue  # bundles come in later
        if conflicting_with_primary.get(sid, 0.0) >= conflict_threshold:
            continue
        fams = set(skill.get("families") or [])
        # Strong redundancy: exact same family set → skip.
        if fams and fams == primary_families:
            continue
        # Prefer aux whose families extend the coverage.
        if fams and fams.issubset(aux_family_union) and aux_family_union:
            # Already covered — still allow but with lower priority: skip this
            # one in the greedy phase.
            continue
        aux_sids.append(sid)
        aux_family_union |= fams
        if len(aux_sids) >= max_aux:
            break

    ordered: List[str] = [primary_sid] + aux_sids

    # Bundle attachment.
    bundle_sid: str | None = None
    bundle_type = "primary_only"
    if is_multi_skill_likely:
        # Does any bundle's family set cover the union of primary + aux families?
        member_families = set(primary_families) | aux_family_union
        candidates = _find_bundle_candidates(skills_by_id, member_families)
        # Rank candidates by score.
        candidates.sort(key=lambda sid: _score_for_skill(scores, sid), reverse=True)
        if candidates:
            cand_sid = candidates[0]
            if cand_sid != primary_sid and cand_sid not in aux_sids:
                bundle_sid = cand_sid
                bundle_type = "primary_plus_aux_plus_bundle"

    if bundle_sid is not None and len(ordered) < max_bundle_size:
        ordered.append(bundle_sid)
    # Cap by max_bundle_size.
    ordered = ordered[:max_bundle_size]

    if len(ordered) == 1:
        bundle_type = "primary_only"
    elif bundle_sid is None:
        bundle_type = "primary_plus_aux"

    return Bundle(
        primary_skill_id=primary_sid,
        auxiliary_skill_ids=aux_sids,
        bundle_skill_id=bundle_sid,
        scores={sid: _score_for_skill(scores, sid) for sid in ordered},
        ordered_skill_ids=ordered,
        bundle_type=bundle_type,
    )
