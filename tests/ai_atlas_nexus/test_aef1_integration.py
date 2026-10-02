"""AEF-1 (Minimum Operating Conditions) integration: schema + data."""

import pytest
from linkml_runtime.utils.schemaview import SchemaView

from ai_atlas_nexus import AIAtlasNexus
from ai_atlas_nexus.blocks.evaluation_conformance import check_engagement_conformance


_SCHEMA = "src/ai_atlas_nexus/ai_risk_ontology/schema/ai-risk-ontology.yaml"


@pytest.fixture(scope="module")
def sv():
    sv = SchemaView(_SCHEMA)
    sv.all_classes()
    return sv


@pytest.fixture(scope="module")
def ran():
    return AIAtlasNexus()


def test_evaluation_standard_class_registered(sv):
    assert sv.get_class("EvaluationStandard") is not None


def test_evaluation_standard_is_entry(sv):
    assert "Entry" in sv.class_ancestors("EvaluationStandard")


_CONDITION_CLASSES = (
    "controlactivityobligation",
    "controlactivityprohibition",
    "controlactivityrecommendation",
)

# AEF-1 Appendix A: which of the 26 conditions are recommendations; the rest are requirements.
_RECOMMENDATIONS = {
    "aef1-ctrl-access-2",
    "aef1-ctrl-access-5",
    "aef1-ctrl-coi-6",
    "aef1-ctrl-autonomy-1",
    "aef1-ctrl-autonomy-3",
    "aef1-ctrl-transparency-2",
    "aef1-ctrl-transparency-3",
    "aef1-ctrl-transparency-4",
    "aef1-ctrl-transparency-5",
    "aef1-ctrl-transparency-7",
    "aef1-ctrl-sensitive-info-2",
}


def _all_conditions(ran):
    return [c for cls in _CONDITION_CLASSES for c in ran.get_all(class_name=cls, taxonomy="aef-1")]


def _top_level_conditions(ran):
    principles = ran.get_all(class_name="principle", taxonomy="aef-1")
    ids = {rule_id for p in principles for rule_id in p.hasRule}
    return [c for c in _all_conditions(ran) if c.id in ids]


def test_evaluation_standard_is_concrete(sv):
    assert not sv.get_class("EvaluationStandard").abstract


def test_aef1_entity_counts(ran):
    assert len(ran.get_all(class_name="evaluationstandard", taxonomy="aef-1")) == 1
    assert len(ran.get_all(class_name="principle", taxonomy="aef-1")) == 5
    assert len(_top_level_conditions(ran)) == 26
    # 26 conditions plus the 8 sub-elements of 1.1 and the 6 sub-elements of 2.4
    assert len(_all_conditions(ran)) == 40


def test_aef1_conditions_per_principle(ran):
    counts = {
        p.id: len(p.hasRule) for p in ran.get_all(class_name="principle", taxonomy="aef-1")
    }
    assert counts == {
        "aef1-principle-access": 5,
        "aef1-principle-coi": 6,
        "aef1-principle-autonomy": 4,
        "aef1-principle-transparency": 7,
        "aef1-principle-sensitive-info": 4,
    }


def test_aef1_principle_rules_resolve(ran):
    ids = {c.id for c in _all_conditions(ran)}
    for principle in ran.get_all(class_name="principle", taxonomy="aef-1"):
        assert set(principle.hasRule) <= ids


def test_aef1_requirement_vs_recommendation(ran):
    for condition in _top_level_conditions(ran):
        expected = condition.id in _RECOMMENDATIONS
        assert (condition.type == "ControlActivityRecommendation") == expected, condition.id
        assert condition.description.startswith(
            "Recommendation:" if expected else "Requirement:"
        ), condition.id


def test_aef1_sub_elements(ran):
    access = ran.get_by_id(class_name="controlactivityobligation", identifier="aef1-ctrl-access-1")
    assert len(access.hasRule) == 8
    # Only query access (1.1.1) is required among the 1.1 sub-elements
    types = {c.id: c.type for c in _all_conditions(ran)}
    required = [
        rule_id for rule_id in access.hasRule if types[rule_id] == "ControlActivityObligation"
    ]
    assert required == ["aef1-ctrl-access-1-1"]

    disclosure = ran.get_by_id(class_name="controlactivityobligation", identifier="aef1-ctrl-coi-4")
    assert len(disclosure.hasRule) == 6


