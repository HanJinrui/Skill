"""One-line Pass2 progress logging (grep-friendly)."""
from __future__ import annotations

import time
from pathlib import Path
from typing import Any

from sdf.io_utils import read_jsonl
from src.logging_utils import get_logger

LOG = get_logger(__name__)


def load_pass2_resume_keys(
    out_dir: Path,
    *,
    resume: bool,
    retry_quarantine: bool = False,
) -> set[str]:
    """Keys already attempted in a prior Pass2 run.

    By default resume skips labeled, quarantine, and rule_candidates rows so work continues
    forward without re-picking the same solutions. Set retry_quarantine to re-LLM only
    quarantine rows (still skips labeled).
    """
    if not resume:
        return set()
    done: set[str] = set()
    names = ["labeled_solutions.jsonl", "rule_candidates.jsonl"]
    if not retry_quarantine:
        names.append("quarantine.jsonl")
    for name in names:
        path = out_dir / name
        if not path.exists():
            continue
        for row in read_jsonl(path):
            pid = row.get("problem_id")
            sid = row.get("solution_id")
            if pid and sid:
                done.add(f"{pid}::{sid}")
    return done


def count_planned_slots(by_problem: dict[str, list[Any]], *, max_per_problem: int) -> int:
    cap = max(1, int(max_per_problem))
    return sum(min(len(rows), cap) for rows in by_problem.values())


class Pass2Progress:
    """Emit one log line after each solution labeling attempt."""

    def __init__(self, *, track: str, total_slots: int, already_done: int = 0) -> None:
        self.track = track
        self.total_slots = max(0, int(total_slots))
        self.done = max(0, int(already_done))
        self.labeled = 0
        self.quarantine = 0
        self._started = time.monotonic()

    def log_skip_resume(self, problem_id: str, solution_id: str) -> None:
        LOG.info(
            "Pass2 %s progress skip-resume %s %s (already labeled)",
            self.track,
            problem_id,
            solution_id,
        )

    def log_item(
        self,
        *,
        problem_id: str,
        solution_id: str,
        status: str,
        detail: str = "",
    ) -> None:
        self.done += 1
        if status == "ok":
            self.labeled += 1
        elif status.startswith("quarantine"):
            self.quarantine += 1

        elapsed = time.monotonic() - self._started
        rate_h = (self.done / elapsed * 3600.0) if elapsed > 1.0 else 0.0
        remaining = max(0, self.total_slots - self.done)
        eta_h = (remaining / rate_h) if rate_h > 0 else 0.0
        pct = (self.done / self.total_slots * 100.0) if self.total_slots else 0.0

        extra = f" {detail}" if detail else ""
        LOG.info(
            "Pass2 %s progress [%d/%d] %.1f%% %s %s %s%s | labeled=%d quarantine=%d ETA~%.1fh",
            self.track,
            self.done,
            self.total_slots,
            pct,
            status,
            problem_id,
            solution_id,
            extra,
            self.labeled,
            self.quarantine,
            eta_h,
        )
