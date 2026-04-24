from __future__ import annotations

from pathlib import Path
import json
import shutil
from time import perf_counter
from typing import Any, Callable

from config import Settings
from dataset_loader import DatasetManifest, get_cluster, list_clusters, load_dataset_manifest
from deepseek_client import OpenAICompatibleClient
from prompt_builder import build_prompt
from schema import (
    SUPPORTED_FAMILIES,
    AlgorithmRouterSpec,
    FamilySkillSpec,
    SkillSpecValidationError,
    SubtypeSkillSpec,
    canonicalize_family_name,
    ensure_supported_family_name,
    load_json_schema,
    validate_algorithm_router_payload,
    validate_family_skill_payload,
    validate_subtype_skill_payload,
)
from skill_renderer import SkillRenderer
from validators import (
    format_validation_errors,
    validate_algorithm_router_spec,
    validate_family_skill_spec,
    validate_generated_spec_dir,
    validate_subtype_skill_spec,
)

ProgressCallback = Callable[[str], None]


def _request_and_validate_payload(
    settings: Settings,
    client: OpenAICompatibleClient,
    prompt: str,
    schema_path: Path,
    validator: Callable[[dict[str, Any], Path], Any],
    label: str,
    progress_callback: ProgressCallback | None = None,
) -> Any:
    repair_prompt = prompt
    for attempt in range(1, settings.llm_validation_retries + 2):
        payload = client.generate_skill_payload(repair_prompt)
        try:
            return validator(payload, schema_path)
        except SkillSpecValidationError as exc:
            if attempt > settings.llm_validation_retries:
                raise
            _emit_progress(
                progress_callback,
                f"[{label}] schema validation failed on attempt {attempt}; requesting repaired json",
            )
            repair_prompt = _build_schema_repair_prompt(prompt, payload, str(exc))
    raise RuntimeError(f"[{label}] unreachable validation retry state")


def _build_schema_repair_prompt(original_prompt: str, payload: dict[str, Any], validation_error: str) -> str:
    return (
        f"{original_prompt}\n\n"
        "[PREVIOUS_INVALID_JSON]\n"
        f"{json.dumps(payload, ensure_ascii=False, indent=2)}\n\n"
        "[VALIDATION_ERRORS]\n"
        f"{validation_error}\n\n"
        "Repair the previous JSON so it satisfies the schema exactly.\n"
        "You must address every validation error.\n"
        "Return valid json only.\n"
        "Do not use markdown code fences.\n"
        "Do not explain your changes."
    )


def generate_subskill(
    settings: Settings,
    manifest: DatasetManifest,
    family_name: str,
    subtype_name: str,
    client: OpenAICompatibleClient | None = None,
    progress_callback: ProgressCallback | None = None,
) -> SubtypeSkillSpec:
    family_name = ensure_supported_family_name(family_name)

    cluster = get_cluster(manifest, family_name, subtype_name)
    if cluster.sample_count < 2:
        raise ValueError(
            f"subtype cluster '{family_name}/{subtype_name}' requires at least 2 samples, got {cluster.sample_count}"
        )

    _emit_progress(
        progress_callback,
        f"[subskill] preparing cluster {family_name}/{subtype_name} with {cluster.sample_count} samples",
    )
    client = client or OpenAICompatibleClient(settings)
    schema = load_json_schema(settings.subtype_skill_schema_path)
    prompt = build_prompt(
        prompt_template_path=settings.prompt_template_path,
        target_kind="subtype_skill",
        output_schema_name=settings.subtype_skill_schema_path.name,
        output_schema=schema,
        cluster_metadata=cluster.to_metadata(manifest.dataset_name),
        samples=[sample.to_prompt_dict() for sample in cluster.samples],
        child_specs=[],
    )
    _emit_progress(progress_callback, f"[subskill] requesting model output for {subtype_name}")
    request_started = perf_counter()
    spec = _request_and_validate_payload(
        settings,
        client,
        prompt,
        settings.subtype_skill_schema_path,
        validate_subtype_skill_payload,
        label=f"subskill:{subtype_name}",
        progress_callback=progress_callback,
    )
    _emit_progress(
        progress_callback,
        f"[subskill] model response received for {subtype_name} in {perf_counter() - request_started:.1f}s",
    )
    validate_subtype_skill_spec(spec)
    output_dir = settings.generated_subskills_dir / spec.skill_name
    if not spec.generation_decision.should_generate_skill:
        if output_dir.exists():
            shutil.rmtree(output_dir)
        _emit_progress(
            progress_callback,
            f"[subskill] skipped {subtype_name}: {spec.generation_decision.reason}",
        )
        return spec
    if spec.generation_decision.should_generate_skill:
        _rewrite_output_dir(output_dir)
        SkillRenderer(settings.templates_dir).render_to_directory(spec, output_dir)
        errors = validate_generated_spec_dir(
            output_dir,
            spec.required_file_paths,
            expected_name=spec.identity_name,
            expected_description=spec.description,
        )
        if errors:
            shutil.rmtree(output_dir, ignore_errors=True)
            raise RuntimeError(
                f"Generated subskill '{spec.skill_name}' failed validation:\n"
                + format_validation_errors(errors)
            )
        _emit_progress(
            progress_callback,
            f"[subskill] wrote {spec.skill_name} to {output_dir}",
        )
    return spec


