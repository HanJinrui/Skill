from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from config import get_settings
from dataset_loader import list_clusters, load_dataset_manifest
from deepseek_client import ModelClientError, OpenAICompatibleClient, download_local_model
from hierarchy_generator import (
    generate_family,
    generate_hierarchy,
    generate_router,
    generate_subskill,
    write_manifests,
)
from packager import package_skill
from schema import SkillSpecValidationError
from selector import classify_family, classify_subtype, solve_with_selected_skill
from taco_importer import (
    format_composite_subtype_normalization_summary,
    format_import_summary,
    format_subtype_normalization_summary,
    import_taco_dataset,
    normalize_taco_composite_subtypes,
    normalize_taco_subtypes,
)
from validators import format_validation_errors, validate_hierarchy_outputs


def _print_progress(message: str) -> None:
    print(message, flush=True)


def cmd_generate_subskill(args: argparse.Namespace) -> int:
    settings = get_settings()
    manifest = load_dataset_manifest(settings.datasets_dir, settings.dataset_manifest_schema_path)
    spec = generate_subskill(
        settings,
        manifest,
        family_name=args.family,
        subtype_name=args.subtype,
        progress_callback=_print_progress,
    )
    write_manifests(settings, [spec] if spec.generation_decision.should_generate_skill else [], [], None)
    if not spec.generation_decision.should_generate_skill:
        print(f"Subskill generation skipped: {spec.generation_decision.reason}")
        return 0
    print(f"Generated subtype skill: {settings.generated_subskills_dir / spec.skill_name}")
    return 0


def cmd_generate_family(args: argparse.Namespace) -> int:
    settings = get_settings()
    manifest = load_dataset_manifest(settings.datasets_dir, settings.dataset_manifest_schema_path)
    clusters = list_clusters(manifest, family_name=args.family)
    if not clusters:
        raise ValueError(f"no dataset clusters found for family '{args.family}'")

    client = OpenAICompatibleClient(settings)
    subtype_specs = [
        generate_subskill(
            settings,
            manifest,
            cluster.family_name,
            cluster.subtype_name,
            client=client,
            progress_callback=_print_progress,
        )
        for cluster in clusters
    ]
    subtype_specs = [spec for spec in subtype_specs if spec.generation_decision.should_generate_skill]
    family_spec = generate_family(
        settings,
        args.family,
        subtype_specs,
        client=client,
        progress_callback=_print_progress,
    )
    if not family_spec.generation_decision.should_generate_skill:
        print(f"Family generation skipped: {family_spec.generation_decision.reason}")
        return 0
    write_manifests(settings, subtype_specs, [family_spec], None)
    print(f"Generated family skill: {settings.generated_families_dir / family_spec.skill_name}")
    return 0


def cmd_generate_router(args: argparse.Namespace) -> int:
    settings = get_settings()
    result = generate_hierarchy(settings, progress_callback=_print_progress)
    print(f"Generated router skill: {settings.generated_router_dir / result['router'].skill_name}")
    print(f"Generated {len(result['subskills'])} subtype skills and {len(result['families'])} family skills")
    return 0


def cmd_generate_hierarchy(args: argparse.Namespace) -> int:
    settings = get_settings()
    result = generate_hierarchy(settings, progress_callback=_print_progress)
    print(f"Hierarchy generated under: {settings.generated_dir}")
    print(
        f"Subskills: {len(result['subskills'])}, "
        f"families: {len(result['families'])}, router: 1"
    )
    return 0


def cmd_validate_hierarchy(args: argparse.Namespace) -> int:
    settings = get_settings()
    errors = validate_hierarchy_outputs(
        settings.generated_dir,
        settings.subtype_skill_schema_path,
        settings.family_skill_schema_path,
        settings.algorithm_router_schema_path,
    )
    if errors:
        print("Validation failed:")
        print(format_validation_errors(errors))
        return 1
    print(f"Hierarchy validation passed: {settings.generated_dir}")
    return 0


