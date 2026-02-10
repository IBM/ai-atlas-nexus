# Class: Adapter

_Adapter-based methods add extra trainable parameters after the attention and fully-connected layers of a frozen pretrained model to reduce memory-usage and speed up training. The adapters are typically small but demonstrate comparable performance to a fully finetuned model and enable training larger models with fewer resources. (https://huggingface.co/docs/peft/en/conceptual_guides/adapter)_

URI: [nexus:Adapter](https://ibm.github.io/ai-atlas-nexus/ontology/Adapter)

```mermaid
 classDiagram
    class Adapter
    click Adapter href "../Adapter/"
      LargeLanguageModel <|-- Adapter
        click LargeLanguageModel href "../LargeLanguageModel/"
      Entry <|-- Adapter
        click Entry href "../Entry/"

      Adapter : adaptsModel





        Adapter --> "0..1" LargeLanguageModel : adaptsModel
        click LargeLanguageModel href "../LargeLanguageModel/"



      Adapter : architecture

      Adapter : broad_mappings





        Adapter --> "*" Any : broad_mappings
        click Any href "../Any/"



      Adapter : carbon_emitted

      Adapter : close_mappings





        Adapter --> "*" Any : close_mappings
        click Any href "../Any/"



      Adapter : contextWindowSize

      Adapter : dateCreated

      Adapter : dateModified

      Adapter : description

      Adapter : exact_mappings





        Adapter --> "*" Any : exact_mappings
        click Any href "../Any/"



      Adapter : fine_tuning

      Adapter : gpu_hours

      Adapter : hasAdapterType





        Adapter --> "0..1" AdapterType : hasAdapterType
        click AdapterType href "../AdapterType/"



      Adapter : hasCapability





        Adapter --> "*" Capability : hasCapability
        click Capability href "../Capability/"



      Adapter : hasDocumentation





        Adapter --> "*" Documentation : hasDocumentation
        click Documentation href "../Documentation/"



      Adapter : hasEvaluation





        Adapter --> "*" AiEvalResult : hasEvaluation
        click AiEvalResult href "../AiEvalResult/"



      Adapter : hasInputModality





        Adapter --> "*" Modality : hasInputModality
        click Modality href "../Modality/"



      Adapter : hasLicense





        Adapter --> "0..1" License : hasLicense
        click License href "../License/"



      Adapter : hasModelCard

      Adapter : hasOutputModality





        Adapter --> "*" Modality : hasOutputModality
        click Modality href "../Modality/"



      Adapter : hasRelatedRisk





        Adapter --> "*" Risk : hasRelatedRisk
        click Risk href "../Risk/"



      Adapter : hasRiskControl





        Adapter --> "*" RiskControl : hasRiskControl
        click RiskControl href "../RiskControl/"



      Adapter : hasTrainingData





        Adapter --> "*" Dataset : hasTrainingData
        click Dataset href "../Dataset/"



      Adapter : id

      Adapter : implementedByAdapter





        Adapter --> "*" Adapter : implementedByAdapter
        click Adapter href "../Adapter/"



      Adapter : implementsCapability





        Adapter --> "*" Capability : implementsCapability
        click Capability href "../Capability/"



      Adapter : isDefinedByTaxonomy





        Adapter --> "0..1" Taxonomy : isDefinedByTaxonomy
        click Taxonomy href "../Taxonomy/"



      Adapter : isDefinedByVocabulary





        Adapter --> "0..1" Vocabulary : isDefinedByVocabulary
        click Vocabulary href "../Vocabulary/"



      Adapter : isPartOf





        Adapter --> "0..1" LargeLanguageModelFamily : isPartOf
        click LargeLanguageModelFamily href "../LargeLanguageModelFamily/"



      Adapter : isProvidedBy





        Adapter --> "0..1" AiProvider : isProvidedBy
        click AiProvider href "../AiProvider/"



      Adapter : name

      Adapter : narrow_mappings





        Adapter --> "*" Any : narrow_mappings
        click Any href "../Any/"



      Adapter : numParameters

      Adapter : numTrainingTokens

      Adapter : performsTask





        Adapter --> "*" AiTask : performsTask
        click AiTask href "../AiTask/"



      Adapter : power_consumption_w

      Adapter : producer





        Adapter --> "0..1" Organization : producer
        click Organization href "../Organization/"



      Adapter : related_mappings





        Adapter --> "*" Any : related_mappings
        click Any href "../Any/"



      Adapter : requiredByTask





        Adapter --> "*" AiTask : requiredByTask
        click AiTask href "../AiTask/"



      Adapter : requiresCapability





        Adapter --> "*" Capability : requiresCapability
        click Capability href "../Capability/"



      Adapter : supported_languages

      Adapter : type

      Adapter : url


```

## Inheritance

- [Entity](Entity.md)
  - [Entry](Entry.md)
    - **Adapter** [ [LargeLanguageModel](LargeLanguageModel.md)]

## Slots

| Name                                              | Cardinality and Range                                                                                        | Description                                                                      | Inheritance                                                    |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| [hasAdapterType](hasAdapterType.md)               | 0..1 <br/> [AdapterType](AdapterType.md)                                                                     | The Adapter type, for example: LORA, ALORA, X-LORA                               | direct                                                         |
| [isDefinedByVocabulary](isDefinedByVocabulary.md) | 0..1 <br/> [Vocabulary](Vocabulary.md)                                                                       | A relationship where a term or a term group is defined by a vocabulary           | direct                                                         |
| [hasDocumentation](hasDocumentation.md)           | \* <br/> [Documentation](Documentation.md)                                                                   | Indicates documentation associated with an entity                                | direct                                                         |
| [hasLicense](hasLicense.md)                       | 0..1 <br/> [License](License.md)                                                                             | Indicates licenses associated with a resource                                    | direct                                                         |
| [hasRelatedRisk](hasRelatedRisk.md)               | \* <br/> [Risk](Risk.md)&nbsp;or&nbsp;<br />[RiskConcept](RiskConcept.md)&nbsp;or&nbsp;<br />[Term](Term.md) | A relationship where an entity relates to a risk                                 | direct                                                         |
| [adaptsModel](adaptsModel.md)                     | 0..1 <br/> [LargeLanguageModel](LargeLanguageModel.md)                                                       | The LargeLanguageModel being adapted                                             | direct                                                         |
| [implementsCapability](implementsCapability.md)   | \* <br/> [Capability](Capability.md)                                                                         | Indicates that this adapter implements a specific capability                     | direct                                                         |
| [hasCapability](hasCapability.md)                 | \* <br/> [Capability](Capability.md)                                                                         | Indicates the technical capabilities this entry possesses                        | direct                                                         |
| [requiresCapability](requiresCapability.md)       | \* <br/> [Capability](Capability.md)                                                                         | Indicates that this entry requires a specific capability                         | direct                                                         |
| [numParameters](numParameters.md)                 | 0..1 <br/> [Integer](Integer.md)                                                                             | A property indicating the number of parameters in a LLM                          | [LargeLanguageModel](LargeLanguageModel.md)                    |
| [numTrainingTokens](numTrainingTokens.md)         | 0..1 <br/> [Integer](Integer.md)                                                                             | The number of tokens a AI model was trained on                                   | [LargeLanguageModel](LargeLanguageModel.md)                    |
| [contextWindowSize](contextWindowSize.md)         | 0..1 <br/> [Integer](Integer.md)                                                                             | The total length, in bytes, of an AI model's context window                      | [LargeLanguageModel](LargeLanguageModel.md)                    |
| [hasInputModality](hasInputModality.md)           | \* <br/> [Modality](Modality.md)                                                                             | A relationship indicating the input modalities supported by an AI component      | [LargeLanguageModel](LargeLanguageModel.md)                    |
| [hasOutputModality](hasOutputModality.md)         | \* <br/> [Modality](Modality.md)                                                                             | A relationship indicating the output modalities supported by an AI component     | [LargeLanguageModel](LargeLanguageModel.md)                    |
| [hasTrainingData](hasTrainingData.md)             | \* <br/> [Dataset](Dataset.md)                                                                               | A relationship indicating the datasets an AI model was trained on                | [LargeLanguageModel](LargeLanguageModel.md)                    |
| [fine_tuning](fine_tuning.md)                     | 0..1 <br/> [String](String.md)                                                                               | A description of the fine-tuning mechanism(s) applied to a model                 | [LargeLanguageModel](LargeLanguageModel.md)                    |
| [supported_languages](supported_languages.md)     | \* <br/> [String](String.md)                                                                                 | A list of languages, expressed as ISO two letter codes                           | [LargeLanguageModel](LargeLanguageModel.md)                    |
| [isPartOf](isPartOf.md)                           | 0..1 <br/> [LargeLanguageModelFamily](LargeLanguageModelFamily.md)                                           | Annotation that a Large Language model is part of a family of models             | [LargeLanguageModel](LargeLanguageModel.md), [Entry](Entry.md) |
| [isDefinedByTaxonomy](isDefinedByTaxonomy.md)     | 0..1 <br/> [Taxonomy](Taxonomy.md)                                                                           | A relationship where a concept or a concept group is defined by a taxonomy       | [Entry](Entry.md)                                              |
| [requiredByTask](requiredByTask.md)               | \* <br/> [AiTask](AiTask.md)                                                                                 | Indicates that this entry is required to perform a specific AI task              | [Entry](Entry.md)                                              |
| [implementedByAdapter](implementedByAdapter.md)   | \* <br/> [Adapter](Adapter.md)                                                                               | Indicates that this capability is implemented by a specific adapter              | [Entry](Entry.md)                                              |
| [type](type.md)                                   | 0..1 <br/> [String](String.md)                                                                               |                                                                                  | [Entry](Entry.md)                                              |
| [id](id.md)                                       | 1 <br/> [String](String.md)                                                                                  | A unique identifier to this instance of the model element                        | [Entity](Entity.md)                                            |
| [name](name.md)                                   | 0..1 <br/> [String](String.md)                                                                               | A text name of this instance                                                     | [Entity](Entity.md)                                            |
| [description](description.md)                     | 0..1 <br/> [String](String.md)                                                                               | The description of an entity                                                     | [Entity](Entity.md)                                            |
| [url](url.md)                                     | 0..1 <br/> [Uri](Uri.md)                                                                                     | An optional URL associated with this instance                                    | [Entity](Entity.md)                                            |
| [dateCreated](dateCreated.md)                     | 0..1 <br/> [Date](Date.md)                                                                                   | The date on which the entity was created                                         | [Entity](Entity.md)                                            |
| [dateModified](dateModified.md)                   | 0..1 <br/> [Date](Date.md)                                                                                   | The date on which the entity was most recently modified                          | [Entity](Entity.md)                                            |
| [exact_mappings](exact_mappings.md)               | \* <br/> [Any](Any.md)                                                                                       | The property is used to link two concepts, indicating a high degree of confid... | [Entity](Entity.md)                                            |
| [close_mappings](close_mappings.md)               | \* <br/> [Any](Any.md)                                                                                       | The property is used to link two concepts that are sufficiently similar that ... | [Entity](Entity.md)                                            |
| [related_mappings](related_mappings.md)           | \* <br/> [Any](Any.md)                                                                                       | The property skos:relatedMatch is used to state an associative mapping link b... | [Entity](Entity.md)                                            |
| [narrow_mappings](narrow_mappings.md)             | \* <br/> [Any](Any.md)                                                                                       | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md)                                            |
| [broad_mappings](broad_mappings.md)               | \* <br/> [Any](Any.md)                                                                                       | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md)                                            |
| [hasEvaluation](hasEvaluation.md)                 | \* <br/> [AiEvalResult](AiEvalResult.md)                                                                     | A relationship indicating that an entity has an AI evaluation result             | [AiModel](AiModel.md)                                          |
| [architecture](architecture.md)                   | 0..1 <br/> [String](String.md)                                                                               | A description of the architecture of an AI such as 'Decoder-only'                | [AiModel](AiModel.md)                                          |
| [gpu_hours](gpu_hours.md)                         | 0..1 <br/> [Integer](Integer.md)                                                                             | GPU consumption in terms of hours                                                | [AiModel](AiModel.md)                                          |
| [power_consumption_w](power_consumption_w.md)     | 0..1 <br/> [Integer](Integer.md)                                                                             | power consumption in Watts                                                       | [AiModel](AiModel.md)                                          |
| [carbon_emitted](carbon_emitted.md)               | 0..1 <br/> [Float](Float.md)                                                                                 | The number of tons of carbon dioxide equivalent that are emitted during train... | [AiModel](AiModel.md)                                          |
| [hasRiskControl](hasRiskControl.md)               | \* <br/> [RiskControl](RiskControl.md)                                                                       | Indicates the control measures associated with a system or component to modif... | [AiModel](AiModel.md)                                          |
| [producer](producer.md)                           | 0..1 <br/> [Organization](Organization.md)                                                                   | A relationship to the Organization instance which produces this instance         | [BaseAi](BaseAi.md)                                            |
| [hasModelCard](hasModelCard.md)                   | \* <br/> [String](String.md)                                                                                 | A relationship to model card references                                          | [BaseAi](BaseAi.md)                                            |
| [performsTask](performsTask.md)                   | \* <br/> [AiTask](AiTask.md)                                                                                 | relationship indicating the AI tasks an AI model can perform                     | [BaseAi](BaseAi.md)                                            |
| [isProvidedBy](isProvidedBy.md)                   | 0..1 <br/> [AiProvider](AiProvider.md)                                                                       | A relationship indicating the AI model has been provided by an AI model provi... | [BaseAi](BaseAi.md)                                            |

