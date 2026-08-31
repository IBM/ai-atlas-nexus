"""Public API tests for risk identification.

The detector classes are covered in
`tests/ai_atlas_nexus/blocks/risk_detector/test_generic_metadata.py`. This module
covers what `AIAtlasNexus` does on top of them: composing the detector decorators
from the `return_metadata` / `explanation_type` flags, and the shape of the dict
`identify_risks_and_actions_from_usecases` returns.
"""

import pytest

from ai_atlas_nexus import AIAtlasNexus
from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk
from ai_atlas_nexus.blocks.risk_detector import DetectionResult, RiskWithExplanation
from ai_atlas_nexus.metadata_base import ExplanationType
from tests.ai_atlas_nexus.stub_inference import StubInferenceEngine, StubResponse


TAXONOMY = "ibm-risk-atlas"


def _engine(*responses: StubResponse) -> StubInferenceEngine:
    """Batch-mode engine: one response per usecase."""
    return StubInferenceEngine(responses)


@pytest.fixture(scope="module")
def nexus():
    return AIAtlasNexus()


@pytest.fixture(scope="module")
def risk_names(nexus):
    risks = nexus.get_all("risks", taxonomy=TAXONOMY)
    assert len(risks) >= 2, "taxonomy needs at least two risks for these tests"
    return [risks[0].name, risks[1].name]


def _identify(nexus, engine, usecases, **kwargs):
    return nexus.identify_risks_from_usecases(
        usecases=usecases,
        inference_engine=engine,
        taxonomy=TAXONOMY,
        **kwargs,
    )


class TestIdentifyRisksComposition:
    """The flags must compose into exactly the requested return type."""

    def test_default_returns_bare_risks(self, nexus, risk_names):
        engine = _engine(StubResponse([risk_names[0]]))

        result = _identify(nexus, engine, ["a usecase"])

        assert isinstance(result, list)
        assert not isinstance(result, DetectionResult)
        assert isinstance(result[0][0], Risk)
        assert result[0][0].name == risk_names[0]

    def test_explicit_none_explanation_returns_bare_risks(self, nexus, risk_names):
        """`ExplanationType.NONE` must not wrap; it is the undecorated detector."""
        engine = _engine(StubResponse([risk_names[0]]))

        result = _identify(
            nexus, engine, ["a usecase"], explanation_type=ExplanationType.NONE
        )

        assert isinstance(result[0][0], Risk)

    def test_explanation_type_returns_explained_risks(self, nexus, risk_names):
        engine = _engine(StubResponse([risk_names[0]]))

        result = _identify(
            nexus, engine, ["a usecase"], explanation_type=ExplanationType.DESCRIPTION
        )

        assert isinstance(result[0][0], RiskWithExplanation)
        assert result[0][0].risk.name == risk_names[0]
        assert result[0][0].explanation == result[0][0].risk.description

    def test_return_metadata_wraps_with_usage(self, nexus, risk_names):
        engine = _engine(StubResponse([risk_names[0]]))

        result = _identify(nexus, engine, ["a usecase"], return_metadata=True)

        assert isinstance(result, DetectionResult)
        assert isinstance(result.data[0][0], Risk)
        assert result.metadata.model == "stub-model"
        assert result.metadata.token_usage.total_tokens == 110
        assert len(result.metadata.per_usecase) == 1

    def test_both_flags_compose(self, nexus, risk_names):
        engine = _engine(StubResponse([risk_names[0]]))

        result = _identify(
            nexus,
            engine,
            ["a usecase"],
            return_metadata=True,
            explanation_type=ExplanationType.DESCRIPTION,
        )

        assert isinstance(result, DetectionResult)
        assert isinstance(result.data[0][0], RiskWithExplanation)
        assert result.metadata.token_usage.total_tokens == 110

    def test_per_usecase_metadata_aligns_with_data(self, nexus, risk_names):
        engine = _engine(
            StubResponse([risk_names[0]]),
            StubResponse([risk_names[1]], 101, 11),
        )

        result = _identify(nexus, engine, ["first", "second"], return_metadata=True)

        assert len(result.data) == len(result.metadata.per_usecase) == 2
        assert [risks[0].name for risks in result.data] == risk_names
        # Stub bills 100+index in / 10+index out, so usecase 2 costs one more of each.
        per_usecase = result.metadata.per_usecase
        assert [u.token_usage.input_tokens for u in per_usecase] == [100, 101]
        assert result.metadata.token_usage.input_tokens == 201

    def test_self_explanation_requests_a_schema_with_explanations(
        self, nexus, risk_names
    ):
        prediction = {
            "risks": [{"risk_name": risk_names[0], "explanation": "because of X"}]
        }
        engine = _engine(StubResponse(prediction))

        result = _identify(
            nexus,
            engine,
            ["a usecase"],
            explanation_type=ExplanationType.SELF_EXPLANATION,
        )

        assert result[0][0].explanation == "because of X"
        schema = engine.calls[0].response_format.model_json_schema()
        assert (
            "explanation"
            in schema["$defs"]["RiskWithExplanationItem"]["properties"]
        )


