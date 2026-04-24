from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import ast
import json
import re
from typing import Any, Iterable

from schema import SUPPORTED_FAMILIES, canonicalize_family_name
from taco_taxonomy import (
    build_canonical_composite_subtype,
    build_canonical_single_family_subtype,
    build_family_combo_name,
    normalize_taco_tags,
)


ASSIGNMENT_MODES = {"quarantine-multi", "single-only"}
SKIP_REASON_ORDER = (
    "missing_question",
    "missing_solution",
    "no_supported_family",
    "multiple_supported_families",
)
NORMALIZATION_SKIP_REASON_ORDER = (
    "missing_metadata",
    "non_taco_sample",
    "non_single_family_sample",
)
COMPOSITE_NORMALIZATION_SKIP_REASON_ORDER = (
    "missing_metadata",
    "non_taco_sample",
    "non_multi_family_sample",
)
CANONICAL_SUBTYPE_STRATEGY = "canonical_family_tag_rules_v1"
CANONICAL_COMPOSITE_SUBTYPE_STRATEGY = "canonical_composite_tag_rules_v1"


@dataclass(frozen=True)
class TacoImportSummary:
    dataset_name: str
    split: str
    output_root: Path
    composite_output_root: Path | None
    records_read: int
    single_family_records: int
    multi_family_records: int
    single_family_records_written: int
    composite_records_written: int
    skipped_records: int
    skipped_reasons: dict[str, int]
    family_counts: dict[str, int]
    composite_family_combo_counts: dict[str, int]
    subtype_counts: dict[str, int]
    composite_subtype_counts: dict[str, int]


@dataclass(frozen=True)
class TacoSubtypeNormalizationSummary:
    dataset_root: Path
    dry_run: bool
    eligible_records: int
    moved_records: int
    rewritten_metadata_records: int
    skipped_records: int
    skipped_reasons: dict[str, int]
    unique_subtypes_before: int
    unique_subtypes_after: int
    family_sample_counts: dict[str, int]
    family_subtypes_before: dict[str, int]
    family_subtypes_after: dict[str, int]
    top_subtypes_after: dict[str, int]


@dataclass(frozen=True)
class TacoCompositeSubtypeNormalizationSummary:
    dataset_root: Path
    dry_run: bool
    eligible_records: int
    moved_records: int
    rewritten_metadata_records: int
    skipped_records: int
    skipped_reasons: dict[str, int]
    unique_subtypes_before: int
    unique_subtypes_after: int
    combo_sample_counts: dict[str, int]
    combo_subtypes_before: dict[str, int]
    combo_subtypes_after: dict[str, int]
    top_subtypes_after: dict[str, int]


