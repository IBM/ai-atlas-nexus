---
search:
  boost: 10.0
---

# Class: ControlActivityRecommendation

_A control activity (rule) describing a recommendation for performing an activity_

<div data-search-exclude markdown="1">

URI: [nexus:ControlActivityRecommendation](https://w3id.org/ai-atlas-nexus/ControlActivityRecommendation)

```mermaid
 classDiagram
    class ControlActivityRecommendation
    click ControlActivityRecommendation href "../ControlActivityRecommendation/"
      ControlActivity <|-- ControlActivityRecommendation
        click ControlActivity href "../ControlActivity/"
      Recommendation <|-- ControlActivityRecommendation
        click Recommendation href "../Recommendation/"

      ControlActivityRecommendation : broad_mappings





        ControlActivityRecommendation --> "*" Any : broad_mappings
        click Any href "../Any/"



      ControlActivityRecommendation : close_mappings





        ControlActivityRecommendation --> "*" Any : close_mappings
        click Any href "../Any/"



      ControlActivityRecommendation : dateCreated

      ControlActivityRecommendation : dateModified

      ControlActivityRecommendation : description

      ControlActivityRecommendation : exact_mappings





        ControlActivityRecommendation --> "*" Any : exact_mappings
        click Any href "../Any/"



      ControlActivityRecommendation : hasControlApplication





        ControlActivityRecommendation --> "0..1" AIUC1ControlApplicationCategory : hasControlApplication
        click AIUC1ControlApplicationCategory href "../AIUC1ControlApplicationCategory/"



      ControlActivityRecommendation : hasEvidenceCategory





        ControlActivityRecommendation --> "*" AIUC1EvidenceCategory : hasEvidenceCategory
        click AIUC1EvidenceCategory href "../AIUC1EvidenceCategory/"



      ControlActivityRecommendation : hasLifecycleStatus





        ControlActivityRecommendation --> "0..1" LifecycleStatus : hasLifecycleStatus
        click LifecycleStatus href "../LifecycleStatus/"



      ControlActivityRecommendation : hasRequirement





        ControlActivityRecommendation --> "0..1" Requirement : hasRequirement
        click Requirement href "../Requirement/"



      ControlActivityRecommendation : hasRequirementType





        ControlActivityRecommendation --> "0..1" AIUC1RequirementType : hasRequirementType
        click AIUC1RequirementType href "../AIUC1RequirementType/"



      ControlActivityRecommendation : hasRule





        ControlActivityRecommendation --> "*" Rule : hasRule
        click Rule href "../Rule/"



      ControlActivityRecommendation : hasTypicalEvidence

      ControlActivityRecommendation : hasTypicalLocation

      ControlActivityRecommendation : id

      ControlActivityRecommendation : isApplicableToCapability





        ControlActivityRecommendation --> "*" AiTask : isApplicableToCapability
        click AiTask href "../AiTask/"



      ControlActivityRecommendation : isCategorizedAs





        ControlActivityRecommendation --> "*" Any : isCategorizedAs
        click Any href "../Any/"



      ControlActivityRecommendation : isDefinedByTaxonomy





        ControlActivityRecommendation --> "0..1" Taxonomy : isDefinedByTaxonomy
        click Taxonomy href "../Taxonomy/"



      ControlActivityRecommendation : name

      ControlActivityRecommendation : narrow_mappings





        ControlActivityRecommendation --> "*" Any : narrow_mappings
        click Any href "../Any/"



      ControlActivityRecommendation : notes

      ControlActivityRecommendation : related_mappings





        ControlActivityRecommendation --> "*" Any : related_mappings
        click Any href "../Any/"



      ControlActivityRecommendation : type

      ControlActivityRecommendation : url


```

## Inheritance

- [Entity](Entity.md)
  - [Rule](Rule.md)
    - [Recommendation](Recommendation.md)
      - **ControlActivityRecommendation** [ [ControlActivity](ControlActivity.md)]

## Class Properties

| Property  | Value                                                                                                |
| --------- | ---------------------------------------------------------------------------------------------------- |
| Class URI | [nexus:ControlActivityRecommendation](https://w3id.org/ai-atlas-nexus/ControlActivityRecommendation) |

## Slots

| Name                                                    | Cardinality and Range                                                            | Description                                                                      | Inheritance                           |
| ------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------- |
| [type](type.md)                                         | 0..1 <br/> [String](String.md)                                                   |                                                                                  | direct                                |
| [hasControlApplication](hasControlApplication.md)       | 0..1 <br/> [AIUC1ControlApplicationCategory](AIUC1ControlApplicationCategory.md) | Which of the AIUC-1 ControlApplicationCategory this control activity (rule) b... | [ControlActivity](ControlActivity.md) |
| [hasEvidenceCategory](hasEvidenceCategory.md)           | \* <br/> [AIUC1EvidenceCategory](AIUC1EvidenceCategory.md)                       | The evidence category, ie Technical Implementation, Operational Practices, et... | [ControlActivity](ControlActivity.md) |
| [hasTypicalLocation](hasTypicalLocation.md)             | \* <br/> [String](String.md)                                                     | The evidence is usually found here                                               | [ControlActivity](ControlActivity.md) |
| [isApplicableToCapability](isApplicableToCapability.md) | \* <br/> [AiTask](AiTask.md)                                                     | This evidence only applies to AI systems with this capability                    | [ControlActivity](ControlActivity.md) |
| [hasRequirement](hasRequirement.md)                     | 0..1 <br/> [Requirement](Requirement.md)                                         | This requirement this rule belongs to                                            | [ControlActivity](ControlActivity.md) |
| [hasRequirementType](hasRequirementType.md)             | 0..1 <br/> [AIUC1RequirementType](AIUC1RequirementType.md)                       | The requirement type of whether this is preventive, detective, etc               | [ControlActivity](ControlActivity.md) |
| [hasTypicalEvidence](hasTypicalEvidence.md)             | 0..1 <br/> [String](String.md)                                                   | The evidence is usually found here                                               | [ControlActivity](ControlActivity.md) |
| [isDefinedByTaxonomy](isDefinedByTaxonomy.md)           | 0..1 <br/> [Taxonomy](Taxonomy.md)                                               | A relationship where a concept or a concept group is defined by a taxonomy       | [Rule](Rule.md)                       |
| [hasRule](hasRule.md)                                   | \* <br/> [Rule](Rule.md)                                                         | Specifying applicability or inclusion of a rule within specified context         | [Rule](Rule.md)                       |
| [id](id.md)                                             | 1 <br/> [String](String.md)                                                      | A unique identifier to this instance of the model element                        | [Entity](Entity.md)                   |
| [name](name.md)                                         | 0..1 <br/> [String](String.md)                                                   | A text name of this instance                                                     | [Entity](Entity.md)                   |
| [description](description.md)                           | 0..1 <br/> [String](String.md)                                                   | The description of an entity                                                     | [Entity](Entity.md)                   |
| [url](url.md)                                           | 0..1 <br/> [Uri](Uri.md)                                                         | An optional URL associated with this instance                                    | [Entity](Entity.md)                   |
| [dateCreated](dateCreated.md)                           | 0..1 <br/> [Date](Date.md)                                                       | The date on which the entity was created                                         | [Entity](Entity.md)                   |
| [dateModified](dateModified.md)                         | 0..1 <br/> [Date](Date.md)                                                       | The date on which the entity was most recently modified                          | [Entity](Entity.md)                   |
| [exact_mappings](exact_mappings.md)                     | \* <br/> [Any](Any.md)                                                           | The property is used to link two concepts, indicating a high degree of confid... | [Entity](Entity.md)                   |
| [close_mappings](close_mappings.md)                     | \* <br/> [Any](Any.md)                                                           | The property is used to link two concepts that are sufficiently similar that ... | [Entity](Entity.md)                   |
| [related_mappings](related_mappings.md)                 | \* <br/> [Any](Any.md)                                                           | The property skos:relatedMatch is used to state an associative mapping link b... | [Entity](Entity.md)                   |
| [narrow_mappings](narrow_mappings.md)                   | \* <br/> [Any](Any.md)                                                           | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md)                   |
| [broad_mappings](broad_mappings.md)                     | \* <br/> [Any](Any.md)                                                           | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md)                   |
| [isCategorizedAs](isCategorizedAs.md)                   | \* <br/> [Any](Any.md)                                                           | A relationship where an entity has been deemed to be categorized                 | [Entity](Entity.md)                   |
| [hasLifecycleStatus](hasLifecycleStatus.md)             | 0..1 <br/> [LifecycleStatus](LifecycleStatus.md)                                 | The editorial / publication lifecycle state of this entity                       | [Entity](Entity.md)                   |
| [notes](notes.md)                                       | \* <br/> [String](String.md)                                                     | Free-text editorial notes, source breadcrumbs, or build-time provenance that ... | [Entity](Entity.md)                   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value                        |
| ------------ | ----------------------------------- |
| self         | nexus:ControlActivityRecommendation |
| native       | nexus:ControlActivityRecommendation |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ControlActivityRecommendation
description: A control activity (rule) describing a recommendation for performing
  an activity
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Recommendation
mixins:
- ControlActivity
attributes:
  type:
    name: type
    from_schema: https://w3id.org/ai-atlas-nexus/ai_aiuc
    designates_type: true
    domain_of:
    - Vocabulary
    - Taxonomy
    - Concept
    - Control
    - Group
    - Entry
    - Policy
    - Rule
    - Permission
    - Prohibition
    - Obligation
    - Recommendation
    - Certification
    - BenchmarkMetadataCard
    - ControlActivity
    - ControlActivityPermission
    - ControlActivityProhibition
    - ControlActivityObligation
    - ControlActivityRecommendation
    - Requirement
    range: string
