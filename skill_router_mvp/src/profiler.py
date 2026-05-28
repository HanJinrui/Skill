"""Structured problem profiling with one schema-repair attempt."""
from __future__ import annotations

from .config import Settings
from .prompt_builder import PromptBuilder
from .qwen_client import LanguageModel, generate_contract
from .schemas import ProblemProfile


class ProblemProfiler:
    def __init__(self, settings: Settings, llm: LanguageModel, prompts: PromptBuilder) -> None:
        self.settings = settings
        self.llm = llm
        self.prompts = prompts

    def profile(self, problem_id: str, problem_statement: str) -> ProblemProfile:
        system, user = self.prompts.profiler(problem_id, problem_statement)
        cfg = self.settings.data["model"]
        routing = self.settings.data["routing"]
        profile = generate_contract(
            self.llm,
            system=system,
            user=user,
            contract=ProblemProfile,
            temperature=float(cfg["profile_temperature"]),
            max_new_tokens=int(cfg["max_profile_tokens"]),
            retries=int(routing["structured_retry_count"]),
        )
        if not profile.problem_id:
            profile.problem_id = problem_id
        return profile
