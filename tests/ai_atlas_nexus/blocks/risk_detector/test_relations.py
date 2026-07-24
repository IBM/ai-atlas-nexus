"""Tests for RiskRelationDetector (RiskMapper INFERENCE relation classification).

Two engine stubs are used, both deterministic and CI-safe:

* ``_FakeEngine`` returns already-parsed predictions, to exercise the detector's
  parsing/filtering logic in isolation.
* ``_RawEngine`` returns raw model strings and runs them through the real
  ``json_object`` postprocessor, to exercise the full model-output -> parse
  chain the way a real inference engine (Ollama, vLLM, WML, ...) would.
"""

from types import SimpleNamespace

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk
from ai_atlas_nexus.blocks.inference.postprocessing import POSTPROCESSORS_REGISTRY
from ai_atlas_nexus.blocks.risk_detector import RiskRelationDetector


def _risk(rid, name, description, taxonomy="tax-existing"):
    return Risk(
        id=rid, name=name, description=description, isDefinedByTaxonomy=taxonomy
    )


class _FakeEngine:
    """Engine stub returning already-postprocessed predictions."""

    def __init__(self, predictions):
        self._predictions = predictions
        self.captured = {}

    def generate(self, prompts, response_format=None, postprocessors=None):
        self.captured = {
            "prompts": prompts,
            "response_format": response_format,
            "postprocessors": postprocessors,
        }
        return [
            SimpleNamespace(prediction=pred)
            for pred in self._predictions[: len(prompts)]
        ]


class _RawEngine:
    """Engine stub returning raw model strings, run through real postprocessors.

    This mirrors what a real InferenceEngine does: the model emits text, and the
    registered postprocessors turn it into a Python object before the detector
    parses it. It keeps the test deterministic while covering the real chain.
    """

    def __init__(self, raw_outputs):
        self._raw = raw_outputs

    def generate(self, prompts, response_format=None, postprocessors=None):
        outputs = []
        for raw in self._raw[: len(prompts)]:
            prediction = raw
            for processor in postprocessors or []:
                prediction = POSTPROCESSORS_REGISTRY[processor]().apply(prediction)
            outputs.append(SimpleNamespace(prediction=prediction))
        return outputs


def _detector(engine, risks):
    return RiskRelationDetector(risks=risks, inference_engine=engine, cot_examples=None)


CANDIDATES = [
    _risk("atlas-a", "Alpha risk", "About alpha"),
    _risk("atlas-b", "Beta risk", "About beta"),
]


class TestParsing:
    """Detector parsing/filtering logic (predictions already postprocessed)."""

    def test_maps_relation_labels_to_skos_predicates(self):
        engine = _FakeEngine([[{"category": "Beta risk", "relation": "closeMatch"}]])
        result = _detector(engine, CANDIDATES).detect(["a new risk"])
        assert len(result) == 1 and len(result[0]) == 1
        risk, predicate = result[0][0]
        assert risk.id == "atlas-b"
        assert predicate == "skos:closeMatch"

    def test_named_tuple_fields(self):
        engine = _FakeEngine([[{"category": "Alpha risk", "relation": "exactMatch"}]])
        rel = _detector(engine, CANDIDATES).detect(["x"])[0][0]
        assert rel.risk.id == "atlas-a"
        assert rel.predicate == "skos:exactMatch"

    def test_schema_enumerates_candidate_names_and_relations(self):
        engine = _FakeEngine([[]])
        _detector(engine, CANDIDATES).detect(["a new risk"])
        schema = engine.captured["response_format"]
        assert schema["items"]["properties"]["category"]["enum"] == [
            "Alpha risk",
            "Beta risk",
        ]
        assert schema["items"]["properties"]["relation"]["enum"] == [
            "exactMatch",
            "closeMatch",
            "relatedMatch",
        ]
        assert engine.captured["postprocessors"] == ["json_object"]

    def test_omits_unknown_names_and_invalid_relations(self):
        engine = _FakeEngine(
            [
                [
                    {"category": "Beta risk", "relation": "exactMatch"},
                    {"category": "Ghost risk", "relation": "closeMatch"},  # unknown
                    {"category": "Alpha risk", "relation": "broadMatch"},  # excluded
                    {"category": "Alpha risk", "relation": "noMatch"},  # not a match
                ]
            ]
        )
        result = _detector(engine, CANDIDATES).detect(["a new risk"])
        assert [(r.id, p) for r, p in result[0]] == [("atlas-b", "skos:exactMatch")]

    def test_relation_label_is_case_sensitive(self):
        engine = _FakeEngine([[{"category": "Alpha risk", "relation": "ExactMatch"}]])
        assert _detector(engine, CANDIDATES).detect(["x"]) == [[]]

    def test_item_missing_keys_is_skipped(self):
        engine = _FakeEngine(
            [
                [
                    {"category": "Alpha risk"},  # no relation
                    {"relation": "exactMatch"},  # no category
                    {"category": "Beta risk", "relation": "relatedMatch"},
                ]
            ]
        )
        result = _detector(engine, CANDIDATES).detect(["x"])
        assert [(r.id, p) for r, p in result[0]] == [("atlas-b", "skos:relatedMatch")]

    def test_non_list_prediction_yields_no_pairs(self):
        engine = _FakeEngine(["not json"])
        assert _detector(engine, CANDIDATES).detect(["a new risk"]) == [[]]

    def test_multiple_usecases_return_aligned_results(self):
        engine = _FakeEngine(
            [
                [{"category": "Alpha risk", "relation": "relatedMatch"}],
                [{"category": "Beta risk", "relation": "exactMatch"}],
            ]
        )
        result = _detector(engine, CANDIDATES).detect(["risk one", "risk two"])
        assert [(r.id, p) for r, p in result[0]] == [("atlas-a", "skos:relatedMatch")]
        assert [(r.id, p) for r, p in result[1]] == [("atlas-b", "skos:exactMatch")]


