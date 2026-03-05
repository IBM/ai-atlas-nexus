## A knowledge graph represented as LinkML instance data

This folder contains YAML files with data about concrete instances of the AI risk ontology.
Some of these files have been generated using some tooling as described in the [src\ai_atlas_nexus\ai_risk_ontology\util](../../ai_risk_ontology/util/README.md) folder.

For more information about LinkML data instances see [the LinkML documentation](https://linkml.io/linkml/intro/tutorial01.html#creating-and-validating-data).

- `ai_commons_data.yaml`: Some basic common definitions like licenses, modalities or AI tasks that are used by AI models and AI risks alike

### Resources

| File name                                   | Type                   | Description                                                                                           |
| ------------------------------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------- |
| `risk_atlas_data.yaml`                      | RiskTaxonomy           | The IBM risk atlas taxonomy                                                                           |
| `granite_guardian_dimensions.yaml`          | RiskTaxonomy           | Risk dimensions as covered by the IBM Granite Guardian models                                         |
| `nist_ai_rmf_data.yaml`                     | RiskTaxonomy           | The NIST AI Risk Management Framework risk taxonomy                                                   |
| `nist_ai_rmf_actions_data.yaml`             | Actions                | The NIST AI Risk Management Framework risk related actions                                            |
| `owasp_llm_2.0_data.yaml`                   | RiskTaxonomy           | The OWASP Top 10 for Large Language Model Applications version 2 risk definitions.                    |
| `mit_ai_risk_repository_data.yaml`          | RiskTaxonomy           | The MIT AI Risk Repository risk taxonomy                                                              |
| `ailuminate.yaml`                           | RiskTaxonomy           | The AILuminate benchmark risk taxonomy                                                                |
| `credo.yaml`                                | RiskTaxonomy           | the Unified Control Framework from Credo                                                              |
| `shieldgemma_dimensions.yaml`               | RiskTaxonomy           | ShieldGemma Safety Categories for content moderation                                                  |
| `shieldgemma_models.yaml`                   | AiModels               | ShieldGemma AI Models                                                                                 |
| `ibm_capabilities_data.yaml`                | AICapabilitiesTaxonomy | The IBM risk atlas taxonomy                                                                           |
| `principles_australia.yaml`                 | Principles             | Australia's AI Ethics Principles                                                                      |
| `principles_un.yaml`                        | Principles             | Principles for the ethical use of artificial intelligence in the United Nations system                |
| `principles_oecd.yaml`                      | Principles             | OECD AI Principles                                                                                    |
| `principles_ibm_trust.yaml`                 | Principles             | IBM's Principles for Trust and Transparency                                                           |
| `mit_ai_risk_mitigation_data.yaml`          | RiskControlTaxonomy    | MIT AI Risk Mitigation Taxonomy                                                                       |
| `mit_ai_risk_repository_data_controls.yaml` | RiskControls           | Controls categorised by MIT AI Risk Mitigation Taxonomy                                               |
| `datasets.yaml`                             | Datasets               | A collection of datasets that are used for AI model training                                          |
| `ai_eval_data.yaml`                         | AIEvals                | A collection of AI model evaluation methods, e.g. to evaluate the toxicity of an AI model             |
| `ibm_granite_3_instruct_data.yaml`          | AIModels               | A collection of IBM Granite 3.0 instruct models including results of some model evaluations performed |
