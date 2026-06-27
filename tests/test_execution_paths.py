from pprint import pprint

from graph_builder.knowledge_graph.function_call_parser import (
    FunctionCallParser
)

from graph_builder.knowledge_graph.execution_graph_builder import (
    ExecutionGraphBuilder
)

from graph_builder.knowledge_graph.execution_path_finder import (
    ExecutionPathFinder
)

parser = FunctionCallParser(".")

calls = parser.parse()

graph = ExecutionGraphBuilder(calls).build()

paths = ExecutionPathFinder(graph).build_paths()

print()

print("Execution Paths")

print()

pprint(paths[:20])

print()

print("Total Paths:", len(paths))