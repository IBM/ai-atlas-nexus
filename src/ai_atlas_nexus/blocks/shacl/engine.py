import io
import logging
import re
from collections import defaultdict
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import quote, unquote

import pyoxigraph
import pyshacl

from ai_atlas_nexus.blocks.graph_explorer.query_builder import NEXUS_URI
from ai_atlas_nexus.blocks.shacl.shape_loader import load_shapes


logger = logging.getLogger(__name__)

_SH = "http://www.w3.org/ns/shacl#"
_RDF_TYPE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"

# SPARQL to enumerate all sh:SPARQLRule entries with their target class
_RULES_SPARQL = f"""
PREFIX sh: <{_SH}>
SELECT ?targetClass ?construct WHERE {{
    ?shape a sh:NodeShape ;
           sh:targetClass ?targetClass ;
           sh:rule ?rule .
    ?rule a sh:SPARQLRule ;
          sh:construct ?construct .
}}
"""

# SPARQL to enumerate sh:TripleRule entries
_TRIPLE_RULES_SPARQL = f"""
PREFIX sh: <{_SH}>
SELECT ?targetClass ?subject ?predicate ?object WHERE {{
    ?shape a sh:NodeShape ;
           sh:targetClass ?targetClass ;
           sh:rule ?rule .
    ?rule a sh:TripleRule ;
          sh:subject ?subject ;
          sh:predicate ?predicate ;
          sh:object ?object .
}}
"""


class ValidationReport:
    """Wrapper around a pyshacl validation result."""

    def __init__(self, conforms: bool, results_text: str):
        self.conforms = conforms
        self.results_text = results_text

    def __repr__(self):
        return f"ValidationReport(conforms={self.conforms})"


class SHACLEngine:
    """Applies SHACL shapes to a pyoxigraph Store.

    Supports:
    - ``validate()`` — constraint checking via pyshacl
    - ``infer()``    — rule application via pyoxigraph SPARQL
    - ``augment_objects()`` — attach derived attributes to Pydantic instances
    """

    def __init__(self, shapes_store: pyoxigraph.Store):
        self._shapes = shapes_store

    # ------------------------------------------------------------------
    # Factory
    # ------------------------------------------------------------------

    @classmethod
    def from_discovery(
        cls, base_dir: Optional[str], container=None
    ) -> Optional["SHACLEngine"]:
        """Discover and load shapes, returns None when none are found."""
        store = load_shapes(base_dir, container)
        if sum(1 for _ in store) == 0:
            logger.debug("No SHACL shapes found — engine not created")
            return None
        logger.info(
            "SHACLEngine created with %d shape quads", sum(1 for _ in store)
        )
        return cls(store)

    def has_shapes(self) -> bool:
        return sum(1 for _ in self._shapes) > 0

    def validate(self, data_store: pyoxigraph.Store) -> ValidationReport:
        """Validate ``data_store`` against the loaded shapes.

        Uses pyshacl with N-Quads bytes serialised from pyoxigraph
        """
        data_nq = _store_to_nquads(data_store)
        shapes_nq = _store_to_nquads(self._shapes)
        conforms, _, results_text = pyshacl.validate(
            data_nq,
            shacl_graph=shapes_nq,
            data_graph_format="nquads",
            shacl_graph_format="nquads",
            inference=None,
        )
        return ValidationReport(conforms, results_text)

    def infer(self, data_store: pyoxigraph.Store) -> Dict[str, Dict[str, Any]]:
        """Execute SHACL rules against ``data_store`` using pyoxigraph SPARQL.

        Adds inferred triples to ``data_store`` in-place and returns a mapping
        of ``{subject_uri: {predicate_localname: value}}`` for all new triples.
        """
        derived: Dict[str, Dict[str, Any]] = defaultdict(dict)

        derived.update(self._apply_sparql_rules(data_store))
        derived.update(self._apply_triple_rules(data_store))

        return dict(derived)

    def augment_objects(
        self,
        instances: list,
        derived: Dict[str, Dict[str, Any]],
    ) -> list:
        """Attach a ``derived_attrs`` dict to each instance that has derived data.

        Uses ``object.__setattr__`` to bypass Pydantic's ``extra='forbid'``
        guard — the attribute is invisible to serialisation but accessible
        on the live object.
        """
        for obj in instances:
            if not hasattr(obj, "id"):
                continue
            subject_uri = f"{NEXUS_URI}{quote(obj.id, safe='')}"
            attrs = derived.get(subject_uri)
            if attrs:
                object.__setattr__(obj, "derived_attrs", attrs)
        return instances

    def _apply_sparql_rules(
        self, data_store: pyoxigraph.Store
    ) -> Dict[str, Dict[str, Any]]:
        """Run all sh:SPARQLRule CONSTRUCT queries and collect new triples."""
        derived: Dict[str, Dict[str, Any]] = defaultdict(dict)
        try:
            rows = list(self._shapes.query(_RULES_SPARQL))
        except Exception as exc:
            logger.warning("Failed to query SPARQL rules from shapes: %s", exc)
            return {}

        for row in rows:
            target_class = row["targetClass"].value
            construct = row["construct"].value

            for subject_uri in _get_targets(data_store, target_class):
                for triple in _exec_construct(
                    data_store, construct, subject_uri
                ):
                    quad = pyoxigraph.Quad(
                        triple.subject,
                        triple.predicate,
                        triple.object,
                        pyoxigraph.DefaultGraph(),
                    )
                    if quad not in data_store:
                        data_store.add(quad)
                        pred_local = _local_name(triple.predicate.value)
                        obj_val = _term_value(triple.object)
                        derived[triple.subject.value][pred_local] = obj_val

        return dict(derived)

    def _apply_triple_rules(
        self, data_store: pyoxigraph.Store
    ) -> Dict[str, Dict[str, Any]]:
        """Run all sh:TripleRule entries (static IRI/literal triple assertions)."""
        derived: Dict[str, Dict[str, Any]] = defaultdict(dict)
        try:
            rows = list(self._shapes.query(_TRIPLE_RULES_SPARQL))
        except Exception as exc:
            logger.warning("Failed to query TripleRules from shapes: %s", exc)
            return {}

        for row in rows:
            target_class = row["targetClass"].value
            pred_uri = row["predicate"].value
            obj_term = row["object"]

            for subject_uri in _get_targets(data_store, target_class):
                subj = pyoxigraph.NamedNode(subject_uri)
                pred = pyoxigraph.NamedNode(pred_uri)
                obj = obj_term
                quad = pyoxigraph.Quad(
                    subj, pred, obj, pyoxigraph.DefaultGraph()
                )
                if quad not in data_store:
                    data_store.add(quad)
                    pred_local = _local_name(pred_uri)
                    derived[subject_uri][pred_local] = _term_value(obj_term)

        return dict(derived)


