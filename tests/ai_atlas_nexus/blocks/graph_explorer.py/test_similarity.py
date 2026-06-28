from unittest.mock import MagicMock, patch

import pytest

from ai_atlas_nexus import AIAtlasNexus
from ai_atlas_nexus.blocks.graph_explorer import (
    PyoxigraphExplorer,
    SimilarityResult,
    SubGraph,
    compute_similarity,
    extract_subgraph,
)


@pytest.fixture
def nexus():
    """Load bundled ontology."""
    return AIAtlasNexus()


@pytest.fixture
def ox_explorer(nexus):
    """PyoxigraphExplorer with bundled ontology."""
    return PyoxigraphExplorer(nexus._ontology)


def get_entity_ids_by_type(nexus, entity_type):
    """Helper to find entity IDs of a specific type."""
    ids = []
    for field in nexus._ontology.model_fields_set:
        items = getattr(nexus._ontology, field, None) or []
        if not isinstance(items, list):
            items = [items]
        for item in items:
            if type(item).__name__ == entity_type:
                if hasattr(item, "id"):
                    ids.append(item.id)
    return ids


class TestExtractSubgraph:
    def test_extract_subgraph_returns_subgraph(self, ox_explorer, nexus):
        """extract_subgraph returns a SubGraph with root_id and nodes populated."""
        # Find any entity with ID
        ids = get_entity_ids_by_type(nexus, "Risk")
        if not ids:
            pytest.skip("No Risk entities in ontology")

        sg = extract_subgraph(ox_explorer, ids[0])

        assert isinstance(sg, SubGraph)
        assert sg.root_id == ids[0]
        assert isinstance(sg.nodes, dict)
        # Root node should always be included
        assert len(sg.nodes) > 0

    def test_extract_subgraph_max_hops_0(self, ox_explorer, nexus):
        """max_hops=0 returns only the root node."""
        ids = get_entity_ids_by_type(nexus, "Risk")
        if not ids:
            pytest.skip("No Risk entities in ontology")

        sg = extract_subgraph(ox_explorer, ids[0], max_hops=0)

        assert isinstance(sg, SubGraph)
        # Should have at least the root node
        all_node_ids = set()
        for node_set in sg.nodes.values():
            all_node_ids.update(node_set)
        assert ids[0] in all_node_ids
        # No edges should be added at depth 0
        assert len(sg.edges) == 0

    def test_extract_subgraph_max_hops_1(self, ox_explorer, nexus):
        """max_hops=1 returns direct neighbours but not their neighbours."""
        ids = get_entity_ids_by_type(nexus, "Risk")
        if not ids:
            pytest.skip("No Risk entities in ontology")

        sg = extract_subgraph(ox_explorer, ids[0], max_hops=1)

        # Check that we have at least the root
        all_node_ids = set()
        for node_set in sg.nodes.values():
            all_node_ids.update(node_set)
        assert ids[0] in all_node_ids

        # Check that all edge endpoints are within distance 1
        for subj_id, pred, obj_id in sg.edges:
            assert subj_id == ids[0]  # All edges should originate from root

    def test_extract_subgraph_unknown_id(self, ox_explorer):
        """Unknown entity ID returns empty SubGraph."""
        sg = extract_subgraph(ox_explorer, "nonexistent_id_xyz")

        assert isinstance(sg, SubGraph)
        assert sg.root_id == "nonexistent_id_xyz"
        assert len(sg.nodes) == 0
        assert len(sg.edges) == 0
        assert sg.text_summary == ""

    def test_extract_subgraph_builds_text_summary(self, ox_explorer, nexus):
        """Text summary is built from node names and descriptions."""
        ids = get_entity_ids_by_type(nexus, "Risk")
        if not ids:
            pytest.skip("No Risk entities in ontology")

        sg = extract_subgraph(ox_explorer, ids[0], max_hops=0)

        # Text summary should be non-empty and contain the entity type and ID
        assert len(sg.text_summary) > 0
        assert "Risk" in sg.text_summary  # Entity type
        assert ids[0] in sg.text_summary  # Entity ID


