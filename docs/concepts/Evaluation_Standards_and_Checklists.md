# Evaluation Standards and Checklists

AI Atlas Nexus can be used to represent standards for how third-party AI evaluations are run. One such standard is
[AEF-1: Minimum Operating Conditions for Independent Third Party AI Evaluations](https://aievaluatorforum.org/AEF_1_Minimum_Operating_Conditions_for_Independent_Third_Party_AI_Evaluations.pdf),
and the completed checklists that evaluators publish alongside their results.

Example notebook: [AEF-1 Minimum Operating Conditions](../examples/notebooks/AEF-1_Minimum_Operating_Conditions.ipynb).

## The standard

A standard is an `EvaluationStandard` entry. It lists its principles with `hasPrinciple`, and each `Principle`
lists its conditions with `hasRule`. Each condition is a control activity whose class says whether it is required:

| Condition      | Class                                                                                                             |
| -------------- | ----------------------------------------------------------------------------------------------------------------- |
| Requirement    | `ControlActivityObligation`, or `ControlActivityProhibition` when it is phrased as something that must not happen |
| Recommendation | `ControlActivityRecommendation`                                                                                   |

A condition with checklist sub-elements, such as AEF-1 1.1 (technical access) or 2.4 (conflict of interest
disclosure), lists them with `hasRule`. A sub-element is only required when its parent condition is.

AEF-1 is in `src/ai_atlas_nexus/data/knowledge_graph/aef1_data.yaml` and contains principles, conditions (requirements
and recommendations), and other sub-elements.

## Engagements and completed checklists

A `ThirdPartyEvaluationEngagement` records one engagement between an evaluator and a system provider:

```
ThirdPartyEvaluationEngagement
├─ hasEvaluator → Organization          hasSystemProvider → Organization
├─ evaluatesAi → BaseAi*                the AI systems or models evaluated
├─ usesEvaluation → AiEval*             the benchmarks run: one or more
├─ hasEvaluation → AiEvalResult*        the results, across all benchmarks
├─ startDate / endDate / hasDocumentation
└─ hasStandardConformance → EvaluationStandardConformance*    one completed checklist per standard
     ├─ conformsToStandard → EvaluationStandard
     ├─ satisfiesAllRequirements        the checklist's overall answer
     └─ hasConditionAssessment → ConditionAssessment*          one checklist row each
          ├─ assessesCondition → ControlActivity
          ├─ hasConformanceOutcome      FULFILLED | NOT_FULFILLED | ALTERNATIVE_MEANS | NOT_APPLICABLE | NOT_ASSESSED
          ├─ evidence                   the checklist's Notes/Evidence
          ├─ justification              required for NOT_FULFILLED and ALTERNATIVE_MEANS
          ├─ disclosureAnswer           for disclosure conditions such as AEF-1 2.4.x: does the circumstance apply?
          └─ appliesToEvaluation → AiEval*   limits the answer to specific benchmarks
```

When a condition is met differently for each benchmark, the checklist has one row per benchmark, each naming its
benchmark in `appliesToEvaluation`. A row without `appliesToEvaluation` applies to the whole engagement.

Organizations take a `type`, so a system provider can be recorded as an `AiProvider`:

```yaml
organizations:
  - id: example-bank
    name: Example Bank
    type: AiProvider
```

## Checking a checklist

```python
from ai_atlas_nexus import AIAtlasNexus

ran = AIAtlasNexus(base_dir="sample_data")

# Who evaluated whose system
ran.get_evaluation_engagements(system_provider="example-bank")
ran.get_evaluation_engagements(evaluator="example-evaluation-lab", ai="credit-risk-llm")

check = ran.check_standard_conformance("my-engagement")
check.satisfies_all_requirements   # derived from the checklist rows
check.is_valid                     # consistent and well-formed
check.independence_issues          # e.g. the evaluator is also the system provider
for standard in check.standards:
    standard.stated_satisfies_all_requirements, standard.derived_satisfies_all_requirements
    standard.issues                # ConditionIssue(condition_id, issue, outcome, evaluations)
```

`check_standard_conformance` works for any `EvaluationStandard`. For each completed checklist it:

- finds the standard's requirements by walking its principles and conditions, including required sub-elements;
- treats a requirement as satisfied when every row answering it is `FULFILLED` or `ALTERNATIVE_MEANS`, and the rows
  together cover every benchmark of the engagement;
- reports each issue as one of `not_met`, `not_answered`, `missing_justification`, `unknown_condition`, or
  `evaluation_not_in_engagement`;
- compares the derived overall answer with the stated `satisfiesAllRequirements`.

It also checks the engagement itself:

- The evaluator and system provider are recorded, and the evaluator is not the system provider.
- Each evaluated AI's `isProvidedBy` matches the system provider.
- Each result belongs to one of the engagement's evaluations.

Unmet or unanswered requirements don't make a checklist invalid, because AEF-1 asks evaluators to report which
requirements were not met and why. They do make the derived overall answer `false`.

The schema includes a LinkML rule requiring `justification` for `NOT_FULFILLED` and `ALTERNATIVE_MEANS`.
The generated Pydantic model doesn't enforce LinkML rules, so the requirement is enforced by
`check_standard_conformance`.

## Vocabulary mappings

The checklist model reuses the W3C [Evaluation and Report Language (EARL)](https://www.w3.org/TR/EARL10-Schema/),
[PROV-O](https://www.w3.org/TR/prov-o/), [Dublin Core terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)
and the [Data Privacy Vocabulary (DPV)](https://w3id.org/dpv) 2.1. The mappings are recorded in the schema as
`class_uri`, `slot_uri`, `meaning`, `close_mappings` and `related_mappings`, so they carry through to the RDF and OWL
exports.

In EARL, an `earl:Assertion` links an `earl:subject`, an `earl:test` and an `earl:result`, and the `earl:TestResult`
carries the `earl:outcome`. `ConditionAssessment` flattens the assertion and its result into one row, so it is a
close rather than exact match for `earl:Assertion`.

### Classes

| AI Atlas Nexus                                                                             | URI                                                                                                                                         | Close mappings   | Related mappings       |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------------------- |
| `EvaluationStandard`                                                                       | `dpv:ManagementStandard`                                                                                                                    |                  |                        |
| `ThirdPartyEvaluationEngagement`                                                           | `nexus:ThirdPartyEvaluationEngagement`                                                                                                      | `prov:Activity`  | `dpv:Assessment`       |
| `EvaluationStandardConformance`                                                            | `nexus:EvaluationStandardConformance`                                                                                                       |                  | `dpv:ComplianceStatus` |
| `ConditionAssessment`                                                                      | `nexus:ConditionAssessment`                                                                                                                 | `earl:Assertion` | `earl:TestResult`      |
| `Principle`                                                                                | `dpv:Principle`                                                                                                                             |                  |                        |
| `ControlActivityObligation`, `ControlActivityProhibition`, `ControlActivityRecommendation` | `nexus:` URIs; subclasses of `Obligation` (`dpv:Obligation`), `Prohibition` (`dpv:Prohibition`) and `Recommendation` (`dpv:Recommendation`) |                  |                        |

### Slots

| AI Atlas Nexus          | URI                                   | Close mappings                            | Related mappings  |
| ----------------------- | ------------------------------------- | ----------------------------------------- | ----------------- |
| `hasEvaluator`          | `nexus:hasEvaluator`                  | `prov:wasAssociatedWith`                  | `earl:assertedBy` |
| `hasSystemProvider`     | `nexus:hasSystemProvider`             |                                           |                   |
| `evaluatesAi`           | `nexus:evaluatesAi`                   |                                           | `earl:subject`    |
| `usesEvaluation`        | `nexus:usesEvaluation`                | `prov:used`                               |                   |
| `hasEvaluation`         | `dqv:hasQualityMeasurement`           |                                           |                   |
| `startDate` / `endDate` | `schema:startDate` / `schema:endDate` | `prov:startedAtTime` / `prov:endedAtTime` |                   |
| `conformsToStandard`    | `dcterms:conformsTo`                  |                                           |                   |
| `assessesCondition`     | `earl:test`                           |                                           |                   |
| `hasConformanceOutcome` | `earl:outcome`                        | `dpv:hasComplianceStatus`                 |                   |
| `justification`         | `nexus:justification`                 |                                           | `earl:info`       |
| `hasPrinciple`          | `dpv:isPartOf`                        |                                           |                   |
| `hasRule`               | `dpv:hasRule`                         |                                           |                   |

### Outcomes (`ConformanceOutcome`)

| Value               | Meaning             | Close mappings          | Related mappings                        |
| ------------------- | ------------------- | ----------------------- | --------------------------------------- |
| `FULFILLED`         | `earl:passed`       | `dpv:Compliant`         |                                         |
| `NOT_FULFILLED`     | `earl:failed`       | `dpv:NonCompliant`      |                                         |
| `ALTERNATIVE_MEANS` |                     |                         | `earl:passed`, `dpv:PartiallyCompliant` |
| `NOT_APPLICABLE`    | `earl:inapplicable` |                         |                                         |
| `NOT_ASSESSED`      | `earl:untested`     | `dpv:ComplianceUnknown` |                                         |

`ALTERNATIVE_MEANS` has no exact counterpart. AEF-1 treats a requirement met via alternative means, with a
justification, as satisfying the principle.

The DPV terms above were checked against DPV 2.1, except `dpv:Recommendation`. That term is the existing class URI
of `Recommendation` in the schema, but it isn't defined in DPV 2.1.

## Legal cross-references

AEF-1 is mapped to the EU General-Purpose AI Code of Practice (Safety and Security Chapter, final version of
10 July 2025) and to California SB 53. The provisions are `Documentation` entries in `eu_gpai_code_of_practice_data.yaml`
and `ca_sb_53_data.yaml`. The mappings are an SSSOM table,
`src/ai_atlas_nexus/data/mappings/aef1_to_legal_provisions.tsv`, lifted into
`knowledge_graph/mappings/aef1_to_legal_provisions_from_tsv_data.yaml` as `related_mappings` (`skos:relatedMatch`) in both
directions.

| AEF-1                                                                              | Provision                                  | Source            |
| ---------------------------------------------------------------------------------- | ------------------------------------------ | ----------------- |
| AEF-1 (the checklist)                                                              | EU CoP Safety & Security Measure 7.3(1)(g) | AEF-1 footnote 1  |
| AEF-1 (the checklist)                                                              | Cal. Bus. & Prof. Code § 22757.12(c)(2)(C) | AEF-1 footnote 1  |
| 1.4 Time                                                                           | EU CoP Appendix 3.4                        | AEF-1 footnote 6  |
| 5.2 Evaluation integrity                                                           | EU CoP Appendix 3.5                        | AEF-1 footnote 9  |
| 5.3 Protecting confidential information                                            | EU CoP Appendix 3.5                        | AEF-1 footnote 10 |
| Principle 1: Sufficient Access and Resources                                       | EU CoP Measure 7.3, Appendix 3.5           | Text comparison   |
| 1.1 Technical access, 1.1.3 Safeguard exemptions, 1.1.4 Intermediate system states | EU CoP Appendix 3.4                        | Text comparison   |
| 1.2 Information, 1.3 Computational resources                                       | EU CoP Appendix 3.4                        | Text comparison   |

Mappings cited by AEF-1 have confidence 0.9. Mappings from text comparison have confidence 0.8 and should be
reviewed by a curator.

```python
ran.get_by_id(class_name="controlactivityobligation", identifier="aef1-ctrl-access-4").related_mappings
# ['eu-gpai-cop-ss-appendix-3-4']
```
