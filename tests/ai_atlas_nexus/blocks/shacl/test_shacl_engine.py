"""Tests for SHACLEngine and shape_loader."""

import io
import os
import tempfile

import pyoxigraph
import pytest

from ai_atlas_nexus import AIAtlasNexus
from ai_atlas_nexus.blocks.shacl import SHACLEngine
from ai_atlas_nexus.blocks.shacl.shape_loader import load_shapes


# ---------------------------------------------------------------------------
# Minimal Turtle shape fixtures
# ---------------------------------------------------------------------------

_PERSON_SHAPE_TTL = b"""
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ex: <http://example.org/> .

ex:PersonShape a sh:NodeShape ;
    sh:targetClass ex:Person ;
    sh:rule [
        a sh:SPARQLRule ;
        sh:construct \"\"\"
PREFIX ex: <http://example.org/>
CONSTRUCT { ?this ex:isAdult true }
WHERE { ?this ex:age ?age . FILTER(?age >= 18) }
\"\"\"
    ] .
"""

_PERSON_DATA_TTL = b"""
@prefix ex: <http://example.org/> .
ex:Bob a ex:Person ; ex:age 25 .
ex:Alice a ex:Person ; ex:age 15 .
"""

_CONSTRAINT_SHAPE_TTL = b"""
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ex: <http://example.org/> .

ex:PersonShape a sh:NodeShape ;
    sh:targetClass ex:Person ;
    sh:property [
        sh:path ex:age ;
        sh:minCount 1 ;
        sh:datatype xsd:integer
    ] .
"""


def _make_store(ttl: bytes) -> pyoxigraph.Store:
    store = pyoxigraph.Store()
    store.load(io.BytesIO(ttl), format=pyoxigraph.RdfFormat.TURTLE)
    return store


def _make_engine(ttl: bytes) -> SHACLEngine:
    return SHACLEngine(_make_store(ttl))


# ---------------------------------------------------------------------------
# shape_loader tests
# ---------------------------------------------------------------------------


class TestShapeLoader:
    def test_load_from_empty_base_dir(self, tmp_path):
        store = load_shapes(str(tmp_path))
        assert sum(1 for _ in store) == 0

    def test_load_from_shapes_dir(self, tmp_path):
        shapes_dir = tmp_path / "shapes"
        shapes_dir.mkdir()
        (shapes_dir / "rule.ttl").write_bytes(_PERSON_SHAPE_TTL)
        store = load_shapes(str(tmp_path))
        assert sum(1 for _ in store) > 0

    def test_load_multiple_shape_files(self, tmp_path):
        shapes_dir = tmp_path / "shapes"
        shapes_dir.mkdir()
        (shapes_dir / "rule1.ttl").write_bytes(_PERSON_SHAPE_TTL)
        (shapes_dir / "rule2.shacl").write_bytes(_CONSTRAINT_SHAPE_TTL)
        store = load_shapes(str(tmp_path))
        assert sum(1 for _ in store) > 0

    def test_load_no_base_dir(self):
        store = load_shapes(None)
        assert sum(1 for _ in store) == 0

    def test_load_yaml_inline_shapes(self, tmp_path):
        class FakeContainer:
            shacl_shapes = [{"turtle": _PERSON_SHAPE_TTL.decode()}]

        store = load_shapes(str(tmp_path), FakeContainer())
        assert sum(1 for _ in store) > 0

    def test_invalid_shape_file_is_skipped(self, tmp_path, caplog):
        shapes_dir = tmp_path / "shapes"
        shapes_dir.mkdir()
        (shapes_dir / "bad.ttl").write_bytes(b"NOT VALID TURTLE !!!")
        store = load_shapes(str(tmp_path))
        # Should not raise; just warns and continues
        assert sum(1 for _ in store) == 0


# ---------------------------------------------------------------------------
# SHACLEngine.from_discovery tests
# ---------------------------------------------------------------------------


class TestSHACLEngineFactory:
    def test_returns_none_when_no_shapes(self, tmp_path):
        engine = SHACLEngine.from_discovery(str(tmp_path))
        assert engine is None

    def test_returns_engine_when_shapes_found(self, tmp_path):
        (tmp_path / "shapes").mkdir()
        (tmp_path / "shapes" / "rule.ttl").write_bytes(_PERSON_SHAPE_TTL)
        engine = SHACLEngine.from_discovery(str(tmp_path))
        assert engine is not None
        assert engine.has_shapes()

    def test_returns_none_for_none_base_dir(self):
        engine = SHACLEngine.from_discovery(None)
        assert engine is None


# ---------------------------------------------------------------------------
# SHACLEngine.infer tests
# ---------------------------------------------------------------------------


