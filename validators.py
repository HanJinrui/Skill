from __future__ import annotations

from pathlib import Path
from typing import Iterable
import json

import yaml

from schema import (
    AlgorithmRouterSpec,
    BaseGeneratedSpec,
    FAMILY_REQUIRED_FILE_PATHS,
    FamilySkillSpec,
    ROUTER_REQUIRED_FILE_PATHS,
    SUBTYPE_REQUIRED_FILE_PATHS,
    FileSpec,
    SubtypeSkillSpec,
    validate_algorithm_router_payload,
    validate_family_skill_payload,
    validate_subtype_skill_payload,
)


def validate_subtype_skill_spec(spec: SubtypeSkillSpec) -> None:
    errors = validate_spec_file_bundle(spec)
    if errors:
        raise ValueError("Generated subtype skill spec failed validation:\n" + format_validation_errors(errors))


def validate_family_skill_spec(spec: FamilySkillSpec) -> None:
    errors = validate_spec_file_bundle(spec)
    if errors:
        raise ValueError("Generated family skill spec failed validation:\n" + format_validation_errors(errors))


def validate_algorithm_router_spec(spec: AlgorithmRouterSpec) -> None:
    errors = validate_spec_file_bundle(spec)
    if errors:
        raise ValueError("Generated router spec failed validation:\n" + format_validation_errors(errors))


def validate_spec_file_bundle(spec: BaseGeneratedSpec) -> list[str]:
    if not spec.generation_decision.should_generate_skill:
        return []

    _normalize_spec_auxiliary_files(spec)

    errors: list[str] = []
    expected_paths = spec.required_file_paths
    paths = [file.path for file in spec.files]
    if set(paths) != set(expected_paths) or len(paths) != len(expected_paths):
        errors.append("generated files must contain exactly: " + ", ".join(expected_paths))

    files_by_path = {file.path: file.content for file in spec.files}
    skill_md_content = files_by_path.get("SKILL.md")
    if skill_md_content is None:
        errors.append("missing required file: SKILL.md")
    else:
        errors.extend(
            _validate_skill_frontmatter_content(
                skill_md_content,
                expected_name=spec.identity_name,
                expected_description=spec.description,
            )
        )

    openai_yaml_content = files_by_path.get("agents/openai.yaml")
    if openai_yaml_content is None:
        errors.append("missing required file: agents/openai.yaml")
    else:
        errors.extend(_validate_openai_yaml_content(openai_yaml_content))

    return errors


def validate_generated_spec_dir(
    artifact_dir: Path,
    required_file_paths: list[str],
    expected_name: str | None = None,
    expected_description: str | None = None,
) -> list[str]:
    errors: list[str] = []
    if not artifact_dir.exists():
        return [f"generated artifact directory not found: {artifact_dir}"]

    actual_files = sorted(
        str(path.relative_to(artifact_dir)).replace("\\", "/")
        for path in artifact_dir.rglob("*")
        if path.is_file()
    )
    if actual_files != sorted(required_file_paths):
        errors.append(
            "generated artifact directory must contain exactly these files: "
            + ", ".join(required_file_paths)
        )

    skill_md_path = artifact_dir / "SKILL.md"
    if skill_md_path.exists():
        errors.extend(
            _validate_skill_frontmatter_content(
                skill_md_path.read_text(encoding="utf-8"),
                expected_name=expected_name,
                expected_description=expected_description,
            )
        )
    else:
        errors.append("missing required file: SKILL.md")

    refs_dir = artifact_dir / "references"
    if not refs_dir.exists() or not refs_dir.is_dir():
        errors.append("missing references directory")

    openai_yaml = artifact_dir / "agents" / "openai.yaml"
    if openai_yaml.exists():
        errors.extend(_validate_openai_yaml_content(openai_yaml.read_text(encoding="utf-8")))
    else:
        errors.append("missing required file: agents/openai.yaml")

    return errors


