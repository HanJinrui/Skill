"""Central prompt assembly; code prompts contain selected cards only."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from .config import Settings
from .retrieval_text import build_gate_card
from .schemas import AlgorithmPlan, CompositionEdge, GateDecision, ProblemProfile, RetrievalCandidate, UnifiedSkillCard


def _json(value: Any) -> str:
    if hasattr(value, "model_dump"):
        value = value.model_dump(mode="json")
    return json.dumps(value, ensure_ascii=False, indent=2)


def _compact_card(card: UnifiedSkillCard) -> dict[str, Any]:
    out: dict[str, Any] = {
        "skill_id": card.skill_id,
        "skill_type": card.skill_type,
        "status": card.status,
        "trigger_signals": card.trigger_signals[:5],
        "applicability_conditions": card.applicability_conditions[:5],
        "non_applicability_conditions": card.non_applicability_conditions[:4],
        "complexity_pattern": card.complexity_pattern,
        "implementation_notes": card.implementation_notes[:5],
        "common_pitfalls": card.common_pitfalls[:4],
    }
    if card.skill_type == "single_algorithm":
        out.update({"primary_subtype": card.primary_subtype, "core_mechanism": card.core_mechanism})
    else:
        out.update(
            {
                "composition_signature": card.composition_signature,
                "algorithm_flow": card.algorithm_flow,
                "composition_invariants": card.composition_invariants,
                "core_composition_mechanism": card.core_composition_mechanism,
            }
        )
    return out


class PromptBuilder:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.prompts_dir = settings.package_root / "prompts"
        self._cache: dict[str, dict[str, Any]] = {}

    def _prompt(self, name: str) -> dict[str, Any]:
        if name not in self._cache:
            path = self.prompts_dir / f"{name}.yaml"
            with path.open("r", encoding="utf-8") as fh:
                self._cache[name] = yaml.safe_load(fh)
        return self._cache[name]

    @staticmethod
    def _render(template: str, values: dict[str, str]) -> str:
        rendered = template
        for key, value in values.items():
            rendered = rendered.replace("{{" + key + "}}", value)
        return rendered

    def profiler(self, problem_id: str, problem_statement: str) -> tuple[str, str]:
        prompt = self._prompt("profiler")
        return str(prompt["system"]), self._render(
            str(prompt["user_template"]),
            {"problem_id": problem_id, "problem_statement": problem_statement},
        )

    def gate(
        self,
        problem_statement: str,
        profile: ProblemProfile,
        candidates: list[RetrievalCandidate],
        edges: list[CompositionEdge],
    ) -> tuple[str, str]:
        prompt = self._prompt("gate")

        # Compact profile signals — a few keywords instead of the full profile JSON.
        signals = list(profile.algorithm_signals[:5]) if profile else []
        prohibited = list(profile.prohibited_operations[:3]) if profile else []
        profile_signals = "Signals: " + ", ".join(signals) if signals else "Signals: (none detected)"
        if prohibited:
            profile_signals += "  |  Prohibited: " + ", ".join(prohibited)

        # Each candidate rendered as a short text block (~60-80 tokens).
        candidate_cards_text = "\n\n".join(
            build_gate_card(candidate.card.model_dump(mode="json"), rank=i)
            for i, candidate in enumerate(candidates)
        )

        # Composition edges block — only emitted when multi-skill candidates exist.
        multi_ids = {c.skill_id for c in candidates if c.skill_type == "multi_algorithm"}
        relevant_edges = [e for e in edges if e.multi_skill_id in multi_ids]
        if relevant_edges:
            edge_lines = "\n".join(
                f"  {e.multi_skill_id}: requires component '{e.component_subtype}'"
                for e in relevant_edges[:10]
            )
            composition_edges_block = f"[Component Requirements for Multi-Skills]\n{edge_lines}\n"
        else:
            composition_edges_block = ""

        return str(prompt["system"]), self._render(
            str(prompt["user_template"]),
            {
                "problem_statement": problem_statement,
                "profile_signals": profile_signals,
                "candidate_cards_text": candidate_cards_text,
                "composition_edges_block": composition_edges_block,
            },
        )

    def planner(
        self,
        problem_id: str,
        problem_statement: str,
        selected_cards: list[UnifiedSkillCard],
        gate: GateDecision,
    ) -> tuple[str, str]:
        prompt = self._prompt("planner")
        rejected = []
        if gate.runner_up_skill_id:
            rejected.append({"skill_id": gate.runner_up_skill_id, "reason": gate.runner_up_reason})
        return str(prompt["system"]), self._render(
            str(prompt["user_template"]),
            {
                "problem_id": problem_id,
                "problem_statement": problem_statement,
                "selected_cards_json": _json([_compact_card(card) for card in selected_cards]),
                "rejected_skills_json": _json(rejected),
            },
        )

    def code_direct(self, problem_statement: str) -> tuple[str, str]:
        prompt = self._prompt("code_generation")
        return str(prompt["system"]), self._render(str(prompt["direct_template"]), {"problem_statement": problem_statement})

    def code_legacy(self, problem_statement: str, selected_card: UnifiedSkillCard) -> tuple[str, str]:
        prompt = self._prompt("code_generation")
        return str(prompt["system"]), self._render(
            str(prompt["legacy_template"]),
            {"problem_statement": problem_statement, "selected_cards_json": _json([_compact_card(selected_card)])},
        )

    def code_planned(
        self,
        problem_statement: str,
        selected_cards: list[UnifiedSkillCard],
        gate: GateDecision,
        plan: AlgorithmPlan,
    ) -> tuple[str, str]:
        prompt = self._prompt("code_generation")
        rejected = []
        if gate.runner_up_skill_id:
            rejected.append({"skill_id": gate.runner_up_skill_id, "reason": gate.runner_up_reason})
        return str(prompt["system"]), self._render(
            str(prompt["planned_template"]),
            {
                "problem_statement": problem_statement,
                "selected_cards_json": _json([_compact_card(card) for card in selected_cards]),
                "rejected_skills_json": _json(rejected),
                "plan_json": _json(plan),
            },
        )

    def repair(self, problem_statement: str, code: str, plan: AlgorithmPlan, execution: Any) -> tuple[str, str]:
        prompt = self._prompt("repair")
        return str(prompt["system"]), self._render(
            str(prompt["user_template"]),
            {
                "problem_statement": problem_statement,
                "code": code,
                "plan_json": _json(plan),
                "execution_json": _json(execution),
            },
        )
