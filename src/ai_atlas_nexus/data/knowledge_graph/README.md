## A knowledge graph represented as LinkML instance data

This folder contains YAML files with data about concrete instances of the AI risk ontology.
Some of these files have been generated using some tooling as described in the [src\ai_atlas_nexus\ai_risk_ontology\util](../../ai_risk_ontology/util/README.md) folder.

For more information about LinkML data instances see [the LinkML documentation](https://linkml.io/linkml/intro/tutorial01.html#creating-and-validating-data).

- `ai_commons_data.yaml`: Some basic common definitions like licenses, modalities or AI tasks that are used by AI models and AI risks alike

### Risk taxonomies

- `risk_atlas_data.yaml`: The IBM risk atlas taxonomy
- `granite_guardian_dimensions.yaml`: Risk dimensions as covered by the IBM Granite Guardian models
- `nist_ai_rmf_data.yaml`: The NIST AI Risk Management Framework risk taxonomy
- `nist_ai_rmf_actions_data.yaml`: The NIST AI Risk Management Framework risk related actions
- `owasp_llm_2.0_data.yaml`: The OWASP Top 10 for Large Language Model Applications version 2 risk definitions
- `mit_ai_risk_repository_data.yaml`: The MIT AI Risk Repository risk taxonomy
- `ailuminate.yaml`: The AILuminate benchmark risk taxonomy
- `credo.yaml`: the Unified Control Framework from Credo

### Risk mappings

- `ibm2owasp_data.yaml`: Mapping from IBM Risk Atlas risks to OWASP Top 10 for Large Language Model Applications version 2 risks
- `ibm2nistgenai_data.yaml`: Mapping from IBM Risk Atlas risks to the NIST AI Risk Management Framework risks

### AI models

- `datasets.yaml`: A collection of datasets that are used for AI model training
- `ai_eval_data.yaml`: A collection of AI model evaluation methods, e.g. to evaluate the toxicity of an AI model
- `ibm_granite_3_instruct_data.yaml`: A collection of IBM Granite 3.0 instruct models including results of some model evaluations performed
