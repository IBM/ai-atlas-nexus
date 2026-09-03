---
type: Dataset
id: https://w3id.org/ai-atlas-nexus/knowledge/datasets/ai-risk-ontology
title: AI Risk Ontology (LinkML schema)
description: The LinkML schema combining the AI risk view (taxonomies, risks, actions) with an AI model view (AI systems, AI models, model evaluations) into one coherent ontology.
version: "0.5.0"
license: https://www.apache.org/licenses/LICENSE-2.0.html
resource: https://github.com/IBM/ai-atlas-nexus/tree/main/src/ai_atlas_nexus/ai_risk_ontology/schema
generated:
  by: process:lokf-librarian
  at: "2026-09-02T16:11:53Z"
distribution:
  - access_url: https://github.com/IBM/ai-atlas-nexus/tree/main/src/ai_atlas_nexus/ai_risk_ontology/schema
    name: LinkML schema sources (YAML)
    media_type: application/yaml
  - access_url: https://github.com/IBM/ai-atlas-nexus/blob/main/graph_export/owl/ai-risk-ontology_schema.ttl
    name: OWL schema export (Turtle)
    media_type: text/turtle
  - access_url: https://ibm.github.io/ai-atlas-nexus/ontology/
    name: Rendered schema documentation
    media_type: text/html
dependsOn:
  - https://w3id.org/ai-atlas-nexus/knowledge/references/linkml
derivedFrom:
  - https://w3id.org/ai-atlas-nexus/knowledge/references/eu-ai-act
---

# Overview

The **AI Risk Ontology** is authored as modular LinkML YAML under `src/ai_atlas_nexus/ai_risk_ontology/schema/`, version `0.5.0`, rooted at `ai-risk-ontology.yaml`. That root imports `common.yaml`, `ai_risk.yaml`, `ai_capability.yaml`, `ai_system.yaml`, `ai_eval.yaml`, `ai_intrinsic.yaml`, and `ai_aiuc.yaml`; `ai_system.yaml` in turn imports `energy.yaml` and the EU AI Act vocabulary `eu_ai_act.yaml`, so both are in the root's transitive import closure. `semweb_context.yaml` is not imported - every module names it in `default_curi_maps` as the shared CURIE map.

Schema modules mint their identifiers in the project's `https://w3id.org/ai-atlas-nexus/` namespace (`nexus` prefix) and align with external vocabularies such as AIRO, DPV, and SKOS. Pydantic datamodel classes under `ai_risk_ontology/datamodel/` are generated from the schema via the repository `Makefile` (`make compile_pydantic_model`).