def generate_family(
    settings: Settings,
    family_name: str,
    subtype_specs: list[SubtypeSkillSpec],
    client: OpenAICompatibleClient | None = None,
    progress_callback: ProgressCallback | None = None,
) -> FamilySkillSpec:
    if not subtype_specs:
        raise ValueError("cannot generate a family skill without at least one subtype skill spec")
    family_name = ensure_supported_family_name(family_name)
    mismatched_families = {spec.algorithm_family for spec in subtype_specs if spec.algorithm_family != family_name}
    if mismatched_families:
        raise ValueError(
            f"cannot generate family '{family_name}' from subtype specs belonging to: {', '.join(sorted(mismatched_families))}"
        )

    _emit_progress(
        progress_callback,
        f"[family] preparing {family_name} generation from {len(subtype_specs)} subtype specs",
    )
    client = client or OpenAICompatibleClient(settings)
    schema = load_json_schema(settings.family_skill_schema_path)
    prompt = build_prompt(
        prompt_template_path=settings.prompt_template_path,
        target_kind="family_skill",
        output_schema_name=settings.family_skill_schema_path.name,
        output_schema=schema,
        cluster_metadata={
            "algorithm_family_hint": family_name,
            "dataset_name": "datasets",
            "sample_count": len(subtype_specs),
            "known_neighbors": [family for family in SUPPORTED_FAMILIES if family != family_name],
            "notes": [
                f"family skill should route within {family_name} rather than solve directly",
                "child specs are reusable subtype skills extracted from multiple samples",
            ],
        },
        samples=[],
        child_specs=[spec.raw_payload for spec in subtype_specs],
    )
    _emit_progress(progress_callback, f"[family] requesting model output for {family_name}")
    request_started = perf_counter()
    spec = _request_and_validate_payload(
        settings,
        client,
        prompt,
        settings.family_skill_schema_path,
        validate_family_skill_payload,
        label=f"family:{family_name}",
        progress_callback=progress_callback,
    )
    _emit_progress(
        progress_callback,
        f"[family] model response received in {perf_counter() - request_started:.1f}s",
    )
    validate_family_skill_spec(spec)
    output_dir = settings.generated_families_dir / spec.skill_name
    if not spec.generation_decision.should_generate_skill:
        if output_dir.exists():
            shutil.rmtree(output_dir)
        _emit_progress(
            progress_callback,
            f"[family] skipped {family_name}: {spec.generation_decision.reason}",
        )
        return spec
    if spec.generation_decision.should_generate_skill:
        _rewrite_output_dir(output_dir)
        SkillRenderer(settings.templates_dir).render_to_directory(spec, output_dir)
        errors = validate_generated_spec_dir(
            output_dir,
            spec.required_file_paths,
            expected_name=spec.identity_name,
            expected_description=spec.description,
        )
        if errors:
            shutil.rmtree(output_dir, ignore_errors=True)
            raise RuntimeError(
                f"Generated family skill '{spec.skill_name}' failed validation:\n"
                + format_validation_errors(errors)
            )
        _emit_progress(
            progress_callback,
            f"[family] wrote {spec.skill_name} to {output_dir}",
        )
    return spec


