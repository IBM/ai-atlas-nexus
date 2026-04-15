# Class: AiAgent

_An artificial intelligence (AI) agent refers to a system or program that is capable of autonomously performing tasks on behalf of a user or another system by designing its workflow and utilizing available tools._

URI: [nexus:AiAgent](https://ibm.github.io/ai-atlas-nexus/ontology/AiAgent)

```mermaid
 classDiagram
    class AiAgent
    click AiAgent href "../AiAgent/"
      AiSystem <|-- AiAgent
        click AiSystem href "../AiSystem/"

      AiAgent : broad_mappings





        AiAgent --> "*" Any : broad_mappings
        click Any href "../Any/"



      AiAgent : close_mappings





        AiAgent --> "*" Any : close_mappings
        click Any href "../Any/"



      AiAgent : dateCreated

      AiAgent : dateModified

      AiAgent : description

      AiAgent : exact_mappings





        AiAgent --> "*" Any : exact_mappings
        click Any href "../Any/"



      AiAgent : hasAISubject





        AiAgent --> "0..1" AISubject : hasAISubject
        click AISubject href "../AISubject/"



      AiAgent : hasAIUser

      AiAgent : hasCapability





        AiAgent --> "*" Capability : hasCapability
        click Capability href "../Capability/"



      AiAgent : hasDocumentation





        AiAgent --> "*" Documentation : hasDocumentation
        click Documentation href "../Documentation/"



      AiAgent : hasEuAiSystemType





        AiAgent --> "0..1" AiSystemType : hasEuAiSystemType
        click AiSystemType href "../AiSystemType/"



      AiAgent : hasEuRiskCategory





        AiAgent --> "0..1" EuAiRiskCategory : hasEuRiskCategory
        click EuAiRiskCategory href "../EuAiRiskCategory/"



      AiAgent : hasLicense





        AiAgent --> "0..1" License : hasLicense
        click License href "../License/"



      AiAgent : hasModelCard

      AiAgent : hasPurpose





        AiAgent --> "0..1" Purpose : hasPurpose
        click Purpose href "../Purpose/"



      AiAgent : hasRelatedRisk





        AiAgent --> "*" Risk : hasRelatedRisk
        click Risk href "../Risk/"



      AiAgent : hasStakeholder





        AiAgent --> "0..1" Stakeholder : hasStakeholder
        click Stakeholder href "../Stakeholder/"



      AiAgent : id

      AiAgent : implementedByAdapter





        AiAgent --> "*" Adapter : implementedByAdapter
        click Adapter href "../Adapter/"



      AiAgent : isAppliedWithinDomain





        AiAgent --> "*" Domain : isAppliedWithinDomain
        click Domain href "../Domain/"



      AiAgent : isCategorizedAs





        AiAgent --> "*" Any : isCategorizedAs
        click Any href "../Any/"



      AiAgent : isComposedOf





        AiAgent --> "*" BaseAi : isComposedOf
        click BaseAi href "../BaseAi/"



      AiAgent : isDefinedByTaxonomy





        AiAgent --> "0..1" Taxonomy : isDefinedByTaxonomy
        click Taxonomy href "../Taxonomy/"



      AiAgent : isDefinedByVocabulary





        AiAgent --> "0..1" Vocabulary : isDefinedByVocabulary
        click Vocabulary href "../Vocabulary/"



      AiAgent : isDeployedBy





        AiAgent --> "0..1" AIDeployer : isDeployedBy
        click AIDeployer href "../AIDeployer/"



      AiAgent : isDevelopedBy





        AiAgent --> "0..1" AIDeveloper : isDevelopedBy
        click AIDeveloper href "../AIDeveloper/"



      AiAgent : isPartOf

      AiAgent : isProvidedBy





        AiAgent --> "0..1" AiProvider : isProvidedBy
        click AiProvider href "../AiProvider/"



      AiAgent : isUsedWithinLocality





        AiAgent --> "*" LocalityOfUse : isUsedWithinLocality
        click LocalityOfUse href "../LocalityOfUse/"



      AiAgent : name

      AiAgent : narrow_mappings





        AiAgent --> "*" Any : narrow_mappings
        click Any href "../Any/"



      AiAgent : performsTask





        AiAgent --> "*" AiTask : performsTask
        click AiTask href "../AiTask/"



      AiAgent : producer





        AiAgent --> "0..1" Organization : producer
        click Organization href "../Organization/"



      AiAgent : related_mappings





        AiAgent --> "*" Any : related_mappings
        click Any href "../Any/"



      AiAgent : requiredByTask





        AiAgent --> "*" AiTask : requiredByTask
        click AiTask href "../AiTask/"



      AiAgent : requiresCapability





        AiAgent --> "*" Capability : requiresCapability
        click Capability href "../Capability/"



      AiAgent : type

      AiAgent : url


```

## Inheritance

- [Entity](Entity.md)
  - [Entry](Entry.md)
    - [AiSystem](AiSystem.md) [ [BaseAi](BaseAi.md)]
      - **AiAgent**

## Slots

| Name                                              | Cardinality and Range                                                                                        | Description                                                                      | Inheritance                            |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- | -------------------------------------- |
| [isComposedOf](isComposedOf.md)                   | \* <br/> [BaseAi](BaseAi.md)                                                                                 | Relationship indicating the AI components from which a complete AI system is ... | [AiSystem](AiSystem.md)                |
| [hasEuAiSystemType](hasEuAiSystemType.md)         | 0..1 <br/> [AiSystemType](AiSystemType.md)                                                                   | The type of system as defined by the EU AI Act                                   | [AiSystem](AiSystem.md)                |
| [hasEuRiskCategory](hasEuRiskCategory.md)         | 0..1 <br/> [EuAiRiskCategory](EuAiRiskCategory.md)                                                           | The risk category of an AI system as defined by the EU AI Act                    | [AiSystem](AiSystem.md)                |
| [hasCapability](hasCapability.md)                 | \* <br/> [Capability](Capability.md)                                                                         | Indicates the technical capabilities this entry possesses                        | [AiSystem](AiSystem.md)                |
| [isAppliedWithinDomain](isAppliedWithinDomain.md) | \* <br/> [Domain](Domain.md)                                                                                 | Specifies the domain an AI system is used within                                 | [AiSystem](AiSystem.md)                |
| [isUsedWithinLocality](isUsedWithinLocality.md)   | \* <br/> [LocalityOfUse](LocalityOfUse.md)                                                                   | Specifies the domain an AI system is used within                                 | [AiSystem](AiSystem.md)                |
| [hasPurpose](hasPurpose.md)                       | 0..1 <br/> [Purpose](Purpose.md)                                                                             | Indicates the purpose of an entity, e                                            | [AiSystem](AiSystem.md)                |
| [hasStakeholder](hasStakeholder.md)               | 0..1 <br/> [Stakeholder](Stakeholder.md)                                                                     | Indicates stakeholders of an AI system or component                              | [AiSystem](AiSystem.md)                |
| [isDeployedBy](isDeployedBy.md)                   | 0..1 <br/> [AIDeployer](AIDeployer.md)                                                                       | Indicates the deployer of an AI system or component                              | [AiSystem](AiSystem.md)                |
| [isDevelopedBy](isDevelopedBy.md)                 | 0..1 <br/> [AIDeveloper](AIDeveloper.md)                                                                     | Indicates the developer of an AI system or component                             | [AiSystem](AiSystem.md)                |
| [hasAISubject](hasAISubject.md)                   | 0..1 <br/> [AISubject](AISubject.md)                                                                         | Indicates the subjects of an AI system                                           | [AiSystem](AiSystem.md)                |
| [hasAIUser](hasAIUser.md)                         | 0..1 <br/> [String](String.md)                                                                               | Indicate the end-user of an AI system                                            | [AiSystem](AiSystem.md)                |
| [hasRelatedRisk](hasRelatedRisk.md)               | \* <br/> [Risk](Risk.md)&nbsp;or&nbsp;<br />[RiskConcept](RiskConcept.md)&nbsp;or&nbsp;<br />[Term](Term.md) | A relationship where an entity relates to a risk                                 | [AiSystem](AiSystem.md)                |
| [producer](producer.md)                           | 0..1 <br/> [Organization](Organization.md)                                                                   | A relationship to the Organization instance which produces this instance         | [BaseAi](BaseAi.md)                    |
| [hasModelCard](hasModelCard.md)                   | \* <br/> [String](String.md)                                                                                 | A relationship to model card references                                          | [BaseAi](BaseAi.md)                    |
| [hasDocumentation](hasDocumentation.md)           | \* <br/> [Documentation](Documentation.md)                                                                   | Indicates documentation associated with an entity                                | [Entry](Entry.md), [BaseAi](BaseAi.md) |
| [hasLicense](hasLicense.md)                       | 0..1 <br/> [License](License.md)                                                                             | Indicates licenses associated with a resource                                    | [BaseAi](BaseAi.md)                    |
| [performsTask](performsTask.md)                   | \* <br/> [AiTask](AiTask.md)                                                                                 | relationship indicating the AI tasks an AI model can perform                     | [BaseAi](BaseAi.md)                    |
| [isProvidedBy](isProvidedBy.md)                   | 0..1 <br/> [AiProvider](AiProvider.md)                                                                       | A relationship indicating the AI agent has been provided by an AI systems pro... | [BaseAi](BaseAi.md)                    |
| [isDefinedByTaxonomy](isDefinedByTaxonomy.md)     | 0..1 <br/> [Taxonomy](Taxonomy.md)                                                                           | A relationship where a concept or a concept group is defined by a taxonomy       | [Entry](Entry.md)                      |
| [isDefinedByVocabulary](isDefinedByVocabulary.md) | 0..1 <br/> [Vocabulary](Vocabulary.md)                                                                       | A relationship where a term or a term group is defined by a vocabulary           | [Entry](Entry.md)                      |
| [isPartOf](isPartOf.md)                           | 0..1 <br/> [String](String.md)                                                                               | A relationship where an entity is part of another entity                         | [Entry](Entry.md)                      |
| [requiredByTask](requiredByTask.md)               | \* <br/> [AiTask](AiTask.md)                                                                                 | Indicates that this entry is required to perform a specific AI task              | [Entry](Entry.md)                      |
| [requiresCapability](requiresCapability.md)       | \* <br/> [Capability](Capability.md)                                                                         | Indicates that this entry requires a specific capability                         | [Entry](Entry.md)                      |
| [implementedByAdapter](implementedByAdapter.md)   | \* <br/> [Adapter](Adapter.md)                                                                               | Indicates that this capability is implemented by a specific adapter              | [Entry](Entry.md)                      |
| [type](type.md)                                   | 0..1 <br/> [String](String.md)                                                                               | The entry type                                                                   | [Entry](Entry.md)                      |
| [id](id.md)                                       | 1 <br/> [String](String.md)                                                                                  | A unique identifier to this instance of the model element                        | [Entity](Entity.md)                    |
| [name](name.md)                                   | 0..1 <br/> [String](String.md)                                                                               | A text name of this instance                                                     | [Entity](Entity.md)                    |
| [description](description.md)                     | 0..1 <br/> [String](String.md)                                                                               | The description of an entity                                                     | [Entity](Entity.md)                    |
| [url](url.md)                                     | 0..1 <br/> [Uri](Uri.md)                                                                                     | An optional URL associated with this instance                                    | [Entity](Entity.md)                    |
| [dateCreated](dateCreated.md)                     | 0..1 <br/> [Date](Date.md)                                                                                   | The date on which the entity was created                                         | [Entity](Entity.md)                    |
| [dateModified](dateModified.md)                   | 0..1 <br/> [Date](Date.md)                                                                                   | The date on which the entity was most recently modified                          | [Entity](Entity.md)                    |
| [exact_mappings](exact_mappings.md)               | \* <br/> [Any](Any.md)                                                                                       | The property is used to link two concepts, indicating a high degree of confid... | [Entity](Entity.md)                    |
| [close_mappings](close_mappings.md)               | \* <br/> [Any](Any.md)                                                                                       | The property is used to link two concepts that are sufficiently similar that ... | [Entity](Entity.md)                    |
| [related_mappings](related_mappings.md)           | \* <br/> [Any](Any.md)                                                                                       | The property skos:relatedMatch is used to state an associative mapping link b... | [Entity](Entity.md)                    |
| [narrow_mappings](narrow_mappings.md)             | \* <br/> [Any](Any.md)                                                                                       | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md)                    |
| [broad_mappings](broad_mappings.md)               | \* <br/> [Any](Any.md)                                                                                       | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md)                    |
| [isCategorizedAs](isCategorizedAs.md)             | \* <br/> [Any](Any.md)                                                                                       | A relationship where an entity has been deemed to be categorized                 | [Entity](Entity.md)                    |