class TestRealPostprocessorChain:
    """Full raw-string -> json_object postprocessor -> parse chain."""

    def test_clean_json_array(self):
        engine = _RawEngine(['[{"category": "Beta risk", "relation": "closeMatch"}]'])
        result = _detector(engine, CANDIDATES).detect(["x"])
        assert [(r.id, p) for r, p in result[0]] == [("atlas-b", "skos:closeMatch")]

    def test_surrounding_whitespace_and_newlines(self):
        engine = _RawEngine(
            ['\n\n  [{"category": "Alpha risk", "relation": "exactMatch"}]  \n']
        )
        result = _detector(engine, CANDIDATES).detect(["x"])
        assert [(r.id, p) for r, p in result[0]] == [("atlas-a", "skos:exactMatch")]

    def test_backtick_fenced_json(self):
        engine = _RawEngine(
            ['```\n[{"category": "Beta risk", "relation": "relatedMatch"}]\n```']
        )
        result = _detector(engine, CANDIDATES).detect(["x"])
        assert [(r.id, p) for r, p in result[0]] == [("atlas-b", "skos:relatedMatch")]

    def test_malformed_model_output_is_handled_gracefully(self):
        engine = _RawEngine(["Sure! Here are the matches: none really."])
        assert _detector(engine, CANDIDATES).detect(["x"]) == [[]]

    def test_empty_json_array(self):
        engine = _RawEngine(["[]"])
        assert _detector(engine, CANDIDATES).detect(["x"]) == [[]]


class TestEdgeCases:

    def test_no_candidates(self):
        engine = _FakeEngine([[]])
        detector = _detector(engine, [])
        result = detector.detect(["x"])
        assert result == [[]]
        assert (
            engine.captured["response_format"]["items"]["properties"]["category"][
                "enum"
            ]
            == []
        )

    def test_no_usecases(self):
        engine = _FakeEngine([])
        assert _detector(engine, CANDIDATES).detect([]) == []

    def test_one_usecase_with_no_matches_among_many(self):
        engine = _FakeEngine(
            [
                [],  # first source risk matches nothing
                [{"category": "Alpha risk", "relation": "exactMatch"}],
            ]
        )
        result = _detector(engine, CANDIDATES).detect(["r1", "r2"])
        assert result[0] == []
        assert [(r.id, p) for r, p in result[1]] == [("atlas-a", "skos:exactMatch")]

    def test_many_candidates_schema_and_parse(self):
        many = [_risk(f"atlas-{i}", f"Risk {i}", f"desc {i}") for i in range(50)]
        engine = _FakeEngine([[{"category": "Risk 42", "relation": "closeMatch"}]])
        detector = _detector(engine, many)
        result = detector.detect(["x"])
        assert (
            len(
                engine.captured["response_format"]["items"]["properties"]["category"][
                    "enum"
                ]
            )
            == 50
        )
        assert [(r.id, p) for r, p in result[0]] == [("atlas-42", "skos:closeMatch")]
