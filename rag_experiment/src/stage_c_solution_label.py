"""Stage C — solution-level labeling + consistency classification.

For every reference solution we:
  1. Compute an AST fingerprint (`rules.solution_ast_features`).
  2. Translate the fingerprint into preliminary family hints.
  3. Call GLM (system+user from `prompts/solution_labeling.yaml`).
  4. Fuse: LLM output must pick from the 8 core families; if its
     `detected_single_skill` contradicts AST hints *and* its confidence is
     low, we override with the strongest AST hint.
  5. Compute consistency against the problem-level labels from Stage B:
        - `consistent`    — detected_multi == problem_multi as sets
        - `partial`       — intersection non-empty but sets differ
        - `inconsistent`  — empty intersection
        - `unknown`       — AST failed or LLM gave up

Outputs (under `outputs/stage_c/`):
  * `solution_labeled.jsonl`      — every (problem, solution) pair
  * `solution_consistent.jsonl`   — consistent + (optionally) partial rows
  * `solution_inconsistent.jsonl` — inconsistent + unknown rows
  * `reports/labeling_guideline.md` — written on first run
"""
from __future__ import annotations

import json
import math
import re
import time
from pathlib import Path
from typing import Any, Iterator

import yaml

from .cache import DiskCache
from .io_utils import append_jsonl, load_jsonl, read_jsonl, save_json
from .llm.base import ChatLLM, LLMError
from .logging_utils import get_logger
from .rules import ast_to_family_hints, solution_ast_features
from .settings import Settings
from .stage_a_filter import load_selected
from .stage_b_problem_label import load_problem_labels
from .subtype_taxonomy import (
    all_subtypes,
    get_subtype,
    infer_candidate_subtypes_from_problem,
    infer_candidate_subtypes_from_solution,
)
from .taxonomy import CORE_FAMILY_SET

LOG = get_logger(__name__)

_VERIFIED_SUBTYPE_PROMPT_VERSION = "stage_c_verified_subtype_v1"
_PRIMARY_DEEPSEEK_PROMPT_VERSION = "stage_c_primary_deepseek_v1"


def _load_prompt(settings: Settings) -> dict[str, Any]:
    with open(settings.prompts_dir / "solution_labeling.yaml", "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _classify(
    detected: list[str],
    problem_skills: list[str],
    *,
    partial_min_overlap: int = 1,
) -> tuple[str, list[str], list[str]]:
    d, p = set(detected), set(problem_skills)
    matched = sorted(d & p)
    unmatched = sorted(p - d)
    if not detected or not problem_skills:
        return "unknown", matched, unmatched
    if d == p:
        return "consistent", matched, unmatched
    if len(matched) >= partial_min_overlap:
        return "partial", matched, unmatched
    return "inconsistent", matched, unmatched


def _fuse_solution(
    llm_payload: dict[str, Any],
    ast_hints: list[str],
) -> dict[str, Any]:
    single = llm_payload.get("detected_single_skill")
    multi = llm_payload.get("detected_multi_skills") or []
    confidence = float(llm_payload.get("confidence") or 0.0)
    multi_clean = [m for m in multi if m in CORE_FAMILY_SET]
    if not multi_clean and single in CORE_FAMILY_SET:
        multi_clean = [single]

    action = "llm_accepted"
    if single not in CORE_FAMILY_SET:
        single = ast_hints[0] if ast_hints else "complete_search"
        action = "ast_override_invalid"
    elif ast_hints and single not in ast_hints and confidence < 0.6:
        single = ast_hints[0]
        action = "ast_override_low_confidence"
        if single not in multi_clean:
            multi_clean = [single] + multi_clean
    return {
        "detected_single_skill": single,
        "detected_multi_skills": multi_clean or [single],
        "fused_confidence": max(confidence, 0.5 if action != "llm_accepted" else confidence),
        "fusion_action": action,
    }


def run_stage_c(settings: Settings, glm: ChatLLM, *, scope: str = "multi") -> dict[str, Path]:
    prompt_cfg = _load_prompt(settings)
    prompt_version = prompt_cfg["version"]
    labeling_cfg = settings.config.get("labeling", {})
    partial_min = int(labeling_cfg.get("consistency", {}).get("partial_overlap_min", 1))

    problems = {r["problem_id"]: r for r in load_selected(settings, scope=scope)}
    problem_labels = load_problem_labels(settings)
    if not problem_labels:
        raise RuntimeError("Stage B labels missing. Run Stage B first.")

    out_dir = settings.stage_dir("stage_c")
    labeled_path = out_dir / "solution_labeled.jsonl"
    consistent_path = out_dir / "solution_consistent.jsonl"
    inconsistent_path = out_dir / "solution_inconsistent.jsonl"
    cache = DiskCache(settings.cache_dir / "glm" / "solution_labeling")

    done: set[str] = set()
    if labeled_path.exists():
        for row in load_jsonl(labeled_path):
            done.add(f"{row['problem_id']}::{row['solution_id']}")

    recommended = prompt_cfg.get("recommended_params", {}) or {}
    temperature = float(recommended.get("temperature", settings.glm.temperature))
    max_tokens = int(recommended.get("max_tokens", settings.glm.max_tokens))

    total_pairs = sum(len(p.get("reference_solutions") or []) for p in problems.values())
    LOG.info("Stage C: %d problems, %d solution pairs to label (done=%d)",
             len(problems), total_pairs, len(done))

    processed = 0
    for pid, prob in problems.items():
        label = problem_labels.get(pid)
        if label is None:
            LOG.warning("No Stage B label for %s — skipping its solutions", pid)
            continue
        problem_skills = label.get("normalized_multi_skills") or [label.get("normalized_single_skill")]
        problem_skills = [s for s in problem_skills if s in CORE_FAMILY_SET]
        problem_summary = label.get("problem_summary", "")

        for sol in prob.get("reference_solutions") or []:
            sid = sol["solution_id"]
            key = f"{pid}::{sid}"
            if key in done:
                continue
            code = sol["code"]
            ast_features = solution_ast_features(code)
            ast_hints = ast_to_family_hints(ast_features)
            label_source = "glm_ast_fused"
            llm_error = ""

            cache_key = DiskCache.make_key({
                "v": prompt_version, "pid": pid, "sid": sid,
                "ast": ast_features.to_dict(), "problem_skills": problem_skills,
            })
            cached = cache.get("solution_labeling", cache_key)
            if cached is not None:
                llm_payload = cached.get("payload") or {}
                if llm_payload.get("core_mechanism_summary") == "LLM failure fallback.":
                    label_source = "ast_fallback"
                    llm_error = str(llm_payload.get("explanation") or "")
            else:
                user = prompt_cfg["user_template"].format(
                    problem_summary=problem_summary,
                    problem_skills=problem_skills,
                    solution_code=code[:6000],  # truncate very long refs
                    ast_features=ast_features.to_dict(),
                )
                try:
                    llm_payload = glm.chat_json(
                        system=prompt_cfg["system"],
                        user=user,
                        temperature=temperature,
                        max_tokens=max_tokens,
                    )
                except LLMError as exc:
                    label_source = "ast_fallback"
                    llm_error = str(exc)
                    LOG.error("GLM failed for %s/%s: %s — AST fallback", pid, sid, exc)
                    llm_payload = {
                        "detected_single_skill": ast_hints[0] if ast_hints else "complete_search",
                        "detected_multi_skills": ast_hints or ["complete_search"],
                        "core_mechanism_summary": "LLM failure fallback.",
                        "explanation": str(exc),
                        "confidence": 0.3,
                    }
                cache.set("solution_labeling", cache_key, {"payload": llm_payload})

            fused = _fuse_solution(llm_payload, ast_hints)
            consistency, matched, unmatched = _classify(
                fused["detected_multi_skills"], problem_skills, partial_min_overlap=partial_min,
            )
            row = {
                "problem_id": pid,
                "solution_id": sid,
                "solution_code": code,
                "problem_skills": problem_skills,
                "ast_features": ast_features.to_dict(),
                "ast_hints": ast_hints,
                "label_source": label_source,
                "llm_error": llm_error,
                "raw_llm_single": llm_payload.get("detected_single_skill"),
                "raw_llm_multi": llm_payload.get("detected_multi_skills") or [],
                "core_mechanism_summary": llm_payload.get("core_mechanism_summary", ""),
                "explanation": llm_payload.get("explanation", ""),
                "llm_confidence": float(llm_payload.get("confidence") or 0.0),
                **fused,
                "matched_problem_skills": matched,
                "unmatched_problem_skills": unmatched,
                "consistency_type": consistency,
                "prompt_version": prompt_version,
                "model": glm.model,
            }
            append_jsonl(labeled_path, row)
            if consistency in ("consistent", "partial"):
                append_jsonl(consistent_path, row)
            else:
                append_jsonl(inconsistent_path, row)
            processed += 1
            if processed % 50 == 0:
                LOG.info("Stage C progress %d pairs", processed)

    _write_guideline(settings)
    LOG.info("Stage C done.")
    return {
        "labeled": labeled_path,
        "consistent": consistent_path,
        "inconsistent": inconsistent_path,
    }


