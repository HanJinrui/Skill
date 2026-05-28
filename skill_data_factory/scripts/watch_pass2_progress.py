"""Watch Pass2 DeepSeek labeling progress and estimate ETA."""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT.parent / "rag_experiment"))

from sdf.factory_settings import get_settings  # noqa: F401,E402


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Watch Pass2 DeepSeek labeling progress.")
    p.add_argument("--interval", type=float, default=15.0, help="Refresh seconds (default 15).")
    p.add_argument("--once", action="store_true", help="Print one snapshot and exit.")
    p.add_argument("--no-clear", action="store_true", help="Do not clear screen between refreshes.")
    p.add_argument(
        "--track",
        choices=("single", "multi", "both"),
        default="both",
        help="Which track to show (default both).",
    )
    return p.parse_args()


def _load_yaml_pass2() -> dict[str, Any]:
    settings = get_settings()
    raw = settings.config.get("pass2") or {}
    return dict(raw) if isinstance(raw, dict) else {}


def _unique_solution_keys(path: Path) -> set[tuple[str, str]]:
    keys: set[tuple[str, str]] = set()
    if not path.exists():
        return keys
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            keys.add((str(row.get("problem_id") or ""), str(row.get("solution_id") or "")))
    return keys


def _planned_slots(solutions_path: Path, *, max_per_problem: int) -> tuple[int, int]:
    """Return (num_problems, max_llm_slots)."""
    by_problem: dict[str, int] = defaultdict(int)
    if not solutions_path.exists():
        return 0, 0
    with solutions_path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            pid = str(row.get("problem_id") or "")
            if pid:
                by_problem[pid] += 1
    cap = max(1, int(max_per_problem))
    slots = sum(min(n, cap) for n in by_problem.values())
    return len(by_problem), slots


def _parse_log_phase(log_path: Path) -> dict[str, Any]:
    info: dict[str, Any] = {
        "phase": "unknown",
        "pass2_single_started": None,
        "pass2_multi_started": None,
        "truncation_warnings": 0,
        "last_log_line": "",
    }
    if not log_path.exists():
        return info
    phase_re = re.compile(r"=== Pass(\d+) (\w+)")
    ts_re = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")
    with log_path.open("r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            info["last_log_line"] = line.strip()[:200]
            m = ts_re.match(line)
            ts = None
            if m:
                try:
                    ts = datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S").timestamp()
                except ValueError:
                    ts = None
            if "=== Pass2 single ===" in line and ts:
                info["pass2_single_started"] = ts
                info["phase"] = "pass2_single"
            if "=== Pass2 multi ===" in line and ts:
                info["pass2_multi_started"] = ts
                info["phase"] = "pass2_multi"
            if "=== Pass3" in line:
                info["phase"] = "pass3"
            if "Pass2 single done" in line:
                info["phase"] = "pass2_multi_pending"
            if "truncated at max_tokens" in line or "finish_reason=length" in line:
                info["truncation_warnings"] += 1
    return info


def _format_duration(seconds: float | None) -> str:
    if seconds is None or seconds < 0:
        return "—"
    s = int(seconds)
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    if h:
        return f"{h}h {m}m"
    if m:
        return f"{m}m {sec}s"
    return f"{sec}s"


def _format_time(ts: float | None) -> str:
    if ts is None:
        return "—"
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


def _track_snapshot(settings: Any, track: str, p2: dict[str, Any], log_info: dict[str, Any]) -> dict[str, Any]:
    track_dir = "single_algorithm" if track == "single" else "multi_algorithm"
    pass1_dir = settings.pass1_dir(track_dir)
    pass2_dir = settings.pass2_dir(track_dir)
    max_per = int(p2.get("max_llm_solutions_per_problem", 3))

    problems_n, planned = _planned_slots(pass1_dir / "solutions.jsonl", max_per_problem=max_per)
    processed = _unique_solution_keys(pass2_dir / "rule_candidates.jsonl")
    labeled = _unique_solution_keys(pass2_dir / "labeled_solutions.jsonl")
    quarantine = _unique_solution_keys(pass2_dir / "quarantine.jsonl")
    quarantine_only = quarantine - labeled

    done_slots = len(processed)
    remaining = max(0, planned - done_slots)
    pct = (done_slots / planned * 100.0) if planned else 0.0

    start_key = "pass2_single_started" if track == "single" else "pass2_multi_started"
    started = log_info.get(start_key)
    if started is None and track == "single":
        started = log_info.get("pass2_single_started")
    elapsed = (time.time() - started) if started else None
    rate_h = (done_slots / (elapsed / 3600.0)) if elapsed and elapsed > 60 and done_slots else 0.0
    eta_s = (remaining / rate_h * 3600.0) if rate_h > 0 else None
    finish_at = (time.time() + eta_s) if eta_s is not None else None

    return {
        "track": track,
        "problems": problems_n,
        "planned_slots": planned,
        "processed": done_slots,
        "labeled": len(labeled),
        "quarantine_only": len(quarantine_only),
        "remaining": remaining,
        "pct": pct,
        "elapsed": elapsed,
        "rate_per_hour": rate_h,
        "eta": eta_s,
        "finish_at": finish_at,
        "pass2_dir": pass2_dir,
    }


def _render(snapshots: list[dict[str, Any]], log_info: dict[str, Any], p2: dict[str, Any]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        f"Pass2 DeepSeek labeling  |  {now}",
        f"model: deepseek-v4-pro (from .env)  |  max {p2.get('max_llm_solutions_per_problem', 3)} solutions/problem",
        f"pipeline phase (from run.log): {log_info.get('phase', 'unknown')}",
        f"truncation warnings in log (cumulative): {log_info.get('truncation_warnings', 0)}",
        "",
    ]
    for s in snapshots:
        lines.extend(
            [
                f"── {s['track']} ({s['track']}_algorithm) ──",
                f"  problems routed      : {s['problems']}",
                f"  planned LLM slots    : {s['planned_slots']}  (unique solutions, cap {p2.get('max_llm_solutions_per_problem', 3)}/problem)",
                f"  processed (unique)   : {s['processed']}  ({s['pct']:.1f}%)",
                f"  ├─ labeled OK        : {s['labeled']}",
                f"  └─ quarantine only   : {s['quarantine_only']}",
                f"  remaining slots      : {s['remaining']}",
                f"  elapsed (this track) : {_format_duration(s['elapsed'])}",
                f"  rate                 : {s['rate_per_hour']:.1f} solutions/h" if s["rate_per_hour"] else "  rate                 : — (waiting for data)",
                f"  ETA                  : {_format_duration(s['eta'])}",
                f"  est. finish          : {_format_time(s['finish_at'])}",
                f"  output               : {s['pass2_dir']}",
                "",
            ]
        )
    if log_info.get("last_log_line"):
        lines.append(f"last log: {log_info['last_log_line'][:120]}")
    lines.append("Ctrl+C to exit watch")
    return "\n".join(lines)


def main() -> int:
    args = _parse_args()
    settings = get_settings()
    p2 = _load_yaml_pass2()
    log_path = settings.factory_root / "run.log"
    tracks = ["single", "multi"] if args.track == "both" else [args.track]

    try:
        while True:
            log_info = _parse_log_phase(log_path)
            snapshots = [_track_snapshot(settings, t, p2, log_info) for t in tracks]
            if not args.once and not args.no_clear:
                print("\033[2J\033[H", end="")
            print(_render(snapshots, log_info, p2), flush=True)
            if args.once:
                return 0
            time.sleep(max(1.0, float(args.interval)))
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
