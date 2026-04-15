# Class: AIDeployer

_Any natural or legal person, public authority, agency or other body using an AI system under its authority except where the AI system is used in the course of a personal non-professional activity._

URI: [airo:AIDeployer](https://w3id.org/airo#AIDeployer)

```mermaid
 classDiagram
    class AIDeployer
    click AIDeployer href "../AIDeployer/"
      AIOperator <|-- AIDeployer
        click AIOperator href "../AIOperator/"

      AIDeployer : broad_mappings





        AIDeployer --> "*" Any : broad_mappings
        click Any href "../Any/"



      AIDeployer : close_mappings





        AIDeployer --> "*" Any : close_mappings
        click Any href "../Any/"



      AIDeployer : dateCreated

      AIDeployer : dateModified

      AIDeployer : description

      AIDeployer : exact_mappings





        AIDeployer --> "*" Any : exact_mappings
        click Any href "../Any/"



      AIDeployer : id

      AIDeployer : isCategorizedAs





        AIDeployer --> "*" Any : isCategorizedAs
        click Any href "../Any/"



      AIDeployer : isDefinedByTaxonomy





        AIDeployer --> "0..1" Taxonomy : isDefinedByTaxonomy
        click Taxonomy href "../Taxonomy/"



      AIDeployer : isPartOf





        AIDeployer --> "0..1" StakeholderGroup : isPartOf
        click StakeholderGroup href "../StakeholderGroup/"



      AIDeployer : name

      AIDeployer : narrow_mappings





        AIDeployer --> "*" Any : narrow_mappings
        click Any href "../Any/"



      AIDeployer : related_mappings





        AIDeployer --> "*" Any : related_mappings
        click Any href "../Any/"



      AIDeployer : url


```

## Inheritance

- [Entity](Entity.md)
  - [Stakeholder](Stakeholder.md)
    - [AIOperator](AIOperator.md)
      - **AIDeployer**

## Slots

| Name                                          | Cardinality and Range                              | Description                                                                      | Inheritance                   |
| --------------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------------- | ----------------------------- |
| [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | 0..1 <br/> [Taxonomy](Taxonomy.md)                 | A relationship where a concept or a concept group is defined by a taxonomy       | [Stakeholder](Stakeholder.md) |
| [isPartOf](isPartOf.md)                       | 0..1 <br/> [StakeholderGroup](StakeholderGroup.md) | A relationship where a stakeholder is part of a stakeholder group                | [Stakeholder](Stakeholder.md) |
| [id](id.md)                                   | 1 <br/> [String](String.md)                        | A unique identifier to this instance of the model element                        | [Entity](Entity.md)           |
| [name](name.md)                               | 0..1 <br/> [String](String.md)                     | A text name of this instance                                                     | [Entity](Entity.md)           |
| [description](description.md)                 | 0..1 <br/> [String](String.md)                     | The description of an entity                                                     | [Entity](Entity.md)           |
| [url](url.md)                                 | 0..1 <br/> [Uri](Uri.md)                           | An optional URL associated with this instance                                    | [Entity](Entity.md)           |
| [dateCreated](dateCreated.md)                 | 0..1 <br/> [Date](Date.md)                         | The date on which the entity was created                                         | [Entity](Entity.md)           |
| [dateModified](dateModified.md)               | 0..1 <br/> [Date](Date.md)                         | The date on which the entity was most recently modified                          | [Entity](Entity.md)           |
| [exact_mappings](exact_mappings.md)           | \* <br/> [Any](Any.md)                             | The property is used to link two concepts, indicating a high degree of confid... | [Entity](Entity.md)           |
| [close_mappings](close_mappings.md)           | \* <br/> [Any](Any.md)                             | The property is used to link two concepts that are sufficiently similar that ... | [Entity](Entity.md)           |
| [related_mappings](related_mappings.md)       | \* <br/> [Any](Any.md)                             | The property skos:relatedMatch is used to state an associative mapping link b... | [Entity](Entity.md)           |
| [narrow_mappings](narrow_mappings.md)         | \* <br/> [Any](Any.md)                             | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md)           |
| [broad_mappings](broad_mappings.md)           | \* <br/> [Any](Any.md)                             | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md)           |
| [isCategorizedAs](isCategorizedAs.md)         | \* <br/> [Any](Any.md)                             | A relationship where an entity has been deemed to be categorized                 | [Entity](Entity.md)           |

