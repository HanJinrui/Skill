"""Merge TACO and CodeContests composition evidence with leakage protection."""
from __future__ import annotations

import glob
from collections import Counter
from pathlib import Path
from typing import Any

from sdf.codecontests_adapter import problem_fingerprint
from sdf.factory_settings import Settings, cfg_section
from sdf.io_utils import read_jsonl, save_json, write_jsonl


def _resolve(settings: Settings, raw: str) -> Path:
    path = Path(raw)
    if not path.is_absolute():
        path = settings.factory_root / path
    return path.resolve()


def _with_provenance(row: dict[str, Any], source_dataset: str) -> dict[str, Any]:
    out = dict(row)
    out["source_dataset"] = str(out.get("source_dataset") or source_dataset)
    out["verification_source"] = str(
        out.get("verification_source")
        or ("taco-verified" if source_dataset == "TACO" else "codecontests-local")
    )
    out["source_problem_fingerprint"] = str(
        out.get("source_problem_fingerprint")
        or problem_fingerprint(str(out.get("problem_statement") or ""))
    )
    return out


def _evaluation_fingerprints(settings: Settings, pattern: str) -> tuple[set[str], list[str]]:
    path = Path(pattern)
    glob_path = str(path if path.is_absolute() else settings.factory_root / path)
    files = sorted(glob.glob(glob_path))
    fingerprints: set[str] = set()
    for filename in files:
        for row in read_jsonl(Path(filename)):
            statement = str(row.get("problem_statement") or "")
            if statement:
                fingerprints.add(problem_fingerprint(statement))
    return fingerprints, files


def merge_composition_ledgers(settings: Settings) -> dict[str, Path]:
    config = cfg_section(settings, "merge")
    taco_path = _resolve(
        settings,
        str(config.get("taco_composition_path", "outputs/multi_algorithm/pass3_evidence/composition_rows.jsonl")),
    )
    code_path = _resolve(
        settings,
        str(
            config.get(
                "codecontests_composition_path",
                "outputs/codecontests/multi_algorithm/pass3_evidence/composition_rows.jsonl",
            )
        ),
    )
    output_dir = _resolve(
        settings,
        str(config.get("output_dir", "outputs/merged_multi_algorithm/pass3_evidence")),
    )
    eval_pattern = str(config.get("eval_manifest_glob", "../rag_experiment/outputs/eval_manifests/*.jsonl"))
    if not taco_path.exists():
        raise FileNotFoundError(taco_path)
    if not code_path.exists():
        raise FileNotFoundError(code_path)

    taco_rows = [_with_provenance(row, "TACO") for row in read_jsonl(taco_path)]
    code_rows = [_with_provenance(row, "CodeContests") for row in read_jsonl(code_path)]
    taco_fingerprints = {row["source_problem_fingerprint"] for row in taco_rows}
    eval_fingerprints, eval_files = _evaluation_fingerprints(settings, eval_pattern)
    accepted: list[dict[str, Any]] = list(taco_rows)
    excluded: list[dict[str, Any]] = []
    code_seen: set[str] = set()
    excluded_reasons: Counter[str] = Counter()

    for row in code_rows:
        fingerprint = row["source_problem_fingerprint"]
        reason = ""
        if fingerprint in eval_fingerprints:
            reason = "evaluation_manifest_leakage"
        elif fingerprint in taco_fingerprints:
            reason = "duplicate_of_taco_evidence"
        elif fingerprint in code_seen:
            reason = "duplicate_within_codecontests"
        if reason:
            excluded_reasons[reason] += 1
            excluded.append({**row, "exclusion_reason": reason})
            continue
        code_seen.add(fingerprint)
        accepted.append(row)

    dataset_counts = Counter(str(row.get("source_dataset") or "") for row in accepted)
    language_counts = Counter(str(row.get("source_language") or "") for row in accepted if row.get("source_language"))
    signature_counts = Counter(
        " -> ".join(row.get("composition_order") or row.get("primary_composition_subtypes") or [])
        for row in accepted
    )
    code_pass1_summary_path = config.get("codecontests_pass1_summary")
    code_pass1_summary: dict[str, Any] = {}
    if code_pass1_summary_path:
        path = _resolve(settings, str(code_pass1_summary_path))
        if path.exists():
            import json

            code_pass1_summary = json.loads(path.read_text(encoding="utf-8"))
    code_pass1_stats = code_pass1_summary.get("stats", {})

    output_dir.mkdir(parents=True, exist_ok=True)
    merged_path = output_dir / "composition_rows.jsonl"
    excluded_path = output_dir / "excluded_codecontests_rows.jsonl"
    report_path = output_dir / "merge_report.json"
    write_jsonl(merged_path, accepted)
    write_jsonl(excluded_path, excluded)
    save_json(
        report_path,
        {
            "inputs": {"taco": str(taco_path), "codecontests": str(code_path)},
            "evaluation_manifests": eval_files,
            "input_rows": {"TACO": len(taco_rows), "CodeContests": len(code_rows)},
            "accepted_rows": len(accepted),
            "accepted_source_dataset_counts": dict(dataset_counts),
            "accepted_source_language_counts": dict(language_counts),
            "excluded_codecontests_rows": len(excluded),
            "excluded_reason_counts": dict(excluded_reasons),
            "composition_signature_count": len(signature_counts),
            "top_composition_signatures": dict(signature_counts.most_common(30)),
            "codecontests_pass1_stats": code_pass1_stats,
            "codecontests_full_pass_solution_language_counts": code_pass1_stats.get(
                "full_pass_solution_language_counts", {}
            ),
            "codecontests_verification_failure_reasons": code_pass1_stats.get("failure_reasons", {}),
        },
    )
    return {
        "composition_rows": merged_path,
        "excluded_rows": excluded_path,
        "report": report_path,
    }