def _store_to_nquads(store: pyoxigraph.Store) -> bytes:
    buf = io.BytesIO()
    store.dump(buf, format=pyoxigraph.RdfFormat.N_QUADS)
    return buf.getvalue()


def _get_targets(
    data_store: pyoxigraph.Store, target_class_uri: str
) -> List[str]:
    """Return subject URIs of all instances of ``target_class_uri``."""
    q = f"SELECT ?this WHERE {{ ?this <{_RDF_TYPE}> <{target_class_uri}> }}"
    try:
        return [row["this"].value for row in data_store.query(q)]
    except Exception as exc:
        logger.debug("Target query failed for <%s>: %s", target_class_uri, exc)
        return []


def _exec_construct(
    data_store: pyoxigraph.Store, construct: str, subject_uri: str
):
    """Execute a CONSTRUCT query with ``?this`` bound to ``subject_uri``."""
    inject = f"VALUES ?this {{ <{subject_uri}> }} "
    modified = re.sub(
        r"\bWHERE\s*\{", f"WHERE {{ {inject}", construct, flags=re.IGNORECASE
    )
    try:
        return list(data_store.query(modified))
    except Exception as exc:
        logger.debug("CONSTRUCT failed for <%s>: %s", subject_uri, exc)
        return []


def _local_name(uri: str) -> str:
    """Extract the local name from a URI (after # or last /)."""
    for sep in ("#", "/"):
        idx = uri.rfind(sep)
        if idx != -1:
            return uri[idx + 1 :]
    return uri


1


def _term_value(term) -> Any:
    """Return a Python-native value from a pyoxigraph term."""
    if isinstance(term, pyoxigraph.Literal):
        raw = term.value
        dt = str(term.datatype) if term.datatype else ""
        if "boolean" in dt:
            return raw.lower() == "true"
        if "integer" in dt or "int" in dt:
            try:
                return int(raw)
            except ValueError:
                pass
        if "decimal" in dt or "float" in dt or "double" in dt:
            try:
                return float(raw)
            except ValueError:
                pass
        return raw
    if isinstance(term, pyoxigraph.NamedNode):
        return term.value
    return str(term)