def generate_router(
    settings: Settings,
    family_specs: list[FamilySkillSpec],
    client: OpenAICompatibleClient | None = None,
    progress_callback: ProgressCallback | None = None,
) -> AlgorithmRouterSpec:
    if not family_specs:
        raise ValueError("cannot generate an algorithm router without at least one family skill spec")

    _emit_progress(
        progress_callback,
        f"[router] preparing router generation from {len(family_specs)} family specs",
    )
    client = client or OpenAICompatibleClient(settings)
    schema = load_json_schema(settings.algorithm_router_schema_path)
    prompt = build_prompt(
        prompt_template_path=settings.prompt_template_path,
        target_kind="algorithm_router",
        output_schema_name=settings.algorithm_router_schema_path.name,
        output_schema=schema,
        cluster_metadata={
            "dataset_name": "datasets",
            "supported_families": SUPPORTED_FAMILIES,
            "generated_family_count": len(family_specs),
            "notes": [
                "family skills are generated from labeled dataset clusters",
                "router should compare only the generated families and preserve ambiguity when evidence is weak",
            ],
        },
        samples=[],
        child_specs=[spec.raw_payload for spec in family_specs],
    )
    _emit_progress(progress_callback, "[router] requesting model output for algorithm router")
    request_started = perf_counter()
    spec = _request_and_validate_payload(
        settings,
        client,
        prompt,
        settings.algorithm_router_schema_path,
        validate_algorithm_router_payload,
        label="router",
        progress_callback=progress_callback,
    )
    _emit_progress(
        progress_callback,
        f"[router] model response received in {perf_counter() - request_started:.1f}s",
    )
    validate_algorithm_router_spec(spec)
    output_dir = settings.generated_router_dir / spec.skill_name
    if not spec.generation_decision.should_generate_skill:
        if output_dir.exists():
            shutil.rmtree(output_dir)
        _emit_progress(
            progress_callback,
            f"[router] skipped {spec.skill_name}: {spec.generation_decision.reason}",
        )
        return spec
    if spec.generation_decision.should_generate_skill:
        _rewrite_output_dir(output_dir)
        SkillRenderer(settings.templates_dir).render_to_directory(spec, output_dir)
        errors = validate_generated_spec_dir(
            output_dir,
            spec.required_file_paths,
            expected_name=spec.identity_name,
            expected_description=spec.description,
        )
        if errors:
            shutil.rmtree(output_dir, ignore_errors=True)
            raise RuntimeError(
                f"Generated router '{spec.skill_name}' failed validation:\n"
                + format_validation_errors(errors)
            )
        _emit_progress(
            progress_callback,
            f"[router] wrote {spec.skill_name} to {output_dir}",
        )
    return spec


