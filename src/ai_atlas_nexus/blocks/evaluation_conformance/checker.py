import dataclasses
from typing import Any, Callable, Dict, List, Optional, Set

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import (
    ConditionAssessment,
    EvaluationStandardConformance,
    ThirdPartyEvaluationEngagement,
)


# Outcomes that satisfy a requirement. ALTERNATIVE_MEANS also needs a justification.
ACCEPTED_FOR_REQUIREMENT = {"FULFILLED", "ALTERNATIVE_MEANS"}
REQUIRES_JUSTIFICATION = {"NOT_FULFILLED", "ALTERNATIVE_MEANS"}
# Rule types that are not requirements of a standard.
NON_REQUIRED_RULE_TYPES = {"ControlActivityRecommendation", "ControlActivityPermission"}


@dataclasses.dataclass(kw_only=True)
class ConditionIssue:
    """A problem with how one condition of a standard was answered.

    Attributes:
        condition_id: The id of the condition (a ControlActivity).
        issue: One of "not_met", "not_answered", "missing_justification",
            "unknown_condition", "evaluation_not_in_engagement".
        outcome: The ConformanceOutcome of the answer, where there is one.
        evaluations: The evaluations the issue applies to. Empty when it applies
            to the engagement as a whole.
    """

    condition_id: str
    issue: str
    outcome: Optional[str] = None
    evaluations: List[str] = dataclasses.field(default_factory=list)


@dataclasses.dataclass(kw_only=True)
class StandardConformanceCheck:
    """The result of checking one completed checklist against its standard.

    Attributes:
        standard_id: The id of the EvaluationStandard.
        required_conditions: Ids of the conditions that are requirements of the
            standard, including required sub-elements.
        stated_satisfies_all_requirements: The overall answer given in the checklist.
        derived_satisfies_all_requirements: The overall answer derived from the rows.
        issues: Problems found in the checklist rows.
    """

    standard_id: str
    required_conditions: List[str]
    stated_satisfies_all_requirements: Optional[bool]
    derived_satisfies_all_requirements: bool
    issues: List[ConditionIssue] = dataclasses.field(default_factory=list)

    @property
    def is_consistent(self) -> bool:
        """Whether the stated overall answer, if any, matches the derived one."""
        return self.stated_satisfies_all_requirements in (
            None,
            self.derived_satisfies_all_requirements,
        )

    @property
    def is_valid(self) -> bool:
        """Whether the checklist is consistent and well-formed. Unmet or unanswered
        requirements do not make a checklist invalid, as AEF-1 allows reporting them."""
        return self.is_consistent and not any(
            i.issue not in ("not_met", "not_answered") for i in self.issues
        )


@dataclasses.dataclass(kw_only=True)
class EngagementConformanceCheck:
    """The result of checking a third-party evaluation engagement.

    Attributes:
        engagement_id: The id of the ThirdPartyEvaluationEngagement.
        evaluator: The id of the evaluator organization.
        system_provider: The id of the system provider organization.
        independence_issues: Problems with who evaluated whose system, e.g. the
            evaluator being the system provider.
        evaluation_issues: Problems linking results to the engagement's evaluations.
        standards: One check per completed checklist.
    """

    engagement_id: str
    evaluator: Optional[str]
    system_provider: Optional[str]
    independence_issues: List[str] = dataclasses.field(default_factory=list)
    evaluation_issues: List[str] = dataclasses.field(default_factory=list)
    standards: List[StandardConformanceCheck] = dataclasses.field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return (
            not self.independence_issues
            and not self.evaluation_issues
            and all(s.is_valid for s in self.standards)
        )

    @property
    def satisfies_all_requirements(self) -> bool:
        """Whether every completed checklist satisfies all requirements of its standard."""
        return bool(self.standards) and all(
            s.derived_satisfies_all_requirements for s in self.standards
        )


def required_condition_ids(standard: Any, get_by_id: Callable[[str], Any]) -> List[str]:
    """Ids of the conditions that are requirements of an evaluation standard.

    Walks the standard's principles (hasPrinciple) and rules (hasRule) down through
    each condition's sub-elements. A sub-element is only required when its parent is.
    """
    required: List[str] = []

    def visit(rule_id: str):
        rule = get_by_id(rule_id)
        if rule is None or getattr(rule, "type", None) in NON_REQUIRED_RULE_TYPES:
            return
        if rule_id not in required:
            required.append(rule_id)
        for sub_id in getattr(rule, "hasRule", None) or []:
            visit(sub_id)

    roots = list(getattr(standard, "hasRule", None) or [])
    for principle_id in getattr(standard, "hasPrinciple", None) or []:
        principle = get_by_id(principle_id)
        roots.extend(getattr(principle, "hasRule", None) or [])
    for rule_id in roots:
        visit(rule_id)
    return required


