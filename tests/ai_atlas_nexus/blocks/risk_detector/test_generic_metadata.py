"""Tests for token usage metadata exposure in GenericRiskDetector."""

import pytest

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk
from ai_atlas_nexus.blocks.inference.params import (
    InferenceMetadata,
    TextGenerationInferenceOutput,
    TokenUsage,
)
from ai_atlas_nexus.blocks.prompt_response_schema import LIST_OF_STR_SCHEMA
from ai_atlas_nexus.blocks.risk_detector import (
    DetectionResult,
    GenericRiskDetector,
    RiskDetectorWithExplanation,
    RiskDetectorWithMetadata,
    RiskWithExplanation,
)
from ai_atlas_nexus.metadata_base import ExplanationType
from tests.ai_atlas_nexus.stub_inference import StubInferenceEngine, StubResponse


def _risk(rid, name, description, taxonomy="ibm-risk-atlas"):
    return Risk(
        id=rid, name=name, description=description, isDefinedByTaxonomy=taxonomy
    )


THINKING = "<thinking>...</thinking>"


def _engine(*responses: StubResponse) -> StubInferenceEngine:
    """Engine for the batch path: one response per usecase."""
    return StubInferenceEngine(responses)


def _per_risk_engine(answers_per_usecase) -> StubInferenceEngine:
    """Engine for the per-risk path: one yes/no response per risk, per usecase.

    Each response's thinking is tagged with its own usecase and risk index, so an
    explanation landing on the wrong risk shows up in the assertion rather than
    looking plausible.
    """
    return StubInferenceEngine(
        [
            StubResponse(
                prediction={"answer": answer},
                input_tokens=10,
                output_tokens=5,
                thinking=f"thinking-u{usecase_index}-r{risk_index}",
            )
            for usecase_index, answers in enumerate(answers_per_usecase)
            for risk_index, answer in enumerate(answers)
        ]
    )


def _detector(engine, risks, max_risk=None):
    return GenericRiskDetector(
        risks=risks,
        inference_engine=engine,
        cot_examples=None,
        batch_inference=True,
        max_risk=max_risk,
    )


def _detector_per_risk(engine, risks):
    return GenericRiskDetector(
        risks=risks, inference_engine=engine, cot_examples=None, batch_inference=False
    )


def _with_explanation(engine, risks, explanation_type, batch_inference=True):
    return RiskDetectorWithExplanation(
        GenericRiskDetector(
            risks=risks,
            inference_engine=engine,
            cot_examples=None,
            batch_inference=batch_inference,
        ),
        explanation_type,
    )


RISKS = [
    _risk("risk-a", "Risk A", "Description of risk A"),
    _risk("risk-b", "Risk B", "Description of risk B"),
]


