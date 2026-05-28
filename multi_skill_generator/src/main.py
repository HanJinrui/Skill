from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from .filter_rows import filter_rows
from .group_compositions import group_by_composition_signature, summarize_composition_groups
from .io_utils import load_jsonl, load_yaml, resolve_path, write_json, write_jsonl
from .normalize_composition import normalize_row
from .repair_composition_order import repair_composition_orders
from .report_builder import (
    build_evidence_map,
    build_filtering_report,
    build_generation_report,
    build_grouping_report,
    build_normalization_report,
    build_relation_report,
)
from .scoring import compute_quality_score
from .skill_generator import (
    fill_program_owned_fields,
    generate_all_skills,
    prepare_generation_inputs,
    slim_source_row,
)
from .skill_normalizer import normalize_skill_for_cluster
from .skill_validator import validate_final_skill, validate_skill_schema

RELEASABLE_DECISIONS = {"accept", "provisional_review_required"}


def _project_root(config_path: Path) -> Path:
    return config_path.resolve().parent.parent


def _load_dotenv(project_root: Path) -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    for candidate in (
        project_root / ".env",
        project_root.parent / "single_skill_generator" / ".env",
        project_root.parent / "skill_data_factory" / ".env",
    ):
        if candidate.exists():
            load_dotenv(candidate, override=False)


def load_config(config_path: Path) -> dict[str, Any]:
    root = _project_root(config_path)
    _load_dotenv(root)
    config = load_yaml(config_path)
    config["_project_root"] = str(root)
    config["_config_path"] = str(config_path)

    for section in ("input", "output", "release"):
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


def _resolve_input_path(config: dict[str, Any]) -> str:
    input_path = Path(config["input"]["composition_path"])
    if input_path.exists():
        return str(input_path)
    if not config["input"].get("allow_legacy_taco_fallback", False):
        raise FileNotFoundError(f"Input not found: {input_path}")
    alt = (
        Path(config["_project_root"]).parent
        / "skill_data_factory/outputs/multi_algorithm/pass3_evidence/composition_rows.jsonl"
    )
    if alt.exists():
        return str(alt)
    raise FileNotFoundError(f"Input not found: {input_path}")


def _load_and_prepare(config: dict[str, Any]) -> tuple[list[dict], list[dict], list[dict], dict, list[dict], list[dict]]:
    input_path = _resolve_input_path(config)
    config["input"]["composition_path"] = input_path
    logs_dir = Path(config["output"]["output_dir"]) / "logs"
    bad_lines = logs_dir / "bad_json_lines.jsonl"

    rows = load_jsonl(input_path, bad_lines_path=bad_lines)
    filtered = filter_rows(rows, config)
    for r in filtered:
        r["quality_score"] = compute_quality_score(r)

    normalized_batch = [normalize_row(r) for r in filtered]
    valid_rows, manual_review = repair_composition_orders(normalized_batch, config)

    groups = group_by_composition_signature(valid_rows)
    return rows, filtered, valid_rows, groups, manual_review, []


def mode_inspect(config: dict[str, Any]) -> dict[str, Any]:
    rows, filtered, valid_rows, groups, manual_review, _ = _load_and_prepare(config)
    summary = summarize_composition_groups(groups, config)
    report = {
        "input_file": config["input"]["composition_path"],
        "total_rows": len(rows),
        "hard_filtered_rows": len(filtered),
        "valid_order_rows": len(valid_rows),
        "manual_review_rows": len(manual_review),
        **summary,
    }
    print(f"Total rows: {len(rows)}")
    print(f"Hard filtered: {len(filtered)}")
    print(f"Valid order rows: {len(valid_rows)}")
    print(f"Composition signatures: {summary['num_composition_signatures']}")
    print(
        f"Stable: {summary['num_stable']}, Provisional: {summary['num_provisional']}, "
        f"Classic: {summary['num_provisional_classic']}, Hold: {summary['num_hold']}"
    )
    return report