def import_taco_dataset(
    input_path: Path,
    output_root: Path,
    split: str = "train",
    assignment_mode: str = "single-only",
    composite_output_root: Path | None = None,
) -> TacoImportSummary:
    if assignment_mode not in ASSIGNMENT_MODES:
        raise ValueError(
            f"unsupported assignment_mode '{assignment_mode}'; expected one of: {', '.join(sorted(ASSIGNMENT_MODES))}"
        )
    if assignment_mode == "quarantine-multi" and composite_output_root is None:
        raise ValueError("composite_output_root is required when assignment_mode='quarantine-multi'")

    records = list(_load_taco_records(input_path, split))
    output_root.mkdir(parents=True, exist_ok=True)
    if composite_output_root is not None:
        composite_output_root.mkdir(parents=True, exist_ok=True)

    single_family_records = 0
    multi_family_records = 0
    single_family_records_written = 0
    composite_records_written = 0
    skipped_records = 0
    skipped_reasons = {reason: 0 for reason in SKIP_REASON_ORDER}
    family_counts: dict[str, int] = {}
    composite_family_combo_counts: dict[str, int] = {}
    subtype_counts: dict[str, int] = {}
    composite_subtype_counts: dict[str, int] = {}

    for index, record in enumerate(records, start=1):
        question = _coerce_non_empty_string(record.get("question"))
        if not question:
            skipped_records += 1
            skipped_reasons["missing_question"] += 1
            continue

        reference_solution = _select_reference_solution(record)
        if not reference_solution:
            skipped_records += 1
            skipped_reasons["missing_solution"] += 1
            continue

        families = _resolve_supported_families(record.get("skill_types"))
        if not families:
            skipped_records += 1
            skipped_reasons["no_supported_family"] += 1
            continue

        normalized_tags = _normalize_tags(record.get("tags"))
        if not normalized_tags:
            normalized_tags = _normalize_tags(record.get("raw_tags"))

        base_sample_id = _slugify_identifier(
            str(record.get("task_id") or record.get("id") or record.get("problem_id") or f"{split}-{index:06d}")
        )
        starter_code = _coerce_non_empty_string(record.get("starter_code"))
        problem_text = question
        if starter_code:
            problem_text += f"\n\nStarter code:\n```python\n{starter_code}\n```"

        source_id = str(record.get("task_id") or record.get("id") or record.get("problem_id") or index)
        sample_id = f"taco_{split}_{index:06d}_{base_sample_id}"
        difficulty = _coerce_non_empty_string(record.get("difficulty"))

        if len(families) == 1:
            single_family_records += 1
            family_name = families[0]
            subtype_name = build_canonical_single_family_subtype(
                family_name=family_name,
                normalized_tags=normalized_tags,
            )
            _write_sample(
                root=output_root,
                family_or_group_name=family_name,
                subtype_name=subtype_name,
                sample_id=sample_id,
                problem_text=problem_text,
                reference_solution=reference_solution,
                metadata={
                    "source_dataset": "TACO",
                    "split": split,
                    "source_id": source_id,
                    "difficulty": difficulty,
                    "skill_types": families,
                    "tags": normalized_tags,
                    "family_assignment": family_name,
                    "family_assignments": families,
                    "subtype_assignment": subtype_name,
                    "subtype_assignment_strategy": CANONICAL_SUBTYPE_STRATEGY,
                    "assignment_scope": "single_family",
                },
            )
            single_family_records_written += 1
            family_counts[family_name] = family_counts.get(family_name, 0) + 1
            subtype_key = f"{family_name}/{subtype_name}"
            subtype_counts[subtype_key] = subtype_counts.get(subtype_key, 0) + 1
            continue

        multi_family_records += 1
        if assignment_mode == "single-only":
            skipped_records += 1
            skipped_reasons["multiple_supported_families"] += 1
            continue

        family_combo_name = build_family_combo_name(families)
        subtype_name = build_canonical_composite_subtype(
            family_names=families,
            normalized_tags=normalized_tags,
        )
        assert composite_output_root is not None
        _write_sample(
            root=composite_output_root,
            family_or_group_name=family_combo_name,
            subtype_name=subtype_name,
            sample_id=sample_id,
            problem_text=problem_text,
            reference_solution=reference_solution,
            metadata={
                "source_dataset": "TACO",
                "split": split,
                "source_id": source_id,
                "difficulty": difficulty,
                "skill_types": families,
                "tags": normalized_tags,
                "family_assignments": families,
                "family_combo": family_combo_name,
                "subtype_assignment": subtype_name,
                "subtype_assignment_strategy": CANONICAL_COMPOSITE_SUBTYPE_STRATEGY,
                "assignment_scope": "multi_family",
            },
        )
        composite_records_written += 1
        composite_family_combo_counts[family_combo_name] = composite_family_combo_counts.get(family_combo_name, 0) + 1
        composite_subtype_key = f"{family_combo_name}/{subtype_name}"
        composite_subtype_counts[composite_subtype_key] = composite_subtype_counts.get(composite_subtype_key, 0) + 1

    return TacoImportSummary(
        dataset_name="TACO",
        split=split,
        output_root=output_root,
        composite_output_root=composite_output_root,
        records_read=len(records),
        single_family_records=single_family_records,
        multi_family_records=multi_family_records,
        single_family_records_written=single_family_records_written,
        composite_records_written=composite_records_written,
        skipped_records=skipped_records,
        skipped_reasons={reason: count for reason, count in skipped_reasons.items() if count},
        family_counts=dict(sorted(family_counts.items())),
        composite_family_combo_counts=_sort_counts(composite_family_combo_counts),
        subtype_counts=_sort_counts(subtype_counts),
        composite_subtype_counts=_sort_counts(composite_subtype_counts),
    )


