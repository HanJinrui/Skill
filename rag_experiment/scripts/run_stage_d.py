"""Stage D runner — synthesize the algorithm-skill knowledge base."""
from __future__ import annotations

import fcntl
import os
import sys
from contextlib import contextmanager
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.llm import build_glm_client  # noqa: E402
from src.logging_utils import setup_logging, get_logger  # noqa: E402
from src.settings import get_settings  # noqa: E402
from src.stage_d_skill_build import run_stage_d  # noqa: E402


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


def main() -> int:
    settings = get_settings()
    setup_logging(settings.config["logging"]["level"], settings.output_dir / "run.log")
    log = get_logger("stage_d")
    lock_path = settings.output_dir / "stage_d.lock"
    try:
        with _stage_lock(lock_path):
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