def run_stage_c_verified_subtype(
    settings: Settings,
    *,
    labeler: str = "rule-only",
    subtype_llm: ChatLLM | None = None,
    limit: int = 0,
    examples: int = 0,
    resume: bool = False,
    log_every: int = 100,
) -> dict[str, Path]:
    """Run Stage C on Stage C0 full-pass solutions and attach subtype labels.

    The default path is deterministic. When `labeler="deepseek"`, the model can
    only rerank the rule-generated subtype candidates; correctness remains the
    Stage C0 `full_pass` signal.
    """
    labeler = labeler.strip().lower()
    if labeler not in {"rule-only", "deepseek"}:
        raise ValueError("labeler must be one of: rule-only, deepseek")
    if labeler == "deepseek" and subtype_llm is None:
        raise RuntimeError("DeepSeek subtype labeler requested but no ChatLLM client was provided.")
    model = subtype_llm.model if subtype_llm is not None else "rule-only"

    out_dir = settings.stage_dir("stage_c")
    labeled_path = out_dir / "solution_labeled.jsonl"
    consistent_path = out_dir / "solution_consistent.jsonl"
    inconsistent_path = out_dir / "solution_inconsistent.jsonl"
    primary_path = out_dir / "primary_solutions.jsonl"
    summary_path = out_dir / "subtype_summary.json"

    if not resume:
        for path in (labeled_path, consistent_path, inconsistent_path, primary_path, summary_path):
            if path.exists():
                path.unlink()
    for path in (labeled_path, consistent_path, inconsistent_path, primary_path):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()

    total_eligible, total_groups = _count_stage_c0_verified_rows(settings, limit=limit)
    existing = _load_existing_verified_progress(
        labeled_path,
        primary_path,
        labeler=labeler,
        model=model,
        require_compatible=resume,
    ) if resume else _empty_existing_progress()

    cache = DiskCache(settings.cache_dir / "deepseek" / "verified_subtype")
    started = time.monotonic()
    summary: dict[str, Any] = {
        "prompt_version": _VERIFIED_SUBTYPE_PROMPT_VERSION,
        "labeler": labeler,
        "model": model,
        "resume": bool(resume),
        "log_every": int(log_every or 0),
        "stage_c0_inputs": [
            str(settings.output_dir / "stage_c0" / "single_skill_generation_dataset.jsonl"),
            str(settings.output_dir / "stage_c0" / "multi_skill_composition_dataset.jsonl"),
        ],
        "limit": int(limit or 0),
        "eligible_solutions": total_eligible,
        "eligible_problem_groups": total_groups,
        "already_done_solutions": len(existing["done_keys"]),
        "remaining_solutions_at_start": max(0, total_eligible - len(existing["done_keys"])),
        "taxonomy": _taxonomy_summary(),
        "groups_seen": 0,
        "groups_processed": 0,
        "groups_skipped_done": 0,
        "solutions_seen": 0,
        "solutions_labeled": len(existing["done_keys"]),
        "new_solutions_labeled": 0,
        "skipped_completed_solutions": 0,
        "consistent_rows": existing["consistent_rows"],
        "inconsistent_rows": existing["inconsistent_rows"],
        "primary_solutions": len(existing["primary_by_problem"]),
        "new_primary_solutions": 0,
        "subtype_counts": dict(existing["subtype_counts"]),
        "family_counts": dict(existing["family_counts"]),
        "label_source_counts": dict(existing["label_source_counts"]),
        "examples": [],
    }

    LOG.info(
        "Stage C verified subtype: labeler=%s model=%s limit=%s resume=%s log_every=%s "
        "eligible=%d done=%d remaining=%d groups=%d",
        labeler,
        model,
        limit or "all",
        resume,
        log_every,
        total_eligible,
        summary["already_done_solutions"],
        summary["remaining_solutions_at_start"],
        total_groups,
    )
    done_keys: set[str] = existing["done_keys"]
    primary_by_problem: dict[str, dict[str, Any]] = existing["primary_by_problem"]
    next_log_at = int(log_every or 0)
    for raw_group in _iter_stage_c0_verified_groups(settings, limit=limit):
        summary["groups_seen"] += 1
        summary["solutions_seen"] += len(raw_group)
        pending_group: list[dict[str, Any]] = []
        for raw in raw_group:
            key = _solution_key(raw)
            if resume and key in done_keys:
                summary["skipped_completed_solutions"] += 1
                continue
            pending_group.append(raw)

        if not pending_group:
            summary["groups_skipped_done"] += 1
            if next_log_at and summary["solutions_seen"] >= next_log_at:
                _log_verified_progress(summary, started)
                _save_verified_summary(summary_path, summary, started)
                next_log_at += int(log_every or 0)
            continue

        labeled_group: list[dict[str, Any]] = []
        for raw in pending_group:
            row = _label_verified_solution(
                raw,
                labeler=labeler,
                subtype_llm=subtype_llm,
                cache=cache,
            )
            labeled_group.append(row)
            done_keys.add(_solution_key(raw))
            summary["solutions_labeled"] += 1
            summary["new_solutions_labeled"] += 1
            _bump(summary["subtype_counts"], row["primary_subtype"])
            _bump(summary["family_counts"], row["detected_single_skill"])
            _bump(summary["label_source_counts"], row["subtype_label_source"])
            if examples and len(summary["examples"]) < examples:
                summary["examples"].append(_example_payload(row))

        if not labeled_group:
            continue
        pid = str(labeled_group[0]["problem_id"])
        if resume and pid in primary_by_problem:
            primary_payload = primary_by_problem[pid]
        else:
            primary = _select_primary_solution(labeled_group)
            primary_payload = _primary_payload(primary, labeler=labeler, model=model)
            append_jsonl(primary_path, primary_payload)
            primary_by_problem[pid] = primary_payload
            summary["primary_solutions"] += 1
            summary["new_primary_solutions"] += 1

        for row in labeled_group:
            row["primary_solution"] = {
                "problem_id": primary_payload["problem_id"],
                "solution_id": primary_payload["solution_id"],
                "primary_subtype": primary_payload["primary_subtype"],
                "score": primary_payload["primary_solution_score"],
            }
            row["is_primary_solution"] = row["solution_id"] == primary_payload["solution_id"]
            row["primary_selection_reason"] = (
                primary_payload["primary_selection_reason"]
                if row["is_primary_solution"]
                else f"primary_solution={primary['solution_id']} scored higher on verified subtype quality metrics"
            )
            append_jsonl(labeled_path, row)
            if row["consistency_type"] in {"consistent", "partial"}:
                append_jsonl(consistent_path, row)
                summary["consistent_rows"] += 1
            else:
                append_jsonl(inconsistent_path, row)
                summary["inconsistent_rows"] += 1

        summary["groups_processed"] += 1
        if next_log_at and summary["solutions_seen"] >= next_log_at:
            _log_verified_progress(summary, started)
            _save_verified_summary(summary_path, summary, started)
            next_log_at += int(log_every or 0)

    _save_verified_summary(summary_path, summary, started)
    for item in summary["examples"]:
        LOG.info(
            "Example solution->subtype: %s/%s -> %s (family=%s confidence=%.2f source=%s)",
            item["problem_id"],
            item["solution_id"],
            item["primary_subtype"],
            item["family"],
            item["subtype_confidence"],
            item["subtype_label_source"],
        )
    LOG.info(
        "Stage C verified subtype done: solutions=%d groups=%d primary=%d consistent=%d inconsistent=%d",
        summary["solutions_labeled"],
        summary["groups_processed"],
        summary["primary_solutions"],
        summary["consistent_rows"],
        summary["inconsistent_rows"],
    )
    return {
        "labeled": labeled_path,
        "consistent": consistent_path,
        "inconsistent": inconsistent_path,
        "primary_solutions": primary_path,
        "summary": summary_path,
    }


