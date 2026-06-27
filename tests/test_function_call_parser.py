from pprint import pprint

from graph_builder.knowledge_graph.function_call_parser import (
    FunctionCallParser
)

parser = FunctionCallParser(".")

calls = parser.parse()

print()

print("Function Calls")

print()

pprint(calls[:40])

print()

print("Total Calls:", len(calls))