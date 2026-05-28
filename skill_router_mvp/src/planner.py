"""Algorithm-plan generation constrained to the routed skill."""
from __future__ import annotations

from .config import Settings
from .prompt_builder import PromptBuilder
from .qwen_client import LanguageModel, generate_contract
from .schemas import AlgorithmPlan, GateDecision, UnifiedSkillCard


class AlgorithmPlanner:
    def __init__(self, settings: Settings, llm: LanguageModel, prompts: PromptBuilder) -> None:
        self.settings = settings
        self.llm = llm
        self.prompts = prompts

    def plan(
        self,
        problem_id: str,
        problem_statement: str,
        selected_cards: list[UnifiedSkillCard],
        gate: GateDecision,
    ) -> AlgorithmPlan:
        allowed_ids = {card.skill_id for card in selected_cards}
        system, user = self.prompts.planner(problem_id, problem_statement, selected_cards, gate)

        def validate(plan: AlgorithmPlan) -> None:
            plan_ids = {skill.skill_id for skill in plan.selected_skills}
            if not plan_ids or not plan_ids.issubset(allowed_ids):
                raise ValueError("Plan selected_skills must contain only the routed skill.")
            if not plan.problem_decomposition:
                raise ValueError("Plan must include implementation steps.")

        cfg = self.settings.data["model"]
        routing = self.settings.data["routing"]
        return generate_contract(
            self.llm,
            system=system,
            user=user,
            contract=AlgorithmPlan,
            temperature=float(cfg["plan_temperature"]),
            max_new_tokens=int(cfg["max_plan_tokens"]),
            retries=int(routing["structured_retry_count"]),
            semantic_validator=validate,
        )
