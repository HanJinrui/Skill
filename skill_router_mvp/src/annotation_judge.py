"""Independent DeepSeek-assisted route labeling over the frozen skill catalog."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable

import yaml

from .config import Settings
from .schemas import AnnotationRow, AutoAnnotationDecision, StructuredOutputError, json_object_from_text
from .skill_bank import SkillBank


CompletionFn = Callable[[str, str], str]


def _brief(values: list[Any], limit: int = 4) -> str:
    return " | ".join(str(value) for value in values[:limit] if str(value).strip())


def _short(value: Any, limit: int = 360) -> str:
    text = " ".join(str(value or "").split())
    return text[:limit]


class DeepSeekAnnotationClient:
    def __init__(
        self,
        *,
        api_key: str,
        base_url: str,
        model: str,
        max_tokens: int = 1400,
        timeout_seconds: float = 120.0,
        max_retries: int = 3,
        thinking_type: str = "disabled",
    ) -> None:
        from openai import OpenAI

        if thinking_type not in {"enabled", "disabled"}:
            raise ValueError("thinking_type must be enabled or disabled.")
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout_seconds,
            max_retries=max_retries,
        )
        self.model = model
        self.max_tokens = max_tokens
        self.thinking_type = thinking_type

    def complete(self, system: str, user: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
            temperature=0.0,
            max_tokens=self.max_tokens,
            response_format={"type": "json_object"},
            extra_body={"thinking": {"type": self.thinking_type}},
        )
        return str(response.choices[0].message.content or "")


class RouteAutoAnnotator:
    def __init__(self, settings: Settings, complete: CompletionFn, *, prompt_path: Path | None = None) -> None:
        self.complete = complete
        self.bank = SkillBank.from_settings(settings)
        self.skill_ids = set(self.bank.by_id)
        path = prompt_path or settings.package_root / "prompts" / "annotator.yaml"
        with path.open("r", encoding="utf-8") as fh:
            self.prompts = yaml.safe_load(fh)
        self.json_attempts = max(1, int((settings.data.get("annotation_judge") or {}).get("json_attempts", 3)))
        self.catalog = self._render_catalog()

    def _render_catalog(self) -> str:
        sections: list[str] = []
        for card in self.bank.cards:
            composition = _brief(card.composition_signature, 4)
            sections.append(
                "\n".join(
                    line
                    for line in [
                        f"ID: {card.skill_id}",
                        f"TYPE: {card.skill_type}",
                        f"NAME: {card.skill_name}",
                        f"FAMILY: {card.algorithm_family or ''}; SUBTYPE: {card.primary_subtype or ''}",
                        f"MECHANISM: {_short(card.core_mechanism or card.core_composition_mechanism)}",
                        f"TRIGGERS: {_brief(card.trigger_signals)}",
                        f"APPLIES_IF: {_brief(card.applicability_conditions, 3)}",
                        f"REJECT_IF: {_brief(card.non_applicability_conditions, 3)}",
                        f"COMPONENTS: {composition}" if composition else "",
                    ]
                    if line
                )
            )
        return "\n\n".join(sections)

    def _base_request(self, problem: dict[str, Any]) -> str:
        template = str(self.prompts["user_template"])
        values = {
            "problem_id": str(problem["problem_id"]),
            "problem_statement": str(problem.get("problem_statement") or ""),
            "skill_catalog": self.catalog,
        }
        for key, value in values.items():
            template = template.replace("{{" + key + "}}", value)
        return template

    def _parse(self, text: str) -> AutoAnnotationDecision:
        decision = AutoAnnotationDecision.model_validate(json_object_from_text(text))
        normalized: list[str] = []
        normalized_suffix = False
        for skill_id in decision.selected_skill_ids:
            if skill_id in self.skill_ids:
                normalized.append(skill_id)
            elif f"{skill_id}.v1" in self.skill_ids:
                normalized.append(f"{skill_id}.v1")
                normalized_suffix = True
            else:
                raise StructuredOutputError(f"Annotation returned unknown selected skill ID: {skill_id}")
        selected = normalized
        if decision.out_of_bank and selected:
            raise StructuredOutputError("out_of_bank decision must not select a skill.")
        if not decision.out_of_bank and len(selected) != 1:
            raise StructuredOutputError("In-bank annotation must select exactly one skill.")
        alternatives: list[str] = []
        for skill_id in decision.alternative_skill_ids:
            candidate = skill_id if skill_id in self.skill_ids else f"{skill_id}.v1"
            if candidate in self.skill_ids and candidate not in alternatives:
                alternatives.append(candidate)
                normalized_suffix = normalized_suffix or candidate != skill_id
        flags = list(decision.uncertainty_flags)
        if normalized_suffix:
            flags.append("Normalized omitted .v1 suffix in model-provided skill ID.")
        return decision.model_copy(
            update={
                "selected_skill_ids": selected,
                "alternative_skill_ids": alternatives,
                "uncertainty_flags": flags,
            }
        )

    def _generate_decision(self, user: str) -> AutoAnnotationDecision:
        system = str(self.prompts["system"])
        prompt = user
        last_error: Exception | None = None
        for _ in range(self.json_attempts):
            raw = self.complete(system, prompt)
            try:
                return self._parse(raw)
            except Exception as exc:
                last_error = exc
                prompt = (
                    f"{user}\n\nYour previous JSON was invalid or empty: {exc}. "
                    "Return only a corrected JSON object using exact IDs in the catalog."
                )
        raise StructuredOutputError(f"Model did not produce a valid annotation after {self.json_attempts} attempts: {last_error}")

    def annotate(self, problem: dict[str, Any], *, second_pass: bool = True) -> tuple[AutoAnnotationDecision, AutoAnnotationDecision | None]:
        base_request = self._base_request(problem)
        initial = self._generate_decision(base_request)
        if not second_pass:
            return initial, None
        review = str(self.prompts["review_template"])
        review = review.replace("{{initial_decision_json}}", json.dumps(initial.model_dump(mode="json"), ensure_ascii=False))
        review = review.replace("{{base_request}}", base_request)
        return self._generate_decision(review), initial

    @staticmethod
    def to_annotation_row(
        workbook_row: AnnotationRow,
        decision: AutoAnnotationDecision,
        *,
        model: str,
        confidence_threshold: float,
        initial: AutoAnnotationDecision | None,
    ) -> dict[str, Any]:
        accepted = decision.confidence >= confidence_threshold and not decision.requires_human_review
        row = workbook_row.model_copy(
            update={
                "gold_skill_ids": decision.selected_skill_ids,
                "out_of_bank": decision.out_of_bank,
                "annotation_reason": decision.annotation_reason,
                "review_status": "reviewed" if accepted else "needs_review",
            }
        ).model_dump(mode="json")
        row.update(
            {
                "label_source": "deepseek_silver",
                "label_model": model,
                "label_confidence": decision.confidence,
                "label_uncertainty_flags": decision.uncertainty_flags,
                "label_alternative_skill_ids": decision.alternative_skill_ids,
                "label_second_pass": initial is not None,
                "label_initial_decision": initial.model_dump(mode="json") if initial is not None else None,
            }
        )
        return row