## Usages

| used by                 | used in                         | type  | used                        |
| ----------------------- | ------------------------------- | ----- | --------------------------- |
| [AiSystem](AiSystem.md) | [isDeployedBy](isDeployedBy.md) | range | [AIDeployer](AIDeployer.md) |
| [AiAgent](AiAgent.md)   | [isDeployedBy](isDeployedBy.md) | range | [AIDeployer](AIDeployer.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value     |
| ------------ | ---------------- |
| self         | airo:AIDeployer  |
| native       | nexus:AIDeployer |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AIDeployer
description: Any natural or legal person, public authority, agency or other body using
  an AI system under its authority except where the AI system is used in the course
  of a personal non-professional activity.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: AIOperator
class_uri: airo:AIDeployer

````
</details>

### Induced

<details>
```yaml
name: AIDeployer
description: Any natural or legal person, public authority, agency or other body using
  an AI system under its authority except where the AI system is used in the course
  of a personal non-professional activity.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: AIOperator
attributes:
  isDefinedByTaxonomy:
    name: isDefinedByTaxonomy
    description: A relationship where a concept or a concept group is defined by a
      taxonomy
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isDefinedByTaxonomy
    owner: AIDeployer
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
    - Stakeholder
    - StakeholderGroup
    - CapabilityGroup
    - Requirement
    range: Taxonomy
  isPartOf:
    name: isPartOf
    description: A relationship where a stakeholder is part of a stakeholder group
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isPartOf
    owner: AIDeployer
    domain_of:
    - Entry
    - Risk
    - LargeLanguageModel
    - Stakeholder
    - CapabilityGroup
    range: StakeholderGroup
  id:
    name: id
    description: A unique identifier to this instance of the model element. Example
      identifiers include UUID, URI, URN, etc.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: AIDeployer
    domain_of:
    - Entity
    range: string
    required: true
  name:
    name: name
    description: A text name of this instance.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:name
    alias: name
    owner: AIDeployer
    domain_of:
    - Entity
    - BenchmarkMetadataCard
    range: string
  description:
    name: description
    description: The description of an entity
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:description
    alias: description
    owner: AIDeployer
    domain_of:
    - Entity
    range: string
  url:
    name: url
    description: An optional URL associated with this instance.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:url
    alias: url
    owner: AIDeployer
    domain_of:
    - Entity
    range: uri
  dateCreated:
    name: dateCreated
    description: The date on which the entity was created.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateCreated
    alias: dateCreated
    owner: AIDeployer
    domain_of:
    - Entity
    range: date
    required: false
  dateModified:
    name: dateModified
    description: The date on which the entity was most recently modified.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateModified
    alias: dateModified
    owner: AIDeployer
    domain_of:
    - Entity
    range: date
    required: false
  exact_mappings:
    name: exact_mappings
    description: The property is used to link two concepts, indicating a high degree
      of confidence that the concepts can be used interchangeably across a wide range
      of information retrieval applications
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: skos:exactMatch
    alias: exact_mappings
    owner: AIDeployer
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  close_mappings:
    name: close_mappings
    description: The property is used to link two concepts that are sufficiently similar
      that they can be used interchangeably in some information retrieval applications.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: skos:closeMatch
    alias: close_mappings
    owner: AIDeployer
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  related_mappings:
    name: related_mappings
    description: The property skos:relatedMatch is used to state an associative mapping
      link between two concepts.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: skos:relatedMatch
    alias: related_mappings
    owner: AIDeployer
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
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: skos:narrowMatch
    alias: narrow_mappings
    owner: AIDeployer
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
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: skos:broadMatch
    alias: broad_mappings
    owner: AIDeployer
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  isCategorizedAs:
    name: isCategorizedAs
    description: A relationship where an entity has been deemed to be categorized
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: nexus:isCategorizedAs
    alias: isCategorizedAs
    owner: AIDeployer
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
class_uri: airo:AIDeployer

````

</details>
