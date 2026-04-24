"""Glue between RAG pipeline and the Qwen code LLM.

Given a problem + `RAGContext`, returns `n` raw code samples along with the
retrieval trace (for later evaluation).
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from ..llm.base import CodeLLM
from ..logging_utils import get_logger
from ..rag.pipeline import RAGContext, build_generation_prompt

LOG = get_logger(__name__)

_CODE_FENCE_RE = re.compile(r"```(?:python|py)?\s*\n(.*?)```", re.DOTALL | re.IGNORECASE)


def extract_python_code(text: str) -> str:
    """Return the code inside the first ```python``` fence; fallback to trimmed text."""
    if not text:
        return ""
    m = _CODE_FENCE_RE.search(text)
    if m:
        return m.group(1).strip()
    # tolerate models that forget the fence
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = stripped.strip("`").strip()
        if stripped.lower().startswith("python"):
            stripped = stripped[6:].lstrip()
    return stripped


@dataclass
class GenerationTrace:
    retrieved_skill_ids: list[str]
    retrieved_skills: list[dict[str, Any]]
    retrieval_scores: list[float]
    retrieval_method: str
    dense_ids: list[str]
    bm25_ids: list[str]
    raw_completions: list[str]
    extracted_codes: list[str]
    # Graph-specific trace fields (empty in flat mode).
    bundle_type: str = ""
    graph_evidence: list[dict[str, Any]] | None = None
    seed_ids: dict[str, list[str]] | None = None
    supporting_prototypes: list[str] | None = None
    matched_signals: list[str] | None = None
    matched_mechanisms: list[str] | None = None
    query_schema: dict[str, Any] | None = None


def generate_with_rag(
    *,
    code_llm: CodeLLM,
    rag_ctx: RAGContext,
    problem_statement: str,
    n_samples: int,
    seed_base: int = 0,
) -> GenerationTrace:
    retrieved = rag_ctx.retrieve(problem_statement)
    system, user = build_generation_prompt(
        problem_statement=problem_statement,
        retrieved=retrieved,
        max_skill_chars=rag_ctx.max_skill_chars,
    )
    # Per-sample seeding so each of the n generations explores a different mode.
    completions: list[str] = []
    for i in range(n_samples):
        outputs = code_llm.generate(
            system=system,
            user=user,
            temperature=None,
            top_p=None,
            max_new_tokens=None,
            n=1,
            stop=None,
            seed=seed_base + i,
        )
        completions.append(outputs[0] if outputs else "")
    extracted = [extract_python_code(c) for c in completions]
    return GenerationTrace(
        retrieved_skill_ids=list(retrieved.skill_ids) if retrieved else [],
        retrieved_skills=list(retrieved.skills) if retrieved else [],
        retrieval_scores=list(retrieved.scores) if retrieved else [],
        retrieval_method=(retrieved.method if retrieved else "disabled"),
        dense_ids=list(retrieved.dense_ids) if retrieved else [],
        bm25_ids=list(retrieved.bm25_ids) if retrieved else [],
        raw_completions=completions,
        extracted_codes=extracted,
        bundle_type=getattr(retrieved, "bundle_type", "") if retrieved else "",
        graph_evidence=list(getattr(retrieved, "graph_evidence", []) or []) if retrieved else [],
        seed_ids=dict(getattr(retrieved, "seed_ids", {}) or {}) if retrieved else {},
        supporting_prototypes=list(getattr(retrieved, "supporting_prototypes", []) or []) if retrieved else [],
        matched_signals=list(getattr(retrieved, "matched_signals", []) or []) if retrieved else [],
        matched_mechanisms=list(getattr(retrieved, "matched_mechanisms", []) or []) if retrieved else [],
        query_schema=dict(getattr(retrieved, "query_schema", {}) or {}) if retrieved else {},
    )
