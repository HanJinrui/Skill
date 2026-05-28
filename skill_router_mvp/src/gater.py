"""LLM applicability assessment with deterministic single/multi policy enforcement."""
from __future__ import annotations

from .config import Settings
from .prompt_builder import PromptBuilder
from .qwen_client import LanguageModel, generate_contract
from .schemas import CompositionEdge, GateAssessment, GateDecision, ProblemProfile, RetrievalCandidate


class SkillGater:
    def __init__(self, settings: Settings, llm: LanguageModel, prompts: PromptBuilder, edges: list[CompositionEdge]) -> None:
        self.settings = settings
        self.llm = llm
        self.prompts = prompts
        self.edges = edges

    def gate(
        self,
        problem_statement: str,
        profile: ProblemProfile,
        candidates: list[RetrievalCandidate],
    ) -> GateDecision:
        system, user = self.prompts.gate(problem_statement, profile, candidates, self.edges)
        candidate_ids = {candidate.skill_id for candidate in candidates}

        def validate(decision: GateDecision) -> None:
            assessed = {item.skill_id for item in decision.assessments}
            if not assessed or not assessed.issubset(candidate_ids):
                raise ValueError("Gate assessments must refer only to retrieved candidates.")

        model_cfg = self.settings.data["model"]
        route_cfg = self.settings.data["routing"]
        raw = generate_contract(
            self.llm,
            system=system,
            user=user,
            contract=GateDecision,
            temperature=float(model_cfg["route_temperature"]),
            max_new_tokens=int(model_cfg["max_route_tokens"]),
            retries=int(route_cfg["structured_retry_count"]),
            semantic_validator=validate,
        )
        return self._apply_policy(raw, candidates)

    def _apply_policy(self, decision: GateDecision, candidates: list[RetrievalCandidate]) -> GateDecision:
        cfg = self.settings.data["routing"]
        candidate_by_id = {candidate.skill_id: candidate for candidate in candidates}
        assessment_by_id = {assessment.skill_id: assessment for assessment in decision.assessments}
        single: list[GateAssessment] = []
        multi: list[GateAssessment] = []
        for skill_id, assessment in assessment_by_id.items():
            candidate = candidate_by_id.get(skill_id)
            if candidate is None or not assessment.applicable or assessment.complexity_fit == "bad":
                continue
            if candidate.skill_type == "single_algorithm":
                if assessment.confidence >= float(cfg["single_min_confidence"]):
                    single.append(assessment)
                continue
            if assessment.confidence < float(cfg["multi_min_confidence"]):
                continue
            required = candidate.card.composition_signature
            if required and all(
                float(assessment.component_scores.get(component, 0.0)) >= float(cfg["component_min_confidence"])
                for component in required
            ):
                multi.append(assessment)
        single.sort(key=lambda item: item.confidence, reverse=True)
        multi.sort(key=lambda item: item.confidence, reverse=True)
        best_single = single[0] if single else None
        best_multi = multi[0] if multi else None
        selected: GateAssessment | None = None
        selection_type = "fallback"
        if best_multi and (
            best_single is None
            or best_multi.confidence - best_single.confidence >= float(cfg["multi_over_single_margin"])
        ):
            selected, selection_type = best_multi, "multi"
        elif best_single:
            selected, selection_type = best_single, "single"
        all_eligible = sorted(single + multi, key=lambda item: item.confidence, reverse=True)
        if selected is None:
            return decision.model_copy(
                update={
                    "selected_skill_ids": [],
                    "selected_confidence": 0.0,
                    "selection_type": "fallback",
                    "fallback_reason": "no_candidate_satisfied_gate_policy",
                }
            )
        runners = [item for item in all_eligible if item.skill_id != selected.skill_id]
        runner = runners[0] if runners else None
        margin = selected.confidence - runner.confidence if runner else selected.confidence
        return decision.model_copy(
            update={
                "selected_skill_ids": [selected.skill_id],
                "selected_confidence": selected.confidence,
                "selection_type": selection_type,
                "runner_up_skill_id": runner.skill_id if runner else None,
                "runner_up_reason": runner.reason if runner else "",
                "margin": margin,
                "ambiguous": margin < float(cfg["ambiguous_margin"]),
                "fallback_reason": "",
            }
        )
