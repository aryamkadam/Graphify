from pprint import pprint

from graph_builder.knowledge_graph.builder import (
    KnowledgeGraphBuilder
)

builder = KnowledgeGraphBuilder(".")

graph = builder.build()

print("\nKnowledge Graph\n")

pprint(graph)