def test_aef1_condition_names_numbered(ran):
    for condition in _top_level_conditions(ran):
        section = condition.name.split(" ", 1)[0]
        assert section[0] in "12345" and section[1] == ".", condition.name


def test_aef1_controls_reference_aef1_taxonomy(ran):
    for control in _all_conditions(ran):
        assert control.isDefinedByTaxonomy == "aef-1"


def test_aef1_standard_has_principle(ran):
    standard = ran.get_by_id(class_name="evaluationstandard", identifier="aef1-standard")
    principles = ran.get_all(class_name="principle", taxonomy="aef-1")
    assert sorted(standard.hasPrinciple) == sorted(p.id for p in principles)


_SAMPLE_DIR = "docs/examples/notebooks/sample_data"
_ACCEPTED_FOR_REQUIREMENT = {"FULFILLED", "ALTERNATIVE_MEANS"}


@pytest.fixture(scope="module")
def usecase_ran():
    return AIAtlasNexus(base_dir=_SAMPLE_DIR)


@pytest.fixture(scope="module")
def engagement(usecase_ran):
    return usecase_ran.get_by_id(
        class_name="thirdpartyevaluationengagements", identifier="aef1-usecase-engagement"
    )


def _required_condition_ids(ran):
    """Top-level AEF-1 requirements plus required sub-elements (1.1.1 and 2.4.x)."""
    conditions = {c.id: c for c in _all_conditions(ran)}
    required = set()
    for top in _top_level_conditions(ran):
        if top.type == "ControlActivityRecommendation":
            continue
        required.add(top.id)
        required.update(
            sub for sub in top.hasRule or [] if conditions[sub].type != "ControlActivityRecommendation"
        )
    return required


def _derive_satisfies_all_requirements(ran, conformance):
    required = _required_condition_ids(ran)
    answered = set()
    for assessment in conformance.hasConditionAssessment:
        if assessment.assessesCondition not in required:
            continue
        if assessment.hasConformanceOutcome not in _ACCEPTED_FOR_REQUIREMENT:
            return False
        answered.add(assessment.assessesCondition)
    return answered == required


def test_engagement_schema(sv):
    slots = {s.name: s for s in sv.class_induced_slots("ThirdPartyEvaluationEngagement")}
    assert slots["usesEvaluation"].range == "AiEval"
    assert slots["usesEvaluation"].multivalued
    assert slots["hasEvaluation"].range == "AiEvalResult"
    assert slots["hasEvaluation"].multivalued
    assert slots["hasEvaluator"].range == "Organization"
    assert slots["hasStandardConformance"].range == "EvaluationStandardConformance"
    assert sv.get_class("ConditionAssessment").rules


def test_meets_condition_removed(sv):
    assert sv.get_slot("meetsCondition") is None


def test_engagement_has_multiple_benchmarks(usecase_ran, engagement):
    assert len(engagement.usesEvaluation) == 2
    for result_id in engagement.hasEvaluation:
        result = usecase_ran.get_by_id(class_name="aievalresults", identifier=result_id)
        assert result.isResultOf in engagement.usesEvaluation


def test_assessments_scoped_to_engagement_benchmarks(engagement):
    for conformance in engagement.hasStandardConformance:
        for assessment in conformance.hasConditionAssessment:
            assert set(assessment.appliesToEvaluation or []) <= set(engagement.usesEvaluation)


def test_assessments_reference_standard_conditions(usecase_ran, engagement):
    ids = {c.id for c in _all_conditions(usecase_ran)}
    for conformance in engagement.hasStandardConformance:
        assert conformance.conformsToStandard == "aef1-standard"
        for assessment in conformance.hasConditionAssessment:
            assert assessment.assessesCondition in ids


