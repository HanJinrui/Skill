from __future__ import annotations

import logging
import sys
from pathlib import Path

_INIT_DONE = False


def setup_logging(level: str = "INFO", log_file: Path | None = None) -> None:
    global _INIT_DONE
    if _INIT_DONE:
        return
    handlers: list[logging.Handler] = []
    fmt = "%(asctime)s | %(levelname)-7s | %(name)s | %(message)s"
    formatter = logging.Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S")
    stderr = logging.StreamHandler(sys.stderr)
    stderr.setFormatter(formatter)
    handlers.append(stderr)
    if log_file is not None:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(log_file, encoding="utf-8")
        fh.setFormatter(formatter)
        handlers.append(fh)
    root = logging.getLogger()
    root.setLevel(getattr(logging, level.upper(), logging.INFO))
    for h in list(root.handlers):
        root.removeHandler(h)
    for h in handlers:
        root.addHandler(h)
    _INIT_DONE = True


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
