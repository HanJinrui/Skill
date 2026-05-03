"""Stage C0 runner - verify raw TACO train reference solutions.

Usage:
    python scripts/run_stage_c0_verify.py --limit 5 --max-tests 3
    python scripts/run_stage_c0_verify.py --problem-ids taco_train_000584 --max-tests 3
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.logging_utils import get_logger, setup_logging  # noqa: E402
from src.settings import get_settings  # noqa: E402
from src.stage_c0_verify import StageC0Overrides, run_stage_c0  # noqa: E402


def _parse_problem_ids(raw_values: list[str]) -> set[str]:
    out: set[str] = set()
    for raw in raw_values:
        for part in raw.split(","):
            value = part.strip()
            if value:
                out.add(value)
    return out


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Stage C0: verify raw TACO train reference solutions and build base datasets."
    )
    parser.add_argument("--limit", type=int, default=0, help="maximum number of parsed TACO train problems to process")
    parser.add_argument(
        "--problem-ids",
        nargs="*",
        default=[],
        help="optional problem ids to process; accepts repeated values or comma-separated ids",
    )
    parser.add_argument(
        "--max-tests",
        type=int,
        default=None,
        help="override stage_c0.max_tests_per_solution; <=0 means all available tests",
    )
    parser.add_argument(
        "--max-solutions",
        type=int,
        default=None,
        help="override stage_c0.max_solutions_per_problem; <=0 means all reference solutions",
    )
    parser.add_argument(
        "--no-progress",
        action="store_true",
        help="disable the terminal progress bar; progress log lines are still written",
    )
    parser.add_argument(
        "--log-every",
        type=int,
        default=None,
        help="write a progress log line every N parsed problems",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="append to existing Stage C0 artifacts and skip problems already present in router_dataset.jsonl",
    )
    parser.add_argument(
        "--verified-source",
        choices=["local", "taco-verified"],
        default=None,
        help="solution correctness source: local executor or external likaixin/TACO-verified",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    settings = get_settings()
    log_file = settings.output_dir / "run.log"
    setup_logging(settings.config["logging"]["level"], log_file)
    log = get_logger("stage_c0")
    problem_ids = _parse_problem_ids(args.problem_ids)
    max_solutions = args.max_solutions
    if max_solutions is not None and max_solutions <= 0:
        max_solutions = 0
    max_tests = args.max_tests
    if max_tests is not None and max_tests <= 0:
        max_tests = 0
    log.info(
        "Starting Stage C0: limit=%d problem_ids=%d max_tests=%s max_solutions=%s "
        "progress=%s log_every=%s resume=%s verified_source=%s",
        args.limit,
        len(problem_ids),
        max_tests,
        max_solutions,
        not args.no_progress,
        args.log_every,
        args.resume,
        args.verified_source,
    )
    log.info("Stage C0 logs are written to %s", log_file)
    paths = run_stage_c0(
        settings,
        StageC0Overrides(
            limit=args.limit,
            problem_ids=problem_ids or None,
            max_tests=max_tests,
            max_solutions=max_solutions,
            show_progress=not args.no_progress,
            log_every=args.log_every,
            resume=args.resume,
            verified_source=args.verified_source,
        ),
    )
    for name, path in paths.items():
        log.info("%s -> %s", name, path)
    log.info("Stage C0 done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
