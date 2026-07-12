"""
Graphify

Stage 53.0

Engineering Graph Service

Converts completed engineering workflows
into Repository Engineering Graph nodes
and relationships.

Author:
Graphify Core
"""

from graph_builder.graph.repository_engineering_graph import (
    RepositoryEngineeringGraph,
)

from graph_builder.graph.graph_node import (
    GraphNode,
)

from graph_builder.graph.graph_edge import (
    GraphEdge,
)


class EngineeringGraphService:

    VERSION = "53.0"

    def __init__(self):

        self.graph = RepositoryEngineeringGraph()

    # --------------------------------------------------

    def record_workflow(

        self,

        workflow_result,

    ):

        task_node = GraphNode(

            node_type="Task",

            name=workflow_result["task"],

        )

        implementation_node = GraphNode(

            node_type="Implementation",

            name="Implementation",

            metadata=workflow_result["implementation"],

        )

        validation_node = GraphNode(

            node_type="Validation",

            name="Validation",

            metadata=workflow_result["validation"],

        )

        self.graph.add_node(task_node)

        self.graph.add_node(implementation_node)

        self.graph.add_node(validation_node)

        self.graph.add_edge(

            GraphEdge(

                source_id=task_node.node_id,

                target_id=implementation_node.node_id,

                relation="IMPLEMENTED_AS",

            )

        )

        self.graph.add_edge(

            GraphEdge(

                source_id=implementation_node.node_id,

                target_id=validation_node.node_id,

                relation="VERIFIED_BY",

            )

        )

        return {

            "nodes_created": 3,

            "edges_created": 2,

            "graph_status": self.graph.status(),

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def status(self):

        return self.graph.status()