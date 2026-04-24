from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any
import json
import re

from jsonschema import Draft202012Validator
import yaml


SUPPORTED_FAMILIES = [
    "amortized_analysis",
    "bit_manipulation",
    "complete_search",
    "data_structures",
    "dynamic_programming",
    "greedy_algorithms",
    "range_queries",
    "sorting",
]

FAMILY_NAME_ALIASES = {
    "greedy": "greedy_algorithms",
    "greedy_algorithm": "greedy_algorithms",
    "range_query": "range_queries",
    "data_structure": "data_structures",
}

SUBTYPE_REQUIRED_FILE_PATHS = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/pattern-taxonomy.md",
    "references/output-format.md",
    "references/transfer-checklist.md",
]

FAMILY_REQUIRED_FILE_PATHS = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/family-taxonomy.md",
    "references/subtype-selection.md",
    "references/refusal-rules.md",
]

ROUTER_REQUIRED_FILE_PATHS = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/family-selection.md",
    "references/refusal-rules.md",
    "references/handoff-policy.md",
]


class SkillSpecValidationError(ValueError):
    pass


@dataclass(frozen=True)
class FileSpec:
    path: str
    content: str


@dataclass(frozen=True)
class GenerationDecision:
    should_generate_skill: bool
    confidence: float
    reason: str


@dataclass(frozen=True)
class PatternAbstraction:
    core_recognition: str
    state_templates: list[str]
    transition_templates: list[str]
    base_case_rules: list[str]
    iteration_order_rules: list[str]


@dataclass(frozen=True)
class TransferStrategy:
    mapping_steps: list[str]
    uncertainty_policy: list[str]


@dataclass(frozen=True)
class OutputContract:
    sections: list[str]
    default_language: str | None = None
    emit_code_only_if_user_asks: bool | None = None
    emit_code: bool | None = None


@dataclass(frozen=True)
class EvalExamples:
    positive: list[str]
    negative: list[str]


@dataclass(frozen=True)
class SubtypeRegistryEntry:
    subtype: str
    skill_name: str
    short_description: str
    trigger_summary: list[str]


@dataclass(frozen=True)
class NearbyFamilyEntry:
    family_name: str
    confusion_reason: str


@dataclass(frozen=True)
class SupportedFamilyEntry:
    family_name: str
    skill_name: str
    short_description: str
    trigger_summary: list[str]


@dataclass(frozen=True)
class RoutingStrategy:
    selection_steps: list[str]
    tie_breaking_rules: list[str]
    escalation_rules: list[str]


@dataclass(frozen=True)
class HandoffPolicy:
    after_family_selected: list[str]
    when_multiple_families_plausible: list[str]
    when_no_family_matches: list[str]


@dataclass(frozen=True)
class BaseGeneratedSpec:
    kind: str
    description: str
    generation_decision: GenerationDecision
    files: list[FileSpec]
    raw_payload: dict[str, Any]

    @property
    def identity_name(self) -> str:
        raise NotImplementedError

    @property
    def required_file_paths(self) -> list[str]:
        raise NotImplementedError


@dataclass(frozen=True)
class SubtypeSkillSpec(BaseGeneratedSpec):
    skill_name: str
    algorithm_family: str
    subtype: str
    trigger_signals: list[str]
    non_triggers: list[str]
    failure_modes: list[str]
    pattern_abstraction: PatternAbstraction
    transfer_strategy: TransferStrategy
    output_contract: OutputContract
    eval_examples: EvalExamples
    taxonomy_notes: list[str]
    transfer_checklist: list[str]

    @property
    def identity_name(self) -> str:
        return self.skill_name

    @property
    def required_file_paths(self) -> list[str]:
        return SUBTYPE_REQUIRED_FILE_PATHS


@dataclass(frozen=True)
class FamilySkillSpec(BaseGeneratedSpec):
    family_name: str
    skill_name: str
    family_trigger_signals: list[str]
    nearby_families: list[NearbyFamilyEntry]
    subtype_registry: list[SubtypeRegistryEntry]
    subtype_selection_rules: list[str]
    refusal_rules: list[str]
    routing_strategy: RoutingStrategy
    output_contract: OutputContract

    @property
    def identity_name(self) -> str:
        return self.skill_name

    @property
    def required_file_paths(self) -> list[str]:
        return FAMILY_REQUIRED_FILE_PATHS


@dataclass(frozen=True)
class AlgorithmRouterSpec(BaseGeneratedSpec):
    skill_name: str
    supported_families: list[SupportedFamilyEntry]
    family_selection_rules: list[str]
    ambiguity_policy: list[str]
    refusal_rules: list[str]
    handoff_policy: HandoffPolicy
    output_contract: OutputContract

    @property
    def identity_name(self) -> str:
        return self.skill_name

    @property
    def required_file_paths(self) -> list[str]:
        return ROUTER_REQUIRED_FILE_PATHS


