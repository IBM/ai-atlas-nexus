# Slot: hasEvidenceCategory

_The evidence category, ie Technical Implementation, Operational Practices, etc._

URI: [nexus:hasEvidenceCategory](https://ibm.github.io/ai-atlas-nexus/ontology/hasEvidenceCategory)
Alias: hasEvidenceCategory

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ControlActivityPermission](ControlActivityPermission.md)         | A control activity (rule) describing a permission to perform an activity         | no            |
| [ControlActivity](ControlActivity.md)                             | An obligation, permission, or prohibition for AI system assurance                | no            |
| [ControlActivityObligation](ControlActivityObligation.md)         | A control activity (rule) describing an obligation for performing an activity    | no            |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | A control activity (rule) describing a prohibition to perform an activity        | no            |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | A control activity (rule) describing a recommendation for performing an activ... | no            |

## Properties

- Range: [AIUC1EvidenceCategory](AIUC1EvidenceCategory.md)

- Multivalued: True

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value              |
| ------------ | ------------------------- |
| self         | nexus:hasEvidenceCategory |
| native       | nexus:hasEvidenceCategory |

## LinkML Source

<details>
```yaml
name: hasEvidenceCategory
description: The evidence category, ie Technical Implementation, Operational Practices,
  etc.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: nexus:hasEvidenceCategory
alias: hasEvidenceCategory
domain_of:
- ControlActivity
range: AIUC1EvidenceCategory
multivalued: true
inlined: false

```
</details>
```
