"""RBI FREE-AI Committee Report: the seven Sutras as Principles."""

import pytest

from ai_atlas_nexus import AIAtlasNexus


_DOC_ID = "doc-rbi-free-ai-committee-report"

_SUTRAS = {
    "principle-in-rbi-free-ai-trust-is-the-foundation": "Trust is the Foundation (Sutra 1)",
    "principle-in-rbi-free-ai-people-first": "People First (Sutra 2)",
    "principle-in-rbi-free-ai-innovation-over-restraint": "Innovation over Restraint (Sutra 3)",
    "principle-in-rbi-free-ai-fairness-and-equity": "Fairness and Equity (Sutra 4)",
    "principle-in-rbi-free-ai-accountability": "Accountability (Sutra 5)",
    "principle-in-rbi-free-ai-understandable-by-design": "Understandable by Design (Sutra 6)",
    "principle-in-rbi-free-ai-safety-resilience-and-sustainability": "Safety, Resilience, and Sustainability (Sutra 7)",
}


@pytest.fixture(scope="module")
def ran():
    return AIAtlasNexus()


def _free_ai_principles(ran):
    return [
        p for p in ran.get_principles() if p.id.startswith("principle-in-rbi-free-ai-")
    ]


def test_free_ai_document_loaded(ran):
    document = ran.get_document(id=_DOC_ID)
    assert document is not None
    assert document.hasJurisdiction == ["IN"]
    assert str(document.dateCreated) == "2025-08-13"
    assert document.url == "https://www.rbi.org.in/Scripts/FS_Publications.aspx?id=1306"


def test_all_seven_sutras_loaded(ran):
    principles = _free_ai_principles(ran)
    assert {p.id: p.name for p in principles} == _SUTRAS


def test_sutras_reference_the_report(ran):
    principles = _free_ai_principles(ran)
    assert len(principles) == 7
    for principle in principles:
        assert principle.type == "Principle"
        assert principle.hasDocumentation == [_DOC_ID]
        assert principle.description


def test_get_principle_by_id(ran):
    principle = ran.get_principle(id="principle-in-rbi-free-ai-people-first")
    assert principle.name == "People First (Sutra 2)"