class TestMetadataAggregation:
    """Token usage aggregation across the inference calls of a run."""

    def test_generic_detector_returns_bare_list(self):
        """Without the metadata decorator, detect returns a plain list of risks."""
        engine = _engine(
            StubResponse(["Risk A", "Risk B"], 100, 50),
        )
        result = _detector(engine, RISKS).detect(["usecase 1"])

        assert isinstance(result, list)
        assert not isinstance(result, DetectionResult)
        assert len(result) == 1
        assert len(result[0]) == 2
        assert result[0][0].name == "Risk A"

    def test_metadata_decorator_returns_wrapped_result(self):
        engine = _engine(
            StubResponse(["Risk A"], 100, 50),
        )
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["usecase 1"])

        assert isinstance(result, DetectionResult)
        assert isinstance(result.data, list)
        assert len(result.data) == 1
        assert result.data[0][0].name == "Risk A"

    def test_metadata_aggregates_tokens_correctly(self):
        """Token usage aggregation sums across all calls."""
        engine = _engine(
            StubResponse(["Risk A"], 100, 50),
            StubResponse(["Risk B"], 120, 60),
        )
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["usecase 1", "usecase 2"])

        assert result.metadata.token_usage.input_tokens == 220  # 100 + 120
        assert result.metadata.token_usage.output_tokens == 110  # 50 + 60
        assert result.metadata.token_usage.total_tokens == 330  # 220 + 110

    def test_metadata_includes_model_and_engine_info(self):
        """Metadata includes model name and inference engine type."""
        engine = _engine(StubResponse(["Risk A"], 100, 50))
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["usecase 1"])

        assert result.metadata.model == "stub-model"
        assert result.metadata.inference_engine == "STUB"
        assert result.metadata.num_calls == 1
        assert result.metadata.seed is None
        assert result.metadata.stop_reason_summary == {}
        assert result.metadata.has_thinking is False

    def test_metadata_num_calls_reflects_inference_count(self):
        """num_calls field tracks number of underlying LLM calls."""
        engine = _engine(
            StubResponse(["Risk A"], 100, 50),
            StubResponse(["Risk B"], 120, 60),
            StubResponse(["Risk A", "Risk B"], 150, 70),
        )
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["usecase 1", "usecase 2", "usecase 3"])

        assert result.metadata.num_calls == 3

    def test_metadata_with_none_tokens_handled_gracefully(self):
        """Handles responses with missing token counts."""
        engine = _engine(
            StubResponse(["Risk A"], None, 50),  # Missing input_tokens
            StubResponse(["Risk B"], 100, None),  # Missing output_tokens
        )
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["usecase 1", "usecase 2"])

        # Should treat None as 0 for aggregation
        assert result.metadata.token_usage.input_tokens == 100
        assert result.metadata.token_usage.output_tokens == 50
        assert result.metadata.token_usage.total_tokens == 150

    def test_metadata_is_opt_in(self):
        """An undecorated detector never returns a wrapper (backward compatibility)."""
        engine = _engine(StubResponse(["Risk A"], 100, 50))

        result = _detector(engine, RISKS).detect(["usecase 1"])

        assert isinstance(result, list)
        assert not isinstance(result, DetectionResult)

    def test_stop_reason_aggregation(self):
        """Stop reasons are counted across all inference calls."""
        engine = _engine(
            StubResponse(["Risk A"], 100, 50, stop_reason="eos"),
            StubResponse(["Risk B"], 120, 60, stop_reason="eos"),
            StubResponse(["Risk C"], 90, 45, stop_reason="max_tokens"),
        )
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["u1", "u2", "u3"])

        assert result.metadata.stop_reason_summary == {"eos": 2, "max_tokens": 1}

    def test_seed_extracted_when_consistent(self):
        """Seed is stored only when all calls use the same seed."""
        engine = _engine(
            StubResponse(["Risk A"], 100, 50, seed=42),
            StubResponse(["Risk B"], 120, 60, seed=42),
        )
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["u1", "u2"])

        assert result.metadata.seed == 42

    def test_seed_none_when_inconsistent(self):
        """Seed is None when calls use different seeds."""
        engine = _engine(
            StubResponse(["Risk A"], 100, 50, seed=42),
            StubResponse(["Risk B"], 120, 60, seed=99),  # Different seed
        )
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["u1", "u2"])

        assert result.metadata.seed is None

    def test_seed_none_when_only_some_calls_reported_one(self):
        """A lone seeded call must not advertise the run as reproducible."""
        engine = _engine(
            StubResponse(["Risk A"], 100, 50, seed=42),
            StubResponse(["Risk B"], 120, 60),  # engine reported no seed
        )
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["u1", "u2"])

        assert result.metadata.seed is None

    def test_thinking_flag_set_when_present(self):
        """has_thinking is True if any response has thinking content."""
        engine = _engine(
            StubResponse(["Risk A"], 100, 50),  # no thinking
            StubResponse(["Risk B"], 120, 60, thinking=THINKING),
        )
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["u1", "u2"])

        assert result.metadata.has_thinking is True


