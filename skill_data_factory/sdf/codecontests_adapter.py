"""Adapt DeepMind CodeContests rows to the skill data factory contract."""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import Any, Iterable

from sdf.shared import bootstrap  # noqa: F401

from src.rules import ast_to_family_hints, problem_candidate_families, solution_ast_features
from src.taxonomy import CORE_FAMILIES

PYTHON = 1
PYTHON3 = 3
LANGUAGE_NAMES = {PYTHON: "PYTHON", PYTHON3: "PYTHON3"}

CODECONTESTS_TAG_FAMILIES = {
    "dp": "dynamic_programming",
    "dynamic programming": "dynamic_programming",
    "greedy": "greedy_algorithms",
    "data structures": "data_structures",
    "two pointers": "amortized_analysis",
    "bitmasks": "bit_manipulation",
    "bitmask": "bit_manipulation",
    "binary search": "sorting",
    "sortings": "sorting",
    "sorting": "sorting",
    "brute force": "complete_search",
    "dfs and similar": "complete_search",
    "graphs": "complete_search",
    "trees": "complete_search",
    "dsu": "data_structures",
}

TEST_SELECTION_POLICY = "stratified_v1(public<=5,private<=10,generated<=5,fill=private/generated/public,max=20)"


@dataclass(frozen=True)
class CodeContestsProblem:
    problem_id: str
    source_index: int
    source: str | None
    difficulty: str | None
    problem_statement: str
    reference_solutions: list[dict[str, str]]
    input_output: dict[str, Any] | None
    original_skill_types: list[str]
    original_tags: list[str]
    candidate_families: list[str]
    source_dataset: str = "CodeContests"
    split: str = "train"
    family_evidence_method: str = "codecontests_open_inference"
    open_family_candidates: bool = True
    source_problem_fingerprint: str = ""
    selected_test_counts: dict[str, int] | None = None
    test_selection_policy: str = TEST_SELECTION_POLICY
    cf_tags: list[str] | None = None
    cf_contest_id: int | str | None = None
    cf_index: str | None = None


def normalize_problem_statement(text: str) -> str:
    return " ".join(str(text or "").replace("\r\n", "\n").replace("\r", "\n").lower().split())


def problem_fingerprint(text: str) -> str:
    normalized = normalize_problem_statement(text)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def _list_field(value: Any, field: str) -> list[Any]:
    if isinstance(value, dict):
        raw = value.get(field)
        return list(raw) if isinstance(raw, (list, tuple)) else []
    return []


def _test_pairs(record: dict[str, Any], bucket: str) -> list[tuple[str, str]]:
    tests = record.get(f"{bucket}_tests") or {}
    inputs = _list_field(tests, "input")
    outputs = _list_field(tests, "output")
    return [(str(inp), str(out)) for inp, out in zip(inputs, outputs)]


def select_stratified_tests(
    record: dict[str, Any],
    *,
    max_tests: int = 20,
    public_limit: int = 5,
    private_limit: int = 10,
    generated_limit: int = 5,
) -> tuple[dict[str, Any] | None, dict[str, int]]:
    pools = {
        "public": _test_pairs(record, "public"),
        "private": _test_pairs(record, "private"),
        "generated": _test_pairs(record, "generated"),
    }
    limits = {"public": public_limit, "private": private_limit, "generated": generated_limit}
    selected: list[tuple[str, str]] = []
    counts = {"public": 0, "private": 0, "generated": 0}
    seen: set[tuple[str, str]] = set()
    cursor = {"public": 0, "private": 0, "generated": 0}

    def take(bucket: str, limit: int) -> None:
        while cursor[bucket] < len(pools[bucket]) and counts[bucket] < limit and len(selected) < max_tests:
            pair = pools[bucket][cursor[bucket]]
            cursor[bucket] += 1
            if pair in seen:
                continue
            seen.add(pair)
            selected.append(pair)
            counts[bucket] += 1

    for bucket in ("public", "private", "generated"):
        take(bucket, limits[bucket])
    for bucket in ("private", "generated", "public"):
        take(bucket, max_tests)

    if not selected:
        return None, counts
    return {
        "inputs": [pair[0] for pair in selected],
        "outputs": [pair[1] for pair in selected],
    }, counts


def _allowed_language_ids(raw: Iterable[str | int] | None) -> set[int]:
    values = list(raw or ["PYTHON3", "PYTHON"])
    ids: set[int] = set()
    for value in values:
        if isinstance(value, int):
            ids.add(value)
            continue
        label = str(value).strip().upper()
        if label == "PYTHON3":
            ids.add(PYTHON3)
        elif label == "PYTHON":
            ids.add(PYTHON)
    return ids


