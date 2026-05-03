"""Stage C runner.

Default: legacy family-level solution labeling.
Opt-in: verified subtype labeling from Stage C0 with rule-only or DeepSeek rerank.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.llm import build_deepseek_client, build_glm_client  # noqa: E402
from src.logging_utils import setup_logging, get_logger  # noqa: E402
from src.settings import get_settings  # noqa: E402
from src.stage_c_solution_label import (  # noqa: E402
    run_stage_c,
    run_stage_c_primary_deepseek,
    run_stage_c_verified_subtype,
)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Stage C solution labeling.")
    parser.add_argument(
        "--verified-subtype",
        action="store_true",
        help="Use Stage C0 full-pass solutions and output verified subtype labels.",
    )
    parser.add_argument(
        "--subtype-labeler",
        choices=("rule-only", "deepseek", "rule-primary-deepseek"),
        default="rule-only",
        help="Subtype path labeler. rule-primary-deepseek only reranks per-problem primary solutions.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Verified subtype smoke limit in solution rows; 0 means all.",
    )
    parser.add_argument(
        "--examples",
        type=int,
        default=0,
        help="Number of solution->subtype examples to log in verified subtype mode.",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume verified subtype output by skipping already labeled compatible solutions.",
    )
    parser.add_argument(
        "--log-every",
        type=int,
        default=100,
        help="Verified subtype progress log interval in eligible solution rows; 0 disables interval logs.",
    )
    parser.add_argument(
        "--deepseek-scope",
        choices=("single", "multi", "all"),
        default="single",
        help="Primary-only DeepSeek scope: single_clean, multi_clean, or all primary solutions.",
    )
    parser.add_argument(
        "--deepseek-budget",
        type=int,
        default=0,
        help="Maximum primary-solution DeepSeek calls; 0 means unlimited.",
    )
    parser.add_argument(
        "--max-runtime-hours",
        type=float,
        default=0.0,
        help="Stop primary-solution DeepSeek calls after this many hours; 0 means unlimited.",
    )
    parser.add_argument(
        "--scope",
        choices=("single", "multi"),
        default="multi",
        help="Legacy Stage C scope. Ignored by --verified-subtype.",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    settings = get_settings()
    setup_logging(settings.config["logging"]["level"], settings.output_dir / "run.log")
    log = get_logger("stage_c")

    if args.verified_subtype:
        log.info(
            "Starting Stage C verified subtype: labeler=%s limit=%s examples=%s resume=%s log_every=%s",
            args.subtype_labeler,
            args.limit,
            args.examples,
            args.resume,
            args.log_every,
        )
        subtype_llm = None
        if args.subtype_labeler in {"deepseek", "rule-primary-deepseek"}:
            log.info(
                "DeepSeek subtype rerank enabled: model=%s base_url=%s",
                settings.deepseek.model,
                settings.deepseek.base_url,
            )
            subtype_llm = build_deepseek_client(settings.deepseek)
        if args.subtype_labeler == "rule-primary-deepseek":
            paths = run_stage_c_primary_deepseek(
                settings,
                subtype_llm=subtype_llm,
                deepseek_scope=args.deepseek_scope,
                budget=args.deepseek_budget,
                max_runtime_hours=args.max_runtime_hours,
                limit=args.limit,
                examples=args.examples,
                resume=args.resume,
                log_every=args.log_every,
            )
            for name, path in paths.items():
                log.info("%s -> %s", name, path)
            log.info("Stage C primary-only DeepSeek done.")
            return 0
        paths = run_stage_c_verified_subtype(
            settings,
            labeler=args.subtype_labeler,
            subtype_llm=subtype_llm,
            limit=args.limit,
            examples=args.examples,
            resume=args.resume,
            log_every=args.log_every,
        )
        for name, path in paths.items():
            log.info("%s -> %s", name, path)
        log.info("Stage C verified subtype done.")
        return 0

    log.info("Starting Stage C - legacy solution labeling with GLM")
    glm = build_glm_client(settings.glm)
    run_stage_c(settings, glm, scope=args.scope)
    log.info("Stage C done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