def load_json_schema(schema_path: Path) -> dict[str, Any]:
    if not schema_path.exists():
        raise FileNotFoundError(f"schema file not found: {schema_path}")
    with schema_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_json_payload(payload: dict[str, Any], schema_path: Path, label: str) -> None:
    if not isinstance(payload, dict):
        raise SkillSpecValidationError(f"{label} must be a JSON object.")
    schema = load_json_schema(schema_path)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(payload), key=lambda error: list(error.absolute_path))
    if errors:
        raise SkillSpecValidationError(
            f"{label} failed JSON Schema validation:\n"
            + "\n".join(f"- {_format_jsonschema_error(error)}" for error in errors)
        )


def validate_subtype_skill_payload(payload: dict[str, Any], schema_path: Path) -> SubtypeSkillSpec:
    payload = _normalize_payload_before_schema(payload)
    validate_json_payload(payload, schema_path, "subtype skill spec")
    payload = _normalize_skill_markdown_payload(payload)
    payload = _normalize_openai_yaml_payload(payload)
    spec = _build_subtype_skill_spec(payload)
    _validate_base_generation_decision(spec)
    _validate_required_files(spec)
    _validate_frontmatter_against_top_level(spec)
    return spec


def validate_family_skill_payload(payload: dict[str, Any], schema_path: Path) -> FamilySkillSpec:
    payload = _normalize_payload_before_schema(payload)
    validate_json_payload(payload, schema_path, "family skill spec")
    payload = _normalize_skill_markdown_payload(payload)
    payload = _normalize_openai_yaml_payload(payload)
    spec = _build_family_skill_spec(payload)
    _validate_base_generation_decision(spec)
    _validate_required_files(spec)
    _validate_frontmatter_against_top_level(spec)
    return spec


def validate_algorithm_router_payload(payload: dict[str, Any], schema_path: Path) -> AlgorithmRouterSpec:
    payload = _normalize_payload_before_schema(payload)
    validate_json_payload(payload, schema_path, "algorithm router spec")
    payload = _normalize_skill_markdown_payload(payload)
    payload = _normalize_openai_yaml_payload(payload)
    spec = _build_algorithm_router_spec(payload)
    _validate_base_generation_decision(spec)
    _validate_required_files(spec)
    _validate_frontmatter_against_top_level(spec)
    return spec


def _build_subtype_skill_spec(payload: dict[str, Any]) -> SubtypeSkillSpec:
    return SubtypeSkillSpec(
        kind=payload["kind"],
        skill_name=payload["skill_name"],
        description=payload["description"],
        algorithm_family=payload["algorithm_family"],
        subtype=payload["subtype"],
        generation_decision=GenerationDecision(**payload["generation_decision"]),
        trigger_signals=list(payload["trigger_signals"]),
        non_triggers=list(payload["non_triggers"]),
        failure_modes=list(payload["failure_modes"]),
        pattern_abstraction=PatternAbstraction(**payload["pattern_abstraction"]),
        transfer_strategy=TransferStrategy(**payload["transfer_strategy"]),
        output_contract=OutputContract(**payload["output_contract"]),
        eval_examples=EvalExamples(**payload["eval_examples"]),
        taxonomy_notes=list(payload["taxonomy_notes"]),
        transfer_checklist=list(payload["transfer_checklist"]),
        files=[FileSpec(**file_payload) for file_payload in payload["files"]],
        raw_payload=payload,
    )


def _build_family_skill_spec(payload: dict[str, Any]) -> FamilySkillSpec:
    return FamilySkillSpec(
        kind=payload["kind"],
        family_name=payload["family_name"],
        skill_name=payload["skill_name"],
        description=payload["description"],
        generation_decision=GenerationDecision(**payload["generation_decision"]),
        family_trigger_signals=list(payload["family_trigger_signals"]),
        nearby_families=[
            NearbyFamilyEntry(**entry_payload)
            for entry_payload in payload["nearby_families"]
        ],
        subtype_registry=[
            SubtypeRegistryEntry(**entry_payload)
            for entry_payload in payload["subtype_registry"]
        ],
        subtype_selection_rules=list(payload["subtype_selection_rules"]),
        refusal_rules=list(payload["refusal_rules"]),
        routing_strategy=RoutingStrategy(**payload["routing_strategy"]),
        output_contract=OutputContract(**payload["output_contract"]),
        files=[FileSpec(**file_payload) for file_payload in payload["files"]],
        raw_payload=payload,
    )