def format_import_summary(summary: TacoImportSummary) -> str:
    lines = [
        f"Imported {summary.single_family_records_written} single-family samples into {summary.output_root}",
        f"Records read: {summary.records_read}",
        f"Single-family records: {summary.single_family_records}",
        f"Multi-family records: {summary.multi_family_records}",
        f"Skipped records: {summary.skipped_records}",
    ]
    if summary.composite_output_root is not None:
        lines.append(
            f"Quarantined {summary.composite_records_written} multi-family samples into {summary.composite_output_root}"
        )
    if summary.family_counts:
        lines.append("Single-family counts:")
        lines.extend(f"- {family}: {count}" for family, count in summary.family_counts.items())
    if summary.composite_family_combo_counts:
        lines.append("Multi-family combo counts:")
        lines.extend(
            f"- {combo}: {count}"
            for combo, count in list(summary.composite_family_combo_counts.items())[:10]
        )
    if summary.skipped_reasons:
        lines.append("Skip reasons:")
        lines.extend(f"- {reason}: {count}" for reason, count in summary.skipped_reasons.items())
    if summary.subtype_counts:
        lines.append("Top single-family subtype counts:")
        top_subtypes = list(_sort_counts(summary.subtype_counts).items())[:10]
        lines.extend(f"- {subtype}: {count}" for subtype, count in top_subtypes)
    if summary.composite_subtype_counts:
        lines.append("Top multi-family subtype counts:")
        top_composite_subtypes = list(summary.composite_subtype_counts.items())[:10]
        lines.extend(f"- {subtype}: {count}" for subtype, count in top_composite_subtypes)
    return "\n".join(lines)