def check_standard_conformance(
    conformance: EvaluationStandardConformance,
    engagement_evaluations: List[str],
    get_by_id: Callable[[str], Any],
) -> StandardConformanceCheck:
    """Check one completed checklist of an engagement against its standard."""
    standard = get_by_id(conformance.conformsToStandard)
    required = required_condition_ids(standard, get_by_id) if standard else []
    issues: List[ConditionIssue] = []
    rows: Dict[str, List[ConditionAssessment]] = {}

    for row in conformance.hasConditionAssessment or []:
        rows.setdefault(row.assessesCondition, []).append(row)
        if get_by_id(row.assessesCondition) is None:
            issues.append(
                ConditionIssue(condition_id=row.assessesCondition, issue="unknown_condition")
            )
        outside = [e for e in row.appliesToEvaluation or [] if e not in engagement_evaluations]
        if outside:
            issues.append(
                ConditionIssue(
                    condition_id=row.assessesCondition,
                    issue="evaluation_not_in_engagement",
                    evaluations=outside,
                )
            )
        if row.hasConformanceOutcome in REQUIRES_JUSTIFICATION and not row.justification:
            issues.append(
                ConditionIssue(
                    condition_id=row.assessesCondition,
                    issue="missing_justification",
                    outcome=row.hasConformanceOutcome,
                    evaluations=list(row.appliesToEvaluation or []),
                )
            )

    satisfied = standard is not None
    for condition_id in required:
        covered: Set[str] = set()
        whole_engagement = False
        for row in rows.get(condition_id, []):
            if row.hasConformanceOutcome not in ACCEPTED_FOR_REQUIREMENT:
                satisfied = False
                issues.append(
                    ConditionIssue(
                        condition_id=condition_id,
                        issue="not_met",
                        outcome=row.hasConformanceOutcome,
                        evaluations=list(row.appliesToEvaluation or []),
                    )
                )
            if row.appliesToEvaluation:
                covered.update(row.appliesToEvaluation)
            else:
                whole_engagement = True
        # Answers scoped to specific evaluations must together cover all of them.
        uncovered = [] if whole_engagement else [e for e in engagement_evaluations if e not in covered]
        if not rows.get(condition_id) or uncovered:
            satisfied = False
            issues.append(
                ConditionIssue(condition_id=condition_id, issue="not_answered", evaluations=uncovered)
            )

    return StandardConformanceCheck(
        standard_id=conformance.conformsToStandard,
        required_conditions=required,
        stated_satisfies_all_requirements=conformance.satisfiesAllRequirements,
        derived_satisfies_all_requirements=satisfied,
        issues=issues,
    )


def check_engagement_conformance(
    engagement: ThirdPartyEvaluationEngagement, get_by_id: Callable[[str], Any]
) -> EngagementConformanceCheck:
    """Check a third-party evaluation engagement and each of its completed checklists."""
    evaluations = list(engagement.usesEvaluation or [])
    independence_issues = []
    if not engagement.hasEvaluator:
        independence_issues.append("The engagement does not record an evaluator.")
    if not engagement.hasSystemProvider:
        independence_issues.append("The engagement does not record a system provider.")
    if engagement.hasEvaluator and engagement.hasEvaluator == engagement.hasSystemProvider:
        independence_issues.append(
            f"The evaluator {engagement.hasEvaluator} is also the system provider, so it is not a third party."
        )
    for ai_id in engagement.evaluatesAi or []:
        ai = get_by_id(ai_id)
        provider = getattr(ai, "isProvidedBy", None) if ai else None
        if provider and engagement.hasSystemProvider and provider != engagement.hasSystemProvider:
            independence_issues.append(
                f"{ai_id} is provided by {provider}, not the system provider {engagement.hasSystemProvider}."
            )
        if provider and provider == engagement.hasEvaluator:
            independence_issues.append(
                f"{ai_id} is provided by the evaluator {engagement.hasEvaluator}, so it is not a third party."
            )

    evaluation_issues = []
    for result_id in engagement.hasEvaluation or []:
        result = get_by_id(result_id)
        if result is None:
            evaluation_issues.append(f"Result {result_id} was not found.")
        elif result.isResultOf not in evaluations:
            evaluation_issues.append(
                f"Result {result_id} is a result of {result.isResultOf}, which is not one of the engagement's evaluations."
            )

    return EngagementConformanceCheck(
        engagement_id=engagement.id,
        evaluator=engagement.hasEvaluator,
        system_provider=engagement.hasSystemProvider,
        independence_issues=independence_issues,
        evaluation_issues=evaluation_issues,
        standards=[
            check_standard_conformance(c, evaluations, get_by_id)
            for c in engagement.hasStandardConformance or []
        ],
    )