def run_stage_c_primary_deepseek(
    settings: Settings,
    *,
    subtype_llm: ChatLLM,
    deepseek_scope: str = "single",
    budget: int = 0,
    max_runtime_hours: float = 0.0,
    limit: int = 0,
    examples: int = 0,
    resume: bool = False,
    log_every: int = 50,
) -> dict[str, Path]:
    """Rerank only per-problem primary solutions with DeepSeek.

    This is a companion pass after the full rule-only Stage C output exists. It
    keeps the 338k-row solution files intact and writes primary-only DeepSeek
    enhancements plus a merged primary file.
    """
    scope = deepseek_scope.strip().lower()
    if scope not in {"single", "multi", "all"}:
        raise ValueError("deepseek_scope must be one of: single, multi, all")

    out_dir = settings.stage_dir("stage_c")
    labeled_path = out_dir / "solution_labeled.jsonl"
    primary_path = out_dir / "primary_solutions.jsonl"
    enhanced_path = out_dir / "primary_solutions_deepseek.jsonl"
    merged_path = out_dir / "primary_solutions_merged.jsonl"
    summary_path = out_dir / "primary_deepseek_summary.json"
    if not labeled_path.exists() or not primary_path.exists():
        raise FileNotFoundError(
            "Stage C rule-only outputs are missing. Run --verified-subtype --subtype-labeler rule-only first."
        )
    if not resume:
        for path in (enhanced_path, merged_path, summary_path):
            if path.exists():
                path.unlink()
    enhanced_path.parent.mkdir(parents=True, exist_ok=True)
    enhanced_path.touch()

    started = time.monotonic()
    model = subtype_llm.model
    target_rows = _load_primary_deepseek_targets(
        labeled_path,
        primary_path,
        deepseek_scope=scope,
        limit=limit,
    )
    enhanced_existing = (
        _load_existing_primary_deepseek(enhanced_path, model=model) if resume else {}
    )
    budget_limit = int(budget or 0)
    runtime_limit_seconds = float(max_runtime_hours or 0.0) * 3600.0
    cache = DiskCache(settings.cache_dir / "deepseek" / "primary_subtype")
    summary: dict[str, Any] = {
        "prompt_version": _PRIMARY_DEEPSEEK_PROMPT_VERSION,
        "source_prompt_version": _VERIFIED_SUBTYPE_PROMPT_VERSION,
        "labeler": "rule-primary-deepseek",
        "model": model,
        "deepseek_scope": scope,
        "budget": budget_limit,
        "max_runtime_hours": float(max_runtime_hours or 0.0),
        "limit": int(limit or 0),
        "resume": bool(resume),
        "log_every": int(log_every or 0),
        "target_primary_solutions": len(target_rows),
        "already_enhanced": len(enhanced_existing),
        "deepseek_calls_used": 0,
        "skipped_completed": 0,
        "processed_targets": 0,
        "budget_exhausted": False,
        "runtime_exhausted": False,
        "deepseek_label_source_counts": {},
        "rule_subtype_counts": {},
        "final_subtype_counts": {},
        "examples": [],
    }
    LOG.info(
        "Stage C primary DeepSeek: scope=%s targets=%d already=%d budget=%s max_runtime_hours=%s resume=%s",
        scope,
        len(target_rows),
        len(enhanced_existing),
        budget_limit or "unlimited",
        max_runtime_hours or "unlimited",
        resume,
    )

    enhanced_by_key = dict(enhanced_existing)
    next_log_at = int(log_every or 0)
    for row in target_rows:
        key = _solution_key(row)
        summary["processed_targets"] += 1
        if resume and key in enhanced_by_key:
            summary["skipped_completed"] += 1
            enhanced = enhanced_by_key[key]
        else:
            if budget_limit and summary["deepseek_calls_used"] >= budget_limit:
                summary["budget_exhausted"] = True
                break
            if runtime_limit_seconds and (time.monotonic() - started) >= runtime_limit_seconds:
                summary["runtime_exhausted"] = True
                break
            enhanced = _enhance_primary_solution_with_deepseek(
                row,
                subtype_llm=subtype_llm,
                cache=cache,
            )
            append_jsonl(enhanced_path, enhanced)
            enhanced_by_key[key] = enhanced
            summary["deepseek_calls_used"] += 1
            if examples and len(summary["examples"]) < examples:
                summary["examples"].append(_primary_deepseek_example(enhanced))

        _bump(summary["rule_subtype_counts"], str(row.get("primary_subtype") or ""))
        _bump(summary["final_subtype_counts"], str(enhanced.get("primary_subtype") or row.get("primary_subtype") or ""))
        _bump(summary["deepseek_label_source_counts"], str(enhanced.get("subtype_label_source") or ""))
        if next_log_at and summary["processed_targets"] >= next_log_at:
            _log_primary_deepseek_progress(summary, started)
            _save_primary_deepseek_summary(summary_path, summary, started)
            next_log_at += int(log_every or 0)

    merged_count = _write_merged_primary_solutions(merged_path, target_rows, enhanced_by_key)
    summary["enhanced_rows_total"] = len(enhanced_by_key)
    summary["merged_rows"] = merged_count
    summary["rule_only_fallback_rows"] = max(0, len(target_rows) - len(enhanced_by_key))
    _save_primary_deepseek_summary(summary_path, summary, started)
    for item in summary["examples"]:
        LOG.info(
            "Example primary DeepSeek: %s/%s %s -> %s source=%s confidence=%.2f",
            item["problem_id"],
            item["solution_id"],
            item["rule_primary_subtype"],
            item["primary_subtype"],
            item["subtype_label_source"],
            item["subtype_confidence"],
        )
    LOG.info(
        "Stage C primary DeepSeek done: targets=%d enhanced=%d calls=%d fallback=%d budget_exhausted=%s runtime_exhausted=%s",
        len(target_rows),
        len(enhanced_by_key),
        summary["deepseek_calls_used"],
        summary["rule_only_fallback_rows"],
        summary["budget_exhausted"],
        summary["runtime_exhausted"],
    )
    return {
        "primary_deepseek": enhanced_path,
        "primary_merged": merged_path,
        "summary": summary_path,
    }


