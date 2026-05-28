"""Route verified problems/solutions to single_algorithm or multi_algorithm tracks."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from sdf.io_utils import append_jsonl, load_jsonl, read_jsonl, save_json
from sdf.pass2_rule_candidates import build_rule_candidates, rule_mechanism_scope_hint
from sdf.factory_settings import Settings, cfg_section
from sdf.shared import bootstrap  # noqa: F401

from src.logging_utils import get_logger
from src.subtype_taxonomy import get_subtype

LOG = get_logger(__name__)

TRACKS = ("single_algorithm", "multi_algorithm")


def _solution_rows_for_problem(verified_path: Path, problem_id: str, *, min_tests: int) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in read_jsonl(verified_path):
        if row.get("problem_id") != problem_id:
            continue
        if not row.get("full_pass"):
            continue
        if int(row.get("total_tests") or 0) < min_tests:
            continue
        if int(row.get("passed_tests") or 0) != int(row.get("total_tests") or 0):
            continue
        rows.append(row)
    return rows


def decide_algorithm_scope(
    problem_row: dict[str, Any],
    solution_rows: list[dict[str, Any]],
    *,
    route_cfg: dict[str, Any],
) -> str:
    """Return single | multi | quarantine."""
    gap = float(route_cfg.get("single_top2_score_gap", 8.0))
    multi_min_score = float(route_cfg.get("multi_min_subtype_score", 4.0))
    families = list(problem_row.get("problem_families") or [])
    clean = str(problem_row.get("clean_split") or "")

    if clean in {"mismatch", "noisy_or_unverified"}:
        return "quarantine"
    if not solution_rows:
        return "quarantine"

    # Use best solution by tests then pass_rate for scope hint
    best = sorted(
        solution_rows,
        key=lambda r: (-int(r.get("total_tests") or 0), -float(r.get("pass_rate") or 0)),
    )[0]
    rule_pack = build_rule_candidates(best)
    candidates = rule_pack["candidate_subtypes"]
    hint = rule_mechanism_scope_hint(
        candidates,
        gap=gap,
        multi_min_score=multi_min_score,
    )

    if hint == "multi":
        return "multi"
    if hint == "single":
        return "single"
    # ambiguous: problem-level multi tag -> multi if >=2 families else single
    if len(families) >= 2 and bool(route_cfg.get("allow_problem_multi_tag", True)):
        top_fams = {str(c.get("family") or "") for c in candidates[:3]}
        if len(top_fams) >= int(route_cfg.get("multi_min_distinct_families", 2)):
            return "multi"
    return "single"


def run_pass1_route(settings: Settings) -> dict[str, Path]:
    route_cfg = cfg_section(settings, "pass1_route")
    p1 = cfg_section(settings, "pass1")
    min_tests = int(p1.get("min_official_tests", 5))

    shared = settings.output_dir / "pass1_manifest"
    problems_path = shared / "verified_problems.jsonl"
    verified_path = shared / "verified_solutions.jsonl"
    if not problems_path.exists():
        raise FileNotFoundError(f"Run pass1 verify first: {problems_path}")

    route_summary = {"single": 0, "multi": 0, "quarantine": 0}
    outputs: dict[str, Path] = {}

    for track in TRACKS:
        out_dir = settings.pass1_dir(track)
        out_dir.mkdir(parents=True, exist_ok=True)
        outputs[f"{track}_problems"] = out_dir / "problems.jsonl"
        outputs[f"{track}_solutions"] = out_dir / "solutions.jsonl"
        if out_dir.joinpath("problems.jsonl").exists():
            out_dir.joinpath("problems.jsonl").unlink()
        if out_dir.joinpath("solutions.jsonl").exists():
            out_dir.joinpath("solutions.jsonl").unlink()

    quarantine_path = shared / "quarantine_problems.jsonl"
    if quarantine_path.exists():
        quarantine_path.unlink()

    for prob in read_jsonl(problems_path):
        pid = str(prob.get("problem_id") or "")
        sol_rows = _solution_rows_for_problem(verified_path, pid, min_tests=min_tests)
        scope = decide_algorithm_scope(prob, sol_rows, route_cfg=route_cfg)
        route_summary[scope] = route_summary.get(scope, 0) + 1
        prob = {**prob, "algorithm_scope": scope}

        if scope == "quarantine":
            append_jsonl(quarantine_path, prob)
            continue

        track = "single_algorithm" if scope == "single" else "multi_algorithm"
        append_jsonl(settings.pass1_dir(track) / "problems.jsonl", prob)
        for sol in sol_rows:
            sol = {**sol, "algorithm_scope": scope, "clean_split": prob.get("clean_split")}
            append_jsonl(settings.pass1_dir(track) / "solutions.jsonl", sol)

    summary_path = shared / "route_summary.json"
    save_json(summary_path, {"route_counts": route_summary, "outputs": {k: str(v) for k, v in outputs.items()}})
    LOG.info("Pass1 route done: %s", route_summary)
    outputs["summary"] = summary_path
    outputs["quarantine"] = quarantine_path
    return outputs
