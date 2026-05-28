from __future__ import annotations

import copy
import heapq
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Iterator

from .io_utils import load_yaml, write_json, write_jsonl


class AdditionalEvidenceError(RuntimeError):
    pass


def load_algorithm_catalog(config: dict[str, Any]) -> dict[str, Any]:
    path = Path(config["additional"]["catalog_path"])
    catalog = load_yaml(path)
    validate_algorithm_catalog(catalog)
    return catalog


def algorithm_index(catalog: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(item["id"]): item for item in catalog.get("algorithms", [])}


def validate_algorithm_catalog(catalog: dict[str, Any]) -> None:
    algorithms = catalog.get("algorithms") or []
    ids = [str(item.get("id") or "") for item in algorithms]
    if len(ids) != 35 or len(set(ids)) != 35 or any(not item for item in ids):
        raise AdditionalEvidenceError("Priority catalog must contain exactly 35 unique algorithm IDs")
    aliases = catalog.get("direct_aliases") or {}
    targets = set(ids)
    for source, target in aliases.items():
        if source in targets:
            raise AdditionalEvidenceError(f"Alias source collides with canonical ID: {source}")
        if target not in targets:
            raise AdditionalEvidenceError(f"Alias target is not canonical: {source} -> {target}")
        if source == target:
            raise AdditionalEvidenceError(f"Self alias is not allowed: {source}")


def _run_curated_tests(subtype: str, entry: dict[str, Any]) -> None:
    code = str(entry.get("reference_code") or "")
    tests = entry.get("tests") or []
    if not code.strip() or not tests:
        raise AdditionalEvidenceError(f"Curated evidence missing code or tests: {subtype}")
    namespace: dict[str, Any] = {}
    try:
        exec(compile(code, f"<curated:{subtype}>", "exec"), namespace)
    except Exception as exc:
        raise AdditionalEvidenceError(f"Curated code does not compile: {subtype}: {exc}") from exc
    fn = namespace.get("solve_case")
    if not callable(fn):
        raise AdditionalEvidenceError(f"Curated code must define solve_case: {subtype}")
    for case_no, test in enumerate(tests, start=1):
        try:
            actual = fn(*copy.deepcopy(test.get("args") or []))
        except Exception as exc:
            raise AdditionalEvidenceError(
                f"Curated test execution failed: {subtype} case {case_no}: {exc}"
            ) from exc
        if actual != test.get("expected"):
            raise AdditionalEvidenceError(
                f"Curated test failed: {subtype} case {case_no}: "
                f"expected {test.get('expected')!r}, got {actual!r}"
            )