class TestComputeSimilarityStructural:
    def test_compute_similarity_same_subgraph(self, ox_explorer, nexus):
        """Similarity of a subgraph with itself is 1.0."""
        ids = get_entity_ids_by_type(nexus, "Risk")
        if not ids:
            pytest.skip("No Risk entities in ontology")

        sg = extract_subgraph(ox_explorer, ids[0])
        result = compute_similarity(sg, sg, method="structural")

        assert isinstance(result, SimilarityResult)
        assert result.method == "structural"
        assert result.score == 1.0
        assert result.structural_score == 1.0
        assert result.semantic_score is None

    def test_compute_similarity_disjoint_subgraphs(self, ox_explorer, nexus):
        """Two subgraphs with no shared nodes should have similarity ≈ 0.0."""
        # Create two disjoint subgraphs manually
        sg1 = SubGraph(root_id="a")
        sg1.nodes["Risk"] = {"a", "b"}

        sg2 = SubGraph(root_id="c")
        sg2.nodes["Risk"] = {"c", "d"}

        result = compute_similarity(sg1, sg2, method="structural")

        assert result.score == 0.0
        assert result.breakdown["Risk"] == 0.0

    def test_compute_similarity_partial_overlap(self, ox_explorer, nexus):
        """Jaccard similarity correctly computed for overlapping node sets."""
        sg1 = SubGraph(root_id="a")
        sg1.nodes["Risk"] = {"a", "b", "c"}

        sg2 = SubGraph(root_id="b")
        sg2.nodes["Risk"] = {"b", "c", "d"}

        result = compute_similarity(sg1, sg2, method="structural")

        # Jaccard: |{b,c}| / |{a,b,c,d}| = 2/4 = 0.5
        assert result.score == 0.5
        assert result.breakdown["Risk"] == 0.5

    def test_compute_similarity_structural_breakdown(self, ox_explorer, nexus):
        """Breakdown contains per-type Jaccard scores."""
        sg1 = SubGraph(root_id="a")
        sg1.nodes["Risk"] = {"a", "b"}
        sg1.nodes["AiTask"] = {"x", "y"}

        sg2 = SubGraph(root_id="b")
        sg2.nodes["Risk"] = {"b", "c"}
        sg2.nodes["AiTask"] = {"y", "z"}

        result = compute_similarity(sg1, sg2, method="structural")

        assert "Risk" in result.breakdown
        assert "AiTask" in result.breakdown
        # Risk: |{b}| / |{a,b,c}| = 1/3 ≈ 0.333
        # AiTask: |{y}| / |{x,y,z}| = 1/3 ≈ 0.333
        # Average: 0.333
        expected = (1/3 + 1/3) / 2
        assert abs(result.score - expected) < 0.01

    def test_compute_similarity_empty_subgraphs(self, ox_explorer):
        """Empty subgraphs have zero similarity."""
        sg1 = SubGraph(root_id="a")
        sg2 = SubGraph(root_id="b")

        result = compute_similarity(sg1, sg2, method="structural")

        assert result.score == 0.0


class TestComputeSimilaritySemantic:
    @patch("ai_atlas_nexus.blocks.graph_explorer.similarity.Embeddings", None)
    def test_compute_similarity_semantic_no_txtai(self, ox_explorer):
        """Semantic similarity raises ImportError if txtai not installed."""
        sg1 = SubGraph(root_id="a")
        sg1.text_summary = "test summary"

        sg2 = SubGraph(root_id="b")
        sg2.text_summary = "test summary"

        with pytest.raises(ImportError, match="txtai is not installed"):
            compute_similarity(sg1, sg2, method="semantic")

    def test_compute_similarity_semantic_empty_summaries(self, ox_explorer):
        """Semantic similarity with empty summaries returns 0.0."""
        sg1 = SubGraph(root_id="a")
        sg1.text_summary = ""

        sg2 = SubGraph(root_id="b")
        sg2.text_summary = ""

        result = compute_similarity(sg1, sg2, method="semantic")

        assert result.method == "semantic"
        assert result.score == 0.0
        assert result.semantic_score == 0.0

    @pytest.mark.slow
    def test_compute_similarity_semantic_identical_text(self, ox_explorer):
        """Semantic similarity of identical text summaries is ≈ 1.0."""
        text = "Risk management system for AI deployment"

        sg1 = SubGraph(root_id="a")
        sg1.text_summary = text

        sg2 = SubGraph(root_id="b")
        sg2.text_summary = text

        result = compute_similarity(sg1, sg2, method="semantic")

        assert result.method == "semantic"
        assert abs(result.score - 1.0) < 0.1  # Allow some tolerance for embeddings

    @pytest.mark.slow
    def test_compute_similarity_semantic_different_text(self, ox_explorer):
        """Semantic similarity of unrelated texts is < 0.5."""
        sg1 = SubGraph(root_id="a")
        sg1.text_summary = "apples oranges bananas fruit"

        sg2 = SubGraph(root_id="b")
        sg2.text_summary = "network security firewall encryption"

        result = compute_similarity(sg1, sg2, method="semantic")

        assert result.method == "semantic"
        assert result.score < 0.5  # Should be quite different