def generate_hierarchy(
    settings: Settings,
    client: OpenAICompatibleClient | None = None,
    progress_callback: ProgressCallback | None = None,
) -> dict[str, Any]:
    _emit_progress(progress_callback, f"[start] loading datasets from {settings.datasets_dir}")
    manifest = load_dataset_manifest(settings.datasets_dir, settings.dataset_manifest_schema_path)
    all_clusters = list_clusters(manifest)
    if not all_clusters:
        raise ValueError("datasets must contain at least one subtype cluster")

    unsupported_families = sorted(
        {
            canonicalize_family_name(cluster.family_name)
            for cluster in all_clusters
            if canonicalize_family_name(cluster.family_name) not in SUPPORTED_FAMILIES
        }
    )
    if unsupported_families:
        raise SkillSpecValidationError(
            "datasets contain unsupported family labels: " + ", ".join(unsupported_families)
        )

    family_clusters = {
        family_name: [cluster for cluster in all_clusters if cluster.family_name == family_name]
        for family_name in SUPPORTED_FAMILIES
        if any(cluster.family_name == family_name for cluster in all_clusters)
    }
    if not family_clusters:
        raise ValueError(
            "datasets must contain at least one subtype cluster for a supported family: "
            + ", ".join(SUPPORTED_FAMILIES)
        )

    _emit_progress(
        progress_callback,
        f"[start] found {len(all_clusters)} subtype clusters across {len(family_clusters)} families",
    )
    client = client or OpenAICompatibleClient(settings)
    settings.generated_dir.mkdir(parents=True, exist_ok=True)
    legacy_paths = (
        settings.generated_dir / "skill",
        settings.generated_dir / "skill.zip",
        settings.generated_dir / "hierarchy.zip",
    )
    for legacy_path in legacy_paths:
        if legacy_path.is_dir():
            shutil.rmtree(legacy_path)
        elif legacy_path.exists():
            legacy_path.unlink()
    _emit_progress(progress_callback, f"[start] preparing output directories under {settings.generated_dir}")
    for path in (
        settings.generated_subskills_dir,
        settings.generated_families_dir,
        settings.generated_router_dir,
        settings.generated_manifests_dir,
    ):
        if path.exists():
            shutil.rmtree(path)
        path.mkdir(parents=True, exist_ok=True)

    generated_subskills: list[SubtypeSkillSpec] = []
    skipped_subskills: list[dict[str, str]] = []
    generated_families: list[FamilySkillSpec] = []
    for family_name, clusters in family_clusters.items():
        _emit_progress(
            progress_callback,
            f"[progress] family {family_name}: {len(clusters)} subtype clusters",
        )
        family_subskills: list[SubtypeSkillSpec] = []
        for index, cluster in enumerate(clusters, start=1):
            _emit_progress(
                progress_callback,
                f"[progress] {family_name} subtype {index}/{len(clusters)}: {cluster.subtype_name}",
            )
            spec = generate_subskill(
                settings,
                manifest,
                cluster.family_name,
                cluster.subtype_name,
                client=client,
                progress_callback=progress_callback,
            )
            if spec.generation_decision.should_generate_skill:
                generated_subskills.append(spec)
                family_subskills.append(spec)
            else:
                skipped_subskills.append(
                    {
                        "family": family_name,
                        "subtype": cluster.subtype_name,
                        "reason": spec.generation_decision.reason,
                    }
                )
        if not family_subskills:
            _emit_progress(
                progress_callback,
                f"[family] no reusable subtype skills were generated for {family_name}; skipping family skill",
            )
            continue
        family_spec = generate_family(
            settings,
            family_name,
            family_subskills,
            client=client,
            progress_callback=progress_callback,
        )
        if not family_spec.generation_decision.should_generate_skill:
            _emit_progress(
                progress_callback,
                f"[family] skipped {family_name}: {family_spec.generation_decision.reason}",
            )
            continue
        generated_families.append(family_spec)

    if not generated_subskills:
        raise ValueError("no reusable subtype skill was generated from the provided datasets")
    if not generated_families:
        raise ValueError("no reusable family skill was generated from the provided datasets")

    router_spec = generate_router(
        settings,
        generated_families,
        client=client,
        progress_callback=progress_callback,
    )
    if not router_spec.generation_decision.should_generate_skill:
        raise ValueError(f"router generation refused: {router_spec.generation_decision.reason}")

    _emit_progress(progress_callback, "[manifests] writing subtype/family/router registries")
    write_manifests(settings, generated_subskills, generated_families, router_spec)
    _emit_progress(progress_callback, "[done] hierarchy generation completed")
    return {
        "manifest": manifest.raw_payload,
        "subskills": generated_subskills,
        "families": generated_families,
        "router": router_spec,
        "skipped_subskills": skipped_subskills,
    }


