"""Pass3 multi track: build bundle/composition evidence packets for Stage D."""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from sdf.io_utils import read_jsonl, save_json, write_jsonl
from sdf.factory_settings import Settings, cfg_section
from sdf.shared import bootstrap  # noqa: F401

from src.logging_utils import get_logger

LOG = get_logger(__name__)
TRACK = "multi_algorithm"


def _excerpt_examples(rows: list[dict[str, Any]], *, max_n: int, stmt: int, code: int) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for row in rows[:max_n]:
        out.append(
            {
                "problem_id": row.get("problem_id"),
                "solution_id": row.get("solution_id"),
                "composition_key": row.get("composition_key"),
                "composition_subtypes": row.get("composition_subtypes"),
                "composition_order": row.get("composition_order"),
                "reason": (row.get("core_composition_summary") or "")[:260],
                "problem_excerpt": (row.get("problem_statement") or "")[:stmt],
                "solution_excerpt": (row.get("solution_code") or "")[:code],
                "confidence": row.get("subtype_confidence"),
                "tests": row.get("total_tests"),
                "evidence_tier": row.get("evidence_tier"),
            }
        )
    return out


def run_pass3_multi(settings: Settings) -> dict[str, Path]:
    pri = cfg_section(settings, "pass2_primary")
    p3 = cfg_section(settings, "pass3")
    min_rows = int(pri.get("min_rows_per_composition_key", 8))

    primary_path = settings.pass2_dir(TRACK) / "primary_solutions.jsonl"
    rows = [
        r for r in read_jsonl(primary_path)
        if str(r.get("evidence_tier")) in {"gold", "silver"}
    ]
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        key = str(row.get("composition_key") or "")
        if key:
            grouped[key].append(row)

    out_dir = settings.pass3_dir(TRACK)
    out_dir.mkdir(parents=True, exist_ok=True)
    packets_path = out_dir / "composition_evidence_packets.jsonl"
    distillation_path = out_dir / "composition_rows.jsonl"

    max_ex = int(p3.get("max_examples_per_skill", 8))
    stmt = int(p3.get("max_statement_chars", 1000))
    code = int(p3.get("max_code_chars", 1100))

    packets: list[dict[str, Any]] = []
    for comp_key, key_rows in sorted(grouped.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        if len(key_rows) < min_rows:
            continue
        families = sorted({f for r in key_rows for f in (r.get("composition_families") or [])})
        if not families and key_rows:
            families = list(key_rows[0].get("problem_families") or [])
        skill_id = "bundle__" + comp_key.replace("+", "__")
        ranked = sorted(key_rows, key=lambda r: -float(r.get("primary_solution_score") or 0))
        packets.append(
            {
                "skill_id": skill_id,
                "skill_level": "bundle",
                "families": families,
                "composition_key": comp_key,
                "algorithm_scope": "multi",
                "num_source_examples": len(key_rows),
                "trigger_signals": [
                    f"Problem requires coordinated use of: {', '.join(families)}.",
                    f"Composition pattern: {comp_key}.",
                ],
                "representative_examples": _excerpt_examples(ranked, max_n=max_ex, stmt=stmt, code=code),
                "observed_composition_subtypes": key_rows[0].get("composition_subtypes"),
                "source_track": TRACK,
            }
        )

    write_jsonl(packets_path, packets)
    write_jsonl(distillation_path, rows)
    save_json(
        out_dir / "pass3_summary.json",
        {"track": TRACK, "packets": len(packets), "rows": len(rows), "composition_keys": len(grouped)},
    )
    return {"evidence_packets": packets_path, "composition_rows": distillation_path}