def mode_prepare(config: dict[str, Any]) -> list[dict[str, Any]]:
    rows, filtered, valid_rows, groups, manual_review, repaired_log = _load_and_prepare(config)
    out_dir = Path(config["output"]["output_dir"])
    logs_dir = out_dir / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    write_json(logs_dir / "filtering_report.json", build_filtering_report(rows, filtered, config))
    write_json(logs_dir / "normalization_report.json", build_normalization_report(valid_rows))
    write_json(logs_dir / "grouping_report.json", build_grouping_report(groups, config))

    gen_inputs = prepare_generation_inputs(groups, config)
    storage_inputs = [
        {
            **gi,
            "all_source_rows": [slim_source_row(r) for r in gi.get("all_source_rows") or []],
        }
        for gi in gen_inputs
    ]
    write_jsonl(config["output"]["generation_inputs_path"], storage_inputs)
    write_jsonl(config["output"]["manual_review_path"], manual_review)

    held = {
        sig: info
        for sig, info in summarize_composition_groups(groups, config)["group_summary"].items()
        if info["status"] == "hold"
    }
    write_json(config["output"]["rejected_path"], {"held_compositions": held})
    write_json(logs_dir / "relation_classification_report.json", build_relation_report(gen_inputs))

    print(f"Prepared {len(gen_inputs)} generation inputs")
    print(f"Manual review rows: {len(manual_review)}")
    print(f"Held composition patterns: {len(held)}")
    return gen_inputs


def mode_generate(config: dict[str, Any], *, signatures: list[str] | None = None) -> list[dict[str, Any]]:
    from .llm_client import build_llm_client

    gen_path = Path(config["output"]["generation_inputs_path"])
    if gen_path.exists():
        gen_inputs = load_jsonl(gen_path)
    else:
        gen_inputs = mode_prepare(config)

    if not config.get("llm", {}).get("enabled", True):
        print("LLM disabled in config.", file=sys.stderr)
        sys.exit(1)

    root = Path(config["_project_root"])
    client = build_llm_client(config, project_root=root)
    skills = generate_all_skills(gen_inputs, client, config, signatures=signatures)

    accepted = [s for s in skills if (s.get("quality_control") or {}).get("final_decision") == "accept"]
    review_required = [
        s
        for s in skills
        if (s.get("quality_control") or {}).get("final_decision") == "provisional_review_required"
    ]
    releasable = accepted + review_required
    bank_rows = [{k: v for k, v in sk.items() if not k.startswith("_")} for sk in releasable]
    write_jsonl(config["output"]["skill_bank_path"], bank_rows)
    write_json(config["output"]["evidence_map_path"], build_evidence_map(skills, gen_inputs))

    rows, filtered, valid_rows, groups, manual_review, _ = _load_and_prepare(config)
    report = build_generation_report(
        input_file=config["input"]["composition_path"],
        total_rows=len(rows),
        hard_filtered_rows=len(filtered),
        valid_order_rows=len(valid_rows),
        repaired_order_rows=sum(1 for r in valid_rows if r.get("order_repaired")),
        manual_review_rows=len(manual_review),
        config=config,
        groups=groups,
        generation_inputs=gen_inputs,
        skills=skills,
    )
    write_json(config["output"]["report_path"], report)
    print(
        f"Generated {len(skills)} skills; accepted {len(accepted)}; "
        f"provisional review required {len(review_required)}"
    )
    return skills


