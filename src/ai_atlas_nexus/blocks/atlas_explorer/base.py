from abc import ABC
from dataclasses import dataclass
from typing import Any, Dict, List, Set


@dataclass
class StarGraph:
    center_id: str
    center: Any                          # Pydantic entity object
    neighbors: Dict[str, List[Any]]      # field_name -> list of resolved Pydantic objects

    @property
    def neighbor_ids(self) -> Set[str]:
        return {
            obj.id
            for objs in self.neighbors.values()
            for obj in objs
            if hasattr(obj, "id") and obj.id
        }


@dataclass
class StarGraphComparison:
    graph_a: StarGraph
    graph_b: StarGraph
    shared_neighbor_ids: Set[str]
    unique_to_a: Set[str]
    unique_to_b: Set[str]
    jaccard_similarity: float            # |A∩B| / |A∪B|, 0.0 if both empty
    per_field: Dict[str, Dict[str, Any]] # field -> {shared, unique_to_a, unique_to_b}


class ExplorerBase(ABC):

    def __init__(self, data):

        # load the data into the graph
        self._data = data
        self._combined_cache = {}
        self._id_cache = {}
        self._build_id_cache_index()

    def _build_id_cache_index(self):
        """
        A dict which is mapping ID to LinkML obj
        """
        for class_name in self._data.model_fields_set:
            items = getattr(self._data, class_name) or []
            for item in items:
                if hasattr(item, "id") and item.id:
                    self._id_cache[item.id] = item
