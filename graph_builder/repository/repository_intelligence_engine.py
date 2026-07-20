"""
Graphify

Phase 9

Stage P9.7

Repository Intelligence Engine

Synthesizes repository understanding
from engineering knowledge.

Author:
Graphify Core
"""

from graph_builder.repository.repository_intelligence_report import (
    RepositoryIntelligenceReport,
)


class RepositoryIntelligenceEngine:

    VERSION = "P9.7"

    def analyze(

        self,

        knowledge,

        metrics,

        evolution,

        learning,

    ):

        repository_name = knowledge.repository_name

        stage = metrics["repository_size"]

        health = metrics["health"]

        strategy = evolution["strategy"]

        executive_summary = (

            f"{repository_name} is currently "

            f"{stage.lower()} with "

            f"{health.lower()} engineering health."

        )

        historical_context = (

            f"Repository has "

            f"{learning.summary()['repository_history']} "

            f"recorded evolution cycle(s)."

        )

        recommendations = evolution["recommended_actions"]

        return RepositoryIntelligenceReport(

            repository_name,

            stage,

            health,

            strategy,

            executive_summary,

            historical_context,

            recommendations,

        )