def load_validated_curated_evidence(
    config: dict[str, Any],
    catalog: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    curated = load_yaml(config["additional"]["curated_path"])
    entries = curated.get("algorithms") or {}
    targets = set(algorithm_index(catalog))
    if set(entries) != targets:
        missing = sorted(targets - set(entries))
        extra = sorted(set(entries) - targets)
        raise AdditionalEvidenceError(f"Curated catalog mismatch; missing={missing}, extra={extra}")
    for subtype, entry in entries.items():
        _run_curated_tests(subtype, entry)
    return entries


_CURATED_VARIANTS = [
    "canonical small instance",
    "boundary-oriented instance",
    "mixed-value instance",
    "repeated-query instance",
    "mechanism-isolation instance",
]


def build_curated_rows(
    config: dict[str, Any],
    catalog: dict[str, Any],
    curated_entries: dict[str, dict[str, Any]],
    *,
    target_ids: set[str] | None = None,
) -> dict[str, list[dict[str, Any]]]:
    indexed = algorithm_index(catalog)
    variants = int(config.get("additional", {}).get("curated_variants_per_skill", 5))
    if variants < 1 or variants > len(_CURATED_VARIANTS):
        raise AdditionalEvidenceError("curated_variants_per_skill must be between 1 and 5")
    grouped: dict[str, list[dict[str, Any]]] = {}
    aliases_by_target: dict[str, list[str]] = {}
    for source, target in (catalog.get("direct_aliases") or {}).items():
        aliases_by_target.setdefault(str(target), []).append(str(source))
    for subtype, item in indexed.items():
        if target_ids is not None and subtype not in target_ids:
            continue
        entry = curated_entries[subtype]
        tests = entry.get("tests") or []
        rows: list[dict[str, Any]] = []
        for index, variant in enumerate(_CURATED_VARIANTS[:variants], start=1):
            rows.append(
                {
                    "problem_id": f"curated.{subtype}.{index:02d}",
                    "solution_id": "reference",
                    "solution_code": entry["reference_code"],
                    "problem_statement": f"{entry['statement']} Evidence focus: {variant}.",
                    "source": "curated_standard_examples_v1",
                    "difficulty": "REFERENCE",
                    "syntax_ok": True,
                    "safe_exec_ok": True,
                    "full_pass": True,
                    "pass_rate": 1.0,
                    "passed_tests": len(tests),
                    "total_tests": len(tests),
                    "verification_source": "executed_curated_tests",
                    "algorithm_scope": "single",
                    "is_true_composition": False,
                    "is_primary_solution": True,
                    "primary_subtype": subtype,
                    "canonical_subtype": subtype,
                    "alias_subtypes": sorted(aliases_by_target.get(subtype, [])),
                    "detected_single_skill": item["family"],
                    "subtype_confidence": 1.0,
                    "label_confidence": 1.0,
                    "label_reason": entry["mechanism"],
                    "evidence_origin": "curated",
                    "evidence_validation": "executed_tests",
                    "evidence_tier": "curated",
                    "rule_confidence": 1.0,
                    "primary_solution_score": 1.0,
                    "taco_family_alignment": False,
                    "candidate_subtypes": [subtype],
                    "ast_features": {},
                    "core_mechanism_summary": entry["mechanism"],
                    "subtype_rationale": entry["mechanism"],
                    "original_tags": [item["label"]],
                    "problem_families": [item["family"]],
                }
            )
        grouped[subtype] = rows
    return grouped


def _verified_row_text(row: dict[str, Any], *, include_statement: bool = False) -> str:
    tags = " ".join(str(x) for x in (row.get("original_tags") or []))
    families = " ".join(str(x) for x in (row.get("problem_families") or []))
    hints = " ".join(str(x) for x in (row.get("solution_family_hints") or []))
    parts = [tags, families, hints]
    if include_statement:
        parts.append(str(row.get("problem_statement") or "")[:1200])
    return " ".join(parts).lower()


def iter_jsonl(path: str | Path) -> Iterator[dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, start=1):
            if not line.strip():
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as exc:
                raise AdditionalEvidenceError(f"Invalid JSON at {path}:{line_no}") from exc


def prefilter_verified_candidates(
    verified_rows: Iterable[dict[str, Any]],
    catalog: dict[str, Any],
    config: dict[str, Any],
    *,
    target_ids: set[str] | None = None,
    include_statement: bool = False,
    require_execution_validation: bool = True,
) -> dict[str, list[dict[str, Any]]]:
    limit = int(config.get("additional", {}).get("max_verified_candidates_per_skill", 8))
    indexed = algorithm_index(catalog)
    candidates: dict[str, list[tuple[int, int, int, dict[str, Any]]]] = {
        key: [] for key in indexed
    }
    cue_targets: dict[str, set[str]] = {}
    for subtype, item in indexed.items():
        if target_ids is not None and subtype not in target_ids:
            continue
        for cue in item.get("cues", []):
            cue_targets.setdefault(str(cue).lower(), set()).add(subtype)
    cue_pattern = re.compile(
        "|".join(re.escape(cue) for cue in sorted(cue_targets, key=len, reverse=True)),
        re.IGNORECASE,
    )
    serial = 0
    for row in verified_rows:
        if require_execution_validation and not (
            row.get("syntax_ok") is True
            and row.get("safe_exec_ok") is True
            and row.get("full_pass") is True
            and float(row.get("pass_rate") or 0) == 1.0
        ):
            continue
        text = _verified_row_text(row, include_statement=include_statement)
        matched_cues = {match.group(0).lower() for match in cue_pattern.finditer(text)}
        scores: Counter[str] = Counter()
        for cue in matched_cues:
            for subtype in cue_targets[cue]:
                scores[subtype] += 1
        for subtype, score in scores.items():
            serial += 1
            ranked = (score, -len(str(row.get("solution_code") or "")), serial, row)
            heap = candidates[subtype]
            if len(heap) < limit:
                heapq.heappush(heap, ranked)
            elif ranked[:2] > heap[0][:2]:
                heapq.heapreplace(heap, ranked)
    result: dict[str, list[dict[str, Any]]] = {}
    for subtype, matches in candidates.items():
        matches.sort(key=lambda pair: (-pair[0], -pair[1], pair[2]))
        result[subtype] = [row for _, _, _, row in matches]
    return result


def materialize_solution_candidates(
    problem_candidates: dict[str, list[dict[str, Any]]],
    verified_solutions_path: str | Path,
    config: dict[str, Any],
) -> dict[str, list[dict[str, Any]]]:
    limit = int(config.get("additional", {}).get("max_verified_candidates_per_skill", 8))
    wanted: dict[str, set[str]] = {}
    for subtype, rows in problem_candidates.items():
        for row in rows:
            wanted.setdefault(str(row.get("problem_id") or ""), set()).add(subtype)
    selected: dict[str, list[dict[str, Any]]] = {subtype: [] for subtype in problem_candidates}
    if not wanted:
        return selected
    problem_id_pattern = re.compile(r'"problem_id"\s*:\s*"([^"]+)"')
    with open(verified_solutions_path, "r", encoding="utf-8") as fh:
        for line in fh:
            match = problem_id_pattern.search(line[:300])
            if not match:
                continue
            targets = wanted.get(match.group(1))
            if not targets:
                continue
            row = json.loads(line)
            for subtype in targets:
                if len(selected[subtype]) < limit:
                    selected[subtype].append(row)
    return selected


def _label_prompt(subtype: str, item: dict[str, Any], candidates: list[dict[str, Any]]) -> str:
    snippets = []
    for index, row in enumerate(candidates):
        snippets.append(
            "\n".join(
                [
                    f"Candidate index: {index}",
                    f"Problem ID: {row.get('problem_id')}",
                    f"Tags: {row.get('original_tags')}",
                    f"Statement excerpt: {str(row.get('problem_statement') or '')[:700]}",
                    f"Code excerpt:\n{str(row.get('solution_code') or '')[:1800]}",
                ]
            )
        )
    joined = "\n\n---\n\n".join(snippets)
    return f"""You label verified competitive-programming solutions for one precise algorithm mechanism.

Target canonical subtype: {subtype}
Target description: {item.get('label')}
Decision boundary: {item.get('boundary')}

Every candidate already passed execution verification. Decide only whether its core algorithm
mechanism matches the target subtype; do not infer a match from topic words alone.

Return strict JSON:
{{"labels": [{{"candidate_index": 0, "decision": "match|not_match|ambiguous",
"canonical_subtype": "{subtype}|none", "confidence": 0.0,
"reason": "brief mechanism evidence"}}]}}

Candidates:

{joined}
"""


def _taco_distillation_row(
    source_row: dict[str, Any],
    subtype: str,
    item: dict[str, Any],
    confidence: float,
    reason: str,
    aliases: list[str],
) -> dict[str, Any]:
    return {
        **source_row,
        "algorithm_scope": "single",
        "is_true_composition": False,
        "is_primary_solution": True,
        "primary_subtype": subtype,
        "canonical_subtype": subtype,
        "alias_subtypes": aliases,
        "detected_single_skill": item["family"],
        "subtype_confidence": confidence,
        "label_confidence": confidence,
        "label_reason": reason,
        "evidence_origin": "taco_verified",
        "evidence_validation": "external_verified",
        "evidence_tier": "gold",
        "rule_confidence": confidence,
        "primary_solution_score": confidence,
        "taco_family_alignment": True,
        "candidate_subtypes": [subtype],
        "ast_features": {},
        "core_mechanism_summary": reason,
        "subtype_rationale": reason,
    }


def label_verified_candidates(
    candidates: dict[str, list[dict[str, Any]]],
    catalog: dict[str, Any],
    config: dict[str, Any],
    llm_client: Any,
) -> dict[str, list[dict[str, Any]]]:
    from concurrent.futures import ThreadPoolExecutor, as_completed

    indexed = algorithm_index(catalog)
    threshold = float(config.get("additional", {}).get("min_verified_label_confidence", 0.90))
    accepted: dict[str, list[dict[str, Any]]] = {subtype: [] for subtype in candidates}
    aliases_by_target: dict[str, list[str]] = {}
    for source, target in (catalog.get("direct_aliases") or {}).items():
        aliases_by_target.setdefault(str(target), []).append(str(source))
    def label_one(subtype: str, rows: list[dict[str, Any]]) -> tuple[str, list[dict[str, Any]]]:
        if not rows:
            return subtype, []
        response = llm_client.generate_json(
            _label_prompt(subtype, indexed[subtype], rows),
            cache_key={
                "task": "additional_evidence_label",
                "version": "v1",
                "subtype": subtype,
                "ids": [(row.get("problem_id"), row.get("solution_id")) for row in rows],
            },
            routing_key=f"label:{subtype}",
        )
        matches: list[dict[str, Any]] = []
        for label in response.get("labels") or []:
            index = label.get("candidate_index")
            if not isinstance(index, int) or not 0 <= index < len(rows):
                continue
            confidence = float(label.get("confidence") or 0)
            if (
                label.get("decision") == "match"
                and label.get("canonical_subtype") == subtype
                and confidence >= threshold
            ):
                matches.append(
                    _taco_distillation_row(
                        rows[index],
                        subtype,
                        indexed[subtype],
                        confidence,
                        str(label.get("reason") or indexed[subtype]["label"]),
                        sorted(aliases_by_target.get(subtype, [])),
                    )
                )
        return subtype, matches

    tasks = [(subtype, rows) for subtype, rows in candidates.items() if rows]
    max_workers = max(1, int(config.get("llm", {}).get("max_workers", 1)))
    if max_workers == 1:
        for subtype, rows in tasks:
            key, matches = label_one(subtype, rows)
            accepted[key] = matches
        return accepted
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(label_one, subtype, rows): subtype for subtype, rows in tasks
        }
        for future in as_completed(futures):
            subtype, matches = future.result()
            accepted[subtype] = matches
    return accepted