class TestComputeSimilarityHybrid:
    def test_compute_similarity_hybrid_alpha_0(self, ox_explorer):
        """Hybrid with alpha=0 is pure semantic."""
        sg1 = SubGraph(root_id="a")
        sg1.nodes["Risk"] = {"a"}
        sg1.text_summary = ""

        sg2 = SubGraph(root_id="b")
        sg2.nodes["Risk"] = {"b"}
        sg2.text_summary = ""

        result = compute_similarity(sg1, sg2, method="hybrid", alpha=0.0)

        assert result.method == "hybrid"
        assert result.structural_score is not None
        assert result.semantic_score is not None
        # With alpha=0 and empty text, score should be 0
        assert result.score == 0.0

    def test_compute_similarity_hybrid_alpha_1(self, ox_explorer):
        """Hybrid with alpha=1 is pure structural."""
        sg1 = SubGraph(root_id="a")
        sg1.nodes["Risk"] = {"a", "b"}

        sg2 = SubGraph(root_id="b")
        sg2.nodes["Risk"] = {"b", "c"}

        result = compute_similarity(sg1, sg2, method="hybrid", alpha=1.0)

        assert result.method == "hybrid"
        assert result.structural_score is not None
        assert result.semantic_score is not None
        # Score should equal structural only (alpha=1)
        assert abs(result.score - result.structural_score) < 0.001

    def test_compute_similarity_hybrid_default_alpha(self, ox_explorer):
        """Hybrid with default alpha=0.5 blends both scores."""
        sg1 = SubGraph(root_id="a")
        sg1.nodes["Risk"] = {"a"}
        sg1.text_summary = "empty"

        sg2 = SubGraph(root_id="b")
        sg2.nodes["Risk"] = {"b"}
        sg2.text_summary = "empty"

        result = compute_similarity(sg1, sg2, method="hybrid")

        assert result.method == "hybrid"
        # Score should be between structural and semantic
        assert min(result.structural_score, result.semantic_score) <= result.score <= max(result.structural_score, result.semantic_score)


class TestComputeSimilarityValidation:
    def test_compute_similarity_invalid_method(self, ox_explorer):
        """Unknown method raises ValueError."""
        sg1 = SubGraph(root_id="a")
        sg2 = SubGraph(root_id="b")

        with pytest.raises(ValueError, match="Unknown similarity method"):
            compute_similarity(sg1, sg2, method="invalid")


class TestIntegration:
    def test_full_workflow_on_real_data(self, ox_explorer, nexus):
        """End-to-end: extract two subgraphs and compare them."""
        ids = get_entity_ids_by_type(nexus, "Risk")
        if len(ids) < 2:
            pytest.skip("Need at least 2 Risk entities")

        sg1 = extract_subgraph(ox_explorer, ids[0])
        sg2 = extract_subgraph(ox_explorer, ids[1])

        # Structural similarity
        result_struct = compute_similarity(sg1, sg2, method="structural")
        assert 0 <= result_struct.score <= 1
        assert result_struct.method == "structural"

        # Hybrid similarity (should handle gracefully even with empty summaries)
        result_hybrid = compute_similarity(sg1, sg2, method="hybrid")
        assert 0 <= result_hybrid.score <= 1
        assert result_hybrid.method == "hybrid"

    def test_compare_different_entity_types(self, ox_explorer, nexus):
        """extract_subgraph works on different entity types (generic)."""
        risk_ids = get_entity_ids_by_type(nexus, "Risk")
        task_ids = get_entity_ids_by_type(nexus, "AiTask")

        if not risk_ids:
            pytest.skip("No Risk entities")
        if not task_ids:
            pytest.skip("No AiTask entities")

        sg_risk = extract_subgraph(ox_explorer, risk_ids[0])
        sg_task = extract_subgraph(ox_explorer, task_ids[0])

        assert sg_risk.root_id == risk_ids[0]
        assert sg_task.root_id == task_ids[0]

        # Comparison should work generically
        result = compute_similarity(sg_risk, sg_task, method="structural")
        assert 0 <= result.score <= 1
