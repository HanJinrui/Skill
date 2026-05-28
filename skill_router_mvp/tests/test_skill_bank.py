from __future__ import annotations

from pathlib import Path

from src.skill_bank import SkillBank


def test_loads_frozen_67_card_bank_and_writes_only_derived_artifacts(settings, tmp_path: Path) -> None:
    bank = SkillBank.from_settings(settings)
    assert len(bank.cards) == 67
    assert bank.metadata["single_count"] == 54
    assert bank.metadata["multi_count"] == 13
    assert all(card.retrieval_text for card in bank.cards)

    out = tmp_path / "frozen"
    bank.write_frozen_artifacts(out)
    assert (out / "unified_skill_cards.jsonl").exists()
    assert (out / "composition_edges.jsonl").exists()


def test_component_alias_is_explicit_and_unknown_components_remain_unresolved(bank) -> None:
    target = [edge for edge in bank.edges if edge.multi_skill_id == "multi.sorting_binary_search_answer__greedy_two_pointers.v1"]
    assert any(edge.component_subtype == "sorting_binary_search_answer" and edge.resolution == "alias" for edge in target)
    dp_edges = [edge for edge in bank.edges if edge.multi_skill_id == "multi.dp_1d_state__amortized_two_pointers.v1"]
    assert any(edge.component_subtype == "amortized_two_pointers" and edge.resolution == "unresolved_component" for edge in dp_edges)
