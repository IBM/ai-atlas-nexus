"""Coverage for the Cypher export in ``export_cypher.py``.

The tests export the packaged knowledge graph and check the Cypher a graph database
would load from it.
"""

import re

import pytest

from ai_atlas_nexus.ai_risk_ontology.util.export_cypher import (
    export_data_to_cypher,
    to_cypher_literal,
)
from ai_atlas_nexus.toolkit.data_utils import load_yamls_to_container


@pytest.fixture(scope="module")
def cypher() -> str:
    return export_data_to_cypher(load_yamls_to_container(None))


def test_strings_are_escaped():
    assert to_cypher_literal('say "hi"\\\n') == '"say \\"hi\\"\\\\\\n"'


def test_lists_are_cypher_lists(cypher):
    assert not re.search(r"\w+: \"\['", cypher), "a list was written as a Python repr"
    assert re.search(r'hasTypicalLocation: \["', cypher)


def test_edges_use_the_label_of_their_target(cypher):
    nodes = set(re.findall(r"^MERGE \(node:(\w+) \{id: (\"[^\"]*\")\}", cypher, re.M))
    ids = {node_id for _, node_id in nodes}
    targets = re.findall(r"MATCH \(dst: (\w+) \{id: (\"[^\"]*\")\}\)", cypher)
    # A target id that is not a node at all is a gap in the data, not in the export.
    missing = [t for t in targets if t[1] in ids and t not in nodes]
    assert targets and not missing, f"{len(missing)} edges match no node: {missing[:3]}"


def test_enum_values_are_properties(cypher):
    assert "MATCH (dst: AdapterType " not in cypher
    assert re.search(r'hasAdapterType: \["LORA"', cypher)
