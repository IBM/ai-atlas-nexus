# Convenience script to export a loaded graph from all the yaml
# in src/ai_atlas_nexus/data/knowledge_graph

from ai_atlas_nexus import AIAtlasNexus


ran = AIAtlasNexus()

# export the graph to yaml
ran.export("graph_export/yaml/")
