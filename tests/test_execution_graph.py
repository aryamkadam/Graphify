from pprint import pprint

from graph_builder.knowledge_graph.function_call_parser import (
    FunctionCallParser
)

from graph_builder.knowledge_graph.execution_graph_builder import (
    ExecutionGraphBuilder
)

parser = FunctionCallParser(".")

calls = parser.parse()

builder = ExecutionGraphBuilder(calls)

graph = builder.build()

print("\nExecution Graph\n")

items = list(graph.items())[:25]

pprint(items)

print()

print("Execution Nodes:", len(graph))