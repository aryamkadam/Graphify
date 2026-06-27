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

from graph_builder.knowledge_graph.critical_execution_path import (
    CriticalExecutionPath
)

parser = FunctionCallParser(".")

calls = parser.parse()

graph = ExecutionGraphBuilder(calls).build()

paths = ExecutionPathFinder(graph).build_paths()

critical = CriticalExecutionPath(paths).analyze()

print()

print("Critical Execution Functions")

print()

pprint(critical)

print()

print("Total Critical Functions:", len(critical))