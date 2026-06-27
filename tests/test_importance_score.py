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

from graph_builder.knowledge_graph.importance_score import (
    ImportanceScoreEngine
)

parser = FunctionCallParser(".")

calls = parser.parse()

graph = ExecutionGraphBuilder(calls).build()

paths = ExecutionPathFinder(graph).build_paths()

scores = ImportanceScoreEngine(paths).calculate()

print()

print("Repository Importance Ranking")

print()

pprint(scores[:20])

print()

print("Functions Ranked:", len(scores))