import logging
from collections import deque
from dataclasses import dataclass, field
from typing import Optional


logger = logging.getLogger(__name__)

try:
    from txtai import Embeddings
except ImportError:
    Embeddings = None


@dataclass
class SubGraph:
    """Induced subgraph rooted at an entity and its neighborhood within max_hops.

    Attributes:
        root_id: str
            ID of the root entity.
        nodes: dict[str, set[str]]
            Dictionary mapping entity type to set of entity IDs.
        edges: set[tuple[str, str, str]]
            Set of (subject_id, predicate, object_id) tuples representing relationships.
    """

    root_id: str
    nodes: dict[str, set[str]] = field(default_factory=dict)
    edges: set[tuple[str, str, str]] = field(default_factory=set)
    _text_summary: Optional[str] = field(default=None, init=False, repr=False)

    @property
    def text_summary(self) -> str:
        """Concatenation of node names + description for semantic comparison."""
        if self._text_summary is None:
            self._text_summary = ""
        return self._text_summary

    @text_summary.setter
    def text_summary(self, value: str):
        self._text_summary = value


@dataclass
class SimilarityResult:
    """Result of comparing two subgraphs.

    Attributes:
        score: float
            Primary similarity score between 0 and 1.
        method: str
            Similarity method used ("structural", "semantic", or "hybrid").
        structural_score: Optional[float]
            Score from structural comparison, if applicable.
        semantic_score:  Optional[float] | None
            Score from semantic comparison, if applicable.
        breakdown: dict[str, float]
            Per-type Jaccard similarity scores.
    """

    score: float
    method: str
    structural_score: Optional[float] = None
    semantic_score: Optional[float] = None
    breakdown: dict[str, float] = field(default_factory=dict)


# Fields that should never be traversed as edges, even if they contain IDs.
SKIP_FIELDS = {
    "id",
    "name",
    "description",
    "url",
    "dateCreated",
    "dateModified",
    "type",
    "comment",
    # "exact_mappings", "close_mappings",
    # "related_mappings", "narrow_mappings", "broad_mappings",
    "isCategorizedAs",
}


def extract_subgraph(explorer, entity_id: str, max_hops: int = 2) -> SubGraph:
    """
    Extract a subgraph rooted at entity_id with all reachable entities within max_hops.

    Args:
        explorer: AtlasExplorer | PyoxigraphExplorer
            AtlasExplorer or PyoxigraphExplorer instance.
        entity_id: str
            ID of the root entity.
        max_hops: int
            Maximum traversal depth (0 = root only, 1 = direct neighbours, etc.)

    Returns:
        SubGraph
            SubGraph with nodes grouped by type and edges recorded.
    """
    sg = SubGraph(root_id=entity_id)

    id_cache = _get_id_cache(explorer)
    if not id_cache:
        logger.warning(f"Could not build ID cache from explorer")
        return sg

    root_entity = id_cache.get(entity_id)
    if not root_entity:
        logger.warning(f"Entity {entity_id} not found")
        return sg

    # BFS
    queue = deque([(entity_id, 0)])
    visited = {entity_id}
    text_parts = []

    while queue:
        curr_id, depth = queue.popleft()
        curr_entity = id_cache.get(curr_id)
        if not curr_entity:
            continue

        # Record the node
        entity_type = type(curr_entity).__name__
        if entity_type not in sg.nodes:
            sg.nodes[entity_type] = set()
        sg.nodes[entity_type].add(curr_id)

        # Build summary
        name = getattr(curr_entity, "name", "")
        desc = getattr(curr_entity, "description", "")
        text_parts.append(f"{entity_type}:{curr_id} {name} {desc}".strip())

        # Traverse relationships at depth < max_hops
        if depth < max_hops:
            # Iterate model fields to avoid Pydantic deprecation warnings
            from pydantic import BaseModel

            if isinstance(curr_entity, BaseModel):
                field_names = type(curr_entity).model_fields
            else:
                field_names = [
                    f for f in dir(curr_entity) if not f.startswith("_")
                ]

            for field_name in field_names:
                if field_name in SKIP_FIELDS:
                    continue

                try:
                    value = getattr(curr_entity, field_name)
                except (AttributeError, TypeError):
                    continue

                # Skip non-ID-like fields (methods, properties, etc.)
                if callable(value):
                    continue

                # Process string fields and lists
                targets = []
                if isinstance(value, str):
                    if value in id_cache:
                        targets.append(value)
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, str) and item in id_cache:
                            targets.append(item)

                # Add edges and enqueue unvisited targets
                for target_id in targets:
                    sg.edges.add((curr_id, field_name, target_id))
                    if target_id not in visited:
                        visited.add(target_id)
                        queue.append((target_id, depth + 1))

    sg.text_summary = " ".join(sorted(text_parts))
    return sg