class TestSHACLEngineInfer:
    def test_sparql_rule_fires_for_matching_instance(self):
        engine = _make_engine(_PERSON_SHAPE_TTL)
        data_store = _make_store(_PERSON_DATA_TTL)
        derived = engine.infer(data_store)
        # Bob (age 25) should get isAdult derived
        bob_uri = "http://example.org/Bob"
        assert bob_uri in derived
        assert "isAdult" in derived[bob_uri]
        assert derived[bob_uri]["isAdult"] is True

    def test_sparql_rule_does_not_fire_for_non_matching(self):
        engine = _make_engine(_PERSON_SHAPE_TTL)
        data_store = _make_store(_PERSON_DATA_TTL)
        derived = engine.infer(data_store)
        # Alice (age 15) should NOT get isAdult
        alice_uri = "http://example.org/Alice"
        assert alice_uri not in derived or "isAdult" not in derived.get(
            alice_uri, {}
        )

    def test_infer_adds_triples_to_store(self):
        engine = _make_engine(_PERSON_SHAPE_TTL)
        data_store = _make_store(_PERSON_DATA_TTL)
        count_before = sum(1 for _ in data_store)
        engine.infer(data_store)
        count_after = sum(1 for _ in data_store)
        assert count_after > count_before

    def test_infer_idempotent(self):
        engine = _make_engine(_PERSON_SHAPE_TTL)
        data_store = _make_store(_PERSON_DATA_TTL)
        engine.infer(data_store)
        count_after_first = sum(1 for _ in data_store)
        engine.infer(data_store)
        count_after_second = sum(1 for _ in data_store)
        assert count_after_first == count_after_second

    def test_infer_empty_store_returns_empty_derived(self):
        engine = _make_engine(_PERSON_SHAPE_TTL)
        empty_store = pyoxigraph.Store()
        derived = engine.infer(empty_store)
        assert derived == {}


# ---------------------------------------------------------------------------
# SHACLEngine.validate tests
# ---------------------------------------------------------------------------


class TestSHACLEngineValidate:
    def test_valid_data_conforms(self):
        engine = _make_engine(_CONSTRAINT_SHAPE_TTL)
        data_store = _make_store(_PERSON_DATA_TTL)
        report = engine.validate(data_store)
        assert report.conforms is True

    def test_invalid_data_does_not_conform(self):
        engine = _make_engine(_CONSTRAINT_SHAPE_TTL)
        # Missing age property
        bad_data = b"@prefix ex: <http://example.org/> . ex:Anon a ex:Person ."
        data_store = _make_store(bad_data)
        report = engine.validate(data_store)
        assert report.conforms is False

    def test_validation_report_has_text(self):
        engine = _make_engine(_CONSTRAINT_SHAPE_TTL)
        data_store = _make_store(_PERSON_DATA_TTL)
        report = engine.validate(data_store)
        assert isinstance(report.results_text, str)
        assert len(report.results_text) > 0


# ---------------------------------------------------------------------------
# SHACLEngine.augment_objects tests
# ---------------------------------------------------------------------------


class TestSHACLEngineAugmentObjects:
    def test_augments_matching_objects(self):
        from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk

        engine = _make_engine(_PERSON_SHAPE_TTL)
        derived = {
            "https://w3id.org/ai-atlas-nexus/my-risk": {"severity": "high"}
        }

        risk = Risk(id="my-risk", name="Test Risk")
        result = engine.augment_objects([risk], derived)

        assert len(result) == 1
        assert hasattr(result[0], "derived_attrs")
        assert result[0].derived_attrs["severity"] == "high"

    def test_objects_without_derived_data_unchanged(self):
        from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk

        engine = _make_engine(_PERSON_SHAPE_TTL)
        risk = Risk(id="no-match", name="Other Risk")
        result = engine.augment_objects([risk], {})
        assert not hasattr(result[0], "derived_attrs")

    def test_original_pydantic_fields_intact(self):
        from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk

        engine = _make_engine(_PERSON_SHAPE_TTL)
        derived = {"https://w3id.org/ai-atlas-nexus/test-id": {"foo": "bar"}}
        risk = Risk(id="test-id", name="Named Risk")
        result = engine.augment_objects([risk], derived)
        assert result[0].name == "Named Risk"
        assert result[0].id == "test-id"


# ---------------------------------------------------------------------------
# Integration: apply_rules=False is a no-op
# ---------------------------------------------------------------------------


class TestLibraryApplyRulesNoop:
    @pytest.fixture(scope="class")
    def nexus(self):
        return AIAtlasNexus()

    def test_get_all_risks_no_rules_unchanged(self, nexus):
        without_rules = nexus.get_all_risks()
        with_flag_false = nexus.get_all_risks(apply_rules=False)
        assert len(without_rules) == len(with_flag_false)

    def test_get_all_actions_no_rules_unchanged(self, nexus):
        without_rules = nexus.get_all_actions()
        with_flag_false = nexus.get_all_actions(apply_rules=False)
        assert len(without_rules) == len(with_flag_false)

    def test_get_all_risk_controls_no_rules_unchanged(self, nexus):
        without_rules = nexus.get_all_risk_controls()
        with_flag_false = nexus.get_all_risk_controls(apply_rules=False)
        assert len(without_rules) == len(with_flag_false)

    def test_apply_rules_true_no_engine_unchanged(self, nexus):
        # Base AIAtlasNexus() has no base_dir, so no engine — apply_rules=True is a no-op
        risks_no_rules = nexus.get_all_risks()
        risks_apply = nexus.get_all_risks(apply_rules=True)
        assert len(risks_apply) == len(risks_no_rules)
