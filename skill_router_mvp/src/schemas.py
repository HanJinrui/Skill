"""Persisted contracts for routing, planning, generation and evaluation."""
from __future__ import annotations

import json
import re
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator


class ContractModel(BaseModel):
    model_config = ConfigDict(extra="allow")


class UnifiedSkillCard(ContractModel):
    skill_id: str
    skill_name: str
    skill_type: Literal["single_algorithm", "multi_algorithm"]
    version: str = "v1"
    status: str = "seed"
    trigger_signals: list[str] = Field(default_factory=list)
    applicability_conditions: list[str] = Field(default_factory=list)
    non_applicability_conditions: list[str] = Field(default_factory=list)
    complexity_pattern: dict[str, Any] | str = Field(default_factory=dict)
    retrieval_text: str
    implementation_notes: list[str] = Field(default_factory=list)
    common_pitfalls: list[str] = Field(default_factory=list)
    algorithm_family: str | None = None
    primary_subtype: str | None = None
    code_template: str | None = None
    core_mechanism: str | None = None
    composition_signature: list[str] = Field(default_factory=list)
    composition_families: list[str] = Field(default_factory=list)
    algorithm_flow: list[Any] = Field(default_factory=list)
    state_interface: Any = None
    composition_invariants: list[str] = Field(default_factory=list)
    implementation_template: str | None = None
    core_composition_mechanism: str | None = None
    raw_card: dict[str, Any] = Field(default_factory=dict)


class CompositionEdge(ContractModel):
    multi_skill_id: str
    component_subtype: str
    single_skill_id: str | None = None
    required: bool = True
    resolution: Literal["exact", "alias", "unresolved_component"]


class ProblemProfile(ContractModel):
    problem_id: str = ""
    statement_summary: str
    input_structures: list[str] = Field(default_factory=list)
    constraint_profile: dict[str, str] = Field(default_factory=dict)
    objective_types: list[str] = Field(default_factory=list)
    algorithm_signals: list[str] = Field(default_factory=list)
    prohibited_operations: list[str] = Field(default_factory=list)
    likely_multi_skill: bool = False


class RetrievalCandidate(ContractModel):
    skill_id: str
    skill_type: Literal["single_algorithm", "multi_algorithm"]
    sparse_score: float = 0.0
    dense_score: float = 0.0
    rule_score: float = 0.0
    status_score: float = 0.0
    penalty_score: float = 0.0
    router_score: float = 0.0
    rerank_score: float | None = None
    final_score: float = 0.0
    matched_signals: list[str] = Field(default_factory=list)
    blockers: list[str] = Field(default_factory=list)
    card: UnifiedSkillCard


class SimpleGateAssessment(ContractModel):
    """Minimal per-candidate output the LLM produces in the simplified gate prompt."""

    skill_id: str
    applicable: bool = False
    confidence: float = 0.0
    reason: str = ""

    @field_validator("confidence")
    @classmethod
    def bound_simple_confidence(cls, value: float) -> float:
        return max(0.0, min(1.0, float(value)))


class SimplifiedGateOutput(ContractModel):
    """Full LLM gate response under the simplified prompt schema."""

    assessments: list[SimpleGateAssessment]


class GateAssessment(ContractModel):
    skill_id: str
    applicable: bool = False
    confidence: float = 0.0
    matched_signals: list[str] = Field(default_factory=list)
    violated_conditions: list[str] = Field(default_factory=list)
    complexity_fit: Literal["good", "borderline", "bad"] = "borderline"
    component_scores: dict[str, float] = Field(default_factory=dict)
    reason: str = ""

    @field_validator("confidence")
    @classmethod
    def bound_confidence(cls, value: float) -> float:
        return max(0.0, min(1.0, float(value)))


class GateDecision(ContractModel):
    assessments: list[GateAssessment]
    selected_skill_ids: list[str] = Field(default_factory=list)
    selected_confidence: float = 0.0
    selection_type: Literal["single", "multi", "fallback"] = "fallback"
    runner_up_skill_id: str | None = None
    runner_up_reason: str = ""
    margin: float = 0.0
    ambiguous: bool = False
    fallback_reason: str = ""


class SelectedPlanSkill(ContractModel):
    skill_id: str
    role: Literal["main", "component"] = "main"
    confidence: float = 0.0