def mode_finalize(config: dict[str, Any]) -> list[dict[str, Any]]:
    """Rebuild program-owned metadata and decisions without another LLM request."""
    bank_path = Path(config["output"]["skill_bank_path"])
    if not bank_path.exists():
        print("No skill bank found. Run --mode generate first.", file=sys.stderr)
        sys.exit(1)
    drafts = load_jsonl(bank_path)
    draft_by_id = {str(skill.get("skill_id") or ""): skill for skill in drafts}
    gen_inputs = mode_prepare(config)
    active_ids = {str(gi.get("skill_id") or "") for gi in gen_inputs}

    final_skills: list[dict[str, Any]] = []
    validation_rows: list[dict[str, Any]] = []
    missing_drafts: list[str] = []
    for gen_input in gen_inputs:
        skill_id = str(gen_input.get("skill_id") or "")
        draft = draft_by_id.get(skill_id)
        if draft is None:
            missing_drafts.append(skill_id)
            continue
        skill = normalize_skill_for_cluster(draft, gen_input)
        skill = fill_program_owned_fields(skill, gen_input)
        validation = validate_final_skill(skill, gen_input, config)
        decision = validation["decision"]
        validation_rows.append(
            {"skill_id": skill_id, "decision": decision, "errors": validation["errors"]}
        )
        if decision in RELEASABLE_DECISIONS:
            final_skills.append(skill)

    rows, filtered, valid_rows, groups, manual_review, _ = _load_and_prepare(config)
    min_generation_rows = int(config.get("grouping", {}).get("min_rows_for_generation", 3))
    legacy_counts = Counter(
        tuple(row.get("composition_order") or row.get("primary_composition_subtypes") or [])
        for row in filtered
    )
    normalized_counts = Counter(
        tuple(normalize_row(row).get("composition_signature") or []) for row in filtered
    )
    split_below_threshold = {
        f"multi.{'__'.join(signature)}.v1"
        for signature, count in legacy_counts.items()
        if len(signature) >= 2
        and count >= min_generation_rows
        and normalized_counts.get(signature, 0) < min_generation_rows
    }
    removed_obsolete = sorted((set(draft_by_id) - active_ids) | split_below_threshold)
    write_jsonl(bank_path, final_skills)
    write_json(config["output"]["evidence_map_path"], build_evidence_map(final_skills, gen_inputs))
    generation_report = build_generation_report(
        input_file=config["input"]["composition_path"],
        total_rows=len(rows),
        hard_filtered_rows=len(filtered),
        valid_order_rows=len(valid_rows),
        repaired_order_rows=sum(1 for row in valid_rows if row.get("order_repaired")),
        manual_review_rows=len(manual_review),
        config=config,
        groups=groups,
        generation_inputs=gen_inputs,
        skills=final_skills,
    )
    generation_report["removed_obsolete_or_split_clusters"] = removed_obsolete
    generation_report["generation_inputs_without_published_draft"] = missing_drafts
    write_json(config["output"]["report_path"], generation_report)
    finalization_report = {
        "num_input_drafts": len(drafts),
        "num_active_generation_inputs": len(gen_inputs),
        "num_final_skills": len(final_skills),
        "accepted": sum(
            1
            for skill in final_skills
            if skill["quality_control"]["final_decision"] == "accept"
        ),
        "provisional_review_required": sum(
            1
            for skill in final_skills
            if skill["quality_control"]["final_decision"] == "provisional_review_required"
        ),
        "removed_obsolete_or_split_clusters": removed_obsolete,
        "generation_inputs_without_published_draft": missing_drafts,
        "validation_results": validation_rows,
    }
    write_json(Path(config["output"]["output_dir"]) / "logs" / "finalization_report.json", finalization_report)
    print(
        f"Finalized {len(final_skills)} skills from {len(drafts)} drafts; "
        f"removed obsolete/split clusters {len(removed_obsolete)}"
    )
    return final_skills


def mode_validate(config: dict[str, Any]) -> dict[str, Any]:
    bank_path = Path(config["output"]["skill_bank_path"])
    if not bank_path.exists():
        print("No skill bank found. Run --mode generate first.", file=sys.stderr)
        sys.exit(1)
    skills = load_jsonl(bank_path)
    generation_inputs = load_jsonl(config["output"]["generation_inputs_path"])
    inputs_by_id = {str(gi.get("skill_id") or ""): gi for gi in generation_inputs}
    results = []
    for sk in skills:
        generation_input = inputs_by_id.get(str(sk.get("skill_id") or ""))
        if generation_input:
            validation = validate_final_skill(sk, generation_input, config)
            results.append(
                {
                    "skill_id": sk.get("skill_id"),
                    "valid": validation["decision"] in RELEASABLE_DECISIONS,
                    "decision": validation["decision"],
                    "errors": validation["errors"],
                }
            )
        else:
            ok, errs = validate_skill_schema(sk)
            results.append(
                {"skill_id": sk.get("skill_id"), "valid": False, "decision": "reject", "errors": errs + ["no generation input"]}
            )
    out = {"num_skills": len(skills), "results": results}
    write_json(Path(config["output"]["output_dir"]) / "logs" / "validation_report.json", out)
    print(
        f"Validated {len(skills)} skills; "
        f"{sum(1 for r in results if r['valid'])} passed release validation"
    )
    return out


