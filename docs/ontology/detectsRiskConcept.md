---
search:
  boost: 5.0
---

# Slot: detectsRiskConcept

_The property airo:detectsRiskConcept indicates the control used for detecting risks, risk sources, consequences, and impacts._

<div data-search-exclude markdown="1">

URI: [nexus:detectsRiskConcept](https://w3id.org/ai-atlas-nexus/detectsRiskConcept)
Alias: detectsRiskConcept

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                          | Description                                                                      | Modifies Slot |
| ----------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Risk](Risk.md)               | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [Action](Action.md)           | Action to remediate a risk                                                       | no            |
| [RiskControl](RiskControl.md) | A measure that maintains and/or modifies risk (and risk concepts)                | no            |

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

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

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
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
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
</details></div>
```