class_uri: nexus:ControlActivityRecommendation

````
</details>

### Induced

<details>
```yaml
name: ControlActivityRecommendation
description: A control activity (rule) describing a recommendation for performing
  an activity
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Recommendation
mixins:
- ControlActivity
attributes:
  type:
    name: type
    from_schema: https://w3id.org/ai-atlas-nexus/ai_aiuc
    designates_type: true
    owner: ControlActivityRecommendation
    domain_of:
    - Vocabulary
    - Taxonomy
    - Concept
    - Control
    - Group
    - Entry
    - Policy
    - Rule
    - Permission
    - Prohibition
    - Obligation
    - Recommendation
    - Certification
    - BenchmarkMetadataCard
    - ControlActivity
    - ControlActivityPermission
    - ControlActivityProhibition
    - ControlActivityObligation
    - ControlActivityRecommendation
    - Requirement
    range: string
  hasControlApplication:
    name: hasControlApplication
    description: Which of the AIUC-1 ControlApplicationCategory this control activity
      (rule) belongs to
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: ControlActivity
    slot_uri: nexus:hasControlApplication
    owner: ControlActivityRecommendation
    domain_of:
    - ControlActivity
    range: AIUC1ControlApplicationCategory
  hasEvidenceCategory:
    name: hasEvidenceCategory
    description: The evidence category, ie Technical Implementation, Operational Practices,
      etc.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: ControlActivity
    slot_uri: nexus:hasEvidenceCategory
    owner: ControlActivityRecommendation
    domain_of:
    - ControlActivity
    range: AIUC1EvidenceCategory
    multivalued: true
    inlined: false
  hasTypicalLocation:
    name: hasTypicalLocation
    description: The evidence is usually found here
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: ControlActivity
    slot_uri: nexus:hasTypicalLocation
    owner: ControlActivityRecommendation
    domain_of:
    - ControlActivity
    range: string
    multivalued: true
    inlined: false
  isApplicableToCapability:
    name: isApplicableToCapability
    description: This evidence only applies to AI systems with this capability
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: ControlActivity
    slot_uri: nexus:isApplicableToCapability
    owner: ControlActivityRecommendation
    domain_of:
    - ControlActivity
    - Requirement
    range: AiTask
    multivalued: true
    inlined: false
  hasRequirement:
    name: hasRequirement
    description: This requirement this rule belongs to
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: ControlActivity
    slot_uri: nexus:hasRequirement
    owner: ControlActivityRecommendation
    domain_of:
    - ControlActivity
    range: Requirement
    multivalued: false
    inlined: false
  hasRequirementType:
    name: hasRequirementType
    description: The requirement type of whether this is preventive, detective, etc.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: Any
    slot_uri: nexus:hasRequirementType
    owner: ControlActivityRecommendation
    domain_of:
    - ControlActivity
    - Requirement
    range: AIUC1RequirementType
  hasTypicalEvidence:
    name: hasTypicalEvidence
    description: The evidence is usually found here
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: ControlActivity
    slot_uri: nexus:hasTypicalEvidence
    owner: ControlActivityRecommendation
    domain_of:
    - ControlActivity
    range: string
    multivalued: false
    inlined: false
  isDefinedByTaxonomy:
    name: isDefinedByTaxonomy
    description: A relationship where a concept or a concept group is defined by a
      taxonomy
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    owner: ControlActivityRecommendation
    domain_of:
    - Concept
    - Control
    - Group
    - Entry
    - Policy
    - Rule
    - RiskControlGroup
    - RiskGroup
    - Risk
    - RiskControl
    - Action
    - RiskIncident
    - CapabilityGroup
    - AiTaskDomain
    - AiTaskGroup
    - Stakeholder
    - StakeholderGroup
    - Requirement
    range: Taxonomy
  hasRule:
    name: hasRule
    description: Specifying applicability or inclusion of a rule within specified
      context.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: dpv:hasRule
    owner: ControlActivityRecommendation
    domain_of:
    - Entry
    - LLMQuestionPolicy
    - Rule
    - Requirement
    range: Rule
    multivalued: true
    inlined: false
  id:
    name: id
    description: A unique identifier to this instance of the model element. Example
      identifiers include UUID, URI, URN, etc.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    owner: ControlActivityRecommendation
    domain_of:
    - Entity
    range: string
    required: true
  name:
    name: name
    description: A text name of this instance.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:name
    owner: ControlActivityRecommendation
    domain_of:
    - Entity
    - BenchmarkMetadataCard
    range: string
  description:
    name: description
    description: The description of an entity
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:description
    owner: ControlActivityRecommendation
    domain_of:
    - Entity
    range: string
  url:
    name: url
    description: An optional URL associated with this instance.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:url
    owner: ControlActivityRecommendation
    domain_of:
    - Entity
    range: uri
  dateCreated:
    name: dateCreated
    description: The date on which the entity was created.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateCreated
    owner: ControlActivityRecommendation
    domain_of:
    - Entity
    range: date
    required: false
  dateModified:
    name: dateModified
    description: The date on which the entity was most recently modified.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateModified
    owner: ControlActivityRecommendation
    domain_of:
    - Entity
    range: date
    required: false
  exact_mappings:
    name: exact_mappings
    description: The property is used to link two concepts, indicating a high degree
      of confidence that the concepts can be used interchangeably across a wide range
      of information retrieval applications
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:exactMatch
    owner: ControlActivityRecommendation
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  close_mappings:
    name: close_mappings
    description: The property is used to link two concepts that are sufficiently similar
      that they can be used interchangeably in some information retrieval applications.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:closeMatch
    owner: ControlActivityRecommendation
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  related_mappings:
    name: related_mappings
    description: The property skos:relatedMatch is used to state an associative mapping
      link between two concepts.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:relatedMatch
    owner: ControlActivityRecommendation
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  narrow_mappings:
    name: narrow_mappings
    description: The property is used to state a hierarchical mapping link between
      two concepts, indicating that the concept linked to, is a narrower concept than
      the originating concept.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:narrowMatch
    owner: ControlActivityRecommendation
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  broad_mappings:
    name: broad_mappings
    description: The property is used to state a hierarchical mapping link between
      two concepts, indicating that the concept linked to, is a broader concept than
      the originating concept.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:broadMatch
    owner: ControlActivityRecommendation
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  isCategorizedAs:
    name: isCategorizedAs
    description: A relationship where an entity has been deemed to be categorized
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: nexus:isCategorizedAs
    owner: ControlActivityRecommendation
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  hasLifecycleStatus:
    name: hasLifecycleStatus
    description: The editorial / publication lifecycle state of this entity. Distinct
      from AiLifecyclePhase, which describes an AI system's runtime evolution rather
      than the editorial workflow of a catalogued entry.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    aliases:
    - lifecycle_status
    - doc_status
    rank: 1000
    slot_uri: adms:status
    owner: ControlActivityRecommendation
    domain_of:
    - Entity
    range: LifecycleStatus
  notes:
    name: notes
    description: Free-text editorial notes, source breadcrumbs, or build-time provenance
      that do not belong in the user-facing description. Opaque to consumers.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:note
    owner: ControlActivityRecommendation
    domain_of:
    - Entity
    range: string
    recommended: false
    multivalued: true
class_uri: nexus:ControlActivityRecommendation

````

</details></div>