def _load_primary_deepseek_targets(
    labeled_path: Path,
    primary_path: Path,
    *,
    deepseek_scope: str,
    limit: int = 0,
) -> list[dict[str, Any]]:
    primary_keys: list[str] = []
    for row in read_jsonl(primary_path):
        key = _solution_key(row)
        if key not in primary_keys:
            primary_keys.append(key)
    primary_key_set = set(primary_keys)
    found: dict[str, dict[str, Any]] = {}
    for row in read_jsonl(labeled_path):
        key = _solution_key(row)
        if key not in primary_key_set:
            continue
        if not row.get("is_primary_solution"):
            continue
        if not _primary_scope_matches(row, deepseek_scope):
            continue
        found[key] = row
        if limit and len(found) >= limit:
            break
    ordered = [found[key] for key in primary_keys if key in found]
    return ordered[:limit] if limit else ordered


def _primary_scope_matches(row: dict[str, Any], deepseek_scope: str) -> bool:
    if deepseek_scope == "all":
        return True
    clean_split = str(row.get("stage_c0_clean_split") or "")
    dataset = str(row.get("stage_c0_dataset") or "")
    if deepseek_scope == "single":
        return clean_split == "single_clean" or dataset == "single"
    if deepseek_scope == "multi":
        return clean_split == "multi_clean" or dataset == "multi"
    return False


def _load_existing_primary_deepseek(path: Path, *, model: str) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return rows
    for row in read_jsonl(path):
        if row.get("prompt_version") != _PRIMARY_DEEPSEEK_PROMPT_VERSION:
            continue
        if row.get("subtype_labeler") != "rule-primary-deepseek":
            continue
        if str(row.get("model") or "") != model:
            continue
        rows[_solution_key(row)] = row
    return rows


def _enhance_primary_solution_with_deepseek(
    row: dict[str, Any],
    *,
    subtype_llm: ChatLLM,
    cache: DiskCache,
) -> dict[str, Any]:
    candidate_subtypes = row.get("candidate_subtypes") or []
    if not candidate_subtypes:
        candidate_subtypes = [
            {
                "subtype_id": row.get("primary_subtype"),
                "family": row.get("detected_single_skill"),
                "score": row.get("subtype_confidence", 0.5),
                "sources": ["rule_primary"],
                "description": row.get("core_mechanism_summary", ""),
            }
        ]
    allowed_ids = [str(item.get("subtype_id") or "") for item in candidate_subtypes if item.get("subtype_id")]
    cache_key = DiskCache.make_key(
        {
            "v": _PRIMARY_DEEPSEEK_PROMPT_VERSION,
            "pid": row.get("problem_id"),
            "sid": row.get("solution_id"),
            "allowed": allowed_ids,
            "rule_primary": row.get("primary_subtype"),
            "code": (row.get("solution_code") or "")[:8000],
            "problem": (row.get("problem_statement") or "")[:2000],
        }
    )
    cached = cache.get("primary_subtype_rerank", cache_key)
    if cached is not None:
        payload = cached.get("payload") or {}
    else:
        payload = _call_deepseek_subtype_rerank(
            subtype_llm,
            row,
            ast_features=row.get("ast_features") or {},
            candidate_subtypes=candidate_subtypes,
        )
        cache.set("primary_subtype_rerank", cache_key, {"payload": payload})

    selected = str(payload.get("primary_subtype") or "")
    if selected not in allowed_ids:
        selected = str(row.get("primary_subtype") or (allowed_ids[0] if allowed_ids else ""))
        label_source = "deepseek_invalid_rule_primary_fallback"
        rationale = f"DeepSeek returned invalid subtype; kept rule primary subtype {selected}."
        model_confidence = 0.0
    else:
        label_source = "deepseek_primary_rerank"
        rationale = str(payload.get("rationale") or f"DeepSeek confirmed primary subtype {selected}.")[:800]
        model_confidence = _clamp(payload.get("confidence"), 0.0, 1.0)

    subtype = get_subtype(selected)
    family = subtype.family if subtype else str(row.get("detected_single_skill") or "")
    rule_confidence = _safe_float(row.get("subtype_confidence"), 0.0)
    final_confidence = max(0.25, min(0.98, (rule_confidence * 0.45) + (model_confidence * 0.55)))
    enhanced = dict(row)
    enhanced.update(
        {
            "prompt_version": _PRIMARY_DEEPSEEK_PROMPT_VERSION,
            "source_prompt_version": row.get("prompt_version"),
            "subtype_labeler": "rule-primary-deepseek",
            "model": subtype_llm.model,
            "subtype_label_source": label_source,
            "rule_primary_subtype": row.get("primary_subtype"),
            "rule_subtype_confidence": row.get("subtype_confidence"),
            "primary_subtype": selected,
            "detected_single_skill": family,
            "subtype_confidence": round(final_confidence, 4),
            "llm_confidence": model_confidence,
            "raw_llm_single": payload.get("primary_subtype", ""),
            "raw_llm_multi": payload.get("solution_algorithm_tags_verified") or [],
            "subtype_rationale": rationale,
            "core_mechanism_summary": str(payload.get("core_mechanism_summary") or row.get("core_mechanism_summary") or "")[:800],
            "solution_algorithm_tags_verified": _solution_algorithm_tags(selected, family, candidate_subtypes),
            "deepseek_payload": payload,
        }
    )
    return enhanced


def _write_merged_primary_solutions(
    merged_path: Path,
    target_rows: list[dict[str, Any]],
    enhanced_by_key: dict[str, dict[str, Any]],
) -> int:
    merged_path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with open(merged_path, "w", encoding="utf-8") as fh:
        for row in target_rows:
            out = enhanced_by_key.get(_solution_key(row), row)
            fh.write(json.dumps(out, ensure_ascii=False))
            fh.write("\n")
            count += 1
    return count


def _save_primary_deepseek_summary(summary_path: Path, summary: dict[str, Any], started: float) -> None:
    summary["elapsed_seconds"] = round(time.monotonic() - started, 3)
    save_json(summary_path, summary)


def _log_primary_deepseek_progress(summary: dict[str, Any], started: float) -> None:
    elapsed = max(time.monotonic() - started, 0.001)
    processed = int(summary.get("processed_targets") or 0)
    target = int(summary.get("target_primary_solutions") or 0)
    remaining = max(0, target - processed)
    rate = processed / elapsed
    eta = remaining / rate if rate > 0 else 0.0
    LOG.info(
        "Stage C primary DeepSeek progress: processed=%d/%d (%.1f%%) calls=%d skipped=%d "
        "elapsed=%s eta=%s rate=%.3f primary/s",
        processed,
        target,
        (processed / target * 100.0) if target else 100.0,
        int(summary.get("deepseek_calls_used") or 0),
        int(summary.get("skipped_completed") or 0),
        _format_duration(elapsed),
        _format_duration(eta),
        rate,
    )


def _primary_deepseek_example(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "problem_id": row.get("problem_id"),
        "solution_id": row.get("solution_id"),
        "rule_primary_subtype": row.get("rule_primary_subtype"),
        "primary_subtype": row.get("primary_subtype"),
        "subtype_label_source": row.get("subtype_label_source"),
        "subtype_confidence": row.get("subtype_confidence"),
    }


def _iter_stage_c0_verified_groups(settings: Settings, *, limit: int = 0) -> Iterator[list[dict[str, Any]]]:
    """Yield contiguous Stage C0 full-pass rows grouped by problem_id.

    The C0 files are produced in raw-TACO order, so rows for a problem are
    contiguous within each clean split file. `limit` caps solution rows, which is
    useful for small smoke runs.
    """
    stage_c0 = settings.output_dir / "stage_c0"
    inputs = (
        ("single", stage_c0 / "single_skill_generation_dataset.jsonl"),
        ("multi", stage_c0 / "multi_skill_composition_dataset.jsonl"),
    )
    seen = 0
    for dataset_kind, path in inputs:
        if not path.exists():
            raise FileNotFoundError(f"Stage C0 input not found: {path}")
        current_pid = ""
        current: list[dict[str, Any]] = []
        for raw in read_jsonl(path):
            if limit and seen >= limit:
                break
            if not raw.get("full_pass"):
                continue
            if raw.get("clean_split") not in {"single_clean", "multi_clean"}:
                continue
            pid = str(raw.get("problem_id") or "")
            if not pid:
                continue
            if current and pid != current_pid:
                yield current
                current = []
            current_pid = pid
            row = dict(raw)
            row["_stage_c0_dataset"] = dataset_kind
            current.append(row)
            seen += 1
        if current:
            yield current
        if limit and seen >= limit:
            break


