from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

from .filter_rows import filter_rows, generation_filter, hard_filter
from .group_rows import group_by_primary_subtype, summarize_groups
from .io_utils import load_jsonl, load_yaml, resolve_path, write_json, write_jsonl
from .report_builder import build_filtering_report, build_generation_report, build_grouping_report
from .schema import missing_row_fields
from .scoring import compute_quality_score
from .skill_generator import (
    build_evidence_map,
    generate_all_skills,
    prepare_generation_inputs,
)
from .skill_validator import validate_skill_schema


def _project_root(config_path: Path) -> Path:
    return config_path.resolve().parent.parent


def _load_dotenv(project_root: Path) -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    local_env = project_root / ".env"
    if local_env.exists():
        load_dotenv(local_env, override=True)
        return
    fallback = project_root.parent / "skill_data_factory" / ".env"
    if fallback.exists():
        load_dotenv(fallback, override=False)


def load_config(config_path: Path) -> dict[str, Any]:
    root = _project_root(config_path)
    _load_dotenv(root)
    config = load_yaml(config_path)
    config["_project_root"] = str(root)
    config["_config_path"] = str(config_path)

    for section in ("input", "output", "additional"):
        sec = config.get(section, {})
        for key, val in list(sec.items()):
            if isinstance(val, str) and (key.endswith("_path") or key.endswith("_dir")):
                sec[key] = str(resolve_path(root, val))
        config[section] = sec

    llm = config.get("llm", {})
    if "cache_dir" in llm:
        llm["cache_dir"] = str(resolve_path(root, llm["cache_dir"]))
    config["llm"] = llm
    return config


def _load_pipeline_data(config: dict[str, Any]) -> tuple[list[dict], list[dict], list[dict], dict]:
    input_path = config["input"]["distillation_path"]
    rows = load_jsonl(input_path)
    hard = filter_rows(rows, config, use_generation_filter=False)
    gen = filter_rows(rows, config, use_generation_filter=True)
    for r in hard:
        r["quality_score"] = compute_quality_score(r)
    for r in gen:
        r["quality_score"] = compute_quality_score(r)
    groups = group_by_primary_subtype(gen)
    return rows, hard, gen, groups


