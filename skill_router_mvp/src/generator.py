"""Code generation and repair calls after routing and planning."""
from __future__ import annotations

import re

from .config import Settings
from .prompt_builder import PromptBuilder
from .qwen_client import LanguageModel
from .schemas import AlgorithmPlan, ExecutionReport, GateDecision, UnifiedSkillCard


CODE_RE = re.compile(r"```(?:python|py)?\s*\n?(.*?)```", re.DOTALL | re.IGNORECASE)


def extract_python_code(text: str) -> str:
    match = CODE_RE.search(text or "")
    return match.group(1).strip() if match else (text or "").strip()


class CodeGenerator:
    def __init__(self, settings: Settings, llm: LanguageModel, prompts: PromptBuilder) -> None:
        self.settings = settings
        self.llm = llm
        self.prompts = prompts

    def _generate(self, system: str, user: str, *, sample_index: int, seed: int | None = None) -> str:
        cfg = self.settings.data["model"]
        first = sample_index == 0
        text = self.llm.generate(
            system,
            user,
            temperature=float(cfg["code_first_temperature"] if first else cfg["code_later_temperature"]),
            top_p=float(cfg["code_first_top_p"] if first else cfg["code_later_top_p"]),
            max_new_tokens=int(cfg["max_code_tokens"]),
            seed=seed,
        )
        return extract_python_code(text)

    def direct(self, problem_statement: str, *, sample_index: int, seed: int | None = None) -> str:
        return self._generate(*self.prompts.code_direct(problem_statement), sample_index=sample_index, seed=seed)

    def legacy(self, problem_statement: str, card: UnifiedSkillCard, *, sample_index: int, seed: int | None = None) -> str:
        return self._generate(*self.prompts.code_legacy(problem_statement, card), sample_index=sample_index, seed=seed)

    def planned(
        self,
        problem_statement: str,
        cards: list[UnifiedSkillCard],
        gate: GateDecision,
        plan: AlgorithmPlan,
        *,
        sample_index: int,
        seed: int | None = None,
    ) -> str:
        return self._generate(
            *self.prompts.code_planned(problem_statement, cards, gate, plan),
            sample_index=sample_index,
            seed=seed,
        )

    def repair(self, problem_statement: str, code: str, plan: AlgorithmPlan, execution: ExecutionReport, *, seed: int | None = None) -> str:
        cfg = self.settings.data["model"]
        text = self.llm.generate(
            *self.prompts.repair(problem_statement, code, plan, execution),
            temperature=0.1,
            top_p=0.9,
            max_new_tokens=int(cfg["max_code_tokens"]),
            seed=seed,
        )
        return extract_python_code(text)