## Mixin Usage

| mixed into | description |
| ---------- | ----------- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value  |
| ------------ | ------------- |
| self         | nexus:AiAgent |
| native       | nexus:AiAgent |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AiAgent
description: An artificial intelligence (AI) agent refers to a system or program that
  is capable of autonomously performing tasks on behalf of a user or another system
  by designing its workflow and utilizing available tools.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: AiSystem
mixin: true
slot_usage:
  isProvidedBy:
    name: isProvidedBy
    description: A relationship indicating the AI agent has been provided by an AI
      systems provider.

````
</details>

### Induced

<details>
```yaml
name: AiAgent
description: An artificial intelligence (AI) agent refers to a system or program that
  is capable of autonomously performing tasks on behalf of a user or another system
  by designing its workflow and utilizing available tools.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: AiSystem
mixin: true
slot_usage:
  isProvidedBy:
    name: isProvidedBy
    description: A relationship indicating the AI agent has been provided by an AI
      systems provider.
attributes:
  isComposedOf:
    name: isComposedOf
    description: Relationship indicating the AI components from which a complete AI
      system is composed.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: isComposedOf
    owner: AiAgent
    domain_of:
    - AiSystem
    range: BaseAi
    multivalued: true
    inlined: false
  hasEuAiSystemType:
    name: hasEuAiSystemType
    description: The type of system as defined by the EU AI Act.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: hasEuAiSystemType
    owner: AiAgent
    domain_of:
    - AiSystem
    range: AiSystemType
  hasEuRiskCategory:
    name: hasEuRiskCategory
    description: The risk category of an AI system as defined by the EU AI Act.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: hasEuRiskCategory
    owner: AiAgent
    domain_of:
    - AiSystem
    range: EuAiRiskCategory
  hasCapability:
    name: hasCapability
    description: 'Indicates the technical capabilities this entry possesses.

      '
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: tech:hasCapability
    alias: hasCapability
    owner: AiAgent
    domain_of:
    - AiSystem
    - Adapter
    - LLMIntrinsic
    range: Capability
    multivalued: true
    inlined: false
  isAppliedWithinDomain:
    name: isAppliedWithinDomain
    description: Specifies the domain an AI system is used within.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: '[''AISystem'', ''AIComponent'']'
    slot_uri: airo:isAppliedWithinDomain
    alias: isAppliedWithinDomain
    owner: AiAgent
    domain_of:
    - AiSystem
    range: Domain
    multivalued: true
    inlined: false
  isUsedWithinLocality:
    name: isUsedWithinLocality
    description: Specifies the domain an AI system is used within.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: '[''AISystem'', ''AIComponent'']'
    slot_uri: airo:isUsedWithinLocality
    alias: isUsedWithinLocality
    owner: AiAgent
    domain_of:
    - AiSystem
    range: LocalityOfUse
    multivalued: true
    inlined: false
  hasPurpose:
    name: hasPurpose
    description: Indicates the purpose of an entity, e.g. AI system, components.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasPurpose
    alias: hasPurpose
    owner: AiAgent
    domain_of:
    - AiSystem
    range: Purpose
  hasStakeholder:
    name: hasStakeholder
    description: Indicates stakeholders of an AI system or component.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: '[''airo:AISystem'', ''airo:AIComponent'']'
    slot_uri: airo:hasStakeholder
    alias: hasStakeholder
    owner: AiAgent
    domain_of:
    - AiSystem
    range: Stakeholder
  isDeployedBy:
    name: isDeployedBy
    description: Indicates the deployer of an AI system or component.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: '[''AISystem'', ''AIComponent'']'
    slot_uri: airo:isDeployedBy
    alias: isDeployedBy
    owner: AiAgent
    domain_of:
    - AiSystem
    range: AIDeployer
  isDevelopedBy:
    name: isDevelopedBy
    description: Indicates the developer of an AI system or component.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: '[''AISystem'', ''AIComponent'']'
    slot_uri: airo:isDevelopedBy
    alias: isDevelopedBy
    owner: AiAgent
    domain_of:
    - AiSystem
    range: AIDeveloper
  hasAISubject:
    name: hasAISubject
    description: Indicates the subjects of an AI system
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: '[''airo:AISystem'']'
    slot_uri: airo:hasAISubject
    alias: hasAISubject
    owner: AiAgent
    domain_of:
    - AiSystem
    range: AISubject
  hasAIUser:
    name: hasAIUser
    description: Indicate the end-user of an AI system.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: AISystem
    slot_uri: airo:hasAiUser
    alias: hasAIUser
    owner: AiAgent
    domain_of:
    - AiSystem
    range: string
  hasRelatedRisk:
    name: hasRelatedRisk
    description: A relationship where an entity relates to a risk
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: Any
    alias: hasRelatedRisk
    owner: AiAgent
    domain_of:
    - Term
    - LLMQuestionPolicy
    - Action
    - AiSystem
    - AiEval
    - BenchmarkMetadataCard
    - Adapter
    - LLMIntrinsic
    range: Risk
    multivalued: true
    inlined: false
    any_of:
    - range: RiskConcept
    - range: Term
  producer:
    name: producer
    description: A relationship to the Organization instance which produces this instance.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: producer
    owner: AiAgent
    domain_of:
    - BaseAi
    range: Organization
  hasModelCard:
    name: hasModelCard
    description: A relationship to model card references.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: hasModelCard
    owner: AiAgent
    domain_of:
    - BaseAi
    range: string
    multivalued: true
    inlined: true
    inlined_as_list: true
  hasDocumentation:
    name: hasDocumentation
    description: Indicates documentation associated with an entity.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasDocumentation
    alias: hasDocumentation
    owner: AiAgent
    domain_of:
    - Dataset
    - Vocabulary
    - Taxonomy
    - Concept
    - Group
    - Entry
    - Term
    - Principle
    - RiskTaxonomy
    - RiskControlGroupTaxonomy
    - Action
    - BaseAi
    - LargeLanguageModelFamily
    - AiEval
    - BenchmarkMetadataCard
    - Adapter
    - LLMIntrinsic
    range: Documentation
    multivalued: true
    inlined: false
  hasLicense:
    name: hasLicense
    description: Indicates licenses associated with a resource
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasLicense
    alias: hasLicense
    owner: AiAgent
    domain_of:
    - Dataset
    - Documentation
    - Vocabulary
    - Taxonomy
    - RiskTaxonomy
    - RiskControlGroupTaxonomy
    - BaseAi
    - AiEval
    - BenchmarkMetadataCard
    - Adapter
    range: License
  performsTask:
    name: performsTask
    description: relationship indicating the AI tasks an AI model can perform.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: performsTask
    owner: AiAgent
    domain_of:
    - BaseAi
    range: AiTask
    multivalued: true
    inlined: false
  isProvidedBy:
    name: isProvidedBy
    description: A relationship indicating the AI agent has been provided by an AI
      systems provider.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: airo:isProvidedBy
    alias: isProvidedBy
    owner: AiAgent
    domain_of:
    - BaseAi
    range: AiProvider
  isDefinedByTaxonomy:
    name: isDefinedByTaxonomy
    description: A relationship where a concept or a concept group is defined by a
      taxonomy
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isDefinedByTaxonomy
    owner: AiAgent
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
  isDefinedByVocabulary:
    name: isDefinedByVocabulary
    description: A relationship where a term or a term group is defined by a vocabulary
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isDefinedByVocabulary
    owner: AiAgent
    domain_of:
    - Entry
    - Term
    - Adapter
    - LLMIntrinsic
    range: Vocabulary
  isPartOf:
    name: isPartOf
    description: A relationship where an entity is part of another entity
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isPartOf
    owner: AiAgent
    domain_of:
    - Entry
    - Risk
    - LargeLanguageModel
    - Stakeholder
    - CapabilityGroup
    range: string
  requiredByTask:
    name: requiredByTask
    description: Indicates that this entry is required to perform a specific AI task.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: requiredByTask
    owner: AiAgent
    domain_of:
    - Entry
    - Capability
    inverse: requiresCapability
    range: AiTask
    multivalued: true
    inlined: false
  requiresCapability:
    name: requiresCapability
    description: Indicates that this entry requires a specific capability
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: Any
    alias: requiresCapability
    owner: AiAgent
    domain_of:
    - Entry
    - LargeLanguageModel
    - AiTask
    - Adapter
    inverse: requiredByTask
    range: Capability
    multivalued: true
    inlined: false
  implementedByAdapter:
    name: implementedByAdapter
    description: Indicates that this capability is implemented by a specific adapter.
      This relationship distinguishes the abstract capability (what can be done) from
      the technical implementation mechanism (how it is added/extended via adapters).
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: Any
    alias: implementedByAdapter
    owner: AiAgent
    domain_of:
    - Entry
    - Capability
    inverse: implementsCapability
    range: Adapter
    multivalued: true
    inlined: false
  type:
    name: type
    description: The entry type.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/common
    designates_type: true
    alias: type
    owner: AiAgent
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
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: AiAgent
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
    owner: AiAgent
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
    owner: AiAgent
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
    owner: AiAgent
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
    owner: AiAgent
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
    owner: AiAgent
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
    owner: AiAgent
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
    owner: AiAgent
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
    owner: AiAgent
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
    owner: AiAgent
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
    owner: AiAgent
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
    owner: AiAgent
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false

````

</details>
