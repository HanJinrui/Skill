from __future__ import annotations

import json
import sys
from dataclasses import replace
from pathlib import Path

FACTORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FACTORY_ROOT))
sys.path.insert(0, str(FACTORY_ROOT.parent / "rag_experiment" / "src"))

from sdf.factory_settings import get_settings  # noqa: E402
from sdf.io_utils import read_jsonl  # noqa: E402
from sdf.merge_compositions import merge_composition_ledgers  # noqa: E402


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


def test_merge_preserves_taco_and_excludes_duplicate_and_eval_leakage(tmp_path: Path) -> None:
    taco = tmp_path / "taco.jsonl"
    code = tmp_path / "code.jsonl"
    eval_manifest = tmp_path / "eval.jsonl"
    pass1_summary = tmp_path / "pass1_summary.json"
    output = tmp_path / "merged"
    signature = ["sorting_custom_key", "greedy_sorting_order"]
    _write_jsonl(
        taco,
        [{"problem_id": "t1", "problem_statement": "same task", "composition_order": signature}],
    )
    _write_jsonl(
        code,
        [
            {"problem_id": "c1", "problem_statement": "same task", "composition_order": signature},
            {"problem_id": "c2", "problem_statement": "eval task", "composition_order": signature},
            {
                "problem_id": "c3",
                "problem_statement": "new task",
                "composition_order": signature,
                "source_language": "PYTHON3",
            },
        ],
    )
    _write_jsonl(eval_manifest, [{"problem_statement": "eval task"}])
    pass1_summary.write_text(
        json.dumps(
            {
                "stats": {
                    "full_pass_solution_language_counts": {"PYTHON3": 7, "PYTHON": 2},
                    "failure_reasons": {"wrong_answer": 4},
                }
            }
        ),
        encoding="utf-8",
    )
    base = get_settings()
    settings = replace(
        base,
        config={
            "merge": {
                "taco_composition_path": str(taco),
                "codecontests_composition_path": str(code),
                "codecontests_pass1_summary": str(pass1_summary),
                "eval_manifest_glob": str(eval_manifest),
                "output_dir": str(output),
            }
        },
    )
    paths = merge_composition_ledgers(settings)
    merged = list(read_jsonl(paths["composition_rows"]))
    excluded = list(read_jsonl(paths["excluded_rows"]))
    report = json.loads(paths["report"].read_text(encoding="utf-8"))
    assert [row["problem_id"] for row in merged] == ["t1", "c3"]
    assert merged[0]["source_dataset"] == "TACO"
    assert merged[1]["source_dataset"] == "CodeContests"
    assert {row["exclusion_reason"] for row in excluded} == {
        "duplicate_of_taco_evidence",
        "evaluation_manifest_leakage",
    }
    assert report["accepted_source_dataset_counts"] == {"TACO": 1, "CodeContests": 1}
    assert report["codecontests_full_pass_solution_language_counts"] == {
        "PYTHON3": 7,
        "PYTHON": 2,
    }
    assert report["codecontests_verification_failure_reasons"] == {"wrong_answer": 4}
