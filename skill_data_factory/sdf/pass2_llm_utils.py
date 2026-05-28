"""Shared Pass2 DeepSeek JSON labeling with truncation-aware retries."""
from __future__ import annotations

from typing import Any

from src.deepseek_limits import DEEPSEEK_V4_MAX_OUTPUT_TOKENS
from src.llm.base import LLMError
from src.logging_utils import get_logger

LOG = get_logger(__name__)


def _is_truncation_error(exc: LLMError) -> bool:
    msg = str(exc).lower()
    return "truncated" in msg or "finish_reason=length" in msg


def pass2_base_max_tokens(p2: dict[str, Any], *, track: str) -> int:
    default = 12288 if track == "multi" else 4096
    if track == "multi":
        return int(p2.get("llm_max_tokens_multi", p2.get("llm_max_tokens", default)))
    return int(p2.get("llm_max_tokens_single", p2.get("llm_max_tokens", default)))


def pass2_token_ceiling(p2: dict[str, Any], *, track: str) -> int:
    per_track = p2.get("llm_max_tokens_ceiling_multi" if track == "multi" else "llm_max_tokens_ceiling_single")
    ceiling = int(per_track or p2.get("llm_max_tokens_ceiling", 24576 if track == "multi" else 12288))
    return min(DEEPSEEK_V4_MAX_OUTPUT_TOKENS, ceiling)


def pass2_max_retries(p2: dict[str, Any], *, track: str) -> int:
    if track == "multi":
        return max(1, int(p2.get("max_llm_retries_multi", 2)))
    return max(1, int(p2.get("max_llm_retries", 3)))


def pass2_input_limits(p2: dict[str, Any], *, track: str) -> tuple[int, int, int]:
    if track == "multi":
        return (
            int(p2.get("pass2_multi_max_statement_chars", 1200)),
            int(p2.get("pass2_multi_max_code_chars", 2800)),
            int(p2.get("pass2_multi_max_rule_candidates", 8)),
        )
    return (
        int(p2.get("pass2_single_max_statement_chars", 1800)),
        int(p2.get("pass2_single_max_code_chars", 4000)),
        8,
    )


def pass2_truncation_jump_to_ceiling(p2: dict[str, Any]) -> bool:
    return bool(p2.get("llm_truncation_jump_to_ceiling", True))


def chat_json_label(
    client: Any,
    *,
    system: str,
    user: str,
    base_max_tokens: int,
    max_retries: int,
    token_ceiling: int,
    log_label: str,
    temperature: float = 0.0,
    jump_to_ceiling_on_truncation: bool = False,
) -> dict[str, Any]:
    """Call chat_json; on truncation, bump max_tokens (optionally jump straight to ceiling)."""
    max_tokens = max(512, int(base_max_tokens))
    ceiling = max(max_tokens, int(token_ceiling))
    last_exc: LLMError | None = None

    for attempt in range(max(1, int(max_retries))):
        try:
            return client.chat_json(
                system=system,
                user=user,
                temperature=temperature,
                max_tokens=max_tokens,
            )
        except LLMError as exc:
            last_exc = exc
            if not _is_truncation_error(exc) or attempt + 1 >= max_retries:
                LOG.warning("%s attempt %d failed: %s", log_label, attempt + 1, exc)
                break
            if jump_to_ceiling_on_truncation and ceiling > max_tokens:
                bumped = ceiling
            else:
                bumped = min(ceiling, max(max_tokens + 1024, int(round(max_tokens * 1.5))))
            if bumped <= max_tokens:
                LOG.warning(
                    "%s attempt %d truncated at max_tokens=%d (ceiling reached)",
                    log_label,
                    attempt + 1,
                    max_tokens,
                )
                break
            LOG.warning(
                "%s attempt %d truncated at max_tokens=%d; retrying with %d",
                log_label,
                attempt + 1,
                max_tokens,
                bumped,
            )
            max_tokens = bumped

    if last_exc is not None:
        raise last_exc
    raise LLMError(f"{log_label}: labeling failed without a response")