def test_justification_when_not_fulfilled_literally(engagement):
    for conformance in engagement.hasStandardConformance:
        for assessment in conformance.hasConditionAssessment:
            if assessment.hasConformanceOutcome in ("NOT_FULFILLED", "ALTERNATIVE_MEANS"):
                assert assessment.justification, assessment.assessesCondition


def test_disclosure_answers_only_on_disclosure_conditions(engagement):
    for conformance in engagement.hasStandardConformance:
        for assessment in conformance.hasConditionAssessment:
            if assessment.disclosureAnswer is not None:
                assert assessment.assessesCondition.startswith("aef1-ctrl-coi-4-")


def test_every_requirement_answered(usecase_ran, engagement):
    answered = {
        a.assessesCondition for c in engagement.hasStandardConformance for a in c.hasConditionAssessment
    }
    assert _required_condition_ids(usecase_ran) <= answered


def test_satisfies_all_requirements_consistent(usecase_ran, engagement):
    for conformance in engagement.hasStandardConformance:
        assert conformance.satisfiesAllRequirements == _derive_satisfies_all_requirements(
            usecase_ran, conformance
        )


def test_unmet_requirement_is_benchmark_specific(engagement):
    [conformance] = engagement.hasStandardConformance
    unmet = [a for a in conformance.hasConditionAssessment if a.hasConformanceOutcome == "NOT_FULFILLED"]
    assert [(a.assessesCondition, a.appliesToEvaluation) for a in unmet] == [
        ("aef1-ctrl-access-4", ["aef1-usecase-injection-benchmark"])
    ]


def _check(usecase_ran, engagement):
    return check_engagement_conformance(
        engagement, lambda identifier: usecase_ran._atlas_explorer.get_by_id(None, identifier)
    )


def _issues(check, issue):
    return [i for s in check.standards for i in s.issues if i.issue == issue]


def test_conditions_have_documentation(ran):
    for condition in _all_conditions(ran):
        assert condition.hasDocumentation == ["AEF-1-Dec-2025"], condition.id


def test_organizations_are_typed(usecase_ran):
    provider = usecase_ran.get_by_id(class_name="organizations", identifier="aef1-usecase-provider")
    assert type(provider).__name__ == "AiProvider"
    assert [o.id for o in usecase_ran.get_all("aiprovider")] == ["aef1-usecase-provider"]


def test_check_standard_conformance_sample(usecase_ran):
    check = usecase_ran.check_standard_conformance("aef1-usecase-engagement")
    assert check.is_valid
    assert not check.satisfies_all_requirements
    assert check.evaluator == "aef1-usecase-evaluator"
    assert check.system_provider == "aef1-usecase-provider"
    [standard] = check.standards
    assert standard.is_consistent
    # 15 top-level requirements, plus 1.1.1 and 2.4.1-2.4.6
    assert len(standard.required_conditions) == 22
    assert [(i.condition_id, i.issue, i.evaluations) for i in standard.issues] == [
        ("aef1-ctrl-access-4", "not_met", ["aef1-usecase-injection-benchmark"])
    ]


def test_check_standard_conformance_unknown_engagement(usecase_ran):
    # An id of another class is not an engagement
    with pytest.raises(ValueError):
        usecase_ran.check_standard_conformance("aef1-standard")


def test_get_evaluation_engagements(usecase_ran):
    def ids(**kwargs):
        return [e.id for e in usecase_ran.get_evaluation_engagements(**kwargs)]

    assert ids() == ["aef1-usecase-engagement"]
    assert ids(evaluator="aef1-usecase-evaluator") == ["aef1-usecase-engagement"]
    assert ids(system_provider="aef1-usecase-provider") == ["aef1-usecase-engagement"]
    assert ids(ai="aef1-usecase-credit-risk-llm") == ["aef1-usecase-engagement"]
    assert ids(evaluator="aef1-usecase-provider") == []
    assert usecase_ran.get_evaluation_engagement(id="aef1-standard") is None