def _count_stage_c0_verified_rows(settings: Settings, *, limit: int = 0) -> tuple[int, int]:
    total = 0
    groups = 0
    for group in _iter_stage_c0_verified_groups(settings, limit=limit):
        groups += 1
        total += len(group)
    return total, groups


def _solution_key(row: dict[str, Any]) -> str:
    return f"{row.get('problem_id')}::{row.get('solution_id')}"


def _empty_existing_progress() -> dict[str, Any]:
    return {
        "done_keys": set(),
        "primary_by_problem": {},
        "consistent_rows": 0,
        "inconsistent_rows": 0,
        "subtype_counts": {},
        "family_counts": {},
        "label_source_counts": {},
    }


def _load_existing_verified_progress(
    labeled_path: Path,
    primary_path: Path,
    *,
    labeler: str,
    model: str,
    require_compatible: bool,
) -> dict[str, Any]:
    progress = _empty_existing_progress()
    incompatible_seen = False
    if labeled_path.exists():
        for row in read_jsonl(labeled_path):
            if not row:
                continue
            compatible = _is_compatible_verified_row(row, labeler=labeler, model=model)
            if not compatible:
                incompatible_seen = True
                continue
            key = _solution_key(row)
            if key in progress["done_keys"]:
                continue
            progress["done_keys"].add(key)
            if row.get("consistency_type") in {"consistent", "partial"}:
                progress["consistent_rows"] += 1
            else:
                progress["inconsistent_rows"] += 1
            _bump(progress["subtype_counts"], str(row.get("primary_subtype") or ""))
            _bump(progress["family_counts"], str(row.get("detected_single_skill") or ""))
            _bump(progress["label_source_counts"], str(row.get("subtype_label_source") or ""))

    if primary_path.exists():
        for row in read_jsonl(primary_path):
            if not row:
                continue
            if not _is_compatible_verified_row(row, labeler=labeler, model=model):
                incompatible_seen = True
                continue
            pid = str(row.get("problem_id") or "")
            if pid and pid not in progress["primary_by_problem"]:
                progress["primary_by_problem"][pid] = row

    if require_compatible and incompatible_seen and not progress["done_keys"]:
        raise RuntimeError(
            "Existing Stage C outputs are not compatible with this verified subtype run. "
            "Run without --resume to overwrite them, or move outputs/stage_c aside."
        )
    if require_compatible and incompatible_seen:
        LOG.warning(
            "Stage C resume ignored some incompatible existing rows; compatible_done=%d compatible_primary=%d",
            len(progress["done_keys"]),
            len(progress["primary_by_problem"]),
        )
    return progress


def _is_compatible_verified_row(row: dict[str, Any], *, labeler: str, model: str) -> bool:
    if row.get("prompt_version") != _VERIFIED_SUBTYPE_PROMPT_VERSION:
        return False
    if row.get("subtype_labeler") != labeler:
        return False
    return str(row.get("model") or "") == model


def _save_verified_summary(summary_path: Path, summary: dict[str, Any], started: float) -> None:
    summary["elapsed_seconds"] = round(time.monotonic() - started, 3)
    save_json(summary_path, summary)


def _log_verified_progress(summary: dict[str, Any], started: float) -> None:
    elapsed = max(time.monotonic() - started, 0.001)
    seen = int(summary.get("solutions_seen") or 0)
    eligible = int(summary.get("eligible_solutions") or 0)
    new_done = int(summary.get("new_solutions_labeled") or 0)
    skipped = int(summary.get("skipped_completed_solutions") or 0)
    remaining = max(0, eligible - seen)
    rate = seen / elapsed
    eta = remaining / rate if rate > 0 else 0.0
    LOG.info(
        "Stage C verified subtype progress: seen=%d/%d (%.1f%%) new=%d skipped=%d "
        "groups=%d/%d primary=%d elapsed=%s eta=%s rate=%.2f rows/s",
        seen,
        eligible,
        (seen / eligible * 100.0) if eligible else 100.0,
        new_done,
        skipped,
        int(summary.get("groups_seen") or 0),
        int(summary.get("eligible_problem_groups") or 0),
        int(summary.get("primary_solutions") or 0),
        _format_duration(elapsed),
        _format_duration(eta),
        rate,
    )


def _format_duration(seconds: float) -> str:
    seconds = max(0, int(seconds))
    hours, rem = divmod(seconds, 3600)
    minutes, secs = divmod(rem, 60)
    if hours:
        return f"{hours}h{minutes:02d}m{secs:02d}s"
    if minutes:
        return f"{minutes}m{secs:02d}s"
    return f"{secs}s"


def _label_verified_solution(
    raw: dict[str, Any],
    *,
    labeler: str,
    subtype_llm: ChatLLM | None,
    cache: DiskCache,
) -> dict[str, Any]:
    pid = str(raw.get("problem_id") or "")
    sid = str(raw.get("solution_id") or "")
    code = raw.get("solution_code") or ""
    problem_statement = raw.get("problem_statement") or ""
    problem_skills = _row_problem_families(raw)
    ast_features = solution_ast_features(code)
    ast_hints = ast_to_family_hints(ast_features)
    family_filter = _ordered_unique(problem_skills + _row_solution_family_hints(raw) + ast_hints)

    problem_candidates = infer_candidate_subtypes_from_problem(
        problem_statement,
        raw.get("original_skill_types") or [],
        raw.get("original_tags") or [],
        problem_skills,
        max_candidates=10,
    )
    solution_candidates = infer_candidate_subtypes_from_solution(
        code,
        ast_features,
        family_filter=family_filter,
        max_candidates=10,
    )
    candidate_subtypes = _merge_subtype_candidates(
        problem_candidates,
        solution_candidates,
        family_filter=family_filter,
        ast_hints=ast_hints,
    )
    if not candidate_subtypes:
        candidate_subtypes = [_fallback_candidate(problem_skills, ast_hints)]

    selected = _select_subtype_from_candidates(
        raw,
        ast_features=ast_features,
        candidate_subtypes=candidate_subtypes,
        labeler=labeler,
        subtype_llm=subtype_llm,
        cache=cache,
    )
    primary_subtype = selected["primary_subtype"]
    subtype = get_subtype(primary_subtype)
    selected_family = subtype.family if subtype else (candidate_subtypes[0].get("family") or "complete_search")
    detected_multi = _candidate_families_from_subtypes(candidate_subtypes, selected_family)
    consistency, matched, unmatched = _classify(detected_multi, problem_skills)
    metrics = _solution_quality_metrics(
        raw,
        ast_features=ast_features,
        selected_family=str(selected_family),
        subtype_confidence=float(selected["subtype_confidence"]),
        candidate_subtypes=candidate_subtypes,
    )

    return {
        "problem_id": pid,
        "solution_id": sid,
        "solution_code": code,
        "problem_statement": problem_statement,
        "source_dataset": raw.get("source_dataset"),
        "split": raw.get("split"),
        "source_index": raw.get("source_index"),
        "difficulty": raw.get("difficulty"),
        "stage_c0_dataset": raw.get("_stage_c0_dataset"),
        "stage_c0_clean_split": raw.get("clean_split"),
        "stage_c0_scope": raw.get("scope"),
        "verification_source": raw.get("verification_source", "stage_c0"),
        "syntax_ok": bool(raw.get("syntax_ok")),
        "safe_exec_ok": bool(raw.get("safe_exec_ok")),
        "full_pass": bool(raw.get("full_pass")),
        "passed_tests": int(raw.get("passed_tests") or 0),
        "total_tests": int(raw.get("total_tests") or 0),
        "pass_rate": float(raw.get("pass_rate") or 0.0),
        "avg_time_ms": float(raw.get("avg_time_ms") or 0.0),
        "problem_skills": problem_skills,
        "original_skill_types": raw.get("original_skill_types") or [],
        "original_tags": raw.get("original_tags") or [],
        "ast_features": ast_features.to_dict(),
        "ast_hints": ast_hints,
        "problem_candidate_subtypes": problem_candidates,
        "solution_candidate_subtypes": solution_candidates,
        "candidate_subtypes": candidate_subtypes,
        "solution_algorithm_tags_verified": _solution_algorithm_tags(primary_subtype, str(selected_family), candidate_subtypes),
        "primary_subtype": primary_subtype,
        "subtype_confidence": round(_safe_float(selected["subtype_confidence"], 0.0), 4),
        "subtype_label_source": selected["subtype_label_source"],
        "subtype_labeler": labeler,
        "subtype_rationale": selected["subtype_rationale"],
        "detected_single_skill": selected_family,
        "detected_multi_skills": detected_multi,
        "fused_confidence": round(_safe_float(selected["subtype_confidence"], 0.0), 4),
        "fusion_action": selected["fusion_action"],
        "raw_llm_single": selected.get("raw_model_subtype", ""),
        "raw_llm_multi": selected.get("raw_model_tags", []),
        "llm_confidence": _safe_float(selected.get("model_confidence"), 0.0),
        "core_mechanism_summary": selected.get("core_mechanism_summary", ""),
        "explanation": selected["subtype_rationale"],
        "matched_problem_skills": matched,
        "unmatched_problem_skills": unmatched,
        "consistency_type": consistency,
        "algorithm_alignment": metrics["algorithm_alignment"],
        "complexity_match": metrics["complexity_match"],
        "reusability_score": metrics["reusability_score"],
        "generality_score": metrics["generality_score"],
        "implementation_cleanliness": metrics["implementation_cleanliness"],
        "primary_solution_score": metrics["primary_solution_score"],
        "primary_score_components": metrics["primary_score_components"],
        "hard_filter_pass": metrics["hard_filter_pass"],
        "filter_flags": metrics["filter_flags"],
        "quality_breakdown": metrics["quality_breakdown"],
        "prompt_version": _VERIFIED_SUBTYPE_PROMPT_VERSION,
        "model": selected.get("model", "rule-only"),
    }