def _build_algorithm_router_spec(payload: dict[str, Any]) -> AlgorithmRouterSpec:
    return AlgorithmRouterSpec(
        kind=payload["kind"],
        skill_name=payload["skill_name"],
        description=payload["description"],
        generation_decision=GenerationDecision(**payload["generation_decision"]),
        supported_families=[
            SupportedFamilyEntry(**entry_payload)
            for entry_payload in payload["supported_families"]
        ],
        family_selection_rules=list(payload["family_selection_rules"]),
        ambiguity_policy=list(payload["ambiguity_policy"]),
        refusal_rules=list(payload["refusal_rules"]),
        handoff_policy=HandoffPolicy(**payload["handoff_policy"]),
        output_contract=OutputContract(**payload["output_contract"]),
        files=[FileSpec(**file_payload) for file_payload in payload["files"]],
        raw_payload=payload,
    )


def _validate_base_generation_decision(spec: BaseGeneratedSpec) -> None:
    if not spec.generation_decision.should_generate_skill:
        if spec.files:
            raise SkillSpecValidationError(
                "generation_decision.should_generate_skill is false, so files must be []."
            )


def _validate_required_files(spec: BaseGeneratedSpec) -> None:
    if not spec.generation_decision.should_generate_skill:
        return

    paths = [file.path for file in spec.files]
    if len(paths) != len(spec.required_file_paths):
        raise SkillSpecValidationError(
            f"Expected exactly {len(spec.required_file_paths)} files for {spec.kind}, got {len(paths)}."
        )
    if set(paths) != set(spec.required_file_paths):
        raise SkillSpecValidationError(
            f"{spec.kind} files must contain exactly these paths: {', '.join(spec.required_file_paths)}"
        )
    if len(set(paths)) != len(paths):
        raise SkillSpecValidationError(f"{spec.kind} files contain duplicate paths.")


def _validate_frontmatter_against_top_level(spec: BaseGeneratedSpec) -> None:
    if not spec.generation_decision.should_generate_skill:
        return

    skill_file = next((file for file in spec.files if file.path == "SKILL.md"), None)
    if skill_file is None:
        raise SkillSpecValidationError("SKILL.md is required when generating skill files.")

    content = skill_file.content
    if not content.startswith("---"):
        raise SkillSpecValidationError("SKILL.md must begin with YAML frontmatter.")

    parts = content.split("---", 2)
    if len(parts) < 3:
        raise SkillSpecValidationError("SKILL.md frontmatter is not closed properly.")

    try:
        frontmatter = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        raise SkillSpecValidationError(f"SKILL.md frontmatter YAML is invalid: {exc}") from exc

    if not isinstance(frontmatter, dict):
        raise SkillSpecValidationError("SKILL.md frontmatter must be a YAML object.")

    if set(frontmatter.keys()) != {"name", "description"}:
        raise SkillSpecValidationError(
            "SKILL.md frontmatter must contain only 'name' and 'description'."
        )

    if frontmatter["name"] != spec.identity_name:
        raise SkillSpecValidationError(
            "SKILL.md frontmatter 'name' must exactly match the top-level identity field."
        )

    if frontmatter["description"] != spec.description:
        raise SkillSpecValidationError(
            "SKILL.md frontmatter 'description' must exactly match top-level description."
        )


