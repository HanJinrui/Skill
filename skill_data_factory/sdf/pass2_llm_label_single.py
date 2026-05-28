"""Pass2b single track: mandatory DeepSeek subtype labeling."""
from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import yaml

from sdf.io_utils import append_jsonl, read_jsonl, save_json
from sdf.pass2_rule_candidates import build_rule_candidates
from sdf.factory_settings import Settings, cfg_section
from sdf.shared import bootstrap  # noqa: F401

from src.cache import DiskCache
from sdf.llm_client import build_factory_deepseek
from sdf.pass2_progress import Pass2Progress, count_planned_slots, load_pass2_resume_keys
from sdf.pass2_payload_parse import coerce_bool, parse_confidence
from sdf.pass2_llm_utils import (
    chat_json_label,
    pass2_base_max_tokens,
    pass2_input_limits,
    pass2_max_retries,
    pass2_token_ceiling,
    pass2_truncation_jump_to_ceiling,
)
from src.llm.base import LLMError
from src.logging_utils import get_logger
from src.subtype_taxonomy import get_subtype

LOG = get_logger(__name__)
TRACK = "single_algorithm"
PROMPT_VERSION = "solution_subtype_v1.1.1"


def _load_prompt(settings: Settings) -> tuple[str, str]:
    path = settings.prompts_dir / "solution_subtype_v1.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return str(data.get("system") or ""), str(data.get("user_template") or "")


def _rank_solutions(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        rows,
        key=lambda r: (
            -int(r.get("total_tests") or 0),
            -float(r.get("pass_rate") or 0),
            str(r.get("solution_id") or ""),
        ),
    )


def _label_one(
    row: dict[str, Any],
    *,
    client: Any,
    cache: DiskCache,
    system: str,
    user_tmpl: str,
    max_retries: int,
    base_max_tokens: int,
    token_ceiling: int,
    input_limits: tuple[int, int, int],
    jump_to_ceiling: bool,
) -> dict[str, Any] | None:
    rule_pack = build_rule_candidates(row)
    candidates = rule_pack["candidate_subtypes"]
    allowed = [str(c.get("subtype_id") or "") for c in candidates if c.get("subtype_id")]
    cache_key = DiskCache.make_key(
        {
            "v": PROMPT_VERSION,
            "pid": row.get("problem_id"),
            "sid": row.get("solution_id"),
            "allowed": allowed,
            "code": (row.get("solution_code") or "")[:8000],
        }
    )
    cached = cache.get("pass2_single", cache_key)
    if cached is not None:
        payload = cached.get("payload") or {}
    else:
        stmt_cap, code_cap, cand_cap = input_limits
        user = user_tmpl.format(
            problem_id=row.get("problem_id"),
            solution_id=row.get("solution_id"),
            candidate_families=row.get("problem_families") or row.get("candidate_families"),
            rule_top_subtype=rule_pack["rule_top_subtype"],
            rule_confidence=rule_pack["rule_confidence"],
            candidate_subtypes_json=json.dumps(
                [
                    {"subtype_id": c.get("subtype_id"), "family": c.get("family"), "score": c.get("score")}
                    for c in candidates[:cand_cap]
                ],
                ensure_ascii=False,
            ),
            problem_statement=(row.get("problem_statement") or "")[:stmt_cap],
            solution_code=(row.get("solution_code") or "")[:code_cap],
        )
        try:
            payload = chat_json_label(
                client,
                system=system,
                user=user,
                base_max_tokens=base_max_tokens,
                max_retries=max_retries,
                token_ceiling=token_ceiling,
                log_label="DeepSeek single label",
                temperature=0.0,
                jump_to_ceiling_on_truncation=jump_to_ceiling,
            )
        except LLMError:
            payload = None
        if payload is None:
            return None
        cache.set("pass2_single", cache_key, {"payload": payload})

    selected = str(payload.get("primary_subtype") or "")
    if selected not in allowed:
        return None
    subtype = get_subtype(selected)
    family = subtype.family if subtype else str(candidates[0].get("family") or "")
    conf = parse_confidence(payload.get("confidence"))
    problem_families = list(row.get("problem_families") or row.get("candidate_families") or [])
    alignment = True if row.get("open_family_candidates") else (family in problem_families if problem_families else True)
    return {
        **row,
        **rule_pack,
        "primary_subtype": selected,
        "detected_single_skill": family,
        "subtype_confidence": conf,
        "subtype_label_source": "rule_candidates+deepseek_v4",
        "llm_model": client.model,
        "llm_prompt_version": PROMPT_VERSION,
        "core_mechanism_summary": str(payload.get("core_mechanism_summary") or "")[:800],
        "subtype_rationale": str(payload.get("rationale") or "")[:800],
        "family_alignment": alignment,
        "taco_family_alignment": alignment,
        "family_evidence_method": row.get("family_evidence_method", "taco_tag_alignment"),
        "is_true_composition": coerce_bool(payload.get("is_true_composition")),
        "algorithm_scope": "single",
    }


