from pprint import pprint

from graph_builder.knowledge_graph.execution_graph import ExecutionGraphBuilder
from graph_builder.knowledge_graph.reverse_call_index import ReverseCallIndex

graph = ExecutionGraphBuilder(".").build()

reverse = ReverseCallIndex().build(graph)

print("\nReverse Call Index\n")

items = list(reverse.items())[:30]

pprint(items)

print()

print("Functions referenced:", len(reverse))