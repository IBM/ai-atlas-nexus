"""Tests for RiskMapper semantic mapping."""

import pytest

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk
from ai_atlas_nexus.blocks.risk_mapping import RiskMapper
from ai_atlas_nexus.metadata_base import MappingMethod


def _make_mapper():
    return RiskMapper(
        new_risks=[],
        existing_risks=[],
        inference_engine=None,
        new_prefix="test",
        mapping_method=MappingMethod.SEMANTIC,
    )


class TestBucketSemanticScore:
    """_bucket_semantic_score buckets a 0-1 float into a SKOS predicate."""

    def test_exact_match(self):
        assert _make_mapper()._bucket_semantic_score(0.98) == "skos:exactMatch"

    def test_close_match(self):
        assert _make_mapper()._bucket_semantic_score(0.85) == "skos:closeMatch"

    def test_related_match(self):
        assert _make_mapper()._bucket_semantic_score(0.60) == "skos:relatedMatch"

    def test_no_match(self):
        assert _make_mapper()._bucket_semantic_score(0.20) == "noMatch"

    def test_monotonic_ordering(self):
        """Higher similarity never yields a weaker relationship."""
        rank = {
            "noMatch": 0,
            "skos:relatedMatch": 1,
            "skos:closeMatch": 2,
            "skos:exactMatch": 3,
        }
        mapper = _make_mapper()
        scores = [0.1, 0.3, 0.5, 0.7, 0.9, 1.0]
        ranks = [rank[mapper._bucket_semantic_score(s)] for s in scores]
        assert ranks == sorted(ranks)


@pytest.mark.slow
class TestGenerateSemantic:
    """generate() with SEMANTIC uses the similarity score, not the list index."""

    def _risk(self, rid, name, description, taxonomy):
        return Risk(
            id=rid, name=name, description=description, isDefinedByTaxonomy=taxonomy
        )

    def test_similarity_score_is_a_float_not_an_index(self):
        existing = [
            self._risk(
                "atlas-a", "Alpha risk", "A risk about alpha behaviour", "tax-existing"
            ),
            self._risk(
                "atlas-b", "Beta risk", "A risk about beta behaviour", "tax-existing"
            ),
        ]
        # near-verbatim copy of the second existing risk -> high similarity
        new = [
            self._risk("new-b", "Beta risk", "A risk about beta behaviour", "tax-new")
        ]

        mapper = _make_mapper()
        mappings = mapper.generate(
            new_risks=new,
            existing_risks=existing,
            inference_engine=None,
            new_prefix="tax-new",
            mapping_method=MappingMethod.SEMANTIC,
        )

        assert len(mappings) == 1
        m = mappings[0]
        # matched the right existing risk
        assert m.object_id == "tax-existing:atlas-b"
        # similarity_score is a real 0-1 similarity, not the row index
        assert isinstance(m.similarity_score, float)
        assert 0.0 < m.similarity_score <= 1.0
        # a near-identical risk should be a strong match
        assert m.predicate_id in ("skos:exactMatch", "skos:closeMatch")
