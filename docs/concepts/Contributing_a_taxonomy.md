# Contributing a taxonomy or CoT templates

This document will describe how to contribute custom _taxonomy files_ and _CoT templates_ to the AI Atlas Nexus
project.

1. [Overview](#overview)
   1. [What are the taxonomy files?](#what-are-the-taxonomy-files)
   2. [How are mappings created between taxonomies?](#how-are-mappings-maintained-between-taxonomies)
2. [Add your own taxonomies/risks/actions](#add-your-own-taxonomiesrisksactions)
   1. [An example addition of a risk](#an-example-addition-of-a-risk)
3. [Add your own mappings](#add-your-own-mappings)
4. [Add your own Chain of Thought templates](#add-your-own-chain-of-thought-templates)

## Overview

You may wish to contribute your own taxonomy definitions, entity mappings or Chain of Thought templates to the Risk
Atlas Nexus project. We welcome any contributions.

Please familiarise yourself with the
general [contribution guidelines](https://github.com/IBM/ai-atlas-nexus/CONTRIBUTING.md) and set up your own fork of
the project.

### What are the taxonomy files?

The AI Atlas Nexus ontology combines the AI risk view (taxonomies, risks, actions) with an AI model view (AI systems,
AI models, model evaluations) into one schema. These are loaded into the system with LinkML, through yaml
representations, stored in
the [knowledge graph data folder](https://github.com/IBM/ai-atlas-nexus/tree/main/src/ai_atlas_nexus/data/knowledge_graph/).

### How are mappings maintained between taxonomies?

To express some semantically meaningful mapping between risks from different taxonomies, we have used the [Simple
Standard for Sharing Ontological Mappings (SSSOM)](https://academic.oup.com/database/article/doi/10.1093/database/baac035/6591806)
. The mappings are maintained in SSOM TSV files and are converted to LinkML data
YAML using Python helper scripts.

## Add your own taxonomies/risks/actions

You can add your own risk definitions by adding yaml
to [knowledge graph data folder](https://github.com/IBM/ai-atlas-nexus/src/ai_atlas_nexus/data/knowledge_graph/).
Ensure the entries comply with [the schema](../ontology/index.md)

### An example addition of a risk

If you would like to contribute your own taxonomy files to the project for others to use, add one or more yaml files to
the [knowledge graph data directory](https://github.com/IBM/ai-atlas-nexus/tree/main/src/ai_atlas_nexus/data/knowledge_graph/)
.

For example, to add a new risk, create a file with the following sample content, and add it to the knowledge graph data
directory.

```
- id: my-own-risk
  name: A very risky AI behaviour
  description: An LLM-based system is often very risky
  isDefinedByTaxonomy: my-taxonomy
```

## Add your own mappings

1. Prepare a TSV file either
   1. manually, or
   2. semi-automatically, with aid of the python notebook [Prepare taxonomy mappings](../examples/notebooks/Prepare_taxonomy_mappings.ipynb).
2. Verify the TSV mappings are correct.
3. Lift all the TSV files to yaml mapping entries by executing `make lift_mappings_from_tsv`.
4. Ensure the changes were saved to the [knowledge graph data mapping folder](https://github.com/IBM/ai-atlas-nexus/src/ai_atlas_nexus/data/knowledge_graph/mapping/) .

## Add your own Chain of Thought templates

Please follow [Risk Identification](https://ibm.github.io/ai-atlas-nexus/concepts/Chain_of_thought_templates/#risk-identification) section to create custom Chain of Thought examples for your own taxonomy.

### Save your changes

- Save your new taxonomy files in
  the [knowledge graph data directory](https://github.com/IBM/ai-atlas-nexus/tree/main/src/ai_atlas_nexus/data/knowledge_graph)
  . Push your changes and make a PR to the main project.