def cmd_package(args: argparse.Namespace) -> int:
    settings = get_settings()
    errors = validate_hierarchy_outputs(
        settings.generated_dir,
        settings.subtype_skill_schema_path,
        settings.family_skill_schema_path,
        settings.algorithm_router_schema_path,
    )
    if errors:
        raise RuntimeError("Cannot package invalid hierarchy:\n" + format_validation_errors(errors))
    output_zip = settings.generated_dir / "hierarchy.zip"
    package_skill(settings.generated_dir, output_zip)
    print(f"Packaged hierarchy zip: {output_zip}")
    return 0


def cmd_download_model(args: argparse.Namespace) -> int:
    settings = get_settings()
    destination = args.local_dir
    model_dir = download_local_model(settings, destination)
    print(f"Local model is ready at: {model_dir}")
    return 0


def cmd_import_taco(args: argparse.Namespace) -> int:
    settings = get_settings()
    output_root = args.output_root or settings.datasets_dir
    composite_output_root = None
    if args.assignment_mode == "quarantine-multi":
        composite_output_root = args.composite_output_root or settings.datasets_composite_dir
    summary = import_taco_dataset(
        input_path=args.input,
        output_root=output_root,
        split=args.split,
        assignment_mode=args.assignment_mode,
        composite_output_root=composite_output_root,
    )
    print(format_import_summary(summary))
    return 0


def cmd_normalize_taco_subtypes(args: argparse.Namespace) -> int:
    settings = get_settings()
    dataset_root = args.dataset_root or settings.datasets_dir
    summary = normalize_taco_subtypes(dataset_root=dataset_root, dry_run=args.dry_run)
    print(format_subtype_normalization_summary(summary))
    return 0


def cmd_normalize_taco_composite_subtypes(args: argparse.Namespace) -> int:
    settings = get_settings()
    dataset_root = args.dataset_root or settings.datasets_composite_dir
    summary = normalize_taco_composite_subtypes(dataset_root=dataset_root, dry_run=args.dry_run)
    print(format_composite_subtype_normalization_summary(summary))
    return 0


def cmd_classify_family(args: argparse.Namespace) -> int:
    settings = get_settings()
    problem_text = args.problem.read_text(encoding="utf-8")
    result = classify_family(problem_text, settings.generated_manifests_dir)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def cmd_classify_subtype(args: argparse.Namespace) -> int:
    settings = get_settings()
    problem_text = args.problem.read_text(encoding="utf-8")
    family_name = args.family
    if family_name is None:
        family_name = classify_family(problem_text, settings.generated_manifests_dir)["family_name"]
    result = classify_subtype(problem_text, settings.generated_manifests_dir, family_name)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def cmd_solve_with_selected_skill(args: argparse.Namespace) -> int:
    settings = get_settings()
    problem_text = args.problem.read_text(encoding="utf-8")
    skill_name = args.skill_name
    if not skill_name:
        family_result = classify_family(problem_text, settings.generated_manifests_dir)
        subtype_result = classify_subtype(
            problem_text,
            settings.generated_manifests_dir,
            str(family_result["family_name"]),
        )
        skill_name = str(subtype_result["skill_name"])
        if not skill_name:
            raise ValueError("no subtype skill could be selected for the provided problem")
    answer = solve_with_selected_skill(
        settings.generated_manifests_dir,
        skill_name=skill_name,
        problem_text=problem_text,
        emit_code=args.emit_code,
    )
    print(answer)
    return 0


