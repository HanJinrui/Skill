"""Zhipu GLM client implemented via the OpenAI-compatible SDK.

ZHIPU_API_KEY must be set. Defaults to `https://open.bigmodel.cn/api/paas/v4/`
and `glm-4.7`, both overridable via env vars.
"""
from __future__ import annotations

import time
from typing import Any

from openai import APIConnectionError, APITimeoutError, InternalServerError, OpenAI, RateLimitError

from ..settings import GLMConfig
from .base import ChatLLM, LLMError, parse_json_object


class RetryableGLMError(LLMError):
    """Transient provider error worth retrying."""

    def __init__(
        self,
        message: str,
        *,
        kind: str = "transient",
        retry_after_seconds: float | None = None,
    ) -> None:
        super().__init__(message)
        self.kind = kind
        self.retry_after_seconds = retry_after_seconds


class GLMClient:
    provider = "zhipu_glm"

    _MAX_ATTEMPTS = 4
    _BACKOFF_MIN_SECONDS = 2.0
    _BACKOFF_MAX_SECONDS = 30.0

    def __init__(self, config: GLMConfig) -> None:
        if not config.api_key:
            raise LLMError("ZHIPU_API_KEY is missing; set it in .env before running labeling stages.")
        self.config = config
        self.model = config.model
        self._client = OpenAI(
            api_key=config.api_key,
            base_url=config.base_url,
            timeout=config.timeout,
            max_retries=0,
        )

    def _call(
        self,
        system: str,
        user: str,
        *,
        temperature: float,
        max_tokens: int,
        response_format_json: bool,
    ) -> str:
        kwargs: dict[str, Any] = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        if response_format_json:
            kwargs["response_format"] = {"type": "json_object"}
        last_error: RetryableGLMError | None = None
        for attempt in range(1, self._MAX_ATTEMPTS + 1):
            try:
                response = self._client.chat.completions.create(**kwargs)
            except RateLimitError as exc:
                err = self._translate_rate_limit(exc)
                if not isinstance(err, RetryableGLMError) or attempt >= self._MAX_ATTEMPTS:
                    raise err from exc
                last_error = err
                self._sleep_before_retry(err, attempt)
                continue
            except (APITimeoutError, APIConnectionError, InternalServerError) as exc:
                err = RetryableGLMError(
                    f"Transient Zhipu API error: {exc}",
                    kind="transport",
                )
                if attempt >= self._MAX_ATTEMPTS:
                    raise err from exc
                last_error = err
                self._sleep_before_retry(err, attempt)
                continue

            if not response.choices:
                err = RetryableGLMError("GLM returned no choices", kind="empty_choice")
                if attempt >= self._MAX_ATTEMPTS:
                    raise err
                last_error = err
                self._sleep_before_retry(err, attempt)
                continue

            content = response.choices[0].message.content
            if not content:
                err = RetryableGLMError("GLM returned empty content", kind="empty_content")
                if attempt >= self._MAX_ATTEMPTS:
                    raise err
                last_error = err
                self._sleep_before_retry(err, attempt)
                continue

            return content

        raise last_error or LLMError("GLM call failed without an explicit error")

    def _translate_rate_limit(self, exc: RateLimitError) -> LLMError:
        body = getattr(exc, "body", None)
        error: dict[str, Any] = body.get("error", {}) if isinstance(body, dict) else {}
        code = str(error.get("code", "")).strip()
        message = str(error.get("message") or exc).strip()
        if code == "1113" or "余额不足" in message or "无可用资源包" in message:
            return LLMError(
                "Zhipu API request rejected: account balance is insufficient or no resource package is available. "
                f"Provider message: {message}"
            )
        return RetryableGLMError(
            f"Zhipu API rate-limited the request: {message}",
            kind="rate_limit",
            retry_after_seconds=self._extract_retry_after_seconds(exc),
        )

    def _extract_retry_after_seconds(self, exc: RateLimitError) -> float | None:
        response = getattr(exc, "response", None)
        headers = getattr(response, "headers", None) or {}
        if not hasattr(headers, "get"):
            return None
        for key in ("retry-after", "x-ratelimit-reset-after"):
            raw = headers.get(key)
            if raw is None:
                continue
            try:
                value = float(str(raw).strip())
            except ValueError:
                continue
            if value > 0:
                return value
        return None

    def _sleep_before_retry(self, err: RetryableGLMError, attempt: int) -> None:
        if err.retry_after_seconds is not None:
            delay = err.retry_after_seconds
        elif err.kind == "rate_limit":
            delay = min(self._BACKOFF_MAX_SECONDS, max(8.0, 4.0 * attempt))
        else:
            delay = min(
                self._BACKOFF_MAX_SECONDS,
                max(self._BACKOFF_MIN_SECONDS, 1.5 * (2 ** (attempt - 1))),
            )
        time.sleep(delay)

    def chat_json(
        self,
        system: str,
        user: str,
        *,
        temperature: float | None = None,
        max_tokens: int | None = None,
        response_format_json: bool = True,
    ) -> dict[str, Any]:
        temp = self.config.temperature if temperature is None else temperature
        max_tok = self.config.max_tokens if max_tokens is None else max_tokens
        rescue_system = (
            system.rstrip()
            + "\n\nReturn exactly one raw JSON object. Do not emit markdown fences, prose, or an empty response."
        )

        try:
            raw = self._call(
                system=system,
                user=user,
                temperature=temp,
                max_tokens=max_tok,
                response_format_json=response_format_json,
            )
        except RetryableGLMError as exc:
            if not response_format_json or exc.kind not in {"empty_choice", "empty_content"}:
                raise
            raw = self._call(
                system=rescue_system,
                user=user,
                temperature=0.0,
                max_tokens=max_tok,
                response_format_json=False,
            )
            return parse_json_object(raw)

        try:
            return parse_json_object(raw)
        except LLMError:
            if not response_format_json:
                raise
            raw = self._call(
                system=rescue_system,
                user=user,
                temperature=0.0,
                max_tokens=max_tok,
                response_format_json=False,
            )
            return parse_json_object(raw)


def build_glm_client(config: GLMConfig) -> ChatLLM:
    return GLMClient(config)