class TestExplanationTypes:
    """Test different explanation type options."""

    def test_no_explanation_without_the_decorator(self):
        """An undecorated detector returns only the risks."""
        engine = _engine(StubResponse(["Risk A"], 100, 50))
        result = _detector(engine, RISKS).detect(["usecase 1"])

        assert isinstance(result, list)
        assert not isinstance(result[0][0], RiskWithExplanation)
        assert isinstance(result[0][0], Risk)

    def test_explanation_none_is_rejected(self):
        """Wrapping for NONE would only obscure the return type; use the detector."""
        engine = _engine(StubResponse(["Risk A"], 100, 50))

        with pytest.raises(ValueError, match="ExplanationType.NONE"):
            RiskDetectorWithExplanation(
                _detector(engine, RISKS), ExplanationType.NONE
            )

    def test_explanation_description_includes_risk_description(self):
        """DESCRIPTION type includes risk.description."""
        engine = _engine(StubResponse(["Risk A"], 100, 50))
        detector = _with_explanation(engine, RISKS, ExplanationType.DESCRIPTION)
        result = detector.detect(["usecase 1"])

        assert isinstance(result[0][0], RiskWithExplanation)
        assert result[0][0].risk.name == "Risk A"
        assert result[0][0].explanation == "Description of risk A"

    def test_explanation_reasoning_extracts_thinking(self):
        """REASONING type extracts model thinking."""
        engine = _engine(StubResponse(["Risk A"], 100, 50, thinking=THINKING))
        detector = _with_explanation(engine, RISKS, ExplanationType.REASONING)
        result = detector.detect(["usecase 1"])

        assert isinstance(result[0][0], RiskWithExplanation)
        assert result[0][0].explanation == THINKING

    def test_explanation_reasoning_none_when_no_thinking(self):
        """REASONING type returns None if no thinking available."""
        engine = _engine(StubResponse(["Risk A"], 100, 50))
        detector = _with_explanation(engine, RISKS, ExplanationType.REASONING)
        result = detector.detect(["usecase 1"])

        assert isinstance(result[0][0], RiskWithExplanation)
        assert result[0][0].explanation is None

    def test_explanation_self_explanation_none_for_string_prediction(self):
        """SELF_EXPLANATION type returns None if prediction is string (no explanation field)."""
        engine = _engine(StubResponse(["Risk A"], 100, 50))
        detector = _with_explanation(engine, RISKS, ExplanationType.SELF_EXPLANATION)
        result = detector.detect(["usecase 1"])

        assert isinstance(result[0][0], RiskWithExplanation)
        assert result[0][0].explanation is None

    def test_self_explanation_looked_up_by_risk_name(self):
        """The batch schema returns explanations per risk, matched by name."""
        prediction = {
            "risks": [
                {"risk_name": "Risk B", "explanation": "because of B"},
                {"risk_name": "Risk A", "explanation": "because of A"},
            ]
        }
        engine = _engine(StubResponse(prediction, 100, 50))
        detector = _with_explanation(engine, RISKS, ExplanationType.SELF_EXPLANATION)
        result = detector.detect(["usecase 1"])

        # Risks and explanations come back in taxonomy order
        assert [(r.risk.name, r.explanation) for r in result[0]] == [
            ("Risk A", "because of A"),
            ("Risk B", "because of B"),
        ]

    def test_self_explanation_requests_a_schema_carrying_explanations(self):
        """SELF_EXPLANATION must override the batch schema; other types must not."""
        engine = _engine(StubResponse(["Risk A"], 100, 50))
        base = _detector(engine, RISKS)

        assert (
            _with_explanation(
                engine, RISKS, ExplanationType.REASONING
            )._batch_schema_override()
            is None
        )
        schema = RiskDetectorWithExplanation(
            base, ExplanationType.SELF_EXPLANATION
        )._batch_schema_override()
        assert schema is not None
        assert schema.postprocessor == "json_object"
        assert "explanation" in schema.response_format.model_json_schema()["$defs"][
            "RiskWithExplanationItem"
        ]["properties"]

    def test_self_explanation_schema_omits_nameless_risks(self):
        """`Risk.name` is Optional; a null in the enum would match no risk."""
        risks = RISKS + [
            Risk(
                id="risk-unnamed",
                description="no name",
                isDefinedByTaxonomy="ibm-risk-atlas",
            )
        ]
        engine = _engine(StubResponse(["Risk A"], 100, 50))
        schema = _with_explanation(
            engine, risks, ExplanationType.SELF_EXPLANATION
        )._batch_schema_override()

        assert schema.response_format.model_json_schema()["$defs"][
            "RiskWithExplanationItem"
        ]["properties"]["risk_name"]["enum"] == ["Risk A", "Risk B"]

    def test_self_explanation_schema_is_skipped_without_named_risks(self):
        """`Literal[]` is not constructible, so an empty taxonomy must not build one."""
        engine = _engine(StubResponse([], 100, 50))
        detector = _with_explanation(engine, [], ExplanationType.SELF_EXPLANATION)

        assert detector._batch_schema_override() is None
        assert detector.detect(["usecase 1"]) == [[]]


