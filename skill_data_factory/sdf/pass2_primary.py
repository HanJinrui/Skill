"""Pass2c: select primary solution per problem and apply quotas."""
from __future__ import annotations

import hashlib
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from sdf.io_utils import read_jsonl, save_json, write_jsonl
from sdf.factory_settings import Settings, cfg_section
from sdf.shared import bootstrap  # noqa: F401

from src.logging_utils import get_logger

LOG = get_logger(__name__)


def _statement_hash(text: str) -> str:
    return hashlib.md5((text or "")[:500].encode("utf-8")).hexdigest()[:12]


def _primary_score(row: dict[str, Any]) -> float:
    conf = float(row.get("subtype_confidence") or 0.0)
    tests = int(row.get("total_tests") or 0)
    align = 1.0 if row.get("family_alignment", row.get("taco_family_alignment", True)) else 0.0
    return align * (0.55 * conf + 0.45 * min(1.0, tests / 20.0))


def _select_primaries_single(
    rows: list[dict[str, Any]],
    *,
    max_per_subtype: int,
    min_confidence: float,
) -> list[dict[str, Any]]:
    by_problem: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if float(row.get("subtype_confidence") or 0) < min_confidence:
            continue
        by_problem[str(row["problem_id"])].append(row)

    best_per_problem: list[dict[str, Any]] = []
    for pid, prob_rows in by_problem.items():
        best = max(prob_rows, key=_primary_score)
        best = {**best, "is_primary_solution": True, "primary_solution_score": round(_primary_score(best), 4)}
        best_per_problem.append(best)

    by_subtype: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in best_per_problem:
        by_subtype[str(row.get("primary_subtype") or "")].append(row)

    selected: list[dict[str, Any]] = []
    for subtype, items in by_subtype.items():
        if not subtype:
            continue
        seen_hashes: set[str] = set()
        ranked = sorted(items, key=_primary_score, reverse=True)
        kept: list[dict[str, Any]] = []
        for row in ranked:
            h = _statement_hash(str(row.get("problem_statement") or ""))
            if h in seen_hashes and len(kept) >= 3:
                continue
            seen_hashes.add(h)
            kept.append(row)
            if len(kept) >= max_per_subtype:
                break
        selected.extend(kept)
    return selected


def _select_primaries_multi(
    rows: list[dict[str, Any]],
    *,
    max_per_key: int,
    min_confidence: float,
) -> list[dict[str, Any]]:
    by_problem: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if float(row.get("subtype_confidence") or 0) < min_confidence:
            continue
        by_problem[str(row["problem_id"])].append(row)

    best_per_problem: list[dict[str, Any]] = []
    for prob_rows in by_problem.values():
        best = max(prob_rows, key=_primary_score)
        best = {**best, "is_primary_solution": True, "primary_solution_score": round(_primary_score(best), 4)}
        best_per_problem.append(best)

    by_key: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in best_per_problem:
        by_key[str(row.get("composition_key") or "")].append(row)

    selected: list[dict[str, Any]] = []
    for key, items in by_key.items():
        if not key:
            continue
        ranked = sorted(items, key=_primary_score, reverse=True)[:max_per_key]
        selected.extend(ranked)
    return selected


def _assign_tier(row: dict[str, Any], p3: dict[str, Any]) -> str:
    tests = int(row.get("total_tests") or 0)
    conf = float(row.get("subtype_confidence") or 0.0)
    if tests >= int(p3.get("gold_min_tests", 10)) and conf >= float(p3.get("gold_min_confidence", 0.65)):
        return "gold"
    if tests >= int(p3.get("silver_min_tests", 5)):
        return "silver"
    return "bronze"


def run_pass2_primary(settings: Settings, track: str) -> dict[str, Path]:
    p2 = cfg_section(settings, "pass2")
    pri = cfg_section(settings, "pass2_primary")
    p3 = cfg_section(settings, "pass3")
    min_conf = float(p2.get("min_llm_confidence", 0.6))

    labeled_path = settings.pass2_dir(track) / "labeled_solutions.jsonl"
    if not labeled_path.exists():
        raise FileNotFoundError(labeled_path)

    rows = list(read_jsonl(labeled_path))
    if track == "single_algorithm":
        primaries = _select_primaries_single(
            rows,
            max_per_subtype=int(pri.get("max_rows_per_subtype", 200)),
            min_confidence=min_conf,
        )
        out_name = "distillation_rows.jsonl"
    else:
        primaries = _select_primaries_multi(
            rows,
            max_per_key=int(pri.get("max_rows_per_composition_key", 80)),
            min_confidence=min_conf,
        )
        out_name = "composition_rows.jsonl"

    for row in primaries:
        row["evidence_tier"] = _assign_tier(row, p3)

    out_dir = settings.pass2_dir(track)
    primary_path = out_dir / "primary_solutions.jsonl"
    write_jsonl(primary_path, primaries)

    subtype_counts = Counter(
        str(r.get("primary_subtype") or r.get("composition_key") or "") for r in primaries
    )
    tier_counts = Counter(str(r.get("evidence_tier") or "") for r in primaries)
    summary = {
        "track": track,
        "primary_count": len(primaries),
        "subtype_or_key_counts": dict(subtype_counts.most_common(40)),
        "tier_counts": dict(tier_counts),
    }
    save_json(out_dir / "primary_summary.json", summary)
    LOG.info("Pass2 primary %s: %d rows", track, len(primaries))
    return {"primary_solutions": primary_path, "rows_out": out_dir / out_name, "summary": out_dir / "primary_summary.json"}
