"""
Stage 15.2.1

Execution Engine

Central execution intelligence coordinator.

Builds complete repository execution intelligence.
"""

from graph_builder.knowledge_graph.execution_graph_builder import (
    ExecutionGraphBuilder,
)

from graph_builder.knowledge_graph.execution_path_finder import (
    ExecutionPathFinder,
)

from graph_builder.knowledge_graph.reverse_call_index import (
    ReverseCallIndex,
)

from graph_builder.knowledge_graph.importance_score import (
    ImportanceScoreEngine,
)


class ExecutionEngine:

    def __init__(self, repository_path="."):

        self.repository_path = repository_path

    def build(self):

        execution_graph = ExecutionGraphBuilder(
            self.repository_path
        ).build()

        execution_paths = ExecutionPathFinder(
            execution_graph
        ).build_paths()

        reverse_calls = ReverseCallIndex().build(
            execution_graph
        )

        importance = ImportanceScoreEngine(
            execution_paths
        ).calculate()

        return {

            "execution_graph": execution_graph,

            "execution_paths": execution_paths,

            "reverse_call_index": reverse_calls,

            "importance_ranking": importance,

            "statistics": {

                "graph_nodes":
                    len(execution_graph),

                "execution_paths":
                    len(execution_paths),

                "reverse_call_entries":
                    len(reverse_calls),

                "ranked_functions":
                    len(importance),

            },

        }