def test_check_detects_missing_justification(usecase_ran, engagement):
    modified = engagement.model_copy(deep=True)
    row = next(
        a
        for a in modified.hasStandardConformance[0].hasConditionAssessment
        if a.hasConformanceOutcome == "ALTERNATIVE_MEANS"
    )
    row.justification = None
    check = _check(usecase_ran, modified)
    assert [i.condition_id for i in _issues(check, "missing_justification")] == ["aef1-ctrl-autonomy-3"]
    assert not check.is_valid


def test_check_requires_every_benchmark_covered(usecase_ran, engagement):
    modified = engagement.model_copy(deep=True)
    conformance = modified.hasStandardConformance[0]
    # Drop the injection-benchmark answer to 1.4, leaving it answered for the fairness benchmark only
    conformance.hasConditionAssessment = [
        a
        for a in conformance.hasConditionAssessment
        if not (a.assessesCondition == "aef1-ctrl-access-4" and a.hasConformanceOutcome == "NOT_FULFILLED")
    ]
    check = _check(usecase_ran, modified)
    assert [(i.condition_id, i.evaluations) for i in _issues(check, "not_answered")] == [
        ("aef1-ctrl-access-4", ["aef1-usecase-injection-benchmark"])
    ]
    assert not check.standards[0].derived_satisfies_all_requirements


def test_check_detects_inconsistent_overall_answer(usecase_ran, engagement):
    modified = engagement.model_copy(deep=True)
    modified.hasStandardConformance[0].satisfiesAllRequirements = True
    check = _check(usecase_ran, modified)
    assert not check.standards[0].is_consistent
    assert not check.is_valid


def test_check_detects_evaluator_is_provider(usecase_ran, engagement):
    modified = engagement.model_copy(deep=True)
    modified.hasEvaluator = "aef1-usecase-provider"
    check = _check(usecase_ran, modified)
    assert len(check.independence_issues) == 2
    assert not check.is_valid


def test_check_detects_result_outside_engagement(usecase_ran, engagement):
    modified = engagement.model_copy(deep=True)
    modified.usesEvaluation = ["aef1-usecase-fairness-benchmark"]
    check = _check(usecase_ran, modified)
    assert len(check.evaluation_issues) == 1
    assert [i.condition_id for i in _issues(check, "evaluation_not_in_engagement")] == [
        "aef1-ctrl-access-4",
        "aef1-ctrl-autonomy-3",
    ]


def test_legal_cross_references(ran):
    standard = ran.get_by_id(class_name="evaluationstandard", identifier="aef1-standard")
    assert set(standard.related_mappings) == {"eu-gpai-cop-ss-measure-7-3", "ca-sb-53-22757-12-c-2-c"}
    time = ran.get_by_id(class_name="controlactivityobligation", identifier="aef1-ctrl-access-4")
    assert time.related_mappings == ["eu-gpai-cop-ss-appendix-3-4"]
    appendix = ran.get_by_id(class_name="documents", identifier="eu-gpai-cop-ss-appendix-3-5")
    assert set(appendix.related_mappings) == {
        "aef1-ctrl-sensitive-info-2",
        "aef1-ctrl-sensitive-info-3",
        "aef1-principle-access",
    }


def test_legal_cross_references_resolve(ran):
    documents = {d.id for d in ran.get_all("documents")}
    for item in _all_conditions(ran) + ran.get_all("entries", taxonomy="aef-1"):
        for target in item.related_mappings or []:
            assert target in documents, (item.id, target)


def test_vocabulary_mappings_documented(sv):
    assert "prov:Activity" in sv.get_class("ThirdPartyEvaluationEngagement").close_mappings
    assert "earl:Assertion" in sv.get_class("ConditionAssessment").close_mappings
    outcomes = sv.get_enum("ConformanceOutcome").permissible_values
    assert outcomes["FULFILLED"].meaning == "earl:passed"
    assert outcomes["NOT_ASSESSED"].meaning == "earl:untested"
    assert sv.get_slot("hasConformanceOutcome").slot_uri == "earl:outcome"
    assert sv.get_slot("conformsToStandard").slot_uri == "dcterms:conformsTo"
