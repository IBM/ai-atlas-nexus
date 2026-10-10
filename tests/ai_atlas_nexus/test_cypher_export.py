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


def test_enum_values_are_properties(cypher):
    assert "MATCH (dst: AdapterType " not in cypher
    assert re.search(r'hasAdapterType: \["LORA"', cypher)
