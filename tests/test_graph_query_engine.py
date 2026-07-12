from pprint import pprint

from graph_builder.graph.graph_node import GraphNode
from graph_builder.graph.graph_edge import GraphEdge
from graph_builder.graph.repository_engineering_graph import (
    RepositoryEngineeringGraph,
)
from graph_builder.graph.graph_query_engine import (
    GraphQueryEngine,
)

print("\n========================================")
print("Graph Query Engine")
print("========================================\n")

graph = RepositoryEngineeringGraph()

objective = GraphNode(

    "Objective",

    "Improve Security",

)

sprint = GraphNode(

    "Sprint",

    "Sprint 1",

)

task = GraphNode(

    "Task",

    "Refactor Login",

)

graph.add_node(objective)
graph.add_node(sprint)
graph.add_node(task)

graph.add_edge(

    GraphEdge(

        objective.node_id,

        sprint.node_id,

        "CONTAINS",

    )

)

engine = GraphQueryEngine(graph)

print("Objectives\n")

for node in engine.by_node_type("Objective"):

    pprint(node.to_dict())

print("\nTasks\n")

for node in engine.by_node_type("Task"):

    pprint(node.to_dict())

print("\nRelations\n")

for edge in engine.by_relation("CONTAINS"):

    pprint(edge.to_dict())

print("\nStatistics\n")

pprint(engine.statistics())