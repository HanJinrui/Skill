"""Pass2b multi track: mandatory DeepSeek composition labeling."""
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
from src.subtype_taxonomy import all_subtypes, get_subtype
from src.taxonomy import CORE_FAMILIES

LOG = get_logger(__name__)
TRACK = "multi_algorithm"
PROMPT_VERSION = "solution_composition_v1.2.2"


def _composition_key(families: list[str]) -> str:
    return "+".join(sorted(set(families)))


def _load_prompt(settings: Settings) -> tuple[str, str]:
    path = settings.prompts_dir / "solution_composition_v1.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return str(data.get("system") or ""), str(data.get("user_template") or "")


def _rank_solutions(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        rows,
        key=lambda r: (-int(r.get("total_tests") or 0), -float(r.get("pass_rate") or 0)),
    )


def _as_list(value: Any) -> list[Any]:
    """Coerce LLM JSON fields that should be lists (models sometimes return scalars)."""
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return list(value)
    if isinstance(value, dict):
        return [value]
    return []


def _parse_composition_subtypes(comp_raw: Any, allowed: set[str]) -> list[dict[str, str]]:
    comp_subtypes: list[dict[str, str]] = []
    for item in _as_list(comp_raw):
        if isinstance(item, dict):
            st = str(item.get("subtype") or item.get("subtype_id") or "")
            if st in allowed:
                comp_subtypes.append({"subtype": st, "role": str(item.get("role") or "")[:200]})
        elif isinstance(item, str) and item in allowed:
            comp_subtypes.append({"subtype": item, "role": ""})
    return comp_subtypes


def _parse_composition_order(order_raw: Any, comp_subtypes: list[dict[str, str]]) -> list[str]:
    allowed_ids = {c["subtype"] for c in comp_subtypes}
    order = [str(x) for x in _as_list(order_raw) if str(x) in allowed_ids]
    if order:
        return order
    return [c["subtype"] for c in comp_subtypes]


def _parse_composition_families(families_raw: Any, fallback: list[str]) -> list[str]:
    parsed = [str(x) for x in _as_list(families_raw) if str(x)]
    return parsed or list(fallback)


