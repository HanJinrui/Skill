"""End-to-end independent router, planner, generator and execution pipeline."""
from __future__ import annotations

import time
from typing import Any

from .config import Settings
from .executor import PythonExecutor
from .feedback import FeedbackController, better_report
from .gater import SkillGater
from .generator import CodeGenerator
from .planner import AlgorithmPlanner
from .profiler import ProblemProfiler
from .prompt_builder import PromptBuilder
from .qwen_client import LanguageModel
from .reranker import SkillReranker
from .retriever import HybridRetriever
from .schemas import (
    AlgorithmPlan,
    AttemptTrace,
    GateAssessment,
    GateDecision,
    GenerationSample,
    RunTrace,
    StructuredOutputError,
    UnifiedSkillCard,
)
from .skill_bank import SkillBank


MODES = {"direct_qwen", "legacy_hint", "routed_plan", "routed_plan_closed_loop"}


class SkillRouterPipeline:
    def __init__(
        self,
        settings: Settings,
        llm: LanguageModel,
        bank: SkillBank,
        retriever: HybridRetriever,
        reranker: SkillReranker,
    ) -> None:
        self.settings = settings
        self.llm = llm
        self.bank = bank
        self.retriever = retriever
        self.reranker = reranker
        self.prompts = PromptBuilder(settings)
        self.profiler = ProblemProfiler(settings, llm, self.prompts)
        self.gater = SkillGater(settings, llm, self.prompts, bank.edges)
        self.planner = AlgorithmPlanner(settings, llm, self.prompts)
        self.generator = CodeGenerator(settings, llm, self.prompts)
        self.executor = PythonExecutor(settings)
        self.feedback = FeedbackController(settings)

    @classmethod
    def from_settings(
        cls,
        settings: Settings,
        llm: LanguageModel,
        *,
        encoder: Any | None = None,
        rerank_score_fn: Any | None = None,
    ) -> "SkillRouterPipeline":
        bank = SkillBank.from_settings(settings)
        retriever = HybridRetriever.from_index(settings, encoder=encoder)
        reranker = SkillReranker(settings, score_fn=rerank_score_fn)
        return cls(settings, llm, bank, retriever, reranker)

    @staticmethod
    def _elapsed(started: float) -> int:
        return int((time.perf_counter() - started) * 1000)

    def _execute(self, code: str, problem: dict[str, Any]):
        io = dict(problem.get("input_output") or {})
        fn_name = problem.get("fn_name") or io.get("fn_name")
        return self.executor.execute(code, io, fn_name=str(fn_name) if fn_name else None)

    def run_problem(self, problem: dict[str, Any], *, mode: str, n_samples: int | None = None) -> RunTrace:
        if mode not in MODES:
            raise ValueError(f"Unknown evaluation mode: {mode}")
        problem_id = str(problem.get("problem_id") or "")
        statement = str(problem.get("problem_statement") or problem.get("question") or "")
        samples_count = int(n_samples or self.settings.data["evaluation"]["samples_per_problem"])
        latency: dict[str, int] = {}
        profile = None
        candidates = []
        gate: GateDecision | None = None
        plan: AlgorithmPlan | None = None
        selected_cards: list[UnifiedSkillCard] = []
        fallback_reason = ""
        effective_mode = mode

        if mode != "direct_qwen":
            try:
                if mode.startswith("routed_plan"):
                    started = time.perf_counter()
                    profile = self.profiler.profile(problem_id, statement)
                    latency["profile"] = self._elapsed(started)
                started = time.perf_counter()
                candidates = self.retriever.retrieve(statement, profile=profile)
                candidates = self.reranker.rerank(statement, candidates)
                latency["retrieve_rerank"] = self._elapsed(started)
                if mode == "legacy_hint":
                    selected_cards = [candidates[0].card] if candidates else []
                    if not selected_cards:
                        fallback_reason = "no_retrieved_skill"
                        effective_mode = "direct_qwen"
                else:
                    started = time.perf_counter()
                    assert profile is not None
                    gate = self.gater.gate(statement, profile, candidates)
                    latency["gate"] = self._elapsed(started)
                    if not gate.selected_skill_ids:
                        fallback_reason = gate.fallback_reason or "gate_selected_no_skill"
                        effective_mode = "direct_qwen"
                    else:
                        selected_cards = [self.bank.by_id[sid] for sid in gate.selected_skill_ids]
                        started = time.perf_counter()
                        plan = self.planner.plan(problem_id, statement, selected_cards, gate)
                        latency["plan"] = self._elapsed(started)
            except StructuredOutputError as exc:
                fallback_reason = str(exc)
                effective_mode = "direct_qwen"

        generated: list[GenerationSample] = []
        generation_started = time.perf_counter()
        for index in range(samples_count):
            seed = self.settings.seed + index
            if effective_mode == "direct_qwen":
                code = self.generator.direct(statement, sample_index=index, seed=seed)
            elif effective_mode == "legacy_hint":
                code = self.generator.legacy(statement, selected_cards[0], sample_index=index, seed=seed)
            else:
                assert gate is not None and plan is not None
                code = self.generator.planned(statement, selected_cards, gate, plan, sample_index=index, seed=seed)
            execution = self._execute(code, problem)
            attempts = [AttemptTrace(attempt=0, action="generate", code=code, execution=execution, plan=plan)]
            final_attempt = 0
            if mode == "routed_plan_closed_loop" and effective_mode == mode and gate and plan and not execution.all_passed:
                decision = self.feedback.decide(execution, gate, attempts=1)
                improved_code: str | None = None
                alternative_plan = plan
                if decision.action == "repair":
                    improved_code = self.generator.repair(statement, code, plan, execution, seed=seed + 1000)
                elif decision.action == "reroute" and gate.runner_up_skill_id:
                    runner_card = self.bank.by_id.get(gate.runner_up_skill_id)
                    runner_assessment = next(
                        (item for item in gate.assessments if item.skill_id == gate.runner_up_skill_id),
                        GateAssessment(skill_id=gate.runner_up_skill_id, applicable=True, confidence=0.0),
                    )
                    if runner_card:
                        runner_gate = gate.model_copy(
                            update={
                                "selected_skill_ids": [runner_card.skill_id],
                                "selected_confidence": runner_assessment.confidence,
                                "runner_up_skill_id": gate.selected_skill_ids[0],
                                "runner_up_reason": "Initial route failed execution.",
                            }
                        )
                        try:
                            alternative_plan = self.planner.plan(problem_id, statement, [runner_card], runner_gate)
                            improved_code = self.generator.planned(
                                statement, [runner_card], runner_gate, alternative_plan, sample_index=index, seed=seed + 1000
                            )
                        except StructuredOutputError:
                            improved_code = None
                if improved_code:
                    improved_execution = self._execute(improved_code, problem)
                    attempts.append(
                        AttemptTrace(
                            attempt=1,
                            action=decision.action,
                            code=improved_code,
                            execution=improved_execution,
                            plan=alternative_plan,
                        )
                    )
                    if better_report(improved_execution, execution):
                        final_attempt = 1
            generated.append(GenerationSample(sample_id=f"r{index}", attempts=attempts, final_attempt=final_attempt))
        latency["generate_execute"] = self._elapsed(generation_started)

        return RunTrace(
            problem_id=problem_id,
            scope=str(problem.get("scope") or ""),
            mode=mode,
            bank_version=self.settings.bank_version,
            model_name=self.llm.model_name,
            selected_skill_ids=[card.skill_id for card in selected_cards] if effective_mode != "direct_qwen" else [],
            profile=profile,
            candidates=candidates,
            gate=gate,
            plan=plan,
            samples=generated,
            fallback_reason=fallback_reason,
            latency_ms=latency,
            metadata={"effective_mode": effective_mode, "difficulty_bucket": problem.get("difficulty_bucket", "")},
        )
