"""Resolve multi-skill components to published single-skill cards."""
from __future__ import annotations

from .schemas import CompositionEdge, UnifiedSkillCard


EXPLICIT_COMPONENT_ALIASES = {
    "sorting_binary_search_answer": "binary_search_on_answer",
}


def build_composition_edges(cards: list[UnifiedSkillCard]) -> list[CompositionEdge]:
    singles = {
        card.primary_subtype: card.skill_id
        for card in cards
        if card.skill_type == "single_algorithm" and card.primary_subtype
    }
    edges: list[CompositionEdge] = []
    for card in cards:
        if card.skill_type != "multi_algorithm":
            continue
        for component in card.composition_signature:
            if component in singles:
                edges.append(
                    CompositionEdge(
                        multi_skill_id=card.skill_id,
                        component_subtype=component,
                        single_skill_id=singles[component],
                        resolution="exact",
                    )
                )
                continue
            alias = EXPLICIT_COMPONENT_ALIASES.get(component)
            if alias and alias in singles:
                edges.append(
                    CompositionEdge(
                        multi_skill_id=card.skill_id,
                        component_subtype=component,
                        single_skill_id=singles[alias],
                        resolution="alias",
                    )
                )
            else:
                edges.append(
                    CompositionEdge(
                        multi_skill_id=card.skill_id,
                        component_subtype=component,
                        single_skill_id=None,
                        resolution="unresolved_component",
                    )
                )
    return edges