def mode_publish(config: dict[str, Any]) -> dict[str, Any]:
    """Publish a validated expanded bank only if it preserves the baseline."""
    release = config.get("release", {})
    candidate_path = Path(config["output"]["skill_bank_path"])
    baseline_path = Path(release["baseline_skill_bank_path"])
    publish_path = Path(release.get("publish_path", baseline_path))
    snapshot_path = Path(release["baseline_snapshot_path"])
    validation = mode_validate(config)
    candidate = load_jsonl(candidate_path)
    baseline = load_jsonl(baseline_path)
    candidate_ids = {str(row.get("skill_id") or "") for row in candidate}
    baseline_ids = {str(row.get("skill_id") or "") for row in baseline}
    missing_ids = sorted(baseline_ids - candidate_ids)
    validation_failed = [
        str(row.get("skill_id") or "")
        for row in validation["results"]
        if not row.get("valid")
    ]
    errors: list[str] = []
    if missing_ids:
        errors.append(f"candidate drops baseline skill ids: {missing_ids}")
    if len(candidate) <= len(baseline):
        errors.append(
            f"candidate skill count must grow beyond baseline: {len(candidate)} <= {len(baseline)}"
        )
    if validation_failed:
        errors.append(f"candidate has validation failures: {validation_failed}")
    report = {
        "baseline_skill_count": len(baseline),
        "candidate_skill_count": len(candidate),
        "missing_baseline_skill_ids": missing_ids,
        "validation_failed_skill_ids": validation_failed,
        "published": not errors,
        "errors": errors,
    }
    write_json(Path(config["output"]["output_dir"]) / "logs" / "publish_acceptance_report.json", report)
    if errors:
        raise RuntimeError("; ".join(errors))
    write_jsonl(snapshot_path, baseline)
    write_jsonl(publish_path, candidate)
    print(f"Published expanded skill bank with {len(candidate)} skills; baseline snapshot saved.")
    return report


def mode_report(config: dict[str, Any]) -> dict[str, Any]:
    report_path = Path(config["output"]["report_path"])
    if report_path.exists():
        import json

        report = json.loads(report_path.read_text(encoding="utf-8"))
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return report
    return mode_inspect(config)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Multi-algorithm composition skill generator")
    parser.add_argument("--config", default="configs/multi_skill_config.yaml")
    parser.add_argument(
        "--mode",
        choices=["inspect", "prepare", "generate", "finalize", "validate", "publish", "report"],
        default="inspect",
    )
    parser.add_argument(
        "--signatures",
        default="",
        help="Comma-separated composition signatures (arrow-separated) for generate mode",
    )
    args = parser.parse_args(argv)

    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = Path(__file__).resolve().parent.parent / config_path
    config = load_config(config_path)

    try:
        _resolve_input_path(config)
    except FileNotFoundError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)

    sigs = None
    if args.signatures.strip():
        sigs = [s.strip() for s in args.signatures.split(",") if s.strip()]

    if args.mode == "inspect":
        mode_inspect(config)
    elif args.mode == "prepare":
        mode_prepare(config)
    elif args.mode == "generate":
        mode_generate(config, signatures=sigs)
    elif args.mode == "finalize":
        mode_finalize(config)
    elif args.mode == "validate":
        mode_validate(config)
    elif args.mode == "publish":
        mode_publish(config)
    elif args.mode == "report":
        mode_report(config)


if __name__ == "__main__":
    main()
