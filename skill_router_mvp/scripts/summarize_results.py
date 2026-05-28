#!/usr/bin/env python3
"""Aggregate previously persisted RunTrace JSONL without invoking models."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.io_utils import load_jsonl, write_json  # noqa: E402
from src.metrics import aggregate  # noqa: E402
from src.schemas import AnnotationRow, RunTrace  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize independent skill-router runs.")
    parser.add_argument("runs", nargs="+", type=Path)
    parser.add_argument("--annotations", type=Path, default=None)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    traces = [RunTrace.model_validate(row) for path in args.runs for row in load_jsonl(path)]
    annotations = (
        [AnnotationRow.model_validate(row) for row in load_jsonl(args.annotations)]
        if args.annotations
        else None
    )
    metrics = aggregate(traces, annotations)
    if args.output:
        write_json(args.output, metrics)
    print(json.dumps(metrics, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