def merge_incremental_rows(
    existing_rows: list[dict[str, Any]],
    replacement_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    replacement_ids = {str(row.get("skill_id") or "") for row in replacement_rows}
    return [
        row for row in existing_rows if str(row.get("skill_id") or "") not in replacement_ids
    ] + replacement_rows


def merge_base_and_additional_banks(
    base_rows: list[dict[str, Any]],
    addition_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    canonical_ids = {str(row.get("skill_id") or "") for row in addition_rows}
    replaced_aliases = {
        str(alias)
        for row in addition_rows
        for alias in (row.get("alias_subtypes") or [])
    }
    return [
        row
        for row in base_rows
        if str(row.get("skill_id") or "") not in canonical_ids
        and str(row.get("primary_subtype") or "") not in replaced_aliases
    ] + addition_rows


def mode_inspect(config: dict[str, Any]) -> dict[str, Any]:
    rows, hard, gen, groups = _load_pipeline_data(config)
    missing = {}
    for row in rows[:50]:
        m = missing_row_fields(row)
        if m:
            missing[str(row.get("problem_id"))] = m

    report = {
        "input_file": config["input"]["distillation_path"],
        "total_rows": len(rows),
        "hard_filtered_rows": len(hard),
        "generation_filtered_rows": len(gen),
        **summarize_groups(groups, config),
        "sample_missing_fields": missing,
        "algorithm_family_distribution": {},
    }
    from collections import Counter

    report["algorithm_family_distribution"] = dict(
        Counter(str(r.get("detected_single_skill") or "") for r in gen)
    )
    print(f"Total rows: {len(rows)}")
    print(f"Hard filtered: {len(hard)}")
    print(f"Generation filtered: {len(gen)}")
    print(f"Subtypes (generation): {len(groups)}")
    print(f"Stable: {report['num_stable_subtypes']}, Provisional: {report['num_provisional_subtypes']}, Hold: {report['num_hold_subtypes']}")
    return report


def mode_prepare(config: dict[str, Any]) -> list[dict[str, Any]]:
    rows, hard, gen, groups = _load_pipeline_data(config)
    out_dir = Path(config["output"]["output_dir"])
    logs_dir = out_dir / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    write_json(logs_dir / "filtering_report.json", build_filtering_report(rows, hard, gen, config))
    write_json(logs_dir / "grouping_report.json", build_grouping_report(groups, config))

    gen_inputs = prepare_generation_inputs(groups, config)
    write_jsonl(config["output"]["generation_inputs_path"], gen_inputs)

    held = {
        st: summarize_groups({st: groups[st]}, config)["subtype_summary"][st]
        for st in groups
        if summarize_groups({st: groups[st]}, config)["subtype_summary"][st]["status"] == "hold"
    }
    write_json(config["output"]["rejected_path"], {"held_subtypes": held})

    print(f"Prepared {len(gen_inputs)} generation inputs (stable+provisional+seed)")
    print(f"Held subtypes: {len(held)}")
    return gen_inputs


def mode_generate(config: dict[str, Any], *, subtypes: list[str] | None = None) -> list[dict[str, Any]]:
    from .llm_client import build_llm_client, resolve_api_keys

    gen_path = Path(config["output"]["generation_inputs_path"])
    if gen_path.exists():
        gen_inputs = load_jsonl(gen_path)
    else:
        gen_inputs = mode_prepare(config)

    root = Path(config["_project_root"])
    keys = resolve_api_keys(config)
    max_workers = int(config.get("llm", {}).get("max_workers", 1))
    print(
        f"LLM keys={len(keys)}, max_workers={max_workers}, model={config.get('llm', {}).get('model')}",
        flush=True,
    )
    client = build_llm_client(config, project_root=root)
    skills = generate_all_skills(gen_inputs, client, config, subtypes=subtypes)

    accepted = [s for s in skills if (s.get("quality_control") or {}).get("final_decision") == "accept"]
    bank_rows = [{k: v for k, v in sk.items() if not k.startswith("_")} for sk in accepted]
    bank_path = Path(config["output"]["skill_bank_path"])
    if subtypes and bank_path.exists():
        existing = load_jsonl(bank_path)
        bank_rows = merge_incremental_rows(existing, bank_rows)
    write_jsonl(bank_path, bank_rows)

    merged_path = config["output"].get("merged_skill_bank_path")
    base_path = config["output"].get("base_skill_bank_path")
    if merged_path and base_path:
        base_rows = load_jsonl(base_path) if Path(base_path).exists() else []
        addition_rows = load_jsonl(bank_path)
        merged = merge_base_and_additional_banks(base_rows, addition_rows)
        write_jsonl(merged_path, merged)

    write_json(config["output"]["evidence_map_path"], build_evidence_map(gen_inputs))
    rows, hard, gen, groups = _load_pipeline_data(config)
    report = build_generation_report(
        input_file=config["input"]["distillation_path"],
        total_rows=len(rows),
        hard_filtered_rows=len(hard),
        generation_filtered_rows=len(gen),
        config=config,
        groups=groups,
        skills=skills,
    )
    if config.get("additional", {}).get("enabled", False):
        from .additional_evidence import algorithm_index, load_algorithm_catalog

        required = set(algorithm_index(load_algorithm_catalog(config)))
        accepted_subtypes = {str(row.get("primary_subtype") or "") for row in bank_rows}
        report["required_subtypes"] = sorted(required)
        report["missing_accepted_subtypes"] = sorted(required - accepted_subtypes)
        report["all_required_accepted"] = not report["missing_accepted_subtypes"]
    write_json(config["output"]["report_path"], report)
    print(f"Generated {len(skills)} skills; accepted {len(accepted)}")
    return skills


def mode_validate(config: dict[str, Any]) -> dict[str, Any]:
    bank_path = Path(config["output"]["skill_bank_path"])
    if not bank_path.exists():
        print("No skill bank found. Run --mode generate first.", file=sys.stderr)
        sys.exit(1)
    skills = load_jsonl(bank_path)
    results = []
    for sk in skills:
        ok, errs = validate_skill_schema(sk)
        results.append({"skill_id": sk.get("skill_id"), "valid": ok, "errors": errs})
    out = {"num_skills": len(skills), "results": results}
    if config.get("additional", {}).get("enabled", False):
        from .additional_evidence import algorithm_index, load_algorithm_catalog

        required = set(algorithm_index(load_algorithm_catalog(config)))
        found = {str(skill.get("primary_subtype") or "") for skill in skills}
        out["missing_required_subtypes"] = sorted(required - found)
        out["all_required_present"] = not out["missing_required_subtypes"]
    logs_dir = Path(config["output"]["output_dir"]) / "logs"
    write_json(logs_dir / "validation_report.json", out)
    print(f"Validated {len(skills)} skills; {sum(1 for r in results if r['valid'])} passed schema")
    return out


def mode_report(config: dict[str, Any]) -> dict[str, Any]:
    report_path = Path(config["output"]["report_path"])
    if report_path.exists():
        import json

        report = json.loads(report_path.read_text(encoding="utf-8"))
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return report
    return mode_inspect(config)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Single-algorithm skill generator")
    parser.add_argument(
        "--config",
        default="configs/upstream/base_generation.yaml",
        help="Path to config YAML",
    )
    parser.add_argument(
        "--mode",
        choices=["inspect", "prepare-evidence", "prepare", "generate", "validate", "report"],
        default="inspect",
    )
    parser.add_argument(
        "--subtypes",
        default="",
        help="Comma-separated primary_subtype list for generate mode (optional)",
    )
    parser.add_argument(
        "--skip-verified-labeling",
        action="store_true",
        help="Build additional evidence from validated curated examples only; do not call the LLM labeler.",
    )
    args = parser.parse_args(argv)

    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = Path(__file__).resolve().parent.parent / config_path
    config = load_config(config_path)
    subtypes = [s.strip() for s in args.subtypes.split(",") if s.strip()] or None

    if args.mode == "prepare-evidence":
        if not config.get("additional", {}).get("enabled", False):
            print("prepare-evidence requires an additional-skill config.", file=sys.stderr)
            sys.exit(1)
        from .additional_evidence import prepare_additional_evidence

        client = None
        if not args.skip_verified_labeling:
            from .llm_client import build_llm_client

            client = build_llm_client(config, project_root=Path(config["_project_root"]))
        rows = prepare_additional_evidence(
            config,
            llm_client=client,
            label_verified=not args.skip_verified_labeling,
            target_ids=set(subtypes) if subtypes else None,
        )
        print(f"Prepared {len(rows)} additional evidence rows")
        return

    input_path = Path(config["input"]["distillation_path"])
    if not input_path.exists():
        alt = Path(config["_project_root"]).parent / "skill_data_factory/outputs/single_algorithm/pass3_evidence/distillation_rows.jsonl"
        if alt.exists():
            config["input"]["distillation_path"] = str(alt)
        else:
            print(f"Input not found: {input_path}", file=sys.stderr)
            sys.exit(1)

    if args.mode == "inspect":
        mode_inspect(config)
    elif args.mode == "prepare":
        mode_prepare(config)
    elif args.mode == "generate":
        skills = mode_generate(config, subtypes=subtypes)
        if (
            not subtypes
            and config.get("additional", {}).get("enabled", False)
            and config.get("validation", {}).get("require_all_additional_skills", False)
        ):
            accepted = {
                str(skill.get("primary_subtype") or "")
                for skill in skills
                if (skill.get("quality_control") or {}).get("final_decision") == "accept"
            }
            from .additional_evidence import algorithm_index, load_algorithm_catalog

            required = set(algorithm_index(load_algorithm_catalog(config)))
            if required - accepted:
                sys.exit(2)
    elif args.mode == "validate":
        mode_validate(config)
    elif args.mode == "report":
        mode_report(config)


if __name__ == "__main__":
    main()