def _select_subtype_from_candidates(
    raw: dict[str, Any],
    *,
    ast_features: Any,
    candidate_subtypes: list[dict[str, Any]],
    labeler: str,
    subtype_llm: ChatLLM | None,
    cache: DiskCache,
) -> dict[str, Any]:
    top = candidate_subtypes[0]
    rule_confidence = _rule_confidence(candidate_subtypes)
    fallback = {
        "primary_subtype": top["subtype_id"],
        "subtype_confidence": rule_confidence,
        "subtype_label_source": "rule_only",
        "subtype_rationale": f"Top deterministic subtype candidate from problem tags + solution AST/code hints: {top['subtype_id']}.",
        "fusion_action": "verified_subtype_rule",
        "core_mechanism_summary": top.get("description", ""),
        "model": "rule-only",
    }
    if labeler != "deepseek" or subtype_llm is None:
        return fallback

    allowed_ids = [str(item["subtype_id"]) for item in candidate_subtypes]
    cache_key = DiskCache.make_key(
        {
            "v": _VERIFIED_SUBTYPE_PROMPT_VERSION,
            "pid": raw.get("problem_id"),
            "sid": raw.get("solution_id"),
            "allowed": allowed_ids,
            "code": (raw.get("solution_code") or "")[:8000],
            "problem": (raw.get("problem_statement") or "")[:2000],
        }
    )
    cached = cache.get("subtype_rerank", cache_key)
    if cached is not None:
        payload = cached.get("payload") or {}
    else:
        payload = _call_deepseek_subtype_rerank(
            subtype_llm,
            raw,
            ast_features=ast_features,
            candidate_subtypes=candidate_subtypes,
        )
        cache.set("subtype_rerank", cache_key, {"payload": payload})

    selected = str(payload.get("primary_subtype") or "")
    if selected not in allowed_ids:
        fallback["subtype_label_source"] = "deepseek_invalid_rule_fallback"
        fallback["subtype_rationale"] = (
            f"DeepSeek returned invalid subtype {selected!r}; fell back to rule candidate {top['subtype_id']}."
        )
        fallback["model"] = subtype_llm.model
        return fallback

    model_confidence = _clamp(payload.get("confidence"), 0.0, 1.0)
    rule_for_selected = next((item for item in candidate_subtypes if item["subtype_id"] == selected), top)
    blended_confidence = max(0.25, min(0.98, (rule_confidence * 0.55) + (model_confidence * 0.45)))
    return {
        "primary_subtype": selected,
        "subtype_confidence": blended_confidence,
        "subtype_label_source": "deepseek_rerank",
        "subtype_rationale": str(payload.get("rationale") or f"DeepSeek reranked candidate {selected}.")[:800],
        "fusion_action": "verified_subtype_deepseek_rerank",
        "raw_model_subtype": selected,
        "raw_model_tags": payload.get("solution_algorithm_tags_verified") or [],
        "model_confidence": model_confidence,
        "core_mechanism_summary": str(payload.get("core_mechanism_summary") or rule_for_selected.get("description") or "")[:800],
        "model": subtype_llm.model,
    }


def _call_deepseek_subtype_rerank(
    subtype_llm: ChatLLM,
    raw: dict[str, Any],
    *,
    ast_features: Any,
    candidate_subtypes: list[dict[str, Any]],
) -> dict[str, Any]:
    system = (
        "You label verified competitive-programming reference solutions by algorithm subtype. "
        "Correctness has already been decided by tests; do not judge correctness. "
        "Choose exactly one primary_subtype from the provided candidate IDs only. "
        "Return one JSON object."
    )
    candidates = [
        {
            "subtype_id": item["subtype_id"],
            "family": item["family"],
            "rule_score": item.get("score"),
            "description": item.get("description"),
            "sources": item.get("sources", []),
        }
        for item in candidate_subtypes[:8]
    ]
    user = (
        "Problem tags are weak supervision. Solution code is the stronger signal.\n"
        "Return JSON with keys: primary_subtype, confidence, solution_algorithm_tags_verified, "
        "core_mechanism_summary, rationale.\n\n"
        f"problem_id: {raw.get('problem_id')}\n"
        f"solution_id: {raw.get('solution_id')}\n"
        f"original_skill_types: {raw.get('original_skill_types') or []}\n"
        f"original_tags: {raw.get('original_tags') or []}\n"
        f"candidate_families: {_row_problem_families(raw)}\n"
        f"ast_features: {_ast_features_to_dict(ast_features)}\n"
        f"candidate_subtypes: {candidates}\n\n"
        f"problem_statement:\n{(raw.get('problem_statement') or '')[:2200]}\n\n"
        f"solution_code:\n{(raw.get('solution_code') or '')[:5000]}\n"
    )
    try:
        return subtype_llm.chat_json(system=system, user=user, temperature=0.0, max_tokens=800)
    except LLMError as exc:
        LOG.warning(
            "DeepSeek subtype rerank failed for %s/%s: %s; using rule fallback",
            raw.get("problem_id"),
            raw.get("solution_id"),
            exc,
        )
        return {"primary_subtype": "", "confidence": 0.0, "rationale": str(exc)}


