"""Stage B runner — problem-level skill labeling with GLM."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.llm import build_glm_client  # noqa: E402
from src.logging_utils import setup_logging, get_logger  # noqa: E402
from src.settings import get_settings  # noqa: E402
from src.stage_b_problem_label import run_stage_b  # noqa: E402


def main() -> int:
    settings = get_settings()
    setup_logging(settings.config["logging"]["level"], settings.output_dir / "run.log")
    log = get_logger("stage_b")
    log.info("Starting Stage B — problem labeling with GLM %s", settings.glm.model)
    glm = build_glm_client(settings.glm)
    run_stage_b(settings, glm, scope="multi")
    log.info("Stage B done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
