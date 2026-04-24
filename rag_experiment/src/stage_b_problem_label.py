"""Stage B — rule+LLM hybrid problem labeling.

Pipeline per problem:
  1. Rule layer narrows candidate families to ≤3 (taxonomy + regex signals).
  2. GLM (ChatLLM) emits structured JSON obeying `prompts/problem_labeling.yaml`.
  3. We fuse: LLM's `normalized_single_skill` must be in rule candidates OR
     explicit confidence ≥ 0.75 to override; otherwise we fall back to the
     top rule candidate and mark `fusion_action = "rule_override"`.
  4. Results are streamed to JSONL; the on-disk cache keys by
     (prompt_version, problem_id, rule_candidates) so re-running is free.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .cache import DiskCache
from .io_utils import append_jsonl, load_jsonl, write_jsonl
from .llm.base import ChatLLM, LLMError
from .logging_utils import get_logger
from .rules import problem_candidate_families
from .settings import Settings
from .stage_a_filter import load_selected
from .taxonomy import CORE_FAMILIES, CORE_FAMILY_SET

LOG = get_logger(__name__)


def _load_prompt(settings: Settings) -> dict[str, Any]:
    with open(settings.prompts_dir / "problem_labeling.yaml", "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _render_user(template: str, **kwargs: Any) -> str:
    return template.format(**{k: _fmt(v) for k, v in kwargs.items()})


def _fmt(value: Any) -> str:
    if isinstance(value, str):
        return value
    import json as _json
    return _json.dumps(value, ensure_ascii=False)


def _fuse(llm_payload: dict[str, Any], rule_candidates: list[str]) -> dict[str, Any]:
    """Fuse LLM output with rule candidates. Returns adjusted fields + action log."""
    single = llm_payload.get("normalized_single_skill", "")
    multi = llm_payload.get("normalized_multi_skills") or []
    confidence = float(llm_payload.get("confidence") or 0.0)
    multi_clean = [m for m in multi if m in CORE_FAMILY_SET]
    if not multi_clean and single in CORE_FAMILY_SET:
        multi_clean = [single]

    action = "llm_accepted"
    if single not in CORE_FAMILY_SET:
        single = rule_candidates[0] if rule_candidates else "complete_search"
        action = "rule_override_invalid_single"
    elif single not in rule_candidates and confidence < 0.75:
        single = rule_candidates[0]
        action = "rule_override_low_confidence"
        if single not in multi_clean:
            multi_clean = [single] + multi_clean
    is_multi = bool(llm_payload.get("is_multi_skill")) or len(multi_clean) >= 2
    return {
        "normalized_single_skill": single,
        "normalized_multi_skills": multi_clean or [single],
        "is_multi_skill": is_multi,
        "fused_confidence": max(confidence, 0.5 if action.startswith("rule_override") else confidence),
        "fusion_action": action,
    }


def run_stage_b(settings: Settings, glm: ChatLLM, *, scope: str = "multi") -> Path:
    prompt_cfg = _load_prompt(settings)
    prompt_version = prompt_cfg["version"]
    out_dir = settings.stage_dir("stage_b")
    out_path = out_dir / "problem_labels.jsonl"
    cache = DiskCache(settings.cache_dir / "glm" / "problem_labeling")

    already_labeled: set[str] = set()
    if out_path.exists():
        for row in load_jsonl(out_path):
            already_labeled.add(row["problem_id"])

    problems = load_selected(settings, scope=scope)
    LOG.info("Stage B: %d problems (already labeled: %d)", len(problems), len(already_labeled))

    recommended = prompt_cfg.get("recommended_params", {}) or {}
    temperature = float(recommended.get("temperature", settings.glm.temperature))
    max_tokens = int(recommended.get("max_tokens", settings.glm.max_tokens))

    for i, row in enumerate(problems, start=1):
        pid = row["problem_id"]
        if pid in already_labeled:
            continue

        rule = problem_candidate_families(
            problem_text=row.get("problem_statement", ""),
            original_tags=row.get("original_tags") or [],
            skill_types=row.get("original_skill_types") or [],
        )
        cache_parts = {
            "v": prompt_version,
            "pid": pid,
            "rules": rule.families,
        }
        cache_key = DiskCache.make_key(cache_parts)
        cached = cache.get("problem_labeling", cache_key)
        if cached is not None:
            llm_payload = cached.get("payload") or {}
        else:
            user = _render_user(
                prompt_cfg["user_template"],
                problem_statement=row["problem_statement"],
                original_tags=row.get("original_tags") or [],
                rule_candidates=rule.families,
            )
            try:
                llm_payload = glm.chat_json(
                    system=prompt_cfg["system"],
                    user=user,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
            except LLMError as exc:
                LOG.error("GLM failed for %s: %s — fallback to rule only", pid, exc)
                llm_payload = {
                    "problem_summary": "",
                    "signals": [],
                    "normalized_single_skill": rule.families[0] if rule.families else "complete_search",
                    "normalized_multi_skills": rule.families[:1] or ["complete_search"],
                    "is_multi_skill": False,
                    "reasoning": f"LLM failure fallback: {exc}",
                    "confidence": 0.4,
                }
            cache.set("problem_labeling", cache_key, {"payload": llm_payload})

        fused = _fuse(llm_payload, rule.families)
        out_row = {
            "problem_id": pid,
            "prompt_version": prompt_version,
            "model": glm.model,
            "original_tags": row.get("original_tags") or [],
            "original_skill_types": row.get("original_skill_types") or [],
            "rule_candidates": rule.families,
            "rule_scores": rule.scores,
            "problem_summary": llm_payload.get("problem_summary", ""),
            "signals": llm_payload.get("signals") or [],
            "reasoning": llm_payload.get("reasoning", ""),
            "raw_llm_single": llm_payload.get("normalized_single_skill"),
            "raw_llm_multi": llm_payload.get("normalized_multi_skills") or [],
            "llm_confidence": float(llm_payload.get("confidence") or 0.0),
            **fused,
        }
        append_jsonl(out_path, out_row)
        if i % 20 == 0:
            LOG.info("Stage B progress %d/%d", i, len(problems))

    LOG.info("Stage B written to %s", out_path)
    return out_path


def load_problem_labels(settings: Settings) -> dict[str, dict[str, Any]]:
    path = settings.stage_dir("stage_b") / "problem_labels.jsonl"
    if not path.exists():
        return {}
    return {r["problem_id"]: r for r in load_jsonl(path)}