def write_manifests(
    settings: Settings,
    subtype_specs: list[SubtypeSkillSpec],
    family_specs: list[FamilySkillSpec],
    router_spec: AlgorithmRouterSpec | None,
) -> None:
    settings.generated_manifests_dir.mkdir(parents=True, exist_ok=True)

    subtype_registry = {
        "version": 1,
        "subskills": [
            {
                "skill_name": spec.skill_name,
                "algorithm_family": spec.algorithm_family,
                "subtype": spec.subtype,
                "description": spec.description,
                "output_dir": _relative_output_dir(
                    settings.generated_dir,
                    settings.generated_subskills_dir / spec.skill_name,
                ),
                "trigger_signals": spec.trigger_signals,
                "non_triggers": spec.non_triggers,
                "failure_modes": spec.failure_modes,
                "pattern_abstraction": {
                    "core_recognition": spec.pattern_abstraction.core_recognition,
                    "state_templates": spec.pattern_abstraction.state_templates,
                    "transition_templates": spec.pattern_abstraction.transition_templates,
                    "base_case_rules": spec.pattern_abstraction.base_case_rules,
                    "iteration_order_rules": spec.pattern_abstraction.iteration_order_rules,
                },
                "transfer_strategy": {
                    "mapping_steps": spec.transfer_strategy.mapping_steps,
                    "uncertainty_policy": spec.transfer_strategy.uncertainty_policy,
                },
                "output_contract": {
                    "sections": spec.output_contract.sections,
                    "default_language": spec.output_contract.default_language,
                    "emit_code_only_if_user_asks": spec.output_contract.emit_code_only_if_user_asks,
                },
                "taxonomy_notes": spec.taxonomy_notes,
                "transfer_checklist": spec.transfer_checklist,
                "raw_spec": spec.raw_payload,
            }
            for spec in subtype_specs
        ],
    }
    (settings.generated_manifests_dir / "subtype_registry.json").write_text(
        json.dumps(subtype_registry, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    family_registry = {
        "version": 1,
        "families": [
            {
                "family_name": spec.family_name,
                "skill_name": spec.skill_name,
                "description": spec.description,
                "output_dir": _relative_output_dir(
                    settings.generated_dir,
                    settings.generated_families_dir / spec.skill_name,
                ),
                "family_trigger_signals": spec.family_trigger_signals,
                "nearby_families": [
                    {
                        "family_name": entry.family_name,
                        "confusion_reason": entry.confusion_reason,
                    }
                    for entry in spec.nearby_families
                ],
                "subtype_registry": [
                    {
                        "subtype": entry.subtype,
                        "skill_name": entry.skill_name,
                        "short_description": entry.short_description,
                        "trigger_summary": entry.trigger_summary,
                    }
                    for entry in spec.subtype_registry
                ],
                "subtype_selection_rules": spec.subtype_selection_rules,
                "refusal_rules": spec.refusal_rules,
                "routing_strategy": {
                    "selection_steps": spec.routing_strategy.selection_steps,
                    "tie_breaking_rules": spec.routing_strategy.tie_breaking_rules,
                    "escalation_rules": spec.routing_strategy.escalation_rules,
                },
                "output_contract": {
                    "sections": spec.output_contract.sections,
                    "emit_code": spec.output_contract.emit_code,
                },
                "raw_spec": spec.raw_payload,
            }
            for spec in family_specs
        ],
    }
    (settings.generated_manifests_dir / "family_registry.json").write_text(
        json.dumps(family_registry, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    router_manifest_path = settings.generated_manifests_dir / "router.json"
    if router_spec is None:
        if router_manifest_path.exists():
            router_manifest_path.unlink()
        return

    router_manifest = {
        "version": 1,
        "router": {
            "skill_name": router_spec.skill_name,
            "description": router_spec.description,
            "output_dir": _relative_output_dir(
                settings.generated_dir,
                settings.generated_router_dir / router_spec.skill_name,
            ),
            "supported_families": [
                {
                    "family_name": entry.family_name,
                    "skill_name": entry.skill_name,
                    "short_description": entry.short_description,
                    "trigger_summary": entry.trigger_summary,
                }
                for entry in router_spec.supported_families
            ],
            "family_selection_rules": router_spec.family_selection_rules,
            "ambiguity_policy": router_spec.ambiguity_policy,
            "refusal_rules": router_spec.refusal_rules,
            "handoff_policy": {
                "after_family_selected": router_spec.handoff_policy.after_family_selected,
                "when_multiple_families_plausible": router_spec.handoff_policy.when_multiple_families_plausible,
                "when_no_family_matches": router_spec.handoff_policy.when_no_family_matches,
            },
            "output_contract": {
                "sections": router_spec.output_contract.sections,
                "emit_code": router_spec.output_contract.emit_code,
            },
            "raw_spec": router_spec.raw_payload,
        },
    }
    router_manifest_path.write_text(
        json.dumps(router_manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def _rewrite_output_dir(output_dir: Path) -> None:
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)


def _relative_output_dir(generated_root: Path, output_dir: Path) -> str:
    return str(output_dir.relative_to(generated_root)).replace("\\", "/")


def _emit_progress(progress_callback: ProgressCallback | None, message: str) -> None:
    if progress_callback is not None:
        progress_callback(message)