def validate_hierarchy_outputs(
    generated_dir: Path,
    subtype_schema_path: Path,
    family_schema_path: Path,
    router_schema_path: Path,
) -> list[str]:
    errors: list[str] = []
    manifests_dir = generated_dir / "manifests"
    subtype_registry_path = manifests_dir / "subtype_registry.json"
    family_registry_path = manifests_dir / "family_registry.json"
    router_manifest_path = manifests_dir / "router.json"

    for manifest_path in (subtype_registry_path, family_registry_path, router_manifest_path):
        if not manifest_path.exists():
            errors.append(f"missing manifest: {manifest_path.name}")

    if errors:
        return errors

    subtype_registry = json.loads(subtype_registry_path.read_text(encoding="utf-8"))
    family_registry = json.loads(family_registry_path.read_text(encoding="utf-8"))
    router_manifest = json.loads(router_manifest_path.read_text(encoding="utf-8"))

    for entry in subtype_registry.get("subskills", []):
        try:
            spec = validate_subtype_skill_payload(entry["raw_spec"], subtype_schema_path)
        except ValueError as exc:
            errors.append(f"invalid subtype registry entry '{entry.get('skill_name', 'unknown')}': {exc}")
            continue
        errors.extend(
            validate_generated_spec_dir(
                generated_dir / entry["output_dir"],
                SUBTYPE_REQUIRED_FILE_PATHS,
                expected_name=spec.identity_name,
                expected_description=spec.description,
            )
        )

    for entry in family_registry.get("families", []):
        try:
            spec = validate_family_skill_payload(entry["raw_spec"], family_schema_path)
        except ValueError as exc:
            errors.append(f"invalid family registry entry '{entry.get('skill_name', 'unknown')}': {exc}")
            continue
        errors.extend(
            validate_generated_spec_dir(
                generated_dir / entry["output_dir"],
                FAMILY_REQUIRED_FILE_PATHS,
                expected_name=spec.identity_name,
                expected_description=spec.description,
            )
        )

    router_entry = router_manifest.get("router")
    if not isinstance(router_entry, dict):
        errors.append("router manifest missing 'router'")
        return errors

    try:
        router_spec = validate_algorithm_router_payload(router_entry["raw_spec"], router_schema_path)
    except ValueError as exc:
        errors.append(f"invalid router registry entry: {exc}")
        return errors

    errors.extend(
        validate_generated_spec_dir(
            generated_dir / router_entry["output_dir"],
            ROUTER_REQUIRED_FILE_PATHS,
            expected_name=router_spec.identity_name,
            expected_description=router_spec.description,
        )
    )

    generated_subskill_names = {entry["skill_name"] for entry in subtype_registry.get("subskills", [])}
    for family_entry in family_registry.get("families", []):
        for subtype_entry in family_entry.get("subtype_registry", []):
            if subtype_entry["skill_name"] not in generated_subskill_names:
                errors.append(
                    f"family '{family_entry['skill_name']}' references missing subtype '{subtype_entry['skill_name']}'"
                )

    generated_family_names = {entry["family_name"] for entry in family_registry.get("families", [])}
    for supported_family in router_entry["raw_spec"].get("supported_families", []):
        family_name = supported_family["family_name"]
        if family_name not in generated_family_names:
            errors.append(f"router references {family_name} but no generated family skill was found")

    return errors


def _validate_skill_frontmatter_content(
    content: str,
    expected_name: str | None = None,
    expected_description: str | None = None,
) -> list[str]:
    if not content.startswith("---"):
        return ["SKILL.md must begin with YAML frontmatter"]

    parts = content.split("---", 2)
    if len(parts) < 3:
        return ["SKILL.md frontmatter is not closed properly"]

    try:
        frontmatter = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        return [f"SKILL.md frontmatter YAML is invalid: {exc}"]

    if not isinstance(frontmatter, dict):
        return ["SKILL.md frontmatter must be a YAML object"]

    errors = []
    if set(frontmatter.keys()) != {"name", "description"}:
        errors.append("SKILL.md frontmatter must contain only 'name' and 'description'")

    for key in ("name", "description"):
        value = frontmatter.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"SKILL.md frontmatter missing '{key}'")

    if expected_name is not None and frontmatter.get("name") != expected_name:
        errors.append("SKILL.md frontmatter 'name' must exactly match the top-level identity field")

    if expected_description is not None and frontmatter.get("description") != expected_description:
        errors.append("SKILL.md frontmatter 'description' must exactly match top-level description")

    return errors


def _validate_openai_yaml_content(content: str) -> list[str]:
    try:
        payload = yaml.safe_load(content) or {}
    except yaml.YAMLError as exc:
        return [f"agents/openai.yaml is invalid YAML: {exc}"]

    if not isinstance(payload, dict):
        payload = {}

    interface = payload.get("interface")
    if not isinstance(interface, dict):
        interface = {
            "display_name": payload.get("display_name", payload.get("displayName")),
            "short_description": payload.get("short_description", payload.get("shortDescription")),
        }

    if not isinstance(interface, dict):
        return ["agents/openai.yaml missing 'interface' mapping"]

    errors = []
    for key in ("display_name", "short_description"):
        value = interface.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"agents/openai.yaml missing 'interface.{key}'")
    return errors


def _normalize_spec_auxiliary_files(spec: BaseGeneratedSpec) -> None:
    for index, file in enumerate(spec.files):
        if file.path != "agents/openai.yaml":
            continue
        normalized_content = _normalize_openai_yaml_content(file.content, spec.identity_name, spec.description)
        if normalized_content != file.content:
            spec.files[index] = FileSpec(path=file.path, content=normalized_content)


def _normalize_openai_yaml_content(content: str, identity_name: str, description: str) -> str:
    try:
        payload = yaml.safe_load(content) or {}
    except yaml.YAMLError:
        payload = {}

    if not isinstance(payload, dict):
        payload = {}

    interface = payload.get("interface")
    if isinstance(interface, dict):
        display_name = interface.get("display_name", interface.get("displayName"))
        short_description = interface.get("short_description", interface.get("shortDescription"))
    else:
        display_name = payload.get("display_name", payload.get("displayName"))
        short_description = payload.get("short_description", payload.get("shortDescription"))

    if not isinstance(display_name, str) or not display_name.strip():
        display_name = _humanize_identifier(identity_name)
    if not isinstance(short_description, str) or not short_description.strip():
        short_description = description

    normalized_payload = {
        "interface": {
            "display_name": display_name.strip(),
            "short_description": short_description.strip(),
        }
    }
    return yaml.safe_dump(normalized_payload, sort_keys=False, allow_unicode=True).strip()


def _humanize_identifier(value: str) -> str:
    parts = [part for part in value.replace("_", "-").split("-") if part]
    return " ".join(part.capitalize() for part in parts) or value


def format_validation_errors(errors: Iterable[str]) -> str:
    return "\n".join(f"- {error}" for error in errors)
