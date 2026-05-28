"""Pass3 single track: build subtype evidence packets for Stage D."""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from sdf.io_utils import read_jsonl, save_json, write_jsonl
from sdf.factory_settings import Settings, cfg_section
from sdf.shared import bootstrap  # noqa: F401

from src.logging_utils import get_logger
from src.stage_d_skill_build import (
    _mechanism_bucket_key,
    _representative_examples,
    _split_subtype_rows_by_mechanism,
    _subtype_trigger_signals,
)

LOG = get_logger(__name__)
TRACK = "single_algorithm"


def _rank_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        rows,
        key=lambda r: (
            0 if str(r.get("evidence_tier")) == "gold" else 1 if str(r.get("evidence_tier")) == "silver" else 2,
            -float(r.get("primary_solution_score") or 0),
            -int(r.get("total_tests") or 0),
        ),
    )


def _excerpt_examples(rows: list[dict[str, Any]], *, max_n: int, stmt: int, code: int) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for row in rows[:max_n]:
        out.append(
            {
                "problem_id": row.get("problem_id"),
                "solution_id": row.get("solution_id"),
                "family": row.get("detected_single_skill"),
                "subtype": row.get("primary_subtype"),
                "reason": (row.get("subtype_rationale") or row.get("core_mechanism_summary") or "")[:260],
                "problem_excerpt": (row.get("problem_statement") or "")[:stmt],
                "solution_excerpt": (row.get("solution_code") or "")[:code],
                "confidence": row.get("subtype_confidence"),
                "tests": row.get("total_tests"),
                "evidence_tier": row.get("evidence_tier"),
            }
        )
    return out


def run_pass3_single(settings: Settings) -> dict[str, Path]:
    pri = cfg_section(settings, "pass2_primary")
    p3 = cfg_section(settings, "pass3")
    min_rows = int(pri.get("min_rows_per_subtype", 12))

    primary_path = settings.pass2_dir(TRACK) / "primary_solutions.jsonl"
    rows = [
        r for r in read_jsonl(primary_path)
        if str(r.get("evidence_tier")) in {"gold", "silver"}
    ]
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        st = str(row.get("primary_subtype") or "")
        if st:
            grouped[st].append(row)

    out_dir = settings.pass3_dir(TRACK)
    out_dir.mkdir(parents=True, exist_ok=True)
    packets_path = out_dir / "evidence_packets.jsonl"
    distillation_path = out_dir / "distillation_rows.jsonl"

    split_cfg = {
        "enabled": True,
        "min_cluster_rows": 6,
        "min_total_rows_to_split": 16,
    }
    max_ex = int(p3.get("max_examples_per_skill", 8))
    stmt = int(p3.get("max_statement_chars", 1000))
    code = int(p3.get("max_code_chars", 1100))

    packets: list[dict[str, Any]] = []
    for subtype, subtype_rows in sorted(grouped.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        if len(subtype_rows) < min_rows:
            continue
        family = str(subtype_rows[0].get("detected_single_skill") or "")
        clusters = _split_subtype_rows_by_mechanism(subtype_rows, **split_cfg)
        for idx, cluster_rows in enumerate(clusters):
            ranked = _rank_rows(cluster_rows)
            skill_id = (
                f"subtype__{family}__{subtype}"
                if len(clusters) == 1
                else f"subtype__{family}__{subtype}__c{idx}"
            )
            packet = {
                "skill_id": skill_id,
                "skill_level": "subtype",
                "family": family,
                "subtype": subtype,
                "algorithm_scope": "single",
                "num_source_examples": len(cluster_rows),
                "trigger_signals": _subtype_trigger_signals(subtype, family, cluster_rows),
                "representative_examples": _excerpt_examples(ranked, max_n=max_ex, stmt=stmt, code=code),
                "mechanism_bucket_hint": _mechanism_bucket_key(cluster_rows[0]) if cluster_rows else "",
                "source_track": TRACK,
            }
            packets.append(packet)

    write_jsonl(packets_path, packets)
    write_jsonl(distillation_path, rows)
    save_json(
        out_dir / "pass3_summary.json",
        {
            "track": TRACK,
            "primary_in": len(list(read_jsonl(primary_path))),
            "distillation_rows": len(rows),
            "evidence_packets": len(packets),
            "subtypes": len(grouped),
        },
    )
    LOG.info("Pass3 single: %d packets from %d primaries", len(packets), len(rows))
    return {"evidence_packets": packets_path, "distillation_rows": distillation_path}
