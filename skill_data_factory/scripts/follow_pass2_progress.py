#!/usr/bin/env python3
"""Print one line whenever Pass2 writes a new labeled/quarantine row (polling, no inotify)."""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Follow Pass2 jsonl outputs (works with running pipeline).")
    p.add_argument("--track", choices=("single", "multi", "both"), default="single")
    p.add_argument("--interval", type=float, default=2.0, help="Poll interval seconds.")
    p.add_argument("--root", type=Path, default=ROOT / "outputs")
    return p.parse_args()


def _tail_new_lines(path: Path, offset: int) -> tuple[list[str], int]:
    if not path.exists():
        return [], offset
    size = path.stat().st_size
    if size < offset:
        offset = 0
    with path.open("r", encoding="utf-8") as fh:
        fh.seek(offset)
        chunk = fh.read()
        offset = fh.tell()
    return [ln for ln in chunk.splitlines() if ln.strip()], offset


def _format_row(track: str, row: dict, *, source: str) -> str:
    pid = row.get("problem_id", "")
    sid = row.get("solution_id", "")
    if source == "labeled":
        if track == "single":
            detail = f"subtype={row.get('primary_subtype')}"
        else:
            detail = f"composition={row.get('composition_key')}"
        return f"[{track}] OK {pid} {sid} {detail}"
    reason = row.get("quarantine_reason", "quarantine")
    return f"[{track}] QUARANTINE {pid} {sid} {reason}"


def main() -> int:
    args = _parse_args()
    tracks = ["single_algorithm", "multi_algorithm"] if args.track == "both" else [f"{args.track}_algorithm"]
    # normalize track label for display
    display = {"single_algorithm": "single", "multi_algorithm": "multi"}
    state: dict[str, int] = {}
    print(
        f"Following Pass2 outputs under {args.root} (poll every {args.interval}s). Ctrl+C to stop.",
        flush=True,
    )
    try:
        while True:
            for tdir in tracks:
                short = display.get(tdir, tdir)
                base = args.root / tdir / "pass2_label"
                paths = {
                    "labeled": base / "labeled_solutions.jsonl",
                    "quarantine": base / "quarantine.jsonl",
                }
                for name, path in paths.items():
                    key = f"{short}:{name}"
                    if key not in state:
                        state[key] = path.stat().st_size if path.exists() else 0
                    lines, state[key] = _tail_new_lines(path, state[key])
                    for line in lines:
                        try:
                            row = json.loads(line)
                        except json.JSONDecodeError:
                            continue
                        print(_format_row(short, row, source=name), flush=True)
            time.sleep(max(0.5, args.interval))
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