def _merge_subtype_candidates(
    problem_candidates: list[dict[str, Any]],
    solution_candidates: list[dict[str, Any]],
    *,
    family_filter: list[str],
    ast_hints: list[str],
) -> list[dict[str, Any]]:
    merged: dict[str, dict[str, Any]] = {}

    def add(item: dict[str, Any], weight: float, source_prefix: str) -> None:
        subtype_id = str(item.get("subtype_id") or "")
        if not subtype_id:
            return
        current = merged.setdefault(
            subtype_id,
            {
                "subtype_id": subtype_id,
                "family": item.get("family"),
                "score": 0.0,
                "sources": [],
                "description": item.get("description", ""),
            },
        )
        current["score"] = float(current["score"]) + (float(item.get("score") or 0.0) * weight)
        current["sources"].extend(f"{source_prefix}:{src}" for src in item.get("sources", []))

    for item in problem_candidates:
        add(item, 0.45, "problem")
    for item in solution_candidates:
        add(item, 1.0, "solution")

    for item in merged.values():
        family = item.get("family")
        if family in family_filter:
            item["score"] = float(item["score"]) + 0.5
            item["sources"].append(f"alignment:family:{family}")
        if family in ast_hints:
            item["score"] = float(item["score"]) + 0.35
            item["sources"].append(f"alignment:ast:{family}")
        item["score"] = round(float(item["score"]), 4)
        item["sources"] = list(dict.fromkeys(item["sources"]))[:10]

    ranked = sorted(merged.values(), key=lambda item: float(item["score"]), reverse=True)
    return ranked[:10]


def _fallback_candidate(problem_skills: list[str], ast_hints: list[str]) -> dict[str, Any]:
    family = (ast_hints or problem_skills or ["complete_search"])[0]
    fallback_by_family = {
        "amortized_analysis": "amortized_two_pointers",
        "bit_manipulation": "bit_binary_representation",
        "complete_search": "search_dfs_bfs_graph",
        "data_structures": "ds_hash_map",
        "dynamic_programming": "dp_1d_state",
        "greedy_algorithms": "greedy_exchange_argument",
        "range_queries": "range_prefix_sum",
        "sorting": "sorting_custom_key",
    }
    subtype = get_subtype(fallback_by_family.get(family, "search_dfs_bfs_graph"))
    return {
        "subtype_id": subtype.subtype_id if subtype else "search_dfs_bfs_graph",
        "family": subtype.family if subtype else "complete_search",
        "score": 0.5,
        "sources": ["fallback"],
        "description": subtype.description if subtype else "Fallback complete-search subtype.",
    }


def _row_problem_families(raw: dict[str, Any]) -> list[str]:
    families: list[str] = []
    for key in ("candidate_families", "family_set", "problem_skills"):
        value = raw.get(key) or []
        if isinstance(value, str):
            value = [value]
        families.extend(str(item) for item in value)
    if raw.get("family"):
        families.append(str(raw["family"]))
    return _ordered_unique([f for f in families if f in CORE_FAMILY_SET])


def _ast_features_to_dict(ast_features: Any) -> dict[str, Any]:
    if hasattr(ast_features, "to_dict"):
        return ast_features.to_dict()
    if isinstance(ast_features, dict):
        return dict(ast_features)
    return {}


def _row_solution_family_hints(raw: dict[str, Any]) -> list[str]:
    value = raw.get("solution_family_hints") or []
    if isinstance(value, str):
        value = [value]
    return _ordered_unique([str(item) for item in value if item in CORE_FAMILY_SET])


def _candidate_families_from_subtypes(candidate_subtypes: list[dict[str, Any]], selected_family: str) -> list[str]:
    families = [selected_family]
    top_score = float(candidate_subtypes[0].get("score") or 0.0) if candidate_subtypes else 0.0
    for item in candidate_subtypes:
        family = str(item.get("family") or "")
        if family in CORE_FAMILY_SET and float(item.get("score") or 0.0) >= max(0.5, top_score * 0.72):
            families.append(family)
    return _ordered_unique(families)


def _solution_algorithm_tags(
    primary_subtype: str,
    family: str,
    candidate_subtypes: list[dict[str, Any]],
) -> list[str]:
    tags = [primary_subtype, family]
    tags.extend(str(item["subtype_id"]) for item in candidate_subtypes[:3])
    return _ordered_unique([tag for tag in tags if tag])


def _rule_confidence(candidate_subtypes: list[dict[str, Any]]) -> float:
    if not candidate_subtypes:
        return 0.25
    top = float(candidate_subtypes[0].get("score") or 0.0)
    second = float(candidate_subtypes[1].get("score") or 0.0) if len(candidate_subtypes) > 1 else 0.0
    base = top / (top + 3.0)
    gap = max(0.0, top - second) / max(top, 1.0)
    return _clamp(0.25 + (base * 0.55) + (gap * 0.2), 0.25, 0.95)


def _solution_quality_metrics(
    raw: dict[str, Any],
    *,
    ast_features: Any,
    selected_family: str,
    subtype_confidence: float,
    candidate_subtypes: list[dict[str, Any]],
) -> dict[str, Any]:
    code = raw.get("solution_code") or ""
    lines = [line for line in code.splitlines() if line.strip()]
    line_count = max(1, len(lines))
    problem_skills = _row_problem_families(raw)
    solution_hints = _row_solution_family_hints(raw)
    total_tests = int(raw.get("total_tests") or 0)
    top_score = float(candidate_subtypes[0].get("score") or 0.0) if candidate_subtypes else 0.0

    algorithm_alignment = 0.35
    if selected_family in problem_skills:
        algorithm_alignment += 0.35
    if selected_family in solution_hints:
        algorithm_alignment += 0.15
    algorithm_alignment += min(0.15, top_score / 30.0)

    constraints_bonus = _constraint_complexity_bonus(raw.get("problem_statement") or "", ast_features.loops_max_depth)
    complexity_match = 0.55 + constraints_bonus
    if total_tests >= 20:
        complexity_match += 0.1
    if ast_features.loops_max_depth >= 4:
        complexity_match -= 0.12

    has_function = bool(re.search(r"\bdef\s+\w+", code))
    has_class = "class " in code
    reusability_score = 0.45 + (0.18 if has_function else 0.0) + (0.08 if has_class else 0.0)
    if line_count <= 160:
        reusability_score += 0.12
    if line_count > 400:
        reusability_score -= 0.12

    hardcoded_penalty = 0.12 if re.search(r"\[[0-9,\s]{30,}\]", code) else 0.0
    generality_score = 0.55 + (0.12 if "input(" in code or "sys.stdin" in code else 0.0) - hardcoded_penalty
    if line_count <= 220:
        generality_score += 0.08

    implementation_cleanliness = 0.45
    if raw.get("syntax_ok"):
        implementation_cleanliness += 0.18
    if raw.get("safe_exec_ok"):
        implementation_cleanliness += 0.12
    if ast_features.loops_max_depth <= 3:
        implementation_cleanliness += 0.1
    if line_count <= 260:
        implementation_cleanliness += 0.08

    imports = re.findall(r"^\s*(?:from\s+[A-Za-z0-9_\.]+\s+import|import\s+[A-Za-z0-9_\.]+)", code, flags=re.MULTILINE)
    helper_defs = re.findall(r"^\s*def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", code, flags=re.MULTILINE)
    helper_def_count = len(helper_defs)
    unused_helper_estimate = sum(1 for name in helper_defs if len(re.findall(rf"\b{name}\b", code)) <= 1)
    import_ratio = len(imports) / line_count
    unused_helper_ratio = (unused_helper_estimate / helper_def_count) if helper_def_count else 0.0
    boilerplate_markers = ("input = ", "sys.setrecursionlimit", "MOD =", "MAX =", "MIN =")
    boilerplate_lines = sum(1 for ln in lines if any(mark in ln for mark in boilerplate_markers))
    boilerplate_ratio = boilerplate_lines / line_count
    filter_flags: list[str] = []
    if import_ratio > 0.08:
        filter_flags.append("high_import_ratio")
    if unused_helper_ratio > 0.35:
        filter_flags.append("high_unused_helper_ratio")
    if boilerplate_ratio > 0.20:
        filter_flags.append("high_boilerplate_ratio")
    hard_filter_pass = not filter_flags

    components = {
        "algorithm_alignment": _clamp(algorithm_alignment),
        "complexity_match": _clamp(complexity_match),
        "subtype_confidence": _clamp(subtype_confidence),
        "test_strength": _clamp(math.log(total_tests + 1, 10) / 2.0 if total_tests else 0.2),
        "reusability_score": _clamp(reusability_score),
        "generality_score": _clamp(generality_score),
        "implementation_cleanliness": _clamp(implementation_cleanliness),
    }
    score = (
        components["algorithm_alignment"] * 0.26
        + components["subtype_confidence"] * 0.22
        + components["complexity_match"] * 0.16
        + components["test_strength"] * 0.12
        + components["reusability_score"] * 0.10
        + components["generality_score"] * 0.07
        + components["implementation_cleanliness"] * 0.07
    )
    return {
        "algorithm_alignment": round(components["algorithm_alignment"], 4),
        "complexity_match": round(components["complexity_match"], 4),
        "reusability_score": round(components["reusability_score"], 4),
        "generality_score": round(components["generality_score"], 4),
        "implementation_cleanliness": round(components["implementation_cleanliness"], 4),
        "primary_solution_score": round(score, 4),
        "primary_score_components": {key: round(value, 4) for key, value in components.items()},
        "hard_filter_pass": hard_filter_pass,
        "filter_flags": filter_flags,
        "quality_breakdown": {
            "line_count": line_count,
            "import_count": len(imports),
            "import_ratio": round(import_ratio, 4),
            "helper_def_count": helper_def_count,
            "unused_helper_estimate": unused_helper_estimate,
            "unused_helper_ratio": round(unused_helper_ratio, 4),
            "boilerplate_lines": boilerplate_lines,
            "boilerplate_ratio": round(boilerplate_ratio, 4),
        },
    }


