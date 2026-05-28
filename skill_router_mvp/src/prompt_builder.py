"""Central prompt assembly; code prompts contain selected cards only."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from .config import Settings
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
        relevant_ids = {candidate.skill_id for candidate in candidates}
        relevant_edges = [edge.model_dump(mode="json") for edge in edges if edge.multi_skill_id in relevant_ids]
        cards = [
            {
                **_compact_card(candidate.card),
                "router_score": candidate.router_score,
                "rerank_score": candidate.rerank_score,
                "matched_signals": candidate.matched_signals,
                "blockers": candidate.blockers,
            }
            for candidate in candidates
        ]
        return str(prompt["system"]), self._render(
            str(prompt["user_template"]),
            {
                "problem_statement": problem_statement,
                "profile_json": _json(profile),
                "candidate_cards_json": _json(cards),
                "composition_edges_json": _json(relevant_edges),
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
