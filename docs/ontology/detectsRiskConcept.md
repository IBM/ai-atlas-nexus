# Slot: detectsRiskConcept

_The property airo:detectsRiskConcept indicates the control used for detecting risks, risk sources, consequences, and impacts._

URI: [nexus:detectsRiskConcept](https://ibm.github.io/ai-atlas-nexus/ontology/detectsRiskConcept)
Alias: detectsRiskConcept

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                          | Description                                                                      | Modifies Slot |
| ----------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [RiskControl](RiskControl.md) | A measure that maintains and/or modifies risk (and risk concepts)                | no            |
| [Risk](Risk.md)               | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [Action](Action.md)           | Action to remediate a risk                                                       | no            |

## Properties

### Type and Range

| Property  | Value                                          |
| --------- | ---------------------------------------------- |
| Range     | [RiskConcept](RiskConcept.md)                  |
| Domain    | [RiskControl](RiskControl.md)                  |
| Domain Of | [Risk](Risk.md), [RiskControl](RiskControl.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

<details>
<summary>Relationship Properties</summary>

| Property | Value                           |
| -------- | ------------------------------- |
| Inverse  | [isDetectedBy](isDetectedBy.md) |

</details>

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value             |
| ------------ | ------------------------ |
| self         | nexus:detectsRiskConcept |
| native       | nexus:detectsRiskConcept |
| exact        | airo:detectsRiskConcept  |

## LinkML Source

<details>
```yaml
name: detectsRiskConcept
description: The property airo:detectsRiskConcept indicates the control used for detecting
  risks, risk sources, consequences, and impacts.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
exact_mappings:
- airo:detectsRiskConcept
rank: 1000
domain: RiskControl
alias: detectsRiskConcept
domain_of:
- Risk
- RiskControl
inverse: isDetectedBy
range: RiskConcept
multivalued: true
inlined: false

```
</details>
```