THREE_RISKS = [
    _risk("risk-a", "Risk A", "Description of risk A"),
    _risk("risk-b", "Risk B", "Description of risk B"),
    _risk("risk-c", "Risk C", "Description of risk C"),
]


class TestPerRiskExplanations:
    """Explanations on the per-risk path (batch_inference=False).

    This path had no coverage, which is how an off-by-one in the response mapping
    survived: explanations were assigned by a counter that only advanced for identified
    risks, with no per-usecase offset.
    """

    def test_explanation_matches_the_response_that_identified_the_risk(self):
        """Each risk gets the reasoning from its own response, not a neighbour's."""
        # Risk A rejected, so a naive counter would shift B and C down by one.
        engine = _per_risk_engine([["no", "yes", "yes"]])
        detector = _with_explanation(
            engine, THREE_RISKS, ExplanationType.REASONING, batch_inference=False
        )
        result = detector.detect(["usecase 1"])

        assert [r.risk.name for r in result[0]] == ["Risk B", "Risk C"]
        assert result[0][0].explanation == "thinking-u0-r1"
        assert result[0][1].explanation == "thinking-u0-r2"

    def test_explanations_do_not_leak_across_usecases(self):
        """Usecase 2's explanations come from usecase 2's responses."""
        engine = _per_risk_engine([["no", "yes", "yes"], ["yes", "no", "yes"]])
        detector = _with_explanation(
            engine, THREE_RISKS, ExplanationType.REASONING, batch_inference=False
        )
        result = detector.detect(["usecase 1", "usecase 2"])

        assert [r.risk.name for r in result[1]] == ["Risk A", "Risk C"]
        assert result[1][0].explanation == "thinking-u1-r0"
        assert result[1][1].explanation == "thinking-u1-r2"

    def test_per_risk_bare_risks_by_default(self):
        """Default path still returns only the Risk objects."""
        engine = _per_risk_engine([["no", "yes", "no"]])
        detector = _detector_per_risk(engine, THREE_RISKS)
        result = detector.detect(["usecase 1"])

        assert [r.name for r in result[0]] == ["Risk B"]
        assert isinstance(result[0][0], Risk)

    def test_per_risk_metadata_counts_every_call(self):
        """One inference call per risk per usecase."""
        engine = _per_risk_engine([["no", "yes", "yes"], ["yes", "no", "yes"]])
        detector = RiskDetectorWithMetadata(_detector_per_risk(engine, THREE_RISKS))
        result = detector.detect(["u1", "u2"])

        assert result.metadata.num_calls == 6  # 3 risks x 2 usecases
        assert result.metadata.token_usage.input_tokens == 60
        assert result.metadata.token_usage.output_tokens == 30


