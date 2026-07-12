from pprint import pprint

from graph_builder.graph.graph_node import GraphNode
from graph_builder.graph.repository_engineering_graph import (
    RepositoryEngineeringGraph,
)
from graph_builder.reasoning.engineering_reasoning_engine import (
    EngineeringReasoningEngine,
)

print("\n========================================")
print("Engineering Reasoning Engine")
print("========================================\n")

graph = RepositoryEngineeringGraph()

objective = GraphNode(
    "Objective",
    "Improve Security",
)

graph.add_node(objective)

engine = EngineeringReasoningEngine(graph)

results = engine.analyze()

for r in results:

    pprint(r)