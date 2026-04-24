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

from pathlib import Path
from typing import Any

import yaml

from .cache import DiskCache
from .io_utils import append_jsonl, load_jsonl, write_jsonl
from .llm.base import ChatLLM, LLMError
from .logging_utils import get_logger
from .rules import ast_to_family_hints, solution_ast_features
from .settings import Settings
from .stage_a_filter import load_selected
from .stage_b_problem_label import load_problem_labels
from .taxonomy import CORE_FAMILY_SET

LOG = get_logger(__name__)


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
