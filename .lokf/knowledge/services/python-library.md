---
type: Service
id: https://w3id.org/ai-atlas-nexus/knowledge/services/python-library
title: AI Atlas Nexus Python Library
description: The ai-atlas-nexus Python library, whose AIAtlasNexus class exposes methods to explore AI risks, relations and actions, detect potential risks in a use case, and query the knowledge graph.
documentation: https://ibm.github.io/ai-atlas-nexus/
resource: https://github.com/IBM/ai-atlas-nexus/tree/main/src/ai_atlas_nexus
generated:
  by: process:lokf-librarian
  at: "2026-09-02T15:57:00Z"
dependsOn:
  - https://w3id.org/ai-atlas-nexus/knowledge/datasets/ai-risk-ontology
  - https://w3id.org/ai-atlas-nexus/knowledge/datasets/knowledge-graph
  - https://w3id.org/ai-atlas-nexus/knowledge/references/linkml
---

# Overview

The **AI Atlas Nexus Python library** (`ai-atlas-nexus` on PyPI, package `ai_atlas_nexus`) is the project's main deliverable. Its entry point is the `AIAtlasNexus` class in `src/ai_atlas_nexus/library.py`, which loads the AI Risk Ontology and its knowledge-graph instance data and exposes methods for risk exploration, risk identification from use-case descriptions, AI task/domain identification, auto-assisted compliance questionnaires (Chain of Thought), crosswalk generation between taxonomies, and SHACL-based graph validation.

Functional building blocks live under `src/ai_atlas_nexus/blocks/`: `graph_explorer` (including a Pyoxigraph explorer), `risk_detector`, `risk_explorer`, `risk_categorization`, `risk_mapping`, `shacl`, `hf_data_loader`, prompt building, and an `inference` package with engines for IBM watsonx.ai (WML), Ollama, vLLM, RITS, OpenAI-compatible servers, and Hugging Face.

Requires Python `>=3.11, <3.14.4` (see `pyproject.toml`). LLM inference backends are optional extras: `[wml]`, `[ollama]`, `[vllm]`.