def _get_id_cache(explorer) -> dict:
    """Get or build ID cache from explorer.

    Args:
        explorer: AtlasExplorer | PyoxigraphExplorer
            AtlasExplorer or PyoxigraphExplorer instance.

    Returns:
        dict
            Dictionary mapping entity IDs to entity objects.
    """
    if hasattr(explorer, "_id_cache"):
        return explorer._id_cache

    # Build from _data (PyoxigraphExplorer or AtlasExplorer)
    if hasattr(explorer, "_data"):
        cache = {}
        for field in explorer._data.model_fields_set:
            items = getattr(explorer._data, field, None) or []
            if not isinstance(items, list):
                items = [items]
            for item in items:
                if hasattr(item, "id") and item.id:
                    cache[item.id] = item
        return cache

    return {}


def compute_similarity(
    sg1: SubGraph,
    sg2: SubGraph,
    method: str = "structural",
    alpha: float = 0.5,
) -> SimilarityResult:
    """
    Compute similarity between two subgraphs.

    Args:
        sg1: SubGraph
            First SubGraph instance for similarity
        sg2: SubGraph
            Second SubGraph instance for similarity
        method: str
            "structural" (Jaccard on node types), "semantic" (text embeddings),
                or "hybrid" (weighted combination).
        alpha: float
            Weight for structural in hybrid mode (semantic weight = 1 - alpha).

    Returns:
        SimilarityResult
          SimilarityResult with score and breakdown.
    """
    if method == "structural":
        return _structural_similarity(sg1, sg2)
    elif method == "semantic":
        return _semantic_similarity(sg1, sg2)
    elif method == "hybrid":
        return _hybrid_similarity(sg1, sg2, alpha)
    else:
        raise ValueError(f"Unknown similarity method: {method}")


def _structural_similarity(sg1: SubGraph, sg2: SubGraph) -> SimilarityResult:
    """Jaccard similarity on node sets grouped by entity type.

    Args:
        sg1: SubGraph
            First SubGraph instance for similarity
        sg2: SubGraph
            Second SubGraph instance for similarity

    Returns:
        SimilarityResult
            SimilarityResult with structural score and per-type breakdown.
    """
    breakdown = {}
    scores = []

    # Get all entity types across both subgraphs
    all_types = set(sg1.nodes.keys()) | set(sg2.nodes.keys())

    for entity_type in sorted(all_types):
        nodes1 = sg1.nodes.get(entity_type, set())
        nodes2 = sg2.nodes.get(entity_type, set())

        intersection = len(nodes1 & nodes2)
        union = len(nodes1 | nodes2)

        if union == 0:
            jaccard = 0.0
        else:
            jaccard = intersection / union

        breakdown[entity_type] = jaccard
        scores.append(jaccard)

    # Macro-average: unweighted mean across types
    overall_score = sum(scores) / len(scores) if scores else 0.0

    return SimilarityResult(
        score=overall_score,
        method="structural",
        structural_score=overall_score,
        breakdown=breakdown,
    )


def _semantic_similarity(sg1: SubGraph, sg2: SubGraph) -> SimilarityResult:
    """Cosine similarity on text embeddings.

    Args:
        sg1: SubGraph
            First SubGraph instance for similarity
        sg2: SubGraph
            Second SubGraph instance for similarity

    Returns:
        SimilarityResult
            SimilarityResult with semantic similarity score.

    Raises:
        ImportError: If txtai is not installed.
    """
    if Embeddings is None:
        raise ImportError(
            "txtai is not installed. Install it with: pip install txtai[embeddings]"
        )

    embeddings = Embeddings(
        {"path": "sentence-transformers/nli-mpnet-base-v2"}
    )

    # Encode summaries
    text1 = sg1.text_summary or ""
    text2 = sg2.text_summary or ""

    if not text1 or not text2:
        return SimilarityResult(
            score=0.0, method="semantic", semantic_score=0.0
        )

    vec1 = embeddings.transform(text1)
    vec2 = embeddings.transform(text2)

    # Cosine similarity
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = sum(a * a for a in vec1) ** 0.5
    norm2 = sum(b * b for b in vec2) ** 0.5

    if norm1 == 0 or norm2 == 0:
        similarity = 0.0
    else:
        similarity = dot_product / (norm1 * norm2)

    return SimilarityResult(
        score=similarity, method="semantic", semantic_score=similarity
    )


def _hybrid_similarity(
    sg1: SubGraph, sg2: SubGraph, alpha: float
) -> SimilarityResult:
    """Weighted combination of structural and semantic similarity.

    Args:
        sg1: SubGraph
            First SubGraph instance for similarity
        sg2: SubGraph
            Second SubGraph instance for similarity
        alpha: float:
            Weight for structural similarity (semantic weight = 1 - alpha).

    Returns:
        SimilarityResult with combined hybrid score and both component scores.
    """
    structural = _structural_similarity(sg1, sg2)
    semantic = _semantic_similarity(sg1, sg2)

    combined_score = alpha * structural.score + (1 - alpha) * semantic.score

    return SimilarityResult(
        score=combined_score,
        method="hybrid",
        structural_score=structural.score,
        semantic_score=semantic.score,
        breakdown=structural.breakdown,
    )
