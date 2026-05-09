"""Run Stage F comparison modes and write one combined report.

This is a thin orchestrator around `run_stage_f_eval.py`; it does not change
generation, execution, or retrieval internals.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.io_utils import load_jsonl, save_json  # noqa: E402
from src.logging_utils import setup_logging, get_logger  # noqa: E402
from src.settings import get_settings  # noqa: E402


DEFAULT_MODES = ("no_rag", "subtype_rag", "graph_subtype_rag")

# Must stay aligned with `run_stage_f_eval.py --rag-mode` choices (excluding "config").
VALID_COMPARE_MODES = frozenset({"no_rag", "flat_family_rag", "subtype_rag", "graph_subtype_rag"})


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run no_rag/flat/subtype/graph_subtype comparison.")
    parser.add_argument(
        "--eval-manifest",
        type=Path,
        default=Path("rag_experiment/outputs/eval_manifests/taco_test_family_difficulty_balanced_smoke24.jsonl"),
        help="JSONL manifest to evaluate.",
    )
    parser.add_argument(
        "--baseline-vs-graph",
        action="store_true",
        help="Shorthand: run only no_rag and graph_subtype_rag (same as --modes no_rag,graph_subtype_rag).",
    )
    parser.add_argument(
        "--modes",
        default=",".join(DEFAULT_MODES),
        help="Comma-separated modes: no_rag,flat_family_rag,subtype_rag,graph_subtype_rag.",
    )
    parser.add_argument("--retrieval-only", action="store_true", help="Run retrieval-only comparison.")
    parser.add_argument("--skip-graph-build", action="store_true", help="Do not build graph_subtype index first.")
    parser.add_argument("--force", action="store_true", help="Delete existing mode outputs before running.")
    parser.add_argument("--python", default=sys.executable, help="Python executable used for child scripts.")
    parser.add_argument("--seed", type=int, default=0, help="stable seed base; 0 means config experiment.seed")
    parser.add_argument("--run-tag", type=str, default="", help="optional run tag propagated to all modes")
    parser.add_argument("--gpu-policy", type=str, default="auto", help="metadata tag propagated to all modes")
    parser.add_argument(
        "--isolate-baseline-config",
        action="store_true",
        help="run no_rag without the graph/RAG RAG_CONFIG_EXTRA overlay unless --baseline-config-extra is set",
    )
    parser.add_argument(
        "--baseline-config-extra",
        default=None,
        help="optional RAG_CONFIG_EXTRA used only for no_rag when baseline config is isolated",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="if >0, only evaluate this many problems (forwarded to run_stage_f_eval.py)",
    )
    return parser.parse_args()


def _sanitize_stem(path: Path) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", path.stem).strip("_") or "manifest"


def _mode_paths(settings: Any, manifest: Path, mode: str, retrieval_only: bool, run_tag: str = "") -> dict[str, Path]:
    stem = _sanitize_stem(manifest)
    rag_tag = f"retrieval_only_{mode}" if retrieval_only else mode
    if run_tag:
        clean_run_tag = re.sub(r"[^a-zA-Z0-9_-]+", "_", run_tag).strip("_")
        if clean_run_tag:
            rag_tag = f"{rag_tag}_{clean_run_tag}"
    suffix = f"manifest_{stem}_{rag_tag}"
    return {
        "runs": settings.stage_dir("stage_f") / f"runs_{suffix}.jsonl",
        "metrics": settings.stage_dir("stage_f") / f"metrics_summary_{suffix}.json",
        "report": settings.reports_dir / f"experiment_report_{suffix}.md",
    }


def _run(cmd: list[str], *, cwd: Path, log: Any, env: dict[str, str] | None = None) -> None:
    log.info("Running: %s", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True, env=env)


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _pass_at_3(rows: list[dict[str, Any]]) -> float:
    by_problem: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_problem[row["problem_id"]].append(row)
    if not by_problem:
        return 0.0
    passed = sum(1 for runs in by_problem.values() if any(r.get("passed") for r in runs))
    return passed / len(by_problem)


def _pass_at_1(rows: list[dict[str, Any]]) -> float:
    return sum(1 for r in rows if r.get("passed")) / len(rows) if rows else 0.0


def _retrieval_hit_rate(rows: list[dict[str, Any]]) -> float:
    calls = [r for r in rows if r.get("retrieved_skill_ids")]
    return sum(1 for r in calls if r.get("retrieval_hit")) / len(calls) if calls else 0.0


def _breakdown(rows: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        value = row.get(key) or "unknown"
        groups[str(value)].append(row)
    out: dict[str, dict[str, Any]] = {}
    for value, group_rows in sorted(groups.items()):
        problem_ids = {r["problem_id"] for r in group_rows}
        out[value] = {
            "problems": len(problem_ids),
            "runs": len(group_rows),
            "pass_at_1": _pass_at_1(group_rows),
            "pass_at_3": _pass_at_3(group_rows),
            "retrieval_hit_rate": _retrieval_hit_rate(group_rows),
        }
    return out


def _summary_for_mode(paths: dict[str, Path]) -> dict[str, Any]:
    metrics = _load_json(paths["metrics"])
    rows = load_jsonl(paths["runs"]) if paths["runs"].exists() else []
    return {
        "metrics_path": str(paths["metrics"]),
        "runs_path": str(paths["runs"]),
        "report_path": str(paths["report"]),
        "total_problems": metrics.get("total_problems", 0),
        "total_runs": metrics.get("total_runs", 0),
        "pass_at_1": metrics.get("pass_at_1", 0.0),
        "sample_pass_rate": metrics.get("sample_pass_rate", metrics.get("pass_at_1", 0.0)),
        "first_sample_pass_rate": metrics.get("first_sample_pass_rate", 0.0),
        "pass_at_3": metrics.get("pass_at_3", 0.0),
        "retrieval": metrics.get("retrieval", {}),
        "by_difficulty": _breakdown(rows, "difficulty_bucket"),
        "by_scope": _breakdown(rows, "scope"),
    }


def _write_compare_report(path: Path, payload: dict[str, Any]) -> None:
    lines: list[str] = []
    lines.append("# Stage F 对比报告\n\n")
    lines.append(f"- Manifest: `{payload['manifest']}`\n")
    lines.append(f"- Retrieval only: `{payload['retrieval_only']}`\n")
    if payload.get("run_tag"):
        lines.append(f"- Run tag: `{payload['run_tag']}`\n")
    if int(payload.get("limit") or 0) > 0:
        lines.append(f"- Limit: `{payload['limit']}` problems\n")
    if payload.get("rag_config_extra"):
        lines.append(f"- RAG config extra: `{payload['rag_config_extra']}`\n")
    if payload.get("isolate_baseline_config"):
        baseline_extra = payload.get("baseline_config_extra") or "<base config>"
        lines.append(f"- Baseline config: `{baseline_extra}`\n")
    lines.append(f"- Modes: `{', '.join(payload['modes'])}`\n\n")

    lines.append("## Overall\n\n")
    lines.append("| mode | problems | runs | PASS@1 | r0 pass | PASS@3 | retrieval hit | router@1 | family@k | subtype@k | bundle@k | false mechanism |\n")
    lines.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |\n")
    for mode in payload["modes"]:
        item = payload["results"].get(mode, {})
        ret = item.get("retrieval", {})
        lines.append(
            f"| {mode} | {item.get('total_problems', 0)} | {item.get('total_runs', 0)} "
            f"| {item.get('pass_at_1', 0.0):.4f} | {item.get('first_sample_pass_rate', 0.0):.4f} "
            f"| {item.get('pass_at_3', 0.0):.4f} "
            f"| {ret.get('overall_correct_rate', 0.0):.4f} | {ret.get('router_top1_acc', 0.0):.4f} "
            f"| {ret.get('family_recall_at_k', 0.0):.4f} | {ret.get('subtype_recall_at_k', 0.0):.4f} "
            f"| {ret.get('bundle_recall_at_k', 0.0):.4f} | {ret.get('false_mechanism_rate', 0.0):.4f} |\n"
        )

    lines.append("\n## By Difficulty\n\n")
    for diff in ("easy", "medium", "hard", "unknown"):
        lines.append(f"### {diff}\n\n")
        lines.append("| mode | problems | PASS@1 | PASS@3 | retrieval hit |\n")
        lines.append("| --- | ---: | ---: | ---: | ---: |\n")
        for mode in payload["modes"]:
            st = payload["results"].get(mode, {}).get("by_difficulty", {}).get(diff, {})
            lines.append(
                f"| {mode} | {st.get('problems', 0)} | {st.get('pass_at_1', 0.0):.4f} "
                f"| {st.get('pass_at_3', 0.0):.4f} | {st.get('retrieval_hit_rate', 0.0):.4f} |\n"
            )
        lines.append("\n")

    lines.append("## By Scope\n\n")
    lines.append("| scope | mode | problems | PASS@1 | PASS@3 | retrieval hit |\n")
    lines.append("| --- | --- | ---: | ---: | ---: | ---: |\n")
    for scope in ("single", "multi", "unknown"):
        for mode in payload["modes"]:
            st = payload["results"].get(mode, {}).get("by_scope", {}).get(scope, {})
            lines.append(
                f"| {scope} | {mode} | {st.get('problems', 0)} | {st.get('pass_at_1', 0.0):.4f} "
                f"| {st.get('pass_at_3', 0.0):.4f} | {st.get('retrieval_hit_rate', 0.0):.4f} |\n"
            )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(lines), encoding="utf-8")


def main() -> int:
    args = _parse_args()
    settings = get_settings()
    setup_logging(settings.config["logging"]["level"], settings.output_dir / "run.log")
    log = get_logger("stage_f_compare")
    repo_root = settings.parent_root
    manifest = args.eval_manifest
    if not manifest.is_absolute():
        manifest = repo_root / manifest
    if not manifest.exists():
        raise FileNotFoundError(f"eval manifest not found: {manifest}")

    if args.baseline_vs_graph:
        modes_str = "no_rag,graph_subtype_rag"
    else:
        modes_str = args.modes
    modes = [m.strip() for m in modes_str.split(",") if m.strip()]
    bad = [m for m in modes if m not in VALID_COMPARE_MODES]
    if bad:
        raise ValueError(f"unknown modes: {bad}; valid: {sorted(VALID_COMPARE_MODES)}")

    if "graph_subtype_rag" in modes and not args.skip_graph_build:
        _run([args.python, "rag_experiment/scripts/run_stage_e_build_index.py", "--mode", "graph_subtype"], cwd=repo_root, log=log)

    results: dict[str, Any] = {}
    parent_env = os.environ.copy()
    for mode in modes:
        paths = _mode_paths(settings, manifest, mode, args.retrieval_only, args.run_tag)
        if args.force:
            for p in paths.values():
                if p.exists():
                    p.unlink()
        cmd = [
            args.python,
            "rag_experiment/scripts/run_stage_f_eval.py",
            "--eval-manifest",
            str(manifest),
            "--rag-mode",
            mode,
        ]
        if args.seed:
            cmd.extend(["--seed", str(args.seed)])
        if args.run_tag:
            cmd.extend(["--run-tag", args.run_tag])
        if args.gpu_policy:
            cmd.extend(["--gpu-policy", args.gpu_policy])
        if args.retrieval_only:
            cmd.append("--retrieval-only")
        if args.limit > 0:
            cmd.extend(["--limit", str(args.limit)])
        child_env = None
        if mode == "no_rag" and (args.isolate_baseline_config or args.baseline_config_extra is not None):
            child_env = parent_env.copy()
            if args.baseline_config_extra:
                child_env["RAG_CONFIG_EXTRA"] = args.baseline_config_extra
                log.info("no_rag baseline uses isolated RAG_CONFIG_EXTRA=%s", args.baseline_config_extra)
            else:
                child_env.pop("RAG_CONFIG_EXTRA", None)
                log.info("no_rag baseline uses base config with RAG_CONFIG_EXTRA unset")
        _run(cmd, cwd=repo_root, log=log, env=child_env)
        results[mode] = _summary_for_mode(paths)

    stem = _sanitize_stem(manifest)
    tag = "retrieval_only" if args.retrieval_only else "generation"
    clean_run_tag = re.sub(r"[^a-zA-Z0-9_-]+", "_", args.run_tag).strip("_") if args.run_tag else ""
    tag_suffix = f"_{clean_run_tag}" if clean_run_tag else ""
    payload = {
        "manifest": str(manifest),
        "retrieval_only": bool(args.retrieval_only),
        "modes": modes,
        "run_tag": args.run_tag or "",
        "limit": int(args.limit),
        "rag_config_extra": os.environ.get("RAG_CONFIG_EXTRA", ""),
        "isolate_baseline_config": bool(args.isolate_baseline_config or args.baseline_config_extra is not None),
        "baseline_config_extra": args.baseline_config_extra or "",
        "results": results,
    }
    json_path = settings.stage_dir("stage_f") / f"comparison_{stem}_{tag}{tag_suffix}.json"
    md_path = settings.reports_dir / f"comparison_report_{stem}_{tag}{tag_suffix}.md"
    save_json(json_path, payload)
    _write_compare_report(md_path, payload)
    log.info("Comparison JSON -> %s", json_path)
    log.info("Comparison report -> %s", md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