def _constraint_complexity_bonus(problem_statement: str, loop_depth: int) -> float:
    text = problem_statement.lower()
    large_n = bool(re.search(r"10\^?5|100000|2\s*\*\s*10\^?5|10\^?6|1000000", text))
    small_n = bool(re.search(r"n\s*(?:<=|\\leq)\s*(?:20|18|16|15|12|10)", text))
    if large_n and loop_depth <= 2:
        return 0.18
    if small_n and loop_depth >= 2:
        return 0.12
    return 0.06


def _select_primary_solution(rows: list[dict[str, Any]]) -> dict[str, Any]:
    filtered = [r for r in rows if r.get("hard_filter_pass", True)]
    pool = filtered or rows
    return max(
        pool,
        key=lambda row: (
            int(bool(row.get("hard_filter_pass", True))),
            float(row.get("primary_solution_score") or 0.0),
            float(row.get("subtype_confidence") or 0.0),
            int(row.get("total_tests") or 0),
            -len(row.get("solution_code") or ""),
            str(row.get("solution_id") or ""),
        ),
    )


def _primary_payload(row: dict[str, Any], *, labeler: str, model: str) -> dict[str, Any]:
    reason = (
        f"selected by score={row['primary_solution_score']} "
        f"(alignment={row['algorithm_alignment']}, subtype_confidence={row['subtype_confidence']}, "
        f"complexity={row['complexity_match']}, tests={row['total_tests']})"
    )
    return {
        "problem_id": row["problem_id"],
        "solution_id": row["solution_id"],
        "solution_code": row["solution_code"],
        "prompt_version": _VERIFIED_SUBTYPE_PROMPT_VERSION,
        "subtype_labeler": labeler,
        "model": model,
        "primary_subtype": row["primary_subtype"],
        "detected_single_skill": row["detected_single_skill"],
        "solution_algorithm_tags_verified": row["solution_algorithm_tags_verified"],
        "primary_solution_score": row["primary_solution_score"],
        "primary_selection_reason": reason,
        "hard_filter_pass": bool(row.get("hard_filter_pass", True)),
        "filter_flags": list(row.get("filter_flags") or []),
        "quality_breakdown": dict(row.get("quality_breakdown") or {}),
        "algorithm_alignment": row["algorithm_alignment"],
        "complexity_match": row["complexity_match"],
        "reusability_score": row["reusability_score"],
        "generality_score": row["generality_score"],
        "implementation_cleanliness": row["implementation_cleanliness"],
        "subtype_confidence": row["subtype_confidence"],
        "total_tests": row["total_tests"],
        "pass_rate": row["pass_rate"],
    }


def _taxonomy_summary() -> dict[str, Any]:
    subtypes = all_subtypes()
    by_family: dict[str, int] = {}
    for item in subtypes:
        _bump(by_family, str(item["family"]))
    return {
        "subtype_count": len(subtypes),
        "family_count": len(by_family),
        "subtype_count_by_family": by_family,
        "subtypes": subtypes,
    }


def _example_payload(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "problem_id": row["problem_id"],
        "solution_id": row["solution_id"],
        "family": row["detected_single_skill"],
        "primary_subtype": row["primary_subtype"],
        "candidate_subtypes": [item["subtype_id"] for item in row["candidate_subtypes"][:5]],
        "subtype_confidence": row["subtype_confidence"],
        "subtype_label_source": row["subtype_label_source"],
        "primary_solution_score": row["primary_solution_score"],
    }


def _ordered_unique(values: list[str]) -> list[str]:
    out: list[str] = []
    for value in values:
        if value and value not in out:
            out.append(value)
    return out


def _bump(counter: dict[str, int], key: str) -> None:
    counter[key] = int(counter.get(key, 0)) + 1


def _safe_float(value: Any, default: float = 0.0) -> float:
    if isinstance(value, bool):
        return float(value)
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value.strip())
        except ValueError:
            return default
    if isinstance(value, dict):
        for key in ("confidence", "score", "value", "probability"):
            if key in value:
                return _safe_float(value.get(key), default)
        return default
    if isinstance(value, list) and value:
        return _safe_float(value[0], default)
    return default


def _clamp(value: Any, low: float = 0.0, high: float = 1.0) -> float:
    numeric = _safe_float(value, low)
    return max(low, min(high, numeric))


def _write_guideline(settings: Settings) -> None:
    path = settings.reports_dir / "labeling_guideline.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return
    content = """# Labeling Guideline

## Principles
- **Problem labels** come from reading the problem, constraints, and I/O shape.
  The LLM can use the original TACO tags as a hint but must never copy them blindly.
- **Solution labels** come from the code's actual mechanism — AST + regex fingerprint
  is the anchor, not the variable names or the surrounding problem statement.

## Rule ↔ LLM fusion
| signal from LLM | signal from rule | action |
| --- | --- | --- |
| in-set, agrees with rule candidates | any | accept LLM |
| in-set, disagrees, confidence ≥ 0.75 (problem) / 0.6 (solution) | any | accept LLM |
| in-set, disagrees, confidence low | rule suggests something | **override with top rule / AST hint** |
| out-of-set or missing | any | override with top rule / AST hint |

## Consistency classification (Stage C)
- `consistent`    — `detected_multi_skills` equals `problem_skills` as sets.
- `partial`       — intersection non-empty but sets differ. A multi-skill problem
                    whose solution implements only its primary family lands here.
- `inconsistent`  — empty intersection. The labels disagree entirely.
- `unknown`       — code could not be parsed or LLM refused.

Only `consistent` (and optionally `partial`) rows feed Stage D skill synthesis.
"""
    path.write_text(content, encoding="utf-8")


def load_consistent(settings: Settings) -> list[dict[str, Any]]:
    path = settings.stage_dir("stage_c") / "solution_consistent.jsonl"
    if not path.exists():
        return []
    return load_jsonl(path)
