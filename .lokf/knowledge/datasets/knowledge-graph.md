---
type: Dataset
id: https://w3id.org/ai-atlas-nexus/knowledge/datasets/knowledge-graph
title: AI Risk Knowledge Graph (LinkML instance data)
description: YAML instance data populating the AI Risk Ontology with risk taxonomies, risks, actions, controls, principles, AI models, evaluations, and datasets curated from public sources.
resource: https://github.com/IBM/ai-atlas-nexus/tree/main/src/ai_atlas_nexus/data/knowledge_graph
generated:
  by: process:lokf-librarian
  at: "2026-09-02T15:57:00Z"
distribution:
  - access_url: https://github.com/IBM/ai-atlas-nexus/tree/main/src/ai_atlas_nexus/data/knowledge_graph
    name: LinkML instance data (YAML files)
    media_type: application/yaml
dependsOn:
  - https://w3id.org/ai-atlas-nexus/knowledge/datasets/ai-risk-ontology
derivedFrom:
  - https://w3id.org/ai-atlas-nexus/knowledge/references/ibm-ai-risk-atlas
  - https://w3id.org/ai-atlas-nexus/knowledge/references/granite-guardian
  - https://w3id.org/ai-atlas-nexus/knowledge/references/mit-ai-risk-repository
  - https://w3id.org/ai-atlas-nexus/knowledge/references/nist-ai-rmf-genai-profile
  - https://w3id.org/ai-atlas-nexus/knowledge/references/air-2024
  - https://w3id.org/ai-atlas-nexus/knowledge/references/ailuminate
  - https://w3id.org/ai-atlas-nexus/knowledge/references/credo-ucf
  - https://w3id.org/ai-atlas-nexus/knowledge/references/owasp-llm-top10
  - https://w3id.org/ai-atlas-nexus/knowledge/references/owasp-agentic-applications
---

# Overview

The **knowledge graph** lives as LinkML instance data in `src/ai_atlas_nexus/data/knowledge_graph/` - one YAML file per curated source, e.g. `risk_atlas_data.yaml` (IBM AI Risk Atlas), `nist_ai_rmf_data.yaml` and `nist_ai_rmf_actions_data.yaml` (NIST AI RMF), `mit_ai_risk_repository_data.yaml` plus mitigation/controls files (MIT), `owasp_llm_2.0_data.yaml` and `owasp_asi_data.yaml` (OWASP), `air_2024_data.yaml`, `ailuminate.yaml`, `credo.yaml`, `granite_guardian_dimensions.yaml`, ethics principles (`principles_*.yaml`), AI models (`ibm_granite_*`, `shieldgemma_*`), evaluations (`ai_eval_data.yaml`), and shared definitions (`ai_commons_data.yaml`).

The `derivedFrom` list above covers the taxonomies named in the repository README; the authoritative per-file source table (including AIUC-1, CSIRO RAI, Eticas, ShieldGemma, and the ethics principles) is the folder's own [README](https://github.com/IBM/ai-atlas-nexus/blob/main/src/ai_atlas_nexus/data/knowledge_graph/README.md). Raw source extracts also checked into the repo (`resources/TheAIRiskRepositoryV1_16_8_24.csv`, `resources/actions_extracted_from_nist.csv`) feed this data. Cross-taxonomy mappings live in `src/ai_atlas_nexus/data/mappings/` (SSSOM-based).
