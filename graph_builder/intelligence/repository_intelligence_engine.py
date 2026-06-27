"""
Stage 15.3

Repository Intelligence Engine

This engine combines every intelligence
module into one unified repository model.

Future AI reasoning, prediction,
planning and autonomous engineering
will consume this object.
"""

from graph_builder.execution.execution_engine import (
    ExecutionEngine,
)

from graph_builder.repository_metadata import (
    get_repository_metadata,
)

from graph_builder.repository_health_report import (
    generate_health_report,
)

from graph_builder.repository_knowledge_pack import (
    build_repository_knowledge_pack,
)

from graph_builder.project_decision_brain import (
    generate_project_decision_brain,
)

from graph_builder.decision_insights import (
    generate_decision_insights,
)


class RepositoryIntelligenceEngine:

    def __init__(
        self,
        symbol_index,
        knowledge_graph,
        repository_path="."
    ):

        self.symbol_index = symbol_index

        self.knowledge_graph = knowledge_graph

        self.repository_path = repository_path

    # -----------------------------------------

    def build(self):

        metadata = get_repository_metadata()

        health = generate_health_report(

            self.symbol_index,

            self.knowledge_graph

        )

        knowledge = build_repository_knowledge_pack(

            self.symbol_index,

            self.knowledge_graph

        )

        execution = ExecutionEngine(

            self.repository_path

        ).build()

        decision_brain = (

            generate_project_decision_brain()

        )

        decision_insights = (

            generate_decision_insights()

        )

        intelligence = {

            "identity": {

                "current_branch":
                    metadata.get(
                        "current_branch"
                    ),

                "latest_commit":
                    metadata.get(
                        "latest_commit"
                    ),

                "latest_tag":
                    metadata.get(
                        "latest_tag"
                    ),

                "total_commits":
                    metadata.get(
                        "total_commits"
                    ),

                "current_stage":
                    metadata.get(
                        "current_stage"
                    ),

            },

            "health": health,

            "knowledge": knowledge,

            "execution": execution,

            "decisions": {

                "brain":
                    decision_brain,

                "insights":
                    decision_insights,

            }

        }

        return intelligence