def prepare_additional_evidence(
    config: dict[str, Any],
    *,
    llm_client: Any | None = None,
    label_verified: bool = True,
    target_ids: set[str] | None = None,
) -> list[dict[str, Any]]:
    catalog = load_algorithm_catalog(config)
    indexed = algorithm_index(catalog)
    if target_ids is not None:
        unknown = target_ids - set(indexed)
        if unknown:
            raise AdditionalEvidenceError(f"Unknown target subtypes: {sorted(unknown)}")
    curated_entries = load_validated_curated_evidence(config, catalog)
    curated = build_curated_rows(config, catalog, curated_entries, target_ids=target_ids)

    taco: dict[str, list[dict[str, Any]]] = {
        subtype: [] for subtype in indexed if target_ids is None or subtype in target_ids
    }
    candidate_counts: dict[str, int] = {subtype: 0 for subtype in taco}
    if label_verified:
        if llm_client is None:
            raise AdditionalEvidenceError("llm_client is required when verified candidate labeling is enabled")
        problem_candidates = prefilter_verified_candidates(
            iter_jsonl(config["additional"]["verified_problems_path"]),
            catalog,
            config,
            target_ids=target_ids,
            include_statement=True,
            require_execution_validation=False,
        )
        candidates = materialize_solution_candidates(
            problem_candidates,
            config["additional"]["verified_solutions_path"],
            config,
        )
        candidate_counts = {subtype: len(rows) for subtype, rows in candidates.items()}
        taco = label_verified_candidates(candidates, catalog, config, llm_client)

    min_examples = int(config.get("representative_selection", {}).get("min_examples_per_skill", 5))
    rows: list[dict[str, Any]] = []
    coverage: dict[str, Any] = {}
    for subtype in sorted(taco):
        verified_rows = taco[subtype]
        supplement_count = max(0, min_examples - len(verified_rows))
        included_curated = curated[subtype][:supplement_count] if supplement_count else []
        combined = verified_rows + included_curated
        rows.extend(combined)
        if len(verified_rows) >= int(config.get("grouping", {}).get("stable_min_rows", 10)):
            maturity = "stable"
        elif len(verified_rows) >= int(config.get("grouping", {}).get("provisional_min_rows", 5)):
            maturity = "provisional"
        else:
            maturity = "seed"
        coverage[subtype] = {
            "algorithm_family": indexed[subtype]["family"],
            "verified_candidates": candidate_counts.get(subtype, 0),
            "taco_verified_rows": len(verified_rows),
            "curated_rows": len(included_curated),
            "generation_rows": len(combined),
            "maturity": maturity,
        }

    origin_counts = Counter(str(row.get("evidence_origin") or "") for row in rows)
    report = {
        "catalog_version": catalog.get("version"),
        "verified_labeling_enabled": label_verified,
        "target_count": len(taco),
        "row_count": len(rows),
        "origin_counts": dict(origin_counts),
        "coverage": coverage,
    }
    write_jsonl(config["input"]["distillation_path"], rows)
    write_json(config["output"]["coverage_report_path"], report)
    return rows
