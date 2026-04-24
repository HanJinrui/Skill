"""Stage A runner.

Usage:
    python scripts/run_stage_a.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.logging_utils import setup_logging, get_logger  # noqa: E402
from src.settings import get_settings  # noqa: E402
from src.stage_a_filter import select_problems  # noqa: E402


def main() -> int:
    settings = get_settings()
    setup_logging(
        settings.config["logging"]["level"],
        settings.output_dir / "run.log",
    )
    log = get_logger("stage_a")
    log.info("Starting Stage A — TACO selection (raw BAAI/TACO train split)")
    stats = select_problems(settings)
    log.info("Finished Stage A. Unique selected: %d", stats.selected_unique)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
