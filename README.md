# AI Atlas Nexus

<img src="https://github.com/IBM/ai-atlas-nexus/blob/main/resources/images/ai_atlas_nexus_vector.svg?raw=true" width="200">

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](https://www.apache.org/licenses/LICENSE-2.0) ![main branch](https://github.com/IBM/ai-atlas-nexus/actions/workflows/pages/pages-build-deployment/badge.svg?branch=main) [![](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/) <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

👉 (Jun-2025) The [demo projects repository](https://github.com/IBM/ai-atlas-nexus-demos) showcases implementations of AI Atlas Nexus.

## Overview

AI Atlas Nexus provides tooling to bring together resources related to governance of foundation models. We support a community-driven approach to curating and cataloguing resources such as datasets, benchmarks and mitigations. Our goal is to turn abstract risk definitions into actionable workflows that streamline AI governance processes. By connecting fragmented resources, AI Atlas Nexus seeks to fill a critical gap in AI governance, enabling stakeholders to build more robust, transparent, and accountable systems. AI Atlas Nexus builds on the [IBM AI Risk Atlas](https://www.ibm.com/docs/en/watsonx/saas?topic=ai-risk-atlas) making this educational resource a nexus of governance assets and tooling. A knowledge graph of an AI system is used to provide a unified structure that links and contextualizes the very heterogeneous domain data.

Our intention is to create a starting point for an open AI Systems ontology whose focus is on risk and that the community can extend and enhance. This ontology serves as the foundation that unifies innovation and tooling in the AI risk space. By lowering the barrier to entry for developers, it fosters a governance-first approach to AI solutions, while also inviting the broader community to contribute their own tools and methodologies to expand its impact.

## Features

- 🏗️ An ontology that combines the AI risk view (taxonomies, risks, actions) with an AI model view (AI systems, AI models, model evaluations) into one coherent schema
- 📚 AI Risks collected from IBM AI Risk Atlas, IBM Granite Guardian, MIT AI Risk Repository, NIST Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile, the AI Risk Taxonomy (AIR 2024), the AILuminate Benchmark, Credo's Unified Control Framework, and OWASP Top 10 for Large Language Model Applications
- 🔗 Mappings are proposed between the taxonomies and between risks and actions
- 🐍 Use the python library methods to quickly explore available risks, relations and actions
- 🚨 Use the python library methods to detect potential risks in your usecase
- 📤 Download an exported graph populated with data instances
- ✨ Example use-case of auto-assistance in compliance questionnaires using CoT examples and AI Atlas Nexus
- 🔧 Tooling to convert the LinkML schema and instance data into a Cypher representation to populate a graph database

## Architecture

![Architecture](https://github.com/IBM/ai-atlas-nexus/blob/main/resources/images/architecture.png?raw=true)

## Links

- **AI Risk Ontology**
  - [LinkML schema documentation](docs/ontology/index.md)
  - [LinkML instance data for an example knowledge graph](https://github.com/IBM/ai-atlas-nexus/blob/main/src/ai_atlas_nexus/data/knowledge_graph/README.md)
  - [Download a populated graph](https://github.com/IBM/ai-atlas-nexus/blob/main/graph_export/README.md)
  - [Contribute your own taxonomy files and CoT templates](docs/concepts/Contributing_a_taxonomy.md)
- **Notebooks:**
  - [AI Atlas Nexus Quickstart](docs/examples/notebooks/AI_Atlas_Nexus_Quickstart.ipynb) Overview of library functionality
  - [Risk identification](docs/examples/notebooks/risk_identification.ipynb) Uncover risks related to your usecase
  - [Auto assist questionnaire](docs/examples/notebooks/autoassist_questionnaire.ipynb) Auto-fill questionnaire using Chain of Thought or Few-Shot Examples
  - [AI Tasks identification](docs/examples/notebooks/ai_tasks_identification.ipynb) Uncover ai tasks related to your usecase
  - [AI Domain identification](docs/examples/notebooks/domain_identification.ipynb) Uncover ai domain from your usecase
  - [Risk Categorization](docs/examples/notebooks/risk_categorization.ipynb) Assess and categorize the severity of risks associated with an AI system usecase. Prompt templates are used with thanks to https://doi.org/10.48550/arXiv.2407.12454.
  - [Crosswalk](docs/examples/notebooks/generate_crosswalk.ipynb) An example of generating crosswalk information between risks of two different taxonomies.
  - [Risk to ARES Evaluation](docs/examples/notebooks/risk_to_ares_evaluation.ipynb) ARES Integration for AI Atlas Nexus allows you to run AI robustness evaluations on AI Systems derived from use cases.
- **Additional Resources:**
  - [Demonstrations](https://github.com/IBM/ai-atlas-nexus-demos) A repo containing some demo applications using ai-atlas-nexus.
  - [Extensions](https://github.com/IBM/ai-atlas-nexus-extensions) A repo containing extensions and a cookie cutter template to create new open source ai-atlas-nexus extensions.
  - [IBM AI Risk Atlas](https://www.ibm.com/docs/en/watsonx/saas?topic=ai-risk-atlas)
  - [Usage Governance Advisor: From Intent to AI Governance](https://arxiv.org/abs/2412.01957)

## Installation

This project targets python version ">=3.11, <3.12". You can download specific versions of python here: https://www.python.org/downloads/

**Note:** Replace `INFERENCE_LIB` with one of the LLM inference library [ollama, vllm, wml, rits] as explained [here](#install-for-inference-apis)

To install the current release

```
pip install "ai-atlas-nexus[INFERENCE_LIB]"
```

To install the latest code

```
git clone git@github.com:IBM/ai-atlas-nexus.git
cd ai-atlas-nexus
python -m venv v-ai-atlas-nexus
source v-ai-atlas-nexus/bin/activate
pip install -e ".[INFERENCE_LIB]"
```

### Install for inference APIs

AI Atlas Nexus uses Large Language Models (LLMs) to infer risks and risks data. Therefore, requires access to LLMs to inference or call the model. The following LLM inference APIs are supported:

- [IBM Watsonx AI](https://www.ibm.com/products/watsonx-ai) (Watson Machine Learning)
- [Ollama](https://ollama.com/)
- [vLLM](https://docs.vllm.ai/en/latest/)
- [RITS](https://rits.fmaas.res.ibm.com) (IBM Internal Only)

#### IBM Watsonx AI (WML)

When using the WML platform, you need to:

1. Add configuration to `.env` file as follows. Please follow this [documentation](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-credentials.html?context=wx&locale=en) on obtaining WML credentials.

```yaml
WML_API_KEY=<WML api key goes here>
WML_API_URL=<WML url key goes here>
WML_PROJECT_ID=<WML project id goes here, Optional>
WML_SPACE_ID=<WML space id goes here, Optional>
```

Either 'WML_PROJECT_ID' or 'WML_SPACE_ID' need to be specified.

2. Install WML dependencies as follows:

```command
pip install -e ".[wml]"
```

#### Ollama

When using the Ollama inference, you need to:

1. Install Ollama dependencies as follows:

```command
pip install -e ".[ollama]"
```

2. Please follow the [quickstart](https://github.com/ollama/ollama/blob/main/README.md#ollama) guide to start Ollama LLM server. Server will start by default at http://localhost:11434

3. When selecting Ollama engine in AI Atlas Nexus, use the server address `localhost:11434` as the `api_url` in the credentials or set the environment variable `OLLAMA_API_URL` with this value.

#### vLLM

When using the vLLM inference, you need to:

1. For Mac users, follow the instuctions [here](https://docs.vllm.ai/en/stable/getting_started/installation/cpu/index.html?device=apple). Users need to build from the source vLLM to natively run on macOS.

2. For Linux users, install vLLM dependencies as follows:

```command
pip install -e ".[vllm]"
```

Above package is enough to run vLLM in once-off offline mode. When selecting vLLM execution from AI Atlas Nexus, `credentials` should be passed as `None` to use vLLM offline mode.

3. (Optional) To run vLLM on an OpenAI-Compatible vLLM Server, execute the command:

```command
vllm serve ibm-granite/granite-3.1-8b-instruct --max_model_len 4096 --host localhost --port 8000 --api-key <CUSTOM_API_KEY>
```

The CUSTOM_API_KEY can be any string that you choose to use as your API key. Above command will start vLLM server at http://localhost:8000. The server currently hosts one model at a time. Check all supported APIs at `http://localhost:8000/docs`

**Note:** When selecting vLLM engine in AI Atlas Nexus, pass `api_url` as `host:port` and given `api_key` to `credentials` with values from the vllm serve command above.

#### RITS (IBM Internal Only)

When using the RITS platform, you need to:

1. Add configuration to `.env` file as follows:

```yaml
RITS_API_KEY=<RITS api key goes here>
RITS_API_URL=<RITS url key goes here>
```

2. Install RITS dependencies as follows:

```command
pip install -e ".[rits]"
```

## AI Atlas Nexus Extensions

Install AI Atlas Nexus extension using the below command

```command
ran-extension install <EXTENSION_NAME>
```

Currently, following extensions are available

- [ran-ares-integration](https://github.com/ibm/ai-atlas-nexus-extensions/tree/main/ran-ares-integration): ARES Integration for AI Atlas Nexus to run AI robustness evaluations on AI Systems derived from use cases.

## Compatibility

- View the [releases changelog](https://github.com/IBM/ai-atlas-nexus/releases).

## Referencing the project

If you use AI Atlas Nexus in your projects, please consider citing the following:

```bib
@article{airiskatlas2025,
      title={AI Risk Atlas: Taxonomy and Tooling for Navigating AI Risks and Resources},
      author={Frank Bagehorn and Kristina Brimijoin and Elizabeth M. Daly and Jessica He and Michael Hind and Luis Garces-Erice and Christopher Giblin and Ioana Giurgiu and Jacquelyn Martino and Rahul Nair and David Piorkowski and Ambrish Rawat and John Richards and Sean Rooney and Dhaval Salwala and Seshu Tirupathi and Peter Urbanetz and Kush R. Varshney and Inge Vejsbjerg and Mira L. Wolf-Bauwens},
      year={2025},
      eprint={2503.05780},
      archivePrefix={arXiv},
      primaryClass={cs.CY},
      url={https://arxiv.org/abs/2503.05780}
}
```

## License

AI Atlas Nexus is provided under Apache 2.0 license.

## Contributing

- Get started by checking our [contribution guidelines](CONTRIBUTING.md).
- Read the wiki for more technical and design details.
- If you have any questions, just ask!
- [Contribute your own taxonomy files and CoT templates](docs/concepts/Contributing_a_taxonomy.md)

Tip: Use the makefile provided to regenerate artifacts provided in the repository by running `make` in this repository.

## Find out more

- Try out a quick demo at the [HF spaces demo site](https://huggingface.co/spaces/ibm/risk-atlas-nexus)
- Read the publication [AI Risk Atlas: Taxonomy and Tooling for Navigating AI Risks and Resources](https://arxiv.org/pdf/2503.05780)
- Explore [IBM's AI Risk Atlas](https://www.ibm.com/docs/en/watsonx/saas?topic=ai-risk-atlas) on the IBM documentation site
- View the [demo projects repository](https://github.com/IBM/ai-atlas-nexus-demos) showcasing implementations of AI Atlas Nexus.
- Read the the IBM AI Ethics Board publication [Foundation models: Opportunities, risks and mitigations](https://www.ibm.com/downloads/documents/us-en/10a99803d8afd656) which goes into more detail about the risk taxonomy, and describes the point of view of IBM on the ethics of foundation models.
- ['Usage Governance Advisor: From Intent to AI Governance'](https://arxiv.org/abs/2412.01957) presents a system for semi-structured governance information, identifying and prioritising risks according to the intended use case, recommending appropriate benchmarks and risk assessments and proposing mitigation strategies and actions.

## IBM ❤️ Open Source AI

AI Atlas Nexus has been brought to you by IBM.
