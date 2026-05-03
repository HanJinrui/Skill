"""Stage D runner — synthesize the algorithm-skill knowledge base."""
from __future__ import annotations

import fcntl
import os
import argparse
import sys
from contextlib import contextmanager
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.llm import build_deepseek_client, build_glm_client  # noqa: E402
from src.logging_utils import setup_logging, get_logger  # noqa: E402
from src.settings import get_settings  # noqa: E402
from src.stage_d_skill_build import run_stage_d, run_stage_d_v2  # noqa: E402


@contextmanager
def _stage_lock(lock_path: Path):
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with open(lock_path, "a+", encoding="utf-8") as fh:
        try:
            fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise RuntimeError(
                f"Another Stage D process is already running. Lock file: {lock_path}"
            ) from exc
        fh.seek(0)
        fh.truncate(0)
        fh.write(str(os.getpid()))
        fh.flush()
        try:
            yield
        finally:
            fh.seek(0)
            fh.truncate(0)
            fcntl.flock(fh.fileno(), fcntl.LOCK_UN)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Stage D skill synthesis.")
    parser.add_argument("--v2", action="store_true", help="Build hierarchical Stage D v2 skills.")
    parser.add_argument(
        "--skill-writer",
        choices=("rule-only", "deepseek"),
        default="rule-only",
        help="Stage D v2 writer: deterministic draft only or DeepSeek rewrite with rule fallback.",
    )
    parser.add_argument("--resume", action="store_true", help="Resume Stage D v2 by skipping existing skill_ids.")
    parser.add_argument("--log-every", type=int, default=5, help="Stage D v2 progress interval in skills.")
    parser.add_argument("--limit-skills", type=int, default=0, help="Stage D v2 smoke limit; 0 means all.")
    parser.add_argument("--examples", type=int, default=5, help="Number of examples to keep in Stage D v2 logs/summary.")
    parser.add_argument("--deepseek-timeout", type=float, default=180.0, help="Stage D v2 DeepSeek request timeout in seconds.")
    parser.add_argument("--skill-writer-retries", type=int, default=2, help="DeepSeek writer retries per skill after the first attempt.")
    parser.add_argument("--skill-writer-backoff", type=float, default=8.0, help="Seconds to wait before DeepSeek writer retries; multiplied by attempt index.")
    parser.add_argument("--skill-writer-max-tokens", type=int, default=1800, help="Max output tokens for each DeepSeek skill rewrite.")
    parser.add_argument("--skill-writer-examples", type=int, default=2, help="Representative examples sent to DeepSeek per skill.")
    parser.add_argument("--skill-writer-statement-chars", type=int, default=360, help="Problem excerpt chars sent to DeepSeek per example.")
    parser.add_argument("--skill-writer-code-chars", type=int, default=240, help="Solution excerpt chars sent to DeepSeek per example.")
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    settings = get_settings()
    setup_logging(settings.config["logging"]["level"], settings.output_dir / "run.log")
    log = get_logger("stage_d")
    lock_path = settings.output_dir / "stage_d.lock"
    try:
        with _stage_lock(lock_path):
            if args.v2:
                log.info(
                    "Starting Stage D v2 - hierarchical skills writer=%s resume=%s limit_skills=%s",
                    args.skill_writer,
                    args.resume,
                    args.limit_skills,
                )
                writer_llm = None
                if args.skill_writer == "deepseek":
                    deepseek_config = replace(settings.deepseek, timeout=args.deepseek_timeout)
                    log.info(
                        "Stage D v2 DeepSeek writer enabled: model=%s base_url=%s timeout=%.1fs retries=%d max_tokens=%d",
                        deepseek_config.model,
                        deepseek_config.base_url,
                        deepseek_config.timeout,
                        args.skill_writer_retries,
                        args.skill_writer_max_tokens,
                    )
                    writer_llm = build_deepseek_client(deepseek_config)
                paths = run_stage_d_v2(
                    settings,
                    writer=args.skill_writer,
                    llm=writer_llm,
                    resume=args.resume,
                    log_every=args.log_every,
                    limit_skills=args.limit_skills,
                    examples=args.examples,
                    writer_retries=args.skill_writer_retries,
                    writer_backoff_seconds=args.skill_writer_backoff,
                    writer_max_tokens=args.skill_writer_max_tokens,
                    writer_examples=args.skill_writer_examples,
                    writer_statement_chars=args.skill_writer_statement_chars,
                    writer_code_chars=args.skill_writer_code_chars,
                )
                log.info("Stage D v2 outputs: %s", paths)
                return 0
            log.info(
                "Starting Stage D — skill synthesis with model=%s base_url=%s",
                settings.glm.model,
                settings.glm.base_url,
            )
            glm = build_glm_client(settings.glm)
            paths = run_stage_d(settings, glm)
            log.info("Stage D outputs: %s", paths)
    except RuntimeError as exc:
        log.error("%s", exc)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