class TestDecoratorComposition:
    """Metadata over explanations: both features at once, each keeping its shape."""

    def test_metadata_preserves_explanations(self):
        engine = _engine(StubResponse(["Risk A"], 100, 50))
        detector = RiskDetectorWithMetadata(
            _with_explanation(engine, RISKS, ExplanationType.DESCRIPTION)
        )
        result = detector.detect(["usecase 1"])

        assert isinstance(result, DetectionResult)
        assert isinstance(result.data[0][0], RiskWithExplanation)
        assert result.data[0][0].explanation == "Description of risk A"
        assert result.metadata.token_usage.total_tokens == 150
        assert result.metadata.per_usecase[0].num_calls == 1

    def test_explanation_must_be_the_inner_decorator(self):
        """The reverse nesting would drop the metadata wrapper on the floor."""
        engine = _engine(StubResponse(["Risk A"], 100, 50))

        with pytest.raises(TypeError, match="innermost"):
            RiskDetectorWithExplanation(
                RiskDetectorWithMetadata(_detector(engine, RISKS)),
                ExplanationType.DESCRIPTION,
            )


class TestStringPredictionFallback:
    """Raw-string predictions still resolve risks when postprocessing is skipped."""

    def test_substring_match_on_raw_string_prediction(self):
        engine = _engine(StubResponse('["Risk A", "Risk C"]', 100, 50))
        detector = _detector(engine, THREE_RISKS)
        result = detector.detect(["usecase 1"])

        assert [r.name for r in result[0]] == ["Risk A", "Risk C"]

    def test_unnamed_risk_does_not_raise(self):
        """`Risk.name` is Optional; `None in str` would raise TypeError."""
        risks = THREE_RISKS + [
            Risk(id="risk-unnamed", description="no name", isDefinedByTaxonomy="ibm-risk-atlas")
        ]
        engine = _engine(StubResponse('["Risk A"]', 100, 50))
        detector = _detector(engine, risks)
        result = detector.detect(["usecase 1"])

        assert [r.name for r in result[0]] == ["Risk A"]


class TestPartiallyConformingPredictions:
    """A response that half-follows the schema degrades instead of aborting the run."""

    def test_mixed_names_and_objects(self):
        """Indexing a string as a dict would raise TypeError."""
        prediction = {"risks": [{"risk_name": "Risk A", "explanation": "why A"}, "Risk C"]}
        engine = _engine(StubResponse(prediction, 100, 50))
        detector = _detector(engine, THREE_RISKS)
        result = detector.detect(["usecase 1"])

        assert [r.name for r in result[0]] == ["Risk A", "Risk C"]

    def test_object_missing_risk_name_is_dropped(self):
        """`item["risk_name"]` would raise KeyError on the second item."""
        prediction = {
            "risks": [{"risk_name": "Risk B"}, {"explanation": "no name given"}]
        }
        engine = _engine(StubResponse(prediction, 100, 50))
        detector = _detector(engine, THREE_RISKS)
        result = detector.detect(["usecase 1"])

        assert [r.name for r in result[0]] == ["Risk B"]

    def test_null_name_matches_no_risk(self):
        """A JSON null must not match a risk whose own `name` is None."""
        risks = THREE_RISKS + [
            Risk(
                id="risk-unnamed",
                description="no name",
                isDefinedByTaxonomy="ibm-risk-atlas",
            )
        ]
        engine = _engine(StubResponse({"risks": [None, "Risk A"]}, 100, 50))
        detector = _detector(engine, risks)
        result = detector.detect(["usecase 1"])

        assert [r.name for r in result[0]] == ["Risk A"]


