"""
Stage 14.6

Repository Execution Graph

Builds the execution graph of the repository
by using the Function Call Parser.

Graph Structure:

source_function
        │
        ▼
called_function_1
called_function_2
called_function_3

This graph is later used for:

- Reverse Call Index
- Impact Analysis
- Critical Path Detection
- AI Context Generation
- Repository Brain
"""

from graph_builder.knowledge_graph.function_call_parser import (
    FunctionCallParser,
)


class ExecutionGraphBuilder:
    """
    Builds a function execution graph
    for the entire repository.
    """

    def __init__(self, repository_path):
        self.repository_path = repository_path

    def build(self):
        """
        Build execution graph.

        Returns
        -------
        dict

        {
            "file.py::function":
            [
                "called_function1",
                "called_function2"
            ]
        }
        """

        parser = FunctionCallParser(self.repository_path)

        function_calls = parser.parse()

        graph = {}

        for call in function_calls:

            source = (
                f"{call['source_file']}::{call['source_function']}"
            )

            target = call["target_function"]

            if source not in graph:
                graph[source] = []

            graph[source].append(target)

        return graph