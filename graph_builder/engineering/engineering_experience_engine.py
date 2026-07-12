"""
Graphify

Stage 54.0

Engineering Experience Engine

Analyzes the Repository Engineering Graph
to extract engineering insights.

Author:
Graphify Core
"""

from graph_builder.graph.repository_engineering_graph import (
    RepositoryEngineeringGraph,
)


class EngineeringExperienceEngine:

    VERSION = "54.0"

    def __init__(self, graph: RepositoryEngineeringGraph):

        self.graph = graph

    # --------------------------------------------------

    def analyze(self):

        stats = self.graph.status()

        recommendations = []

        if stats["nodes"] == 0:
            recommendations.append(
                "Repository has no engineering knowledge."
            )

        elif stats["nodes"] < 5:
            recommendations.append(
                "Collect more engineering experience."
            )

        if stats["edges"] < stats["nodes"] - 1:
            recommendations.append(
                "Engineering knowledge graph is sparsely connected."
            )

        return {
            "nodes": stats["nodes"],
            "edges": stats["edges"],
            "recommendations": recommendations,
            "version": self.VERSION,
        }

    # --------------------------------------------------

    def repository_health(self):

        stats = self.graph.status()

        if stats["nodes"] == 0:
            health = "EMPTY"

        elif stats["nodes"] < 10:
            health = "GROWING"

        else:
            health = "MATURE"

        return {
            "health": health,
            "version": self.VERSION,
        }