class TestMaxRisk:
    """The prompt asks for the model's top `max_risk`, so its ranking picks the cut."""

    def test_truncates_by_model_ranking_not_taxonomy_order(self):
        engine = _engine(StubResponse(["Risk C", "Risk B", "Risk A"], 100, 50))
        detector = _detector(engine, THREE_RISKS, max_risk=2)
        result = detector.detect(["usecase 1"])

        # C and B were ranked highest; they come back in taxonomy order
        assert [r.name for r in result[0]] == ["Risk B", "Risk C"]

    def test_unknown_names_do_not_consume_slots(self):
        engine = _engine(StubResponse(["Unknown", "Risk C", "Risk B"], 100, 50))
        detector = _detector(engine, THREE_RISKS, max_risk=2)
        result = detector.detect(["usecase 1"])

        assert [r.name for r in result[0]] == ["Risk B", "Risk C"]

    def test_repeated_names_do_not_consume_slots(self):
        engine = _engine(StubResponse(["Risk C", "Risk C", "Risk A"], 100, 50))
        detector = _detector(engine, THREE_RISKS, max_risk=2)
        result = detector.detect(["usecase 1"])

        assert [r.name for r in result[0]] == ["Risk A", "Risk C"]

    def test_sources_align_with_the_truncated_risks(self):
        engine = _engine(StubResponse(["Risk C", "Risk B", "Risk A"], 100, 50))
        detector = _detector(engine, THREE_RISKS, max_risk=2)
        run = detector._run_inference(["usecase 1"])

        assert len(run.sources[0]) == len(run.data[0]) == 2


class TestTokenUsageAggregation:
    """Test TokenUsage dataclass aggregation behavior."""

    def test_token_usage_addition(self):
        """TokenUsage + operator correctly sums fields."""
        usage1 = TokenUsage(input_tokens=100, output_tokens=50, total_tokens=150)
        usage2 = TokenUsage(input_tokens=120, output_tokens=60, total_tokens=180)

        result = usage1 + usage2

        assert result.input_tokens == 220
        assert result.output_tokens == 110
        assert result.total_tokens == 330

    def test_token_usage_sum_with_none_values(self):
        """TokenUsage addition handles None values as 0."""
        usage1 = TokenUsage(input_tokens=100, output_tokens=None, total_tokens=100)
        usage2 = TokenUsage(input_tokens=None, output_tokens=60, total_tokens=60)

        result = usage1 + usage2

        assert result.input_tokens == 100
        assert result.output_tokens == 60
        assert result.total_tokens == 160

    def test_total_derived_from_the_parts(self):
        """A caller reporting only the parts gets the total computed for it."""
        assert TokenUsage(input_tokens=100, output_tokens=50).total_tokens == 150
        assert TokenUsage(input_tokens=100).total_tokens == 100
        assert TokenUsage(output_tokens=50).total_tokens == 50

    def test_explicit_total_is_not_overwritten(self):
        """Engines that report a total including other tokens keep their figure."""
        usage = TokenUsage(input_tokens=100, output_tokens=50, total_tokens=175)
        assert usage.total_tokens == 175

    def test_unreported_usage_stays_none_not_zero(self):
        """Summing two unreported usages must not fabricate a zero."""
        result = TokenUsage() + TokenUsage()

        assert result.input_tokens is None
        assert result.output_tokens is None
        assert result.total_tokens is None

    def test_engine_without_usage_reports_none(self):
        """An engine that reports no token counts yields None, not a misleading 0."""
        engine = _engine(StubResponse(["Risk A"], None, None))
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["usecase 1"])

        assert result.metadata.token_usage.input_tokens is None
        assert result.metadata.token_usage.output_tokens is None
        assert result.metadata.token_usage.total_tokens is None

    def test_token_usage_sum_empty_usage(self):
        """Summing with empty TokenUsage (all None) treats as 0."""
        usage1 = TokenUsage(input_tokens=100, output_tokens=50, total_tokens=150)
        usage_empty = TokenUsage()

        result = usage1 + usage_empty

        assert result.input_tokens == 100
        assert result.output_tokens == 50
        assert result.total_tokens == 150