def select_python_solutions(
    record: dict[str, Any],
    *,
    allowed_languages: Iterable[str | int] | None = None,
    max_solutions: int = 5,
) -> list[dict[str, str]]:
    solutions = record.get("solutions") or {}
    codes = _list_field(solutions, "solution")
    languages = _list_field(solutions, "language")
    allowed = _allowed_language_ids(allowed_languages)
    rows: list[dict[str, str]] = []
    for index, (language, code) in enumerate(zip(languages, codes)):
        try:
            language_id = int(language)
        except (TypeError, ValueError):
            continue
        if language_id not in allowed or not isinstance(code, str) or not code.strip():
            continue
        label = LANGUAGE_NAMES[language_id]
        rows.append(
            {
                "solution_id": f"{label.lower()}_s{index}",
                "code": code,
                "source_language": label,
            }
        )
    rows.sort(key=lambda row: (0 if row["source_language"] == "PYTHON3" else 1, row["solution_id"]))
    return rows[:max_solutions] if max_solutions > 0 else rows


def _ordered_unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            out.append(value)
    return out


def _tag_families(tags: list[str]) -> list[str]:
    return _ordered_unique(
        CODECONTESTS_TAG_FAMILIES.get(str(tag).strip().lower(), "")
        for tag in tags
    )


def _lexical_solution_family_hints(code: str) -> list[str]:
    text = code.lower()
    hints: list[str] = []
    signals = (
        ("dynamic_programming", r"\b(dp|memo|cache)\s*\[|lru_cache"),
        ("data_structures", r"\b(heapq|heappush|heappop|defaultdict|counter|deque|parent\s*\[)"),
        ("sorting", r"\bsorted\s*\(|\.sort\s*\("),
        ("amortized_analysis", r"\b(left|right|l|r)\s*=\s*0|two.?pointer|sliding"),
        ("bit_manipulation", r"\bmask\b|\bbit\b|<<|>>|\^"),
        ("range_queries", r"fenwick|segment.?tree|prefix|lowbit"),
        ("complete_search", r"\b(dfs|bfs|backtrack|permut)"),
    )
    for family, pattern in signals:
        if re.search(pattern, text):
            hints.append(family)
    return hints


def infer_family_seeds(statement: str, tags: list[str], solutions: list[dict[str, str]]) -> tuple[list[str], str]:
    tagged = _tag_families(tags)
    ruled = problem_candidate_families(statement, tags, (), max_candidates=8)
    statement_families = [family for family in ruled.families if float(ruled.scores.get(family, 0.0)) > 0]
    code_families: list[str] = []
    for solution in solutions:
        code = solution["code"]
        code_families.extend(_lexical_solution_family_hints(code))
        if solution["source_language"] == "PYTHON3":
            features = solution_ast_features(code)
            if features.tokens:
                code_families.extend(ast_to_family_hints(features))
    inferred = _ordered_unique([*tagged, *statement_families, *code_families])
    if inferred:
        method = "cf_tags_plus_open_inference" if tagged else "open_statement_solution_inference"
        return inferred, method
    return list(CORE_FAMILIES), "open_unseeded_all_core_families"


def parse_codecontests_problem(
    dataset_index: int,
    record: dict[str, Any],
    *,
    split: str = "train",
    allowed_languages: Iterable[str | int] | None = None,
    max_solutions: int = 5,
    max_tests: int = 20,
    min_tests: int = 5,
) -> CodeContestsProblem | None:
    statement = record.get("description") or ""
    if not isinstance(statement, str) or not statement.strip():
        return None
    solutions = select_python_solutions(
        record,
        allowed_languages=allowed_languages,
        max_solutions=max_solutions,
    )
    if not solutions:
        return None
    tests, test_counts = select_stratified_tests(record, max_tests=max_tests)
    if tests is None or len(tests["inputs"]) < min_tests:
        return None
    tags = [str(tag) for tag in (record.get("cf_tags") or []) if str(tag).strip()]
    families, family_method = infer_family_seeds(statement, tags, solutions)
    difficulty = record.get("difficulty")
    return CodeContestsProblem(
        problem_id=f"codecontests_{split}_{dataset_index:06d}",
        source_index=dataset_index,
        source=str(record.get("source")) if record.get("source") is not None else None,
        difficulty=str(difficulty) if difficulty is not None else None,
        problem_statement=statement.strip(),
        reference_solutions=solutions,
        input_output=tests,
        original_skill_types=[],
        original_tags=tags,
        candidate_families=families,
        split=split,
        family_evidence_method=family_method,
        source_problem_fingerprint=problem_fingerprint(statement),
        selected_test_counts=test_counts,
        cf_tags=tags,
        cf_contest_id=record.get("cf_contest_id"),
        cf_index=str(record.get("cf_index")) if record.get("cf_index") is not None else None,
    )