class AlgorithmPlan(ContractModel):
    problem_id: str = ""
    language: str = "Python 3"
    selected_skills: list[SelectedPlanSkill]
    rejected_skills: list[dict[str, str]] = Field(default_factory=list)
    problem_decomposition: list[str]
    state_design: dict[str, Any] = Field(default_factory=dict)
    core_invariants: list[str] = Field(default_factory=list)
    complexity: dict[str, Any] = Field(default_factory=dict)
    implementation_notes: list[str] = Field(default_factory=list)
    test_focus: list[str] = Field(default_factory=list)
    output_contract: dict[str, Any] = Field(default_factory=lambda: {"only_code": True, "single_file": True})


class TestCaseResult(ContractModel):
    index: int
    passed: bool
    reason: str
    stdout: str = ""
    stderr: str = ""
    duration_ms: int = 0


class ExecutionReport(ContractModel):
    all_passed: bool
    num_tests: int
    num_passed: int
    reason_summary: dict[str, int] = Field(default_factory=dict)
    per_test: list[TestCaseResult] = Field(default_factory=list)


class FeedbackDecision(ContractModel):
    action: Literal["accept", "repair", "reroute", "stop"]
    reason: str


class AttemptTrace(ContractModel):
    attempt: int
    action: str = "generate"
    code: str
    execution: ExecutionReport
    plan: AlgorithmPlan | None = None


class GenerationSample(ContractModel):
    sample_id: str
    attempts: list[AttemptTrace]
    final_attempt: int = 0

    def final_execution(self) -> ExecutionReport:
        return self.attempts[self.final_attempt].execution


class RunTrace(ContractModel):
    problem_id: str
    scope: str = ""
    mode: str
    bank_version: str
    model_name: str
    selected_skill_ids: list[str] = Field(default_factory=list)
    profile: ProblemProfile | None = None
    candidates: list[RetrievalCandidate] = Field(default_factory=list)
    gate: GateDecision | None = None
    plan: AlgorithmPlan | None = None
    samples: list[GenerationSample] = Field(default_factory=list)
    fallback_reason: str = ""
    latency_ms: dict[str, int] = Field(default_factory=dict)
    metadata: dict[str, Any] = Field(default_factory=dict)


class AnnotationRow(ContractModel):
    problem_id: str
    scope: str
    difficulty_bucket: str = ""
    problem_summary: str = ""
    candidate_skill_ids: list[str] = Field(default_factory=list)
    gold_skill_ids: list[str] = Field(default_factory=list)
    out_of_bank: bool | None = None
    annotation_reason: str = ""
    review_status: str = "pending"


class AutoAnnotationDecision(ContractModel):
    selected_skill_ids: list[str] = Field(default_factory=list)
    out_of_bank: bool = False
    confidence: float = 0.0
    annotation_reason: str
    alternative_skill_ids: list[str] = Field(default_factory=list)
    uncertainty_flags: list[str] = Field(default_factory=list)
    requires_human_review: bool = False

    @field_validator("confidence")
    @classmethod
    def bound_annotation_confidence(cls, value: float) -> float:
        return max(0.0, min(1.0, float(value)))


class StructuredOutputError(RuntimeError):
    pass


_FENCE_RE = re.compile(r"```(?:json)?\s*(.*?)```", re.DOTALL | re.IGNORECASE)


def json_object_from_text(text: str) -> dict[str, Any]:
    candidate = text.strip()
    match = _FENCE_RE.search(candidate)
    if match:
        candidate = match.group(1).strip()
    start, end = candidate.find("{"), candidate.rfind("}")
    if start < 0 or end < start:
        raise StructuredOutputError("Model response did not contain a JSON object.")
    try:
        value = json.loads(candidate[start : end + 1])
    except json.JSONDecodeError as exc:
        raise StructuredOutputError(f"Invalid model JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise StructuredOutputError("Model JSON output must be an object.")
    return value


def parse_contract(text: str, contract: type[ContractModel]) -> ContractModel:
    try:
        return contract.model_validate(json_object_from_text(text))
    except ValidationError as exc:
        raise StructuredOutputError(f"{contract.__name__} schema validation failed: {exc}") from exc