class TestPerUsecaseMetadata:
    """Metadata is attributed to the usecase that incurred it, not just the run."""

    def test_one_entry_per_usecase_aligned_with_data(self):
        engine = _engine(
            StubResponse(["Risk A"], 100, 50),
            StubResponse(["Risk B"], 120, 60),
        )
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["usecase 1", "usecase 2"])

        assert len(result.metadata.per_usecase) == len(result.data) == 2

    def test_tokens_attributed_to_their_own_usecase(self):
        engine = _engine(
            StubResponse(["Risk A"], 100, 50),
            StubResponse(["Risk B"], 120, 60),
        )
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["usecase 1", "usecase 2"])

        first, second = result.metadata.per_usecase
        assert first.token_usage.input_tokens == 100
        assert first.token_usage.output_tokens == 50
        assert first.token_usage.total_tokens == 150
        assert second.token_usage.input_tokens == 120
        assert second.token_usage.output_tokens == 60
        assert second.token_usage.total_tokens == 180

    def test_per_usecase_totals_sum_to_the_aggregate(self):
        engine = _engine(
            StubResponse(["Risk A"], 100, 50),
            StubResponse(["Risk B"], 120, 60),
            StubResponse(["Risk A", "Risk B"], 150, 70),
        )
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["u1", "u2", "u3"])
        metadata = result.metadata

        per_usecase = metadata.per_usecase
        assert (
            sum(u.token_usage.input_tokens for u in per_usecase)
            == metadata.token_usage.input_tokens
        )
        assert (
            sum(u.token_usage.output_tokens for u in per_usecase)
            == metadata.token_usage.output_tokens
        )
        assert sum(u.num_calls for u in per_usecase) == metadata.num_calls == 3

    def test_batch_path_reports_one_call_per_usecase(self):
        engine = _engine(
            StubResponse(["Risk A"], 100, 50), StubResponse(["Risk B"], 120, 60)
        )
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["u1", "u2"])

        assert [u.num_calls for u in result.metadata.per_usecase] == [1, 1]

    def test_per_risk_path_counts_every_call_including_rejections(self):
        """A "no" answer identifies nothing but still costs tokens."""
        engine = _per_risk_engine([["no", "yes", "no"], ["yes", "no", "yes"]])
        detector = RiskDetectorWithMetadata(_detector_per_risk(engine, THREE_RISKS))
        result = detector.detect(["u1", "u2"])

        # 3 risks per usecase, at 10 input / 5 output tokens per call.
        assert [u.num_calls for u in result.metadata.per_usecase] == [3, 3]
        per_usecase = result.metadata.per_usecase
        assert [u.token_usage.input_tokens for u in per_usecase] == [30, 30]
        assert [u.token_usage.output_tokens for u in per_usecase] == [15, 15]

    def test_stop_reasons_isolated_per_usecase(self):
        engine = _engine(
            StubResponse(["Risk A"], 100, 50, stop_reason="eos"),
            StubResponse(["Risk B"], 120, 60, stop_reason="eos"),
            StubResponse(["Risk C"], 90, 45, stop_reason="max_tokens"),
        )
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["u1", "u2", "u3"])

        assert [u.stop_reason_summary for u in result.metadata.per_usecase] == [
            {"eos": 1},
            {"eos": 1},
            {"max_tokens": 1},
        ]
        assert result.metadata.stop_reason_summary == {"eos": 2, "max_tokens": 1}

    def test_thinking_flag_isolated_per_usecase(self):
        engine = _engine(
            StubResponse(["Risk A"], 100, 50),  # no thinking
            StubResponse(["Risk B"], 120, 60, thinking=THINKING),
        )
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["u1", "u2"])

        assert [u.has_thinking for u in result.metadata.per_usecase] == [False, True]
        assert result.metadata.has_thinking is True

    def test_seed_reported_per_usecase(self):
        engine = _engine(
            StubResponse(["Risk A"], 100, 50, seed=42),
            StubResponse(["Risk B"], 120, 60, seed=99),
        )
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["u1", "u2"])

        # Each usecase used one seed, so each reports it; the run as a whole did not.
        assert [u.seed for u in result.metadata.per_usecase] == [42, 99]
        assert result.metadata.seed is None

    def test_unreported_tokens_stay_none_per_usecase(self):
        engine = _engine(StubResponse(["Risk A"], None, None))
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["usecase 1"])

        usage = result.metadata.per_usecase[0].token_usage
        assert usage.input_tokens is None
        assert usage.output_tokens is None
        assert usage.total_tokens is None

    def test_metadata_wrapper_passes_data_through_untouched(self):
        engine = _engine(StubResponse(["Risk A"], 100, 50))
        detector = RiskDetectorWithMetadata(_detector(engine, RISKS))
        result = detector.detect(["usecase 1"])

        assert isinstance(result, DetectionResult)
        assert isinstance(result.metadata, InferenceMetadata)
        assert [r.name for r in result.data[0]] == ["Risk A"]