class TestIdentifyRisksAndActions:
    """The returned dict reports every usecase, not just the first."""

    def test_one_entry_per_usecase(self, nexus, risk_names):
        engine = _engine(
            StubResponse([risk_names[0]]),
            StubResponse([risk_names[1]], 101, 11),
        )

        result = nexus.identify_risks_and_actions_from_usecases(
            usecases=["first", "second"],
            inference_engine=engine,
            taxonomy=TAXONOMY,
        )

        assert result["usecases"] == ["first", "second"]
        assert [entry["usecase"] for entry in result["per_usecase"]] == [
            "first",
            "second",
        ]
        # Each entry reports its own risks, rather than every entry repeating the first.
        assert [entry["risks"][0].name for entry in result["per_usecase"]] == risk_names
        assert [entry["summary"]["risk_ids"] for entry in result["per_usecase"]] == [
            [entry["risks"][0].id] for entry in result["per_usecase"]
        ]

    def test_entry_carries_summary_and_controls(self, nexus, risk_names):
        engine = _engine(StubResponse([risk_names[0]]))

        result = nexus.identify_risks_and_actions_from_usecases(
            usecases=["a usecase"],
            inference_engine=engine,
            taxonomy=TAXONOMY,
        )

        entry = result["per_usecase"][0]
        assert set(entry) == {"usecase", "risks", "summary", "mixed_control_items"}
        assert set(entry["summary"]) >= {"risk_ids", "action_ids", "detector_ids"}
        assert result["model"] == "stub-model"
        assert result["taxonomy"] == TAXONOMY

    def test_no_token_usage_without_return_metadata(self, nexus, risk_names):
        engine = _engine(StubResponse([risk_names[0]]))

        result = nexus.identify_risks_and_actions_from_usecases(
            usecases=["a usecase"],
            inference_engine=engine,
            taxonomy=TAXONOMY,
        )

        assert "token_usage" not in result
        assert "token_usage" not in result["per_usecase"][0]

    def test_token_usage_reported_per_usecase_and_overall(self, nexus, risk_names):
        engine = _engine(
            StubResponse([risk_names[0]]),
            StubResponse([risk_names[1]], 101, 11),
        )

        result = nexus.identify_risks_and_actions_from_usecases(
            usecases=["first", "second"],
            inference_engine=engine,
            taxonomy=TAXONOMY,
            return_metadata=True,
        )

        assert result["token_usage"] == {
            "input_tokens": 201,
            "output_tokens": 21,
            "total_tokens": 222,
            "num_calls": 2,
        }
        assert [entry["token_usage"] for entry in result["per_usecase"]] == [
            {
                "input_tokens": 100,
                "output_tokens": 10,
                "total_tokens": 110,
                "num_calls": 1,
            },
            {
                "input_tokens": 101,
                "output_tokens": 11,
                "total_tokens": 112,
                "num_calls": 1,
            },
        ]
        # The per-usecase entries must account for the whole run.
        assert (
            sum(e["token_usage"]["total_tokens"] for e in result["per_usecase"])
            == result["token_usage"]["total_tokens"]
        )

    def test_explanations_do_not_break_the_summary(self, nexus, risk_names):
        """`summary` and control lookups work off the underlying risks."""
        engine = _engine(StubResponse([risk_names[0]]))

        result = nexus.identify_risks_and_actions_from_usecases(
            usecases=["a usecase"],
            inference_engine=engine,
            taxonomy=TAXONOMY,
            explanation_type=ExplanationType.DESCRIPTION,
        )

        entry = result["per_usecase"][0]
        assert isinstance(entry["risks"][0], RiskWithExplanation)
        assert entry["summary"]["risk_ids"] == [entry["risks"][0].risk.id]