def _normalize_payload_before_schema(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        return payload

    changed = False
    normalized_payload = dict(payload)

    description = payload.get("description")
    if isinstance(description, str):
        normalized_description = description.strip().lower()
        if normalized_description != description:
            normalized_payload["description"] = normalized_description
            changed = True

    eval_examples = payload.get("eval_examples")
    if isinstance(eval_examples, dict):
        normalized_eval_examples = dict(eval_examples)
        eval_examples_changed = False
        for key in ("positive", "negative"):
            examples = eval_examples.get(key)
            if isinstance(examples, list) and len(examples) > 2:
                normalized_eval_examples[key] = examples[:2]
                eval_examples_changed = True
        if eval_examples_changed:
            normalized_payload["eval_examples"] = normalized_eval_examples
            changed = True

    return normalized_payload if changed else payload


def _normalize_skill_markdown_payload(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        return payload

    files = payload.get("files")
    skill_name = payload.get("skill_name")
    description = payload.get("description")
    if not isinstance(files, list) or not isinstance(skill_name, str) or not isinstance(description, str):
        return payload

    normalized_files: list[dict[str, Any]] = []
    changed = False
    for file_payload in files:
        if not isinstance(file_payload, dict) or file_payload.get("path") != "SKILL.md":
            normalized_files.append(file_payload)
            continue

        content = file_payload.get("content")
        normalized_content = _normalize_skill_markdown_content(content, skill_name, description)
        if normalized_content != content:
            changed = True
            updated_file = dict(file_payload)
            updated_file["content"] = normalized_content
            normalized_files.append(updated_file)
        else:
            normalized_files.append(file_payload)

    if not changed:
        return payload

    normalized_payload = dict(payload)
    normalized_payload["files"] = normalized_files
    return normalized_payload


def _normalize_openai_yaml_payload(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        return payload

    files = payload.get("files")
    if not isinstance(files, list):
        return payload

    identity_name = payload.get("skill_name") or payload.get("family_name")
    description = payload.get("description")
    if not isinstance(identity_name, str) or not isinstance(description, str):
        return payload

    normalized_files: list[dict[str, Any]] = []
    changed = False
    for file_payload in files:
        if not isinstance(file_payload, dict) or file_payload.get("path") != "agents/openai.yaml":
            normalized_files.append(file_payload)
            continue

        content = file_payload.get("content")
        normalized_content = _normalize_openai_yaml_content(content, identity_name, description)
        if normalized_content != content:
            changed = True
            updated_file = dict(file_payload)
            updated_file["content"] = normalized_content
            normalized_files.append(updated_file)
        else:
            normalized_files.append(file_payload)

    if not changed:
        return payload

    normalized_payload = dict(payload)
    normalized_payload["files"] = normalized_files
    return normalized_payload


def _normalize_skill_markdown_content(content: Any, skill_name: str, description: str) -> Any:
    if not isinstance(content, str) or not content.startswith("---"):
        return content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return content

    try:
        frontmatter = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return content

    if not isinstance(frontmatter, dict):
        return content

    frontmatter_name = frontmatter.get("name")
    frontmatter_description = frontmatter.get("description")
    normalized_name = frontmatter_name if isinstance(frontmatter_name, str) and frontmatter_name.strip() else skill_name
    normalized_description = (
        frontmatter_description
        if isinstance(frontmatter_description, str) and frontmatter_description.strip()
        else description
    )

    has_extra_keys = not (set(frontmatter.keys()) <= {"name", "description"})
    description_matches_case_insensitively = normalized_description.strip().lower() == description.strip().lower()

    if normalized_name == skill_name:
        normalized_name = skill_name
    if description_matches_case_insensitively:
        normalized_description = description

    if (
        not has_extra_keys
        and isinstance(frontmatter_name, str)
        and isinstance(frontmatter_description, str)
        and frontmatter_name == normalized_name
        and frontmatter_description == normalized_description
    ):
        return content

    if (
        not has_extra_keys
        and isinstance(frontmatter_name, str)
        and frontmatter_name != skill_name
        and isinstance(frontmatter_description, str)
        and not description_matches_case_insensitively
    ):
        return content

    body = parts[2].lstrip("\r\n")
    normalized_frontmatter = yaml.safe_dump(
        {
            "name": normalized_name,
            "description": normalized_description,
        },
        sort_keys=False,
        allow_unicode=True,
    ).strip()
    return f"---\n{normalized_frontmatter}\n---\n\n{body}"


def _normalize_openai_yaml_content(content: Any, identity_name: str, description: str) -> Any:
    if not isinstance(content, str):
        return content

    try:
        payload = yaml.safe_load(content) or {}
    except yaml.YAMLError:
        payload = {}

    if not isinstance(payload, dict):
        payload = {}

    interface = payload.get("interface")
    top_level_display = payload.get("display_name")
    top_level_short = payload.get("short_description")
    if isinstance(interface, dict):
        display_name = interface.get("display_name", top_level_display)
        short_description = interface.get("short_description", top_level_short)
    else:
        display_name = top_level_display
        short_description = top_level_short

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


def canonicalize_family_name(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")
    normalized = FAMILY_NAME_ALIASES.get(normalized, normalized)
    return normalized


def ensure_supported_family_name(value: str) -> str:
    family_name = canonicalize_family_name(value)
    if family_name not in SUPPORTED_FAMILIES:
        raise SkillSpecValidationError(
            f"unsupported family '{value}'; expected one of: {', '.join(SUPPORTED_FAMILIES)}"
        )
    return family_name


def _format_jsonschema_error(error: Any) -> str:
    if not error.absolute_path:
        return f"$: {error.message}"
    location = "$"
    for part in error.absolute_path:
        if isinstance(part, int):
            location += f"[{part}]"
        else:
            location += f".{part}"
    return f"{location}: {error.message}"


# Backward-compatible aliases.
SkillSpec = SubtypeSkillSpec
validate_skill_payload = validate_subtype_skill_payload
REQUIRED_FILE_PATHS = SUBTYPE_REQUIRED_FILE_PATHS