class TestRunInferenceContract:
    """The decorators use this: `sources` pairs items, `outputs` bills.
    """

    def test_batch_sources_parallel_to_data(self):
        engine = _engine(StubResponse(["Risk A", "Risk B"], 100, 50))
        run = _detector(engine, RISKS)._run_inference(["usecase 1"])

        assert [r.name for r in run.data[0]] == ["Risk A", "Risk B"]
        # One batch call names several risks, so every risk shares that response.
        assert len(run.sources[0]) == len(run.data[0])
        assert run.sources[0][0] is run.sources[0][1] is run.outputs[0][0]

    def test_batch_outputs_grouped_one_call_per_usecase(self):
        engine = _engine(
            StubResponse(["Risk A"], 100, 50), StubResponse(["Risk B"], 120, 60)
        )
        run = _detector(engine, RISKS)._run_inference(["u1", "u2"])

        assert [len(o) for o in run.outputs] == [1, 1]
        assert len(run.all_outputs) == 2

    def test_per_risk_sources_pair_each_risk_with_its_own_response(self):
        engine = _per_risk_engine([["no", "yes", "yes"]])
        run = _detector_per_risk(engine, THREE_RISKS)._run_inference(["usecase 1"])

        assert [r.name for r in run.data[0]] == ["Risk B", "Risk C"]
        assert [s.thinking for s in run.sources[0]] == [
            "thinking-u0-r1",
            "thinking-u0-r2",
        ]

    def test_per_risk_outputs_include_calls_that_identified_nothing(self):
        engine = _per_risk_engine([["no", "yes", "yes"], ["yes", "no", "yes"]])
        run = _detector_per_risk(engine, THREE_RISKS)._run_inference(["u1", "u2"])

        # 2 risks identified per usecase, but 3 calls made per usecase.
        assert [len(s) for s in run.sources] == [2, 2]
        assert [len(o) for o in run.outputs] == [3, 3]
        assert len(run.all_outputs) == 6

    def test_module_level_batch_schema_is_not_mutated(self):
        """The risk-name enum must not leak from one detector to the next."""
        engine = _engine(StubResponse(["Risk A"], 100, 50))
        _detector(engine, RISKS)._run_inference(["usecase 1"])

        assert LIST_OF_STR_SCHEMA["items"]["enum"] is None


class TestExplanationTypeValidation:
    """An explanation type with no source must fail loudly, and fail early."""

    def test_unknown_type_rejected_at_construction(self):
        """Deferring to detect() would let a typo through whenever no risk matched."""
        engine = _engine(StubResponse(["Risk A"], 100, 50))

        with pytest.raises(ValueError, match="Unknown explanation type"):
            RiskDetectorWithExplanation(
                _detector(engine, RISKS), "not-an-explanation-type"
            )

    def test_equivalent_string_accepted(self):
        """`ExplanationType` is a str enum, so its values are usable directly."""
        engine = _engine(StubResponse(["Risk A"], 100, 50))
        detector = RiskDetectorWithExplanation(_detector(engine, RISKS), "description")

        result = detector.detect(["usecase 1"])

        assert result[0][0].explanation == "Description of risk A"

    def test_every_explanation_type_has_a_source(self):
        """Adding an ExplanationType member without wiring it must fail this test."""
        for explanation_type in ExplanationType:
            if explanation_type is ExplanationType.NONE:
                continue
            engine = _engine(StubResponse(["Risk A"], 100, 50))
            detector = _with_explanation(engine, RISKS, explanation_type)

            result = detector.detect(["usecase 1"])

            assert isinstance(result[0][0], RiskWithExplanation), explanation_type
