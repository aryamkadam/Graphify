"""
Graphify

Stage 38.0

Engineering Reasoning Engine

Author:
Graphify Core
"""


class EngineeringReasoningEngine:

    VERSION = "38.0"

    def __init__(self, graph):

        self.graph = graph

    # ----------------------------------------

    def analyze(self):

        recommendations = []

        for node in self.graph.nodes.values():

            if node.node_type == "Objective":

                outgoing = self.graph.get_edges_from(node.node_id)

                if len(outgoing) == 0:

                    recommendations.append(

                        {

                            "node": node.name,

                            "type": "Objective",

                            "recommendation":
                            "Objective has no Sprint.",

                            "severity": "HIGH",

                        }

                    )

            elif node.node_type == "Sprint":

                outgoing = self.graph.get_edges_from(node.node_id)

                if len(outgoing) == 0:

                    recommendations.append(

                        {

                            "node": node.name,

                            "type": "Sprint",

                            "recommendation":
                            "Sprint has no Tasks.",

                            "severity": "MEDIUM",

                        }

                    )

        return recommendations