def _composition_candidate_space(
    row: dict[str, Any],
    rule_pack: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[str]]:
    if row.get("open_family_candidates"):
        return all_subtypes(), list(CORE_FAMILIES)
    return (
        list(rule_pack["candidate_subtypes"]),
        list(row.get("problem_families") or row.get("candidate_families") or []),
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
    candidates, candidate_families = _composition_candidate_space(row, rule_pack)
    allowed = [str(c.get("subtype_id") or "") for c in candidates if c.get("subtype_id")]
    allowed_set = set(allowed)
    cache_key = DiskCache.make_key(
        {"v": PROMPT_VERSION, "pid": row.get("problem_id"), "sid": row.get("solution_id"), "allowed": allowed}
    )
    cached = cache.get("pass2_multi", cache_key)
    if cached is not None:
        payload = cached.get("payload") or {}
    else:
        stmt_cap, code_cap, cand_cap = input_limits
        prompt_candidates = candidates if row.get("open_family_candidates") else candidates[:cand_cap]
        user = user_tmpl.format(
            problem_id=row.get("problem_id"),
            solution_id=row.get("solution_id"),
            candidate_families=candidate_families,
            candidate_subtypes_json=json.dumps(
                [{"subtype_id": c.get("subtype_id"), "family": c.get("family")} for c in prompt_candidates],
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
                log_label="DeepSeek multi label",
                temperature=0.0,
                jump_to_ceiling_on_truncation=jump_to_ceiling,
            )
        except LLMError:
            payload = None
        if payload is None:
            return None
        cache.set("pass2_multi", cache_key, {"payload": payload})

    if not coerce_bool(payload.get("is_true_composition")):
        return None

    try:
        comp_subtypes = _parse_composition_subtypes(payload.get("composition_subtypes"), allowed_set)
        if len(comp_subtypes) < 2 or len(comp_subtypes) > 3:
            return None

        families = []
        for cs in comp_subtypes:
            st = get_subtype(cs["subtype"])
            if st:
                families.append(st.family)
        problem_families = list(row.get("problem_families") or [])
        if (
            problem_families
            and not row.get("open_family_candidates")
            and not all(f in problem_families for f in families)
        ):
            return None

        order = _parse_composition_order(payload.get("composition_order"), comp_subtypes)
        comp_families = _parse_composition_families(payload.get("composition_families"), families)
        conf = parse_confidence(payload.get("confidence"))

        return {
            **row,
            **rule_pack,
            "composition_subtypes": comp_subtypes,
            "composition_order": order,
            "composition_families": comp_families,
            "composition_key": _composition_key(families),
            "primary_composition_subtypes": order,
            "subtype_confidence": conf,
            "subtype_label_source": "rule_candidates+deepseek_v4",
            "llm_model": client.model,
            "llm_prompt_version": PROMPT_VERSION,
            "core_composition_summary": str(payload.get("core_composition_summary") or "")[:800],
            "family_alignment": True,
            "taco_family_alignment": True,
            "family_evidence_method": row.get("family_evidence_method", "taco_tag_alignment"),
            "algorithm_scope": "multi",
        }
    except (ValueError, TypeError, KeyError) as exc:
        LOG.warning(
            "Pass2 multi label parse failed for %s %s: %s",
            row.get("problem_id"),
            row.get("solution_id"),
            exc,
        )
        return None


def run_pass2_multi(
    settings: Settings,
    *,
    resume: bool = False,
    budget: int = 0,
    retry_quarantine: bool = False,
) -> dict[str, Path]:
    p2 = cfg_section(settings, "pass2")
    budget = budget or int(p2.get("budget_solutions", 0) or 0)
    max_per_problem = int(p2.get("max_llm_solutions_per_problem", 3))
    max_retries = pass2_max_retries(p2, track="multi")
    base_max_tokens = pass2_base_max_tokens(p2, track="multi")
    token_ceiling = pass2_token_ceiling(p2, track="multi")
    input_limits = pass2_input_limits(p2, track="multi")
    jump_to_ceiling = pass2_truncation_jump_to_ceiling(p2)
    max_workers = max(1, int(p2.get("max_workers", 1)))
    LOG.info(
        "Pass2 multi LLM settings: max_tokens=%d ceiling=%d retries=%d stmt=%d code=%d",
        base_max_tokens,
        token_ceiling,
        max_retries,
        input_limits[0],
        input_limits[1],
    )

    solutions_in = settings.pass1_dir(TRACK) / "solutions.jsonl"
    if not solutions_in.exists():
        raise FileNotFoundError(solutions_in)

    out_dir = settings.pass2_dir(TRACK)
    out_dir.mkdir(parents=True, exist_ok=True)
    labeled_path = out_dir / "labeled_solutions.jsonl"
    quarantine_path = out_dir / "quarantine.jsonl"

    done_keys = load_pass2_resume_keys(out_dir, resume=resume, retry_quarantine=retry_quarantine)
    if resume:
        LOG.info(
            "Pass2 multi resume: skipping %d already-attempted solution keys "
            "(labeled + quarantine + rule_candidates if present)",
            len(done_keys),
        )

    client = build_factory_deepseek(settings)
    api_clients = int(getattr(client, "num_clients", 1))
    cache = DiskCache(settings.cache_dir / "llm_cache")
    system, user_tmpl = _load_prompt(settings)

    by_problem: dict[str, list[dict[str, Any]]] = {}
    for row in read_jsonl(solutions_in):
        by_problem.setdefault(str(row["problem_id"]), []).append(row)

    total_slots = count_planned_slots(by_problem, max_per_problem=max_per_problem)
    progress = Pass2Progress(track="multi", total_slots=total_slots, already_done=len(done_keys))
    LOG.info(
        "Pass2 multi progress: %d slots remaining (%d already attempted, %d total planned); workers=%d api_keys=%d",
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
            pending.append((pid, row))
        if stats["budget_stop"]:
            break

    def label_task(item: tuple[str, dict[str, Any]]) -> dict[str, Any] | None:
        pid, row = item
        sid = str(row.get("solution_id") or "")
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
                input_limits=input_limits,
                jump_to_ceiling=jump_to_ceiling,
            )
        except Exception as exc:
            LOG.warning(
                "Pass2 multi label unexpected error for %s %s: %s",
                pid,
                sid,
                exc,
            )
            return None

    def write_result(item: tuple[str, dict[str, Any]], labeled: dict[str, Any] | None) -> None:
        pid, row = item
        sid = str(row.get("solution_id") or "")
        if labeled is None:
            append_jsonl(quarantine_path, {**row, "quarantine_reason": "not_true_composition_or_llm_fail"})
            stats["quarantine"] += 1
            progress.log_item(
                problem_id=pid,
                solution_id=sid,
                status="quarantine",
                detail="not_true_composition_or_llm_fail",
            )
            return
        append_jsonl(labeled_path, labeled)
        stats["labeled"] += 1
        progress.log_item(
            problem_id=pid,
            solution_id=sid,
            status="ok",
            detail=f"composition={labeled.get('composition_key')}",
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
    return {"labeled": labeled_path, "quarantine": quarantine_path, "summary": summary_path}
