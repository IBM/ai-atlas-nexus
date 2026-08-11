---
search:
  boost: 5.0
---

# Slot: mitigatesRiskConcept

_Indicates the control used for mitigating risks, risk sources, consequences, and impacts._

<div data-search-exclude markdown="1">

URI: [nexus:mitigatesRiskConcept](https://w3id.org/ai-atlas-nexus/mitigatesRiskConcept)
Alias: mitigatesRiskConcept

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                          | Description                                                       | Modifies Slot |
| ----------------------------- | ----------------------------------------------------------------- | ------------- |
| [RiskControl](RiskControl.md) | A measure that maintains and/or modifies risk (and risk concepts) | no            |
| [Action](Action.md)           | Action to remediate a risk                                        | no            |

## Properties

### Type and Range

| Property  | Value                         |
| --------- | ----------------------------- |
| Range     | [RiskConcept](RiskConcept.md) |
| Domain    | [RiskControl](RiskControl.md) |
| Domain Of | [RiskControl](RiskControl.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

<details>
<summary>Relationship Properties</summary>

| Property | Value                             |
| -------- | --------------------------------- |
| Inverse  | [isMitigatedBy](isMitigatedBy.md) |

</details>

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value               |
| ------------ | -------------------------- |
| self         | nexus:mitigatesRiskConcept |
| native       | nexus:mitigatesRiskConcept |
| exact        | airo:mitigatesRiskConcept  |

## LinkML Source

<details>
```yaml
name: mitigatesRiskConcept
description: Indicates the control used for mitigating risks, risk sources, consequences,
  and impacts.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
exact_mappings:
- airo:mitigatesRiskConcept
rank: 1000
domain: RiskControl
alias: mitigatesRiskConcept
domain_of:
- RiskControl
inverse: isMitigatedBy
range: RiskConcept
multivalued: true
inlined: false

```
</details></div>
```
