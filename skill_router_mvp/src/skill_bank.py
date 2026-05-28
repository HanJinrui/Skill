"""Load and freeze the externally produced 54+13 skill bank without modifying it."""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .composition_edges import build_composition_edges
from .config import Settings
from .io_utils import load_jsonl, sha256_file, write_json, write_jsonl
from .retrieval_text import build_retrieval_text
from .schemas import CompositionEdge, UnifiedSkillCard


def _normalize(raw: dict[str, Any]) -> UnifiedSkillCard:
    payload = {
        "skill_id": raw["skill_id"],
        "skill_name": raw["skill_name"],
        "skill_type": raw["skill_type"],
        "version": raw.get("version", "v1"),
        "status": raw.get("status", "seed"),
        "trigger_signals": raw.get("trigger_signals") or [],
        "applicability_conditions": raw.get("applicability_conditions") or [],
        "non_applicability_conditions": raw.get("non_applicability_conditions") or [],
        "complexity_pattern": raw.get("complexity_pattern") or {},
        "retrieval_text": build_retrieval_text(raw),
        "implementation_notes": raw.get("implementation_notes") or [],
        "common_pitfalls": raw.get("common_pitfalls") or [],
        "algorithm_family": raw.get("algorithm_family"),
        "primary_subtype": raw.get("primary_subtype"),
        "code_template": raw.get("code_template"),
        "core_mechanism": raw.get("core_mechanism"),
        "composition_signature": raw.get("composition_signature") or [],
        "composition_families": raw.get("composition_families") or [],
        "algorithm_flow": raw.get("algorithm_flow") or [],
        "state_interface": raw.get("state_interface"),
        "composition_invariants": raw.get("composition_invariants") or [],
        "implementation_template": raw.get("implementation_template"),
        "core_composition_mechanism": raw.get("core_composition_mechanism"),
        "raw_card": raw,
    }
    return UnifiedSkillCard.model_validate(payload)


@dataclass(frozen=True)
class SkillBank:
    cards: list[UnifiedSkillCard]
    edges: list[CompositionEdge]
    metadata: dict[str, Any]

    @classmethod
    def from_settings(cls, settings: Settings) -> "SkillBank":
        single_path = settings.path("single_skill_bank")
        multi_path = settings.path("multi_skill_bank")
        single_rows = load_jsonl(single_path)
        multi_rows = load_jsonl(multi_path)
        expected_single = int(settings.data["experiment"]["expected_single_skills"])
        expected_multi = int(settings.data["experiment"]["expected_multi_skills"])
        if len(single_rows) != expected_single or len(multi_rows) != expected_multi:
            raise ValueError(
                f"Frozen bank count mismatch: single={len(single_rows)}/{expected_single}, "
                f"multi={len(multi_rows)}/{expected_multi}"
            )
        cards = [_normalize(row) for row in single_rows + multi_rows]
        ids = [card.skill_id for card in cards]
        if len(ids) != len(set(ids)):
            raise ValueError("Frozen skill bank contains duplicated skill_id values.")
        metadata = {
            "bank_version": settings.bank_version,
            "single_source": str(single_path),
            "multi_source": str(multi_path),
            "single_sha256": sha256_file(single_path),
            "multi_sha256": sha256_file(multi_path),
            "single_count": len(single_rows),
            "multi_count": len(multi_rows),
            "total_count": len(cards),
            "status_counts": dict(Counter(card.status for card in cards)),
        }
        return cls(cards=cards, edges=build_composition_edges(cards), metadata=metadata)

    @property
    def by_id(self) -> dict[str, UnifiedSkillCard]:
        return {card.skill_id: card for card in self.cards}

    def write_frozen_artifacts(self, output_dir: Path) -> None:
        write_json(output_dir / "bank_metadata.json", self.metadata)
        write_jsonl(output_dir / "unified_skill_cards.jsonl", (card.model_dump(mode="json") for card in self.cards))
        write_jsonl(output_dir / "composition_edges.jsonl", (edge.model_dump(mode="json") for edge in self.edges))