def normalize_taco_subtypes(
    dataset_root: Path,
    dry_run: bool = False,
) -> TacoSubtypeNormalizationSummary:
    if not dataset_root.exists():
        raise FileNotFoundError(f"dataset root not found: {dataset_root}")

    entries: list[_NormalizationEntry] = []
    skipped_records = 0
    skipped_reasons = {reason: 0 for reason in NORMALIZATION_SKIP_REASON_ORDER}
    before_subtype_counts: dict[str, int] = {}
    after_subtype_counts: dict[str, int] = {}
    family_sample_counts: dict[str, int] = {}

    for family_dir in sorted(path for path in dataset_root.iterdir() if path.is_dir()):
        for subtype_dir in sorted(path for path in family_dir.iterdir() if path.is_dir()):
            for sample_dir in sorted(path for path in subtype_dir.iterdir() if path.is_dir()):
                metadata_path = sample_dir / "metadata.json"
                if not metadata_path.exists():
                    skipped_records += 1
                    skipped_reasons["missing_metadata"] += 1
                    continue

                metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
                if metadata.get("source_dataset") != "TACO":
                    skipped_records += 1
                    skipped_reasons["non_taco_sample"] += 1
                    continue

                assignment_scope = metadata.get("assignment_scope")
                if assignment_scope not in (None, "single_family"):
                    skipped_records += 1
                    skipped_reasons["non_single_family_sample"] += 1
                    continue

                family_name = canonicalize_family_name(
                    str(metadata.get("family_assignment") or family_dir.name)
                )
                normalized_tags = normalize_taco_tags(_coerce_string_list(metadata.get("tags")))
                old_subtype_name = subtype_dir.name
                new_subtype_name = build_canonical_single_family_subtype(family_name, normalized_tags)
                sample_id = sample_dir.name
                before_key = f"{family_name}/{old_subtype_name}"
                after_key = f"{family_name}/{new_subtype_name}"
                before_subtype_counts[before_key] = before_subtype_counts.get(before_key, 0) + 1
                after_subtype_counts[after_key] = after_subtype_counts.get(after_key, 0) + 1
                family_sample_counts[family_name] = family_sample_counts.get(family_name, 0) + 1
                entries.append(
                    _NormalizationEntry(
                        source_dir=sample_dir,
                        family_name=family_name,
                        old_subtype_name=old_subtype_name,
                        new_subtype_name=new_subtype_name,
                        sample_id=sample_id,
                        normalized_tags=normalized_tags,
                        metadata=metadata,
                    )
                )

    moved_records = 0
    rewritten_metadata_records = 0
    if not dry_run:
        for entry in entries:
            target_dir = dataset_root / entry.family_name / entry.new_subtype_name / entry.sample_id
            source_dir = entry.source_dir
            if target_dir.exists() and target_dir.resolve() != source_dir.resolve():
                raise FileExistsError(f"target sample directory already exists: {target_dir}")

            metadata = dict(entry.metadata)
            previous_subtype_assignment = str(metadata.get("subtype_assignment") or entry.old_subtype_name)
            if previous_subtype_assignment != entry.new_subtype_name and "raw_subtype_assignment" not in metadata:
                metadata["raw_subtype_assignment"] = previous_subtype_assignment
            metadata["family_assignment"] = entry.family_name
            metadata["tags"] = entry.normalized_tags
            metadata["subtype_assignment"] = entry.new_subtype_name
            metadata["subtype_assignment_strategy"] = CANONICAL_SUBTYPE_STRATEGY

            if target_dir.resolve() != source_dir.resolve():
                target_dir.parent.mkdir(parents=True, exist_ok=True)
                source_dir.rename(target_dir)
                moved_records += 1
                source_dir = target_dir

            (source_dir / "metadata.json").write_text(
                json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            rewritten_metadata_records += 1

        _remove_empty_dirs(dataset_root)

    family_subtypes_before = _count_group_subtypes(before_subtype_counts)
    family_subtypes_after = _count_group_subtypes(after_subtype_counts)
    return TacoSubtypeNormalizationSummary(
        dataset_root=dataset_root,
        dry_run=dry_run,
        eligible_records=len(entries),
        moved_records=moved_records,
        rewritten_metadata_records=rewritten_metadata_records,
        skipped_records=skipped_records,
        skipped_reasons={reason: count for reason, count in skipped_reasons.items() if count},
        unique_subtypes_before=len(before_subtype_counts),
        unique_subtypes_after=len(after_subtype_counts),
        family_sample_counts=dict(sorted(family_sample_counts.items())),
        family_subtypes_before=dict(sorted(family_subtypes_before.items())),
        family_subtypes_after=dict(sorted(family_subtypes_after.items())),
        top_subtypes_after=_sort_counts(after_subtype_counts),
    )


def format_subtype_normalization_summary(summary: TacoSubtypeNormalizationSummary) -> str:
    lines = [
        (
            f"Dry-run analyzed {summary.eligible_records} TACO single-family samples under {summary.dataset_root}"
            if summary.dry_run
            else f"Normalized {summary.eligible_records} TACO single-family samples under {summary.dataset_root}"
        ),
        f"Moved sample directories: {summary.moved_records}",
        f"Rewritten metadata files: {summary.rewritten_metadata_records}",
        f"Skipped records: {summary.skipped_records}",
        f"Unique subtypes before: {summary.unique_subtypes_before}",
        f"Unique subtypes after: {summary.unique_subtypes_after}",
    ]
    if summary.skipped_reasons:
        lines.append("Skip reasons:")
        lines.extend(f"- {reason}: {count}" for reason, count in summary.skipped_reasons.items())
    if summary.family_sample_counts:
        lines.append("Family subtype reduction:")
        for family_name, sample_count in summary.family_sample_counts.items():
            lines.append(
                "- "
                f"{family_name}: {sample_count} samples, "
                f"{summary.family_subtypes_before.get(family_name, 0)} -> "
                f"{summary.family_subtypes_after.get(family_name, 0)} subtypes"
            )
    if summary.top_subtypes_after:
        lines.append("Top canonical subtype counts:")
        lines.extend(
            f"- {subtype}: {count}"
            for subtype, count in list(summary.top_subtypes_after.items())[:10]
        )
    return "\n".join(lines)


def normalize_taco_composite_subtypes(
    dataset_root: Path,
    dry_run: bool = False,
) -> TacoCompositeSubtypeNormalizationSummary:
    if not dataset_root.exists():
        raise FileNotFoundError(f"dataset root not found: {dataset_root}")

    entries: list[_CompositeNormalizationEntry] = []
    skipped_records = 0
    skipped_reasons = {reason: 0 for reason in COMPOSITE_NORMALIZATION_SKIP_REASON_ORDER}
    before_subtype_counts: dict[str, int] = {}
    after_subtype_counts: dict[str, int] = {}
    combo_sample_counts: dict[str, int] = {}

    for combo_dir in sorted(path for path in dataset_root.iterdir() if path.is_dir()):
        for subtype_dir in sorted(path for path in combo_dir.iterdir() if path.is_dir()):
            for sample_dir in sorted(path for path in subtype_dir.iterdir() if path.is_dir()):
                metadata_path = sample_dir / "metadata.json"
                if not metadata_path.exists():
                    skipped_records += 1
                    skipped_reasons["missing_metadata"] += 1
                    continue

                metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
                if metadata.get("source_dataset") != "TACO":
                    skipped_records += 1
                    skipped_reasons["non_taco_sample"] += 1
                    continue

                assignment_scope = metadata.get("assignment_scope")
                if assignment_scope != "multi_family":
                    skipped_records += 1
                    skipped_reasons["non_multi_family_sample"] += 1
                    continue

                families = _resolve_supported_families(metadata.get("family_assignments") or metadata.get("skill_types"))
                if len(families) < 2:
                    skipped_records += 1
                    skipped_reasons["non_multi_family_sample"] += 1
                    continue

                family_combo_name = str(metadata.get("family_combo") or combo_dir.name)
                normalized_tags = normalize_taco_tags(_coerce_string_list(metadata.get("tags")))
                old_subtype_name = subtype_dir.name
                new_subtype_name = build_canonical_composite_subtype(families, normalized_tags)
                sample_id = sample_dir.name
                before_key = f"{family_combo_name}/{old_subtype_name}"
                after_key = f"{family_combo_name}/{new_subtype_name}"
                before_subtype_counts[before_key] = before_subtype_counts.get(before_key, 0) + 1
                after_subtype_counts[after_key] = after_subtype_counts.get(after_key, 0) + 1
                combo_sample_counts[family_combo_name] = combo_sample_counts.get(family_combo_name, 0) + 1
                entries.append(
                    _CompositeNormalizationEntry(
                        source_dir=sample_dir,
                        family_combo_name=family_combo_name,
                        families=families,
                        old_subtype_name=old_subtype_name,
                        new_subtype_name=new_subtype_name,
                        sample_id=sample_id,
                        normalized_tags=normalized_tags,
                        metadata=metadata,
                    )
                )

    moved_records = 0
    rewritten_metadata_records = 0
    if not dry_run:
        for entry in entries:
            target_dir = dataset_root / entry.family_combo_name / entry.new_subtype_name / entry.sample_id
            source_dir = entry.source_dir
            if target_dir.exists() and target_dir.resolve() != source_dir.resolve():
                raise FileExistsError(f"target sample directory already exists: {target_dir}")

            metadata = dict(entry.metadata)
            previous_subtype_assignment = str(metadata.get("subtype_assignment") or entry.old_subtype_name)
            if previous_subtype_assignment != entry.new_subtype_name and "raw_subtype_assignment" not in metadata:
                metadata["raw_subtype_assignment"] = previous_subtype_assignment
            metadata["family_assignments"] = entry.families
            metadata["family_combo"] = entry.family_combo_name
            metadata["tags"] = entry.normalized_tags
            metadata["subtype_assignment"] = entry.new_subtype_name
            metadata["subtype_assignment_strategy"] = CANONICAL_COMPOSITE_SUBTYPE_STRATEGY

            if target_dir.resolve() != source_dir.resolve():
                target_dir.parent.mkdir(parents=True, exist_ok=True)
                source_dir.rename(target_dir)
                moved_records += 1
                source_dir = target_dir

            (source_dir / "metadata.json").write_text(
                json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            rewritten_metadata_records += 1

        _remove_empty_dirs(dataset_root)

    combo_subtypes_before = _count_group_subtypes(before_subtype_counts)
    combo_subtypes_after = _count_group_subtypes(after_subtype_counts)
    return TacoCompositeSubtypeNormalizationSummary(
        dataset_root=dataset_root,
        dry_run=dry_run,
        eligible_records=len(entries),
        moved_records=moved_records,
        rewritten_metadata_records=rewritten_metadata_records,
        skipped_records=skipped_records,
        skipped_reasons={reason: count for reason, count in skipped_reasons.items() if count},
        unique_subtypes_before=len(before_subtype_counts),
        unique_subtypes_after=len(after_subtype_counts),
        combo_sample_counts=dict(sorted(combo_sample_counts.items())),
        combo_subtypes_before=dict(sorted(combo_subtypes_before.items())),
        combo_subtypes_after=dict(sorted(combo_subtypes_after.items())),
        top_subtypes_after=_sort_counts(after_subtype_counts),
    )


def format_composite_subtype_normalization_summary(summary: TacoCompositeSubtypeNormalizationSummary) -> str:
    lines = [
        (
            f"Dry-run analyzed {summary.eligible_records} TACO multi-family samples under {summary.dataset_root}"
            if summary.dry_run
            else f"Normalized {summary.eligible_records} TACO multi-family samples under {summary.dataset_root}"
        ),
        f"Moved sample directories: {summary.moved_records}",
        f"Rewritten metadata files: {summary.rewritten_metadata_records}",
        f"Skipped records: {summary.skipped_records}",
        f"Unique subtypes before: {summary.unique_subtypes_before}",
        f"Unique subtypes after: {summary.unique_subtypes_after}",
    ]
    if summary.skipped_reasons:
        lines.append("Skip reasons:")
        lines.extend(f"- {reason}: {count}" for reason, count in summary.skipped_reasons.items())
    if summary.combo_sample_counts:
        lines.append("Family-combo subtype reduction:")
        for combo_name, sample_count in summary.combo_sample_counts.items():
            lines.append(
                "- "
                f"{combo_name}: {sample_count} samples, "
                f"{summary.combo_subtypes_before.get(combo_name, 0)} -> "
                f"{summary.combo_subtypes_after.get(combo_name, 0)} subtypes"
            )
    if summary.top_subtypes_after:
        lines.append("Top canonical composite subtype counts:")
        lines.extend(
            f"- {subtype}: {count}"
            for subtype, count in list(summary.top_subtypes_after.items())[:10]
        )
    return "\n".join(lines)


def _load_taco_records(input_path: Path, split: str) -> Iterable[dict[str, Any]]:
    if not input_path.exists():
        raise FileNotFoundError(f"TACO input file not found: {input_path}")

    if input_path.is_dir():
        jsonl_candidate = input_path / f"{split}.jsonl"
        json_candidate = input_path / f"{split}.json"
        if jsonl_candidate.exists():
            input_path = jsonl_candidate
        elif json_candidate.exists():
            input_path = json_candidate
        else:
            raise FileNotFoundError(
                f"TACO input directory '{input_path}' must contain either {split}.jsonl or {split}.json"
            )

    if input_path.suffix.lower() == ".jsonl":
        with input_path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                stripped = line.strip()
                if not stripped:
                    continue
                payload = json.loads(stripped)
                if not isinstance(payload, dict):
                    raise ValueError(f"{input_path}:{line_number} must contain one JSON object per line")
                yield payload
        return

    if input_path.suffix.lower() != ".json":
        raise ValueError("TACO input must be a .json or .jsonl file")

    payload = json.loads(input_path.read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        if split in payload:
            payload = payload[split]
        elif "data" in payload and isinstance(payload["data"], dict) and split in payload["data"]:
            payload = payload["data"][split]
    if not isinstance(payload, list):
        raise ValueError("TACO JSON input must contain either a top-level list or a split-keyed mapping")
    for item in payload:
        if not isinstance(item, dict):
            raise ValueError("TACO JSON input must contain only JSON objects")
        yield item


def _resolve_supported_families(raw_skill_types: Any) -> list[str]:
    return _dedupe_preserve_order(
        family_name
        for family_name in (
            _normalize_family_label(skill_type)
            for skill_type in _coerce_string_list(raw_skill_types)
        )
        if family_name in SUPPORTED_FAMILIES
    )


def _normalize_family_label(value: str) -> str:
    return canonicalize_family_name(value)


def _normalize_tags(raw_tags: Any) -> list[str]:
    return normalize_taco_tags(_coerce_string_list(raw_tags))


def _write_sample(
    root: Path,
    family_or_group_name: str,
    subtype_name: str,
    sample_id: str,
    problem_text: str,
    reference_solution: str,
    metadata: dict[str, Any],
) -> None:
    sample_dir = root / family_or_group_name / subtype_name / sample_id
    sample_dir.mkdir(parents=True, exist_ok=True)
    (sample_dir / "problem.md").write_text(problem_text.strip() + "\n", encoding="utf-8")
    (sample_dir / "solution.py").write_text(reference_solution.strip() + "\n", encoding="utf-8")
    (sample_dir / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _select_reference_solution(record: dict[str, Any]) -> str:
    candidates = [item for item in _coerce_string_list(record.get("solutions")) if item.strip()]
    if not candidates:
        return ""
    return min(candidates, key=lambda item: (len(item.strip()), item.count("\n"), item.strip()))


def _coerce_string_list(raw_value: Any) -> list[str]:
    value = _deserialize_embedded_value(raw_value)
    if isinstance(value, list):
        result = []
        for item in value:
            if isinstance(item, str) and item.strip():
                result.append(item.strip())
        return result
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def _deserialize_embedded_value(raw_value: Any) -> Any:
    if not isinstance(raw_value, str):
        return raw_value
    stripped = raw_value.strip()
    if not stripped:
        return []
    if stripped[0] not in "[{(":
        return raw_value
    try:
        return json.loads(stripped)
    except json.JSONDecodeError:
        try:
            return ast.literal_eval(stripped)
        except (ValueError, SyntaxError):
            return raw_value


def _coerce_non_empty_string(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    stripped = value.strip()
    return stripped if stripped else ""


def _slugify_identifier(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")
    return normalized


def _sort_counts(counts: dict[str, int]) -> dict[str, int]:
    return dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))


def _dedupe_preserve_order(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def _count_group_subtypes(subtype_counts: dict[str, int]) -> dict[str, int]:
    family_to_subtypes: dict[str, set[str]] = {}
    for key in subtype_counts:
        family_name, subtype_name = key.split("/", 1)
        family_to_subtypes.setdefault(family_name, set()).add(subtype_name)
    return {
        family_name: len(subtypes)
        for family_name, subtypes in family_to_subtypes.items()
    }


def _remove_empty_dirs(dataset_root: Path) -> None:
    subtype_dirs = sorted(
        (path for path in dataset_root.glob("*/*") if path.is_dir()),
        key=lambda path: len(path.parts),
        reverse=True,
    )
    for subtype_dir in subtype_dirs:
        if any(subtype_dir.iterdir()):
            continue
        subtype_dir.rmdir()

    family_dirs = sorted(path for path in dataset_root.iterdir() if path.is_dir())
    for family_dir in family_dirs:
        if any(family_dir.iterdir()):
            continue
        family_dir.rmdir()


@dataclass(frozen=True)
class _NormalizationEntry:
    source_dir: Path
    family_name: str
    old_subtype_name: str
    new_subtype_name: str
    sample_id: str
    normalized_tags: list[str]
    metadata: dict[str, Any]


@dataclass(frozen=True)
class _CompositeNormalizationEntry:
    source_dir: Path
    family_combo_name: str
    families: list[str]
    old_subtype_name: str
    new_subtype_name: str
    sample_id: str
    normalized_tags: list[str]
    metadata: dict[str, Any]
