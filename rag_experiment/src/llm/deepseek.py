"""DeepSeek chat client using the OpenAI-compatible SDK."""
from __future__ import annotations

from typing import Any

from openai import APIConnectionError, APITimeoutError, InternalServerError, OpenAI, RateLimitError

from ..settings import DeepSeekConfig
from .base import ChatLLM, LLMError, parse_json_object


class DeepSeekClient:
    provider = "deepseek"

    def __init__(self, config: DeepSeekConfig) -> None:
        if not config.api_key:
            raise LLMError("DEEPSEEK_API_KEY is missing; set it in .env before using --subtype-labeler deepseek.")
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
        try:
            response = self._client.chat.completions.create(**kwargs)
        except (APIConnectionError, APITimeoutError, InternalServerError, RateLimitError) as exc:
            raise LLMError(f"DeepSeek API request failed: {exc}") from exc
        if not response.choices:
            raise LLMError("DeepSeek returned no choices")
        content = response.choices[0].message.content
        if not content:
            raise LLMError("DeepSeek returned empty content")
        return content

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
        raw = self._call(
            system=system,
            user=user,
            temperature=temp,
            max_tokens=max_tok,
            response_format_json=response_format_json,
        )
        try:
            return parse_json_object(raw)
        except LLMError:
            if not response_format_json:
                raise
            rescue_system = (
                system.rstrip()
                + "\n\nReturn exactly one raw JSON object. Do not emit markdown fences, prose, or an empty response."
            )
            raw = self._call(
                system=rescue_system,
                user=user,
                temperature=0.0,
                max_tokens=max_tok,
                response_format_json=False,
            )
            return parse_json_object(raw)


def build_deepseek_client(config: DeepSeekConfig) -> ChatLLM:
    return DeepSeekClient(config)
