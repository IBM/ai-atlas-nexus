---
search:
  boost: 10.0
---

# Class: AttributeConditionRule

<div data-search-exclude markdown="1">

URI: [nexus:AttributeConditionRule](https://w3id.org/ai-atlas-nexus/AttributeConditionRule)

```mermaid
 classDiagram
    class AttributeConditionRule
    click AttributeConditionRule href "../AttributeConditionRule/"
      Rule <|-- AttributeConditionRule
        click Rule href "../Rule/"

      AttributeConditionRule : broad_mappings





        AttributeConditionRule --> "*" Any : broad_mappings
        click Any href "../Any/"



      AttributeConditionRule : close_mappings





        AttributeConditionRule --> "*" Any : close_mappings
        click Any href "../Any/"



      AttributeConditionRule : dateCreated

      AttributeConditionRule : dateModified

      AttributeConditionRule : description

      AttributeConditionRule : exact_mappings





        AttributeConditionRule --> "*" Any : exact_mappings
        click Any href "../Any/"



      AttributeConditionRule : hasLifecycleStatus





        AttributeConditionRule --> "0..1" LifecycleStatus : hasLifecycleStatus
        click LifecycleStatus href "../LifecycleStatus/"



      AttributeConditionRule : hasRule





        AttributeConditionRule --> "*" Rule : hasRule
        click Rule href "../Rule/"



      AttributeConditionRule : id

      AttributeConditionRule : isCategorizedAs





        AttributeConditionRule --> "*" Any : isCategorizedAs
        click Any href "../Any/"



      AttributeConditionRule : isDefinedByTaxonomy





        AttributeConditionRule --> "0..1" Taxonomy : isDefinedByTaxonomy
        click Taxonomy href "../Taxonomy/"



      AttributeConditionRule : name

      AttributeConditionRule : narrow_mappings





        AttributeConditionRule --> "*" Any : narrow_mappings
        click Any href "../Any/"



      AttributeConditionRule : postconditions





        AttributeConditionRule --> "0..1" AnonymousClassExpression : postconditions
        click AnonymousClassExpression href "../AnonymousClassExpression/"



      AttributeConditionRule : preconditions





        AttributeConditionRule --> "0..1" AnonymousClassExpression : preconditions
        click AnonymousClassExpression href "../AnonymousClassExpression/"



      AttributeConditionRule : related_mappings





        AttributeConditionRule --> "*" Any : related_mappings
        click Any href "../Any/"



      AttributeConditionRule : type

      AttributeConditionRule : url


```

## Inheritance

- [Entity](Entity.md)
  - [Rule](Rule.md)
    - **AttributeConditionRule**

## Slots

| Name                                          | Cardinality and Range                                              | Description                                                                      | Inheritance         |
| --------------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------- | ------------------- |
| [preconditions](preconditions.md)             | 0..1 <br/> [AnonymousClassExpression](AnonymousClassExpression.md) | Conditions that must be satisfied before the rule applies                        | direct              |
| [postconditions](postconditions.md)           | 0..1 <br/> [AnonymousClassExpression](AnonymousClassExpression.md) | Conditions that result from applying the rule                                    | direct              |
| [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | 0..1 <br/> [Taxonomy](Taxonomy.md)                                 | A relationship where a concept or a concept group is defined by a taxonomy       | [Rule](Rule.md)     |
| [hasRule](hasRule.md)                         | \* <br/> [Rule](Rule.md)                                           | Specifying applicability or inclusion of a rule within specified context         | [Rule](Rule.md)     |
| [type](type.md)                               | 0..1 <br/> [String](String.md)                                     | The type or class designation of this entity instance                            | [Rule](Rule.md)     |
| [id](id.md)                                   | 1 <br/> [String](String.md)                                        | A unique identifier to this instance of the model element                        | [Entity](Entity.md) |
| [name](name.md)                               | 0..1 <br/> [String](String.md)                                     | A text name of this instance                                                     | [Entity](Entity.md) |
| [description](description.md)                 | 0..1 <br/> [String](String.md)                                     | The description of an entity                                                     | [Entity](Entity.md) |
| [url](url.md)                                 | 0..1 <br/> [Uri](Uri.md)                                           | An optional URL associated with this instance                                    | [Entity](Entity.md) |
| [dateCreated](dateCreated.md)                 | 0..1 <br/> [Date](Date.md)                                         | The date on which the entity was created                                         | [Entity](Entity.md) |
| [dateModified](dateModified.md)               | 0..1 <br/> [Date](Date.md)                                         | The date on which the entity was most recently modified                          | [Entity](Entity.md) |
| [exact_mappings](exact_mappings.md)           | \* <br/> [Any](Any.md)                                             | The property is used to link two concepts, indicating a high degree of confid... | [Entity](Entity.md) |
| [close_mappings](close_mappings.md)           | \* <br/> [Any](Any.md)                                             | The property is used to link two concepts that are sufficiently similar that ... | [Entity](Entity.md) |
| [related_mappings](related_mappings.md)       | \* <br/> [Any](Any.md)                                             | The property skos:relatedMatch is used to state an associative mapping link b... | [Entity](Entity.md) |
| [narrow_mappings](narrow_mappings.md)         | \* <br/> [Any](Any.md)                                             | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |
| [broad_mappings](broad_mappings.md)           | \* <br/> [Any](Any.md)                                             | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |
| [isCategorizedAs](isCategorizedAs.md)         | \* <br/> [Any](Any.md)                                             | A relationship where an entity has been deemed to be categorized                 | [Entity](Entity.md) |
| [hasLifecycleStatus](hasLifecycleStatus.md)   | 0..1 <br/> [LifecycleStatus](LifecycleStatus.md)                   | The editorial / publication lifecycle state of this entity                       | [Entity](Entity.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value                 |
| ------------ | ---------------------------- |
| self         | nexus:AttributeConditionRule |
| native       | nexus:AttributeConditionRule |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AttributeConditionRule
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Rule
attributes:
  preconditions:
    name: preconditions
    description: Conditions that must be satisfied before the rule applies.
    from_schema: https://w3id.org/ai-atlas-nexus/common
    rank: 1000
    domain_of:
    - AttributeConditionRule
    range: AnonymousClassExpression
    inlined: true
  postconditions:
    name: postconditions
    description: Conditions that result from applying the rule.
    from_schema: https://w3id.org/ai-atlas-nexus/common
    rank: 1000
    domain_of:
    - AttributeConditionRule
    range: AnonymousClassExpression
    inlined: true

````
</details>

### Induced

<details>
```yaml
name: AttributeConditionRule
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Rule
attributes:
  preconditions:
    name: preconditions
    description: Conditions that must be satisfied before the rule applies.
    from_schema: https://w3id.org/ai-atlas-nexus/common
    rank: 1000
    alias: preconditions
    owner: AttributeConditionRule
    domain_of:
    - AttributeConditionRule
    range: AnonymousClassExpression
    inlined: true
  postconditions:
    name: postconditions
    description: Conditions that result from applying the rule.
    from_schema: https://w3id.org/ai-atlas-nexus/common
    rank: 1000
    alias: postconditions
    owner: AttributeConditionRule
    domain_of:
    - AttributeConditionRule
    range: AnonymousClassExpression
    inlined: true
  isDefinedByTaxonomy:
    name: isDefinedByTaxonomy
    description: A relationship where a concept or a concept group is defined by a
      taxonomy
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isDefinedByTaxonomy
    owner: AttributeConditionRule
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
    alias: hasRule
    owner: AttributeConditionRule
    domain_of:
    - Entry
    - LLMQuestionPolicy
    - Rule
    - Requirement
    range: Rule
    multivalued: true
    inlined: false
  type:
    name: type
    description: The type or class designation of this entity instance.
    from_schema: https://w3id.org/ai-atlas-nexus/common
    designates_type: true
    alias: type
    owner: AttributeConditionRule
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
  id:
    name: id
    description: A unique identifier to this instance of the model element. Example
      identifiers include UUID, URI, URN, etc.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: AttributeConditionRule
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
    alias: name
    owner: AttributeConditionRule
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
    alias: description
    owner: AttributeConditionRule
    domain_of:
    - Entity
    range: string
  url:
    name: url
    description: An optional URL associated with this instance.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:url
    alias: url
    owner: AttributeConditionRule
    domain_of:
    - Entity
    range: uri
  dateCreated:
    name: dateCreated
    description: The date on which the entity was created.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateCreated
    alias: dateCreated
    owner: AttributeConditionRule
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
    alias: dateModified
    owner: AttributeConditionRule
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
    alias: exact_mappings
    owner: AttributeConditionRule
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
    alias: close_mappings
    owner: AttributeConditionRule
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
    alias: related_mappings
    owner: AttributeConditionRule
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
    alias: narrow_mappings
    owner: AttributeConditionRule
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
    alias: broad_mappings
    owner: AttributeConditionRule
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
    alias: isCategorizedAs
    owner: AttributeConditionRule
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
    alias: hasLifecycleStatus
    owner: AttributeConditionRule
    domain_of:
    - Entity
    range: LifecycleStatus

````

</details></div>
