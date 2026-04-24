"""End-to-end RAG pipeline: query → retrieve → skill-injected prompt → code.

This module doesn't call the code LLM directly — Stage F drives the LLM and
uses `build_generation_prompt()` to assemble the conditional prompt. We keep
prompt construction in one place so retrieval and generation stay decoupled.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..logging_utils import get_logger
from ..settings import Settings
from .retrieve import RetrievalResult, SkillRetriever

LOG = get_logger(__name__)


def extract_query_from_problem(problem_statement: str, *, max_chars: int = 2500) -> str:
    """The bge encoder handles the problem statement directly; we just truncate.

    We purposefully keep it simple. A query-rewrite step can be plugged in
    later (LLM summarise → then encode), but for a competitive-programming
    benchmark the raw statement already has extremely high signal.
    """
    text = problem_statement or ""
    return text[:max_chars]


def format_skill_card(
    skill: dict[str, Any],
    *,
    max_chars: int,
    evidence: dict[str, Any] | None = None,
) -> str:
    """Render a single skill card. If `evidence` is provided (graph mode),
    graph-level context (matched signals/mechanisms, prototype evidence)
    is appended at the top of the block."""
    lines: list[str] = []
    lines.append(f"### Skill: {skill.get('skill_name')} ({skill.get('skill_id')})")
    if skill.get("families"):
        lines.append(f"- Families: {', '.join(skill['families'])}")
    if evidence:
        if evidence.get("why_selected"):
            lines.append(f"- Why selected: {evidence['why_selected']}")
        if evidence.get("matched_signals"):
            lines.append(f"- Matched signals: {', '.join(evidence['matched_signals'][:6])}")
        if evidence.get("matched_mechanisms"):
            lines.append(f"- Matched mechanisms: {', '.join(evidence['matched_mechanisms'][:6])}")
    if skill.get("applicable_when"):
        lines.append("- Applicable when:")
        for item in skill["applicable_when"][:6]:
            lines.append(f"  * {item}")
    if skill.get("problem_signals"):
        lines.append("- Problem signals to look for:")
        for item in skill["problem_signals"][:8]:
            lines.append(f"  * {item}")
    if skill.get("core_idea"):
        lines.append(f"- Core idea: {skill['core_idea']}")
    if skill.get("template_strategy"):
        lines.append("- Template strategy:")
        for i, step in enumerate(skill["template_strategy"][:8], start=1):
            lines.append(f"  {i}. {step}")
    if skill.get("common_pitfalls"):
        lines.append("- Pitfalls:")
        for item in skill["common_pitfalls"][:5]:
            lines.append(f"  * {item}")
    if skill.get("complexity_pattern"):
        lines.append(f"- Typical complexity: {skill['complexity_pattern']}")
    if evidence and evidence.get("prototype_evidence"):
        lines.append("- Prototype evidence:")
        for pe in evidence["prototype_evidence"][:2]:
            pid = pe.get("problem_id") or pe.get("prototype_id", "")
            summary = (pe.get("core_mechanism_summary")
                       or pe.get("problem_summary")
                       or "")[:240]
            if summary:
                lines.append(f"  * {pid}: {summary}")
            else:
                lines.append(f"  * {pid}")
    text = "\n".join(lines)
    return text[:max_chars]


CODE_SYSTEM = (
    "You are a senior competitive programmer. You output a single self-contained "
    "Python 3 program that reads from standard input, writes to standard output, "
    "and matches the problem's exact I/O format. Do not include explanations. "
    "Return only the code inside one fenced ```python ... ``` block."
)


def build_generation_prompt(
    *,
    problem_statement: str,
    retrieved: RetrievalResult | None,
    max_skill_chars: int,
) -> tuple[str, str]:
    """Return (system, user) prompts for the code LLM."""
    user_parts: list[str] = []
    if retrieved and retrieved.skills:
        user_parts.append("You retrieved the following algorithm-skill cards — use the "
                          "MOST RELEVANT one to shape your solution; ignore the others "
                          "if they don't apply.")
        evidence_by_sid: dict[str, dict[str, Any]] = {}
        for ev in (retrieved.graph_evidence or []):
            sid = ev.get("skill_id")
            if isinstance(sid, str):
                evidence_by_sid[sid] = ev
        for skill in retrieved.skills:
            ev = evidence_by_sid.get(skill.get("skill_id"))
            user_parts.append(format_skill_card(skill, max_chars=max_skill_chars, evidence=ev))
        user_parts.append("")
    user_parts.append("### Problem")
    user_parts.append(problem_statement)
    user_parts.append("")
    user_parts.append(
        "### Task\n"
        "Write a single Python 3 program that reads input from standard input "
        "and writes the required output to standard output. The solution must "
        "handle all provided constraints within reasonable time/memory."
    )
    user_parts.append("Return only the code inside a ```python ... ``` fence.")
    return CODE_SYSTEM, "\n".join(user_parts)


@dataclass
class RAGContext:
    retriever: Any
    top_k: int
    max_skill_chars: int
    enabled: bool
    mode: str = "flat"

    @classmethod
    def from_settings(cls, settings: Settings, *, enabled: bool = True) -> "RAGContext":
        rag_cfg = settings.config["rag"]
        ret_cfg = rag_cfg.get("retrieval", {}) or {}
        mode = str(ret_cfg.get("mode") or "flat").lower()
        top_k = int(ret_cfg.get("final_top_k") or ret_cfg.get("top_k") or 3)
        max_skill_chars = int(rag_cfg["prompt"]["max_skill_tokens"])
        retriever: Any = None
        if enabled:
            if mode == "graph":
                # Lazy import to avoid loading graph-only deps in flat-only runs.
                from .graph_retrieve import GraphRetriever
                retriever = GraphRetriever.from_settings(settings)
                LOG.info("RAGContext: graph retriever initialised (top_k=%d)", top_k)
            else:
                retriever = SkillRetriever.from_settings(settings)
                LOG.info("RAGContext: flat retriever initialised (top_k=%d)", top_k)
        return cls(
            retriever=retriever,
            top_k=top_k,
            max_skill_chars=max_skill_chars,
            enabled=enabled,
            mode=mode if enabled else "disabled",
        )

    def retrieve(self, problem_statement: str) -> RetrievalResult | None:
        if not (self.enabled and self.retriever):
            return None
        query = extract_query_from_problem(problem_statement)
        return self.retriever.retrieve(query, top_k=self.top_k)