def run_pass2_single(
    settings: Settings,
    *,
    resume: bool = False,
    budget: int = 0,
    retry_quarantine: bool = False,
) -> dict[str, Path]:
    p2 = cfg_section(settings, "pass2")
    if not p2.get("require_llm", True):
        raise ValueError("pass2.require_llm must be true for single track")
    budget = budget or int(p2.get("budget_solutions", 0) or 0)
    max_per_problem = int(p2.get("max_llm_solutions_per_problem", 3))
    max_retries = pass2_max_retries(p2, track="single")
    base_max_tokens = pass2_base_max_tokens(p2, track="single")
    token_ceiling = pass2_token_ceiling(p2, track="single")
    stmt_cap, code_cap, cand_cap = pass2_input_limits(p2, track="single")
    jump_to_ceiling = pass2_truncation_jump_to_ceiling(p2)
    max_workers = max(1, int(p2.get("max_workers", 1)))

    solutions_in = settings.pass1_dir(TRACK) / "solutions.jsonl"
    if not solutions_in.exists():
        raise FileNotFoundError(solutions_in)

    out_dir = settings.pass2_dir(TRACK)
    out_dir.mkdir(parents=True, exist_ok=True)
    labeled_path = out_dir / "labeled_solutions.jsonl"
    quarantine_path = out_dir / "quarantine.jsonl"
    rule_path = out_dir / "rule_candidates.jsonl"

    done_keys = load_pass2_resume_keys(out_dir, resume=resume, retry_quarantine=retry_quarantine)
    if resume:
        LOG.info("Pass2 single resume: skipping %d already-attempted solution keys", len(done_keys))

    client = build_factory_deepseek(settings)
    api_clients = int(getattr(client, "num_clients", 1))
    cache = DiskCache(settings.cache_dir / "llm_cache")
    system, user_tmpl = _load_prompt(settings)

    by_problem: dict[str, list[dict[str, Any]]] = {}
    for row in read_jsonl(solutions_in):
        by_problem.setdefault(str(row["problem_id"]), []).append(row)

    total_slots = count_planned_slots(by_problem, max_per_problem=max_per_problem)
    progress = Pass2Progress(track="single", total_slots=total_slots, already_done=len(done_keys))
    LOG.info(
        "Pass2 single progress: %d slots remaining (%d already attempted, %d total planned); workers=%d api_keys=%d",
        max(0, total_slots - len(done_keys)),
        len(done_keys),
        total_slots,
        max_workers,
        api_clients,
    )

    stats = {"labeled": 0, "quarantine": 0, "skipped_done": 0, "budget_stop": False}
    pending: list[tuple[str, dict[str, Any]]] = []
    for pid, rows in sorted(by_problem.items()):
        for row in _rank_solutions(rows)[:max_per_problem]:
            key = f"{pid}::{row.get('solution_id')}"
            if key in done_keys:
                stats["skipped_done"] += 1
                continue
            if budget > 0 and len(pending) >= budget:
                stats["budget_stop"] = True
                break
            rule_pack = build_rule_candidates(row)
            append_jsonl(rule_path, {**row, **rule_pack, "algorithm_scope": "single"})
            pending.append((pid, row))
        if stats.get("budget_stop"):
            break

    def label_task(item: tuple[str, dict[str, Any]]) -> dict[str, Any] | None:
        pid, row = item
        try:
            return _label_one(
                row,
                client=client,
                cache=cache,
                system=system,
                user_tmpl=user_tmpl,
                max_retries=max_retries,
                base_max_tokens=base_max_tokens,
                token_ceiling=token_ceiling,
                input_limits=(stmt_cap, code_cap, cand_cap),
                jump_to_ceiling=jump_to_ceiling,
            )
        except Exception as exc:
            LOG.warning(
                "Pass2 single label unexpected error for %s %s: %s",
                pid,
                row.get("solution_id"),
                exc,
            )
            return None

    def write_result(item: tuple[str, dict[str, Any]], labeled: dict[str, Any] | None) -> None:
        pid, row = item
        sid = str(row.get("solution_id") or "")
        if labeled is None or labeled.get("is_true_composition"):
            append_jsonl(quarantine_path, {**row, "quarantine_reason": "llm_failed_or_composition"})
            stats["quarantine"] += 1
            progress.log_item(
                problem_id=pid,
                solution_id=sid,
                status="quarantine",
                detail="llm_failed_or_composition",
            )
            return
        if not labeled.get("family_alignment", labeled.get("taco_family_alignment", True)):
            append_jsonl(quarantine_path, {**labeled, "quarantine_reason": "family_mismatch"})
            stats["quarantine"] += 1
            progress.log_item(
                problem_id=pid,
                solution_id=sid,
                status="quarantine",
                detail="family_mismatch",
            )
            return
        append_jsonl(labeled_path, labeled)
        stats["labeled"] += 1
        progress.log_item(
            problem_id=pid,
            solution_id=sid,
            status="ok",
            detail=f"subtype={labeled.get('primary_subtype')}",
        )

    if max_workers <= 1 or len(pending) <= 1:
        for item in pending:
            write_result(item, label_task(item))
    else:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(label_task, item): item for item in pending}
            for future in as_completed(futures):
                write_result(futures[future], future.result())

    calls = len(pending)
    summary_path = out_dir / "pass2_summary.json"
    save_json(
        summary_path,
        {"track": TRACK, "stats": stats, "calls": calls, "max_workers": max_workers, "api_clients": api_clients},
    )
    LOG.info("Pass2 single done: %s", stats)
    return {"labeled": labeled_path, "quarantine": quarantine_path, "summary": summary_path}
