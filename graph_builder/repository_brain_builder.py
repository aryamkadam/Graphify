"""
Repository Brain Builder

Stage 15.3

Builds the Repository Brain using the
Repository Intelligence Engine.

RepositoryBrainBuilder is now only responsible
for converting repository intelligence into
the public Repository Brain format.

Future AI engines consume the Intelligence Engine
instead of directly accessing individual modules.
"""

from graph_builder.intelligence.repository_intelligence_engine import (
    RepositoryIntelligenceEngine,
)


class RepositoryBrainBuilder:

    def __init__(
        self,
        symbol_index,
        knowledge_graph,
        project_name,
        project_purpose,
    ):

        self.symbol_index = symbol_index

        self.knowledge_graph = knowledge_graph

        self.project_name = project_name

        self.project_purpose = project_purpose

    # --------------------------------------------------

    def build(self):

        intelligence = RepositoryIntelligenceEngine(

            self.symbol_index,

            self.knowledge_graph,

            "."

        ).build()

        metadata = intelligence["identity"]

        health = intelligence["health"]

        knowledge = intelligence["knowledge"]

        execution = intelligence["execution"]

        decision_brain = intelligence["decisions"]["brain"]

        decision_insights = intelligence["decisions"]["insights"]

        critical_symbols = [

            item["symbol"]

            for item in knowledge["critical_symbols"][:5]

        ]

        risky_symbols = [

            item["symbol"]

            for item in knowledge["risky_symbols"][:5]

        ]

        brain = {

            "project_name":

                self.project_name,

            "project_purpose":

                self.project_purpose,

            # ------------------------------------------------

            "metadata": metadata,

            # ------------------------------------------------

            "health": health,

            # ------------------------------------------------

            "knowledge": {

                "critical_symbols":

                    critical_symbols,

                "risky_symbols":

                    risky_symbols,

                "dead_code_count":

                    len(
                        knowledge["dead_code"]
                    ),

                "hotspot_count":

                    len(
                        knowledge["hotspots"]
                    ),

            },

            # ------------------------------------------------

            "execution": {

                "graph_nodes":

                    execution["statistics"]["graph_nodes"],

                "execution_paths":

                    execution["statistics"]["execution_paths"],

                "reverse_call_entries":

                    execution["statistics"]["reverse_call_entries"],

                "top_important_functions":

                    execution["importance_ranking"][:20],

            },

            # ------------------------------------------------

            "decisions":

                decision_brain,

            # ------------------------------------------------

            "insights":

                decision_insights,

            # ------------------------------------------------

            "executive_summary": {

                "repository_health":

                    health["status"],

                "health_score":

                    health["health_score"],

                "project_direction":

                    decision_insights["dominant_area"],

                "latest_commit":

                    metadata["latest_commit"],

                "current_branch":

                    metadata["current_branch"],

                "top_recommendations":

                    health["top_recommendations"],

            }

        }

        return brain