def build_parser() -> argparse.ArgumentParser:
    settings = get_settings()
    parser = argparse.ArgumentParser(
        prog="algo-skill-factory",
        description="Generate hierarchical algorithm skill packages from clustered datasets.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate_subskill_parser = subparsers.add_parser(
        "generate-subskill",
        help="Generate a subtype skill from one labeled dataset cluster",
    )
    generate_subskill_parser.add_argument("--family", required=True)
    generate_subskill_parser.add_argument("--subtype", required=True)

    generate_family_parser = subparsers.add_parser(
        "generate-family",
        help="Generate a family routing skill from all generated subtype skills in one family",
    )
    generate_family_parser.add_argument("--family", default="dynamic_programming")

    subparsers.add_parser(
        "generate-router",
        help="Generate the top-level algorithm router, including required hierarchy dependencies",
    )
    subparsers.add_parser(
        "generate-hierarchy",
        help="Generate subtype skills, family skills, router, and manifests from datasets",
    )
    subparsers.add_parser(
        "validate-hierarchy",
        help="Validate generated hierarchy outputs and registries",
    )

    import_taco_parser = subparsers.add_parser(
        "import-taco",
        help="Import a local TACO json/jsonl export into datasets/<family>/<subtype>/<sample>/",
    )
    import_taco_parser.add_argument("--input", type=Path, required=True)
    import_taco_parser.add_argument("--split", default="train")
    import_taco_parser.add_argument("--output-root", type=Path)
    import_taco_parser.add_argument("--composite-output-root", type=Path)
    import_taco_parser.add_argument(
        "--assignment-mode",
        choices=("single-only", "quarantine-multi"),
        default="single-only",
    )

    normalize_taco_subtypes_parser = subparsers.add_parser(
        "normalize-taco-subtypes",
        help="Reassign TACO single-family samples in datasets/ to canonical subtype directories",
    )
    normalize_taco_subtypes_parser.add_argument("--dataset-root", type=Path)
    normalize_taco_subtypes_parser.add_argument("--dry-run", action="store_true")

    normalize_taco_composite_subtypes_parser = subparsers.add_parser(
        "normalize-taco-composite-subtypes",
        help="Reassign TACO multi-family samples in datasets_composite/ to canonical composite subtype directories",
    )
    normalize_taco_composite_subtypes_parser.add_argument("--dataset-root", type=Path)
    normalize_taco_composite_subtypes_parser.add_argument("--dry-run", action="store_true")

    classify_family_parser = subparsers.add_parser(
        "classify-family",
        help="Classify a new problem into the most likely algorithm family using local registries",
    )
    classify_family_parser.add_argument("--problem", type=Path, default=settings.inputs_dir / "problem.md")

    classify_subtype_parser = subparsers.add_parser(
        "classify-subtype",
        help="Classify a new problem into the most likely subtype within a family",
    )
    classify_subtype_parser.add_argument("--problem", type=Path, default=settings.inputs_dir / "problem.md")
    classify_subtype_parser.add_argument("--family")

    solve_parser = subparsers.add_parser(
        "solve-with-selected-skill",
        help="Use a generated subtype skill registry entry to output structured reasoning",
    )
    solve_parser.add_argument("--problem", type=Path, default=settings.inputs_dir / "problem.md")
    solve_parser.add_argument("--skill-name")
    solve_parser.add_argument("--emit-code", action="store_true")

    subparsers.add_parser("generate", help="Backward-compatible alias for generate-hierarchy")
    subparsers.add_parser("validate", help="Backward-compatible alias for validate-hierarchy")
    subparsers.add_parser("package", help="Package the generated hierarchy into generated/hierarchy.zip")

    download_model_parser = subparsers.add_parser(
        "download-model",
        help="Download the configured local Hugging Face model into a local directory",
    )
    download_model_parser.add_argument("--local-dir", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "generate-subskill":
            return cmd_generate_subskill(args)
        if args.command == "generate-family":
            return cmd_generate_family(args)
        if args.command == "generate-router":
            return cmd_generate_router(args)
        if args.command == "generate-hierarchy":
            return cmd_generate_hierarchy(args)
        if args.command == "validate-hierarchy":
            return cmd_validate_hierarchy(args)
        if args.command == "download-model":
            return cmd_download_model(args)
        if args.command == "import-taco":
            return cmd_import_taco(args)
        if args.command == "normalize-taco-subtypes":
            return cmd_normalize_taco_subtypes(args)
        if args.command == "normalize-taco-composite-subtypes":
            return cmd_normalize_taco_composite_subtypes(args)
        if args.command == "classify-family":
            return cmd_classify_family(args)
        if args.command == "classify-subtype":
            return cmd_classify_subtype(args)
        if args.command == "solve-with-selected-skill":
            return cmd_solve_with_selected_skill(args)
        if args.command == "generate":
            return cmd_generate_hierarchy(args)
        if args.command == "validate":
            return cmd_validate_hierarchy(args)
        if args.command == "package":
            return cmd_package(args)
    except (FileNotFoundError, ValueError, ModelClientError, RuntimeError, SkillSpecValidationError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 1


if __name__ == "__main__":
    raise SystemExit(main())


