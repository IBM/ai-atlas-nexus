---
search:
  boost: 5.0
---

# Slot: isApplicableinLocality

_A relationship where an entity has is applicable in these localities._

<div data-search-exclude markdown="1">

URI: [nexus:isApplicableinLocality](https://w3id.org/ai-atlas-nexus/isApplicableinLocality)
Alias: isApplicableinLocality

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                      | Description                                                                      | Modifies Slot |
| ----------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [LLMQuestionPolicy](LLMQuestionPolicy.md) | The policy guides how the language model should answer a diverse set of sensi... | no            |
| [Policy](Policy.md)                       | A guidance document outlining any of: procedures, plans, principles, decision... | no            |
| [Action](Action.md)                       | Action to remediate a risk                                                       | no            |
| [Control](Control.md)                     | A measure that maintains and/or modifies                                         | no            |
| [RiskControl](RiskControl.md)             | A measure that maintains and/or modifies risk (and risk concepts)                | no            |

## Properties

### Type and Range

| Property  | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Range     | [LocalityOfUse](LocalityOfUse.md)                                                      |
| Domain Of | [Control](Control.md), [Policy](Policy.md)                                             |
| Slot URI  | [nexus:isApplicableinLocality](https://w3id.org/ai-atlas-nexus/isApplicableinLocality) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value                 |
| ------------ | ---------------------------- |
| self         | nexus:isApplicableinLocality |
| native       | nexus:isApplicableinLocality |

## LinkML Source

<details>
```yaml
name: isApplicableinLocality
description: A relationship where an entity has is applicable in these localities.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: nexus:isApplicableinLocality
alias: isApplicableinLocality
domain_of:
- Control
- Policy
range: LocalityOfUse
multivalued: true
inlined: false

```
</details></div>
```
