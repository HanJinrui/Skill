"""Add rag_experiment package root to sys.path."""
from __future__ import annotations

import sys
from pathlib import Path

_FACTORY_ROOT = Path(__file__).resolve().parents[2]
_RAG_ROOT = (_FACTORY_ROOT / ".." / "rag_experiment").resolve()

if str(_RAG_ROOT) not in sys.path:
    sys.path.insert(0, str(_RAG_ROOT))

FACTORY_ROOT = _FACTORY_ROOT
RAG_ROOT = _RAG_ROOT