## Usages

| used by                         | used in                                         | type  | used                  |
| ------------------------------- | ----------------------------------------------- | ----- | --------------------- |
| [Container](Container.md)       | [adapters](adapters.md)                         | range | [Adapter](Adapter.md) |
| [Entry](Entry.md)               | [implementedByAdapter](implementedByAdapter.md) | range | [Adapter](Adapter.md) |
| [Term](Term.md)                 | [implementedByAdapter](implementedByAdapter.md) | range | [Adapter](Adapter.md) |
| [Principle](Principle.md)       | [implementedByAdapter](implementedByAdapter.md) | range | [Adapter](Adapter.md) |
| [Risk](Risk.md)                 | [implementedByAdapter](implementedByAdapter.md) | range | [Adapter](Adapter.md) |
| [AiTask](AiTask.md)             | [implementedByAdapter](implementedByAdapter.md) | range | [Adapter](Adapter.md) |
| [Capability](Capability.md)     | [implementedByAdapter](implementedByAdapter.md) | range | [Adapter](Adapter.md) |
| [Adapter](Adapter.md)           | [implementedByAdapter](implementedByAdapter.md) | range | [Adapter](Adapter.md) |
| [LLMIntrinsic](LLMIntrinsic.md) | [hasAdapter](hasAdapter.md)                     | range | [Adapter](Adapter.md) |
| [LLMIntrinsic](LLMIntrinsic.md) | [implementedByAdapter](implementedByAdapter.md) | range | [Adapter](Adapter.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value  |
| ------------ | ------------- |
| self         | nexus:Adapter |
| native       | nexus:Adapter |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Adapter
description: Adapter-based methods add extra trainable parameters after the attention
  and fully-connected layers of a frozen pretrained model to reduce memory-usage and
  speed up training. The adapters are typically small but demonstrate comparable performance
  to a fully finetuned model and enable training larger models with fewer resources.
  (https://huggingface.co/docs/peft/en/conceptual_guides/adapter)
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Entry
mixins:
- LargeLanguageModel
slots:
- hasAdapterType
- isDefinedByVocabulary
- hasDocumentation
- hasLicense
- hasRelatedRisk
- adaptsModel
- implementsCapability
- hasCapability
- requiresCapability

````
</details>

### Induced

<details>
```yaml
name: Adapter
description: Adapter-based methods add extra trainable parameters after the attention
  and fully-connected layers of a frozen pretrained model to reduce memory-usage and
  speed up training. The adapters are typically small but demonstrate comparable performance
  to a fully finetuned model and enable training larger models with fewer resources.
  (https://huggingface.co/docs/peft/en/conceptual_guides/adapter)
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Entry
mixins:
- LargeLanguageModel
attributes:
  hasAdapterType:
    name: hasAdapterType
    description: 'The Adapter type, for example: LORA, ALORA, X-LORA'
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: hasAdapterType
    owner: Adapter
    domain_of:
    - Adapter
    range: AdapterType
  isDefinedByVocabulary:
    name: isDefinedByVocabulary
    description: A relationship where a term or a term group is defined by a vocabulary
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isDefinedByVocabulary
    owner: Adapter
    domain_of:
    - Entry
    - Term
    - Adapter
    - LLMIntrinsic
    range: Vocabulary
  hasDocumentation:
    name: hasDocumentation
    description: Indicates documentation associated with an entity.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasDocumentation
    alias: hasDocumentation
    owner: Adapter
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
    owner: Adapter
    domain_of:
    - Dataset
    - Documentation
    - Vocabulary
    - Taxonomy
    - RiskTaxonomy
    - BaseAi
    - AiEval
    - BenchmarkMetadataCard
    - Adapter
    range: License
  hasRelatedRisk:
    name: hasRelatedRisk
    description: A relationship where an entity relates to a risk
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: Any
    alias: hasRelatedRisk
    owner: Adapter
    domain_of:
    - Term
    - LLMQuestionPolicy
    - Action
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
  adaptsModel:
    name: adaptsModel
    description: The LargeLanguageModel being adapted
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: adaptsModel
    owner: Adapter
    domain_of:
    - Adapter
    range: LargeLanguageModel
  implementsCapability:
    name: implementsCapability
    description: Indicates that this adapter implements a specific capability
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: Any
    alias: implementsCapability
    owner: Adapter
    domain_of:
    - Adapter
    inverse: implementedByAdapter
    range: Capability
    multivalued: true
    inlined: false
  hasCapability:
    name: hasCapability
    description: 'Indicates the technical capabilities this entry possesses.

      '
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: tech:hasCapability
    alias: hasCapability
    owner: Adapter
    domain_of:
    - AiSystem
    - Adapter
    - LLMIntrinsic
    range: Capability
    multivalued: true
    inlined: false
  requiresCapability:
    name: requiresCapability
    description: Indicates that this entry requires a specific capability
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: Any
    alias: requiresCapability
    owner: Adapter
    domain_of:
    - Entry
    - LargeLanguageModel
    - AiTask
    - Adapter
    inverse: requiredByTask
    range: Capability
    multivalued: true
    inlined: false
  numParameters:
    name: numParameters
    description: A property indicating the number of parameters in a LLM.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: numParameters
    owner: Adapter
    domain_of:
    - LargeLanguageModel
    range: integer
    minimum_value: 0
  numTrainingTokens:
    name: numTrainingTokens
    description: The number of tokens a AI model was trained on.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: numTrainingTokens
    owner: Adapter
    domain_of:
    - LargeLanguageModel
    range: integer
    minimum_value: 0
  contextWindowSize:
    name: contextWindowSize
    description: The total length, in bytes, of an AI model's context window.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: contextWindowSize
    owner: Adapter
    domain_of:
    - LargeLanguageModel
    range: integer
    minimum_value: 0
  hasInputModality:
    name: hasInputModality
    description: A relationship indicating the input modalities supported by an AI
      component. Examples include text, image, video.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: hasInputModality
    owner: Adapter
    domain_of:
    - LargeLanguageModel
    range: Modality
    multivalued: true
    inlined: false
  hasOutputModality:
    name: hasOutputModality
    description: A relationship indicating the output modalities supported by an AI
      component. Examples include text, image, video.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: hasOutputModality
    owner: Adapter
    domain_of:
    - LargeLanguageModel
    range: Modality
    multivalued: true
    inlined: false
  hasTrainingData:
    name: hasTrainingData
    description: A relationship indicating the datasets an AI model was trained on.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasTrainingData
    alias: hasTrainingData
    owner: Adapter
    domain_of:
    - LargeLanguageModel
    range: Dataset
    multivalued: true
    inlined: false
  fine_tuning:
    name: fine_tuning
    description: A description of the fine-tuning mechanism(s) applied to a model.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: fine_tuning
    owner: Adapter
    domain_of:
    - LargeLanguageModel
    range: string
  supported_languages:
    name: supported_languages
    description: A list of languages, expressed as ISO two letter codes. For example,
      'jp, fr, en, de'
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: supported_languages
    owner: Adapter
    domain_of:
    - LargeLanguageModel
    range: string
    multivalued: true
    inlined: true
    inlined_as_list: true
  isPartOf:
    name: isPartOf
    description: Annotation that a Large Language model is part of a family of models
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isPartOf
    owner: Adapter
    domain_of:
    - Entry
    - Risk
    - LargeLanguageModel
    - CapabilityGroup
    - Stakeholder
    range: LargeLanguageModelFamily
  isDefinedByTaxonomy:
    name: isDefinedByTaxonomy
    description: A relationship where a concept or a concept group is defined by a
      taxonomy
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isDefinedByTaxonomy
    owner: Adapter
    domain_of:
    - Concept
    - Control
    - Group
    - Entry
    - Policy
    - RiskGroup
    - Risk
    - RiskControl
    - Action
    - RiskIncident
    - CapabilityGroup
    - StakeholderGroup
    - Stakeholder
    range: Taxonomy
  requiredByTask:
    name: requiredByTask
    description: Indicates that this entry is required to perform a specific AI task.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: requiredByTask
    owner: Adapter
    domain_of:
    - Entry
    - Capability
    inverse: requiresCapability
    range: AiTask
    multivalued: true
    inlined: false
  implementedByAdapter:
    name: implementedByAdapter
    description: 'Indicates that this capability is implemented by a specific adapter.
      This relationship distinguishes the abstract capability (what can be done) from
      the technical implementation mechanism (how it is added/extended via adapters).

      '
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: Any
    alias: implementedByAdapter
    owner: Adapter
    domain_of:
    - Entry
    - Capability
    inverse: implementsCapability
    range: Adapter
    multivalued: true
    inlined: false
  type:
    name: type
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/common
    designates_type: true
    alias: type
    owner: Adapter
    domain_of:
    - Vocabulary
    - Taxonomy
    - Concept
    - Control
    - Group
    - Entry
    - Policy
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
    owner: Adapter
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
    owner: Adapter
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
    owner: Adapter
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
    owner: Adapter
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
    owner: Adapter
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
    owner: Adapter
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
    owner: Adapter
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
    owner: Adapter
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
    owner: Adapter
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
    owner: Adapter
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
    owner: Adapter
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  hasEvaluation:
    name: hasEvaluation
    description: A relationship indicating that an entity has an AI evaluation result.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: dqv:hasQualityMeasurement
    alias: hasEvaluation
    owner: Adapter
    domain_of:
    - AiModel
    range: AiEvalResult
    multivalued: true
  architecture:
    name: architecture
    description: A description of the architecture of an AI such as 'Decoder-only'.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: architecture
    owner: Adapter
    domain_of:
    - AiModel
    range: string
  gpu_hours:
    name: gpu_hours
    description: GPU consumption in terms of hours
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: gpu_hours
    owner: Adapter
    domain_of:
    - AiModel
    range: integer
    minimum_value: 0
  power_consumption_w:
    name: power_consumption_w
    description: power consumption in Watts
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: power_consumption_w
    owner: Adapter
    domain_of:
    - AiModel
    range: integer
    minimum_value: 0
  carbon_emitted:
    name: carbon_emitted
    description: The number of tons of carbon dioxide equivalent that are emitted
      during training
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: carbon_emitted
    owner: Adapter
    domain_of:
    - AiModel
    range: float
    minimum_value: 0
    unit:
      symbol: t CO2-eq
      descriptive_name: tons of CO2 equivalent
  hasRiskControl:
    name: hasRiskControl
    description: Indicates the control measures associated with a system or component
      to modify risks.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasRiskControl
    alias: hasRiskControl
    owner: Adapter
    domain_of:
    - AiModel
    range: RiskControl
    multivalued: true
  producer:
    name: producer
    description: A relationship to the Organization instance which produces this instance.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: producer
    owner: Adapter
    domain_of:
    - BaseAi
    range: Organization
  hasModelCard:
    name: hasModelCard
    description: A relationship to model card references.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: hasModelCard
    owner: Adapter
    domain_of:
    - BaseAi
    range: string
    multivalued: true
    inlined: true
    inlined_as_list: true
  performsTask:
    name: performsTask
    description: relationship indicating the AI tasks an AI model can perform.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: performsTask
    owner: Adapter
    domain_of:
    - BaseAi
    range: AiTask
    multivalued: true
    inlined: false
  isProvidedBy:
    name: isProvidedBy
    description: A relationship indicating the AI model has been provided by an AI
      model provider.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: airo:isProvidedBy
    alias: isProvidedBy
    owner: Adapter
    domain_of:
    - BaseAi
    range: AiProvider

````

</details>
