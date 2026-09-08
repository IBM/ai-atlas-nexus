---
search:
  boost: 5.0
---

# Slot: hasAiActorTask

_Pertinent AI Actor Tasks for each subcategory. Not every AI Actor Task listed will apply to every suggested action in the subcategory (i.e., some apply to AI development and others apply to AI deployment)._

<div data-search-exclude markdown="1">

URI: [nexus:hasAiActorTask](https://w3id.org/ai-atlas-nexus/hasAiActorTask)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                | Description                | Modifies Slot |
| ------------------- | -------------------------- | ------------- |
| [Action](Action.md) | Action to remediate a risk | no            |

## Properties

### Type and Range

| Property  | Value               |
| --------- | ------------------- |
| Range     | [String](String.md) |
| Domain Of | [Action](Action.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value         |
| ------------ | -------------------- |
| self         | nexus:hasAiActorTask |
| native       | nexus:hasAiActorTask |

## LinkML Source

<details>
```yaml
name: hasAiActorTask
description: Pertinent AI Actor Tasks for each subcategory. Not every AI Actor Task
  listed will apply to every suggested action in the subcategory (i.e., some apply
  to AI development and others apply to AI deployment).
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain_of:
- Action
range: string
multivalued: true

```
</details></div>
```
