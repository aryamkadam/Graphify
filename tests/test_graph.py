from parser.python_parser import parse_python_file
from graph_builder.builder import build_graph
from graph_builder.exporter import export_graph

data = parse_python_file("test.py")

graph = build_graph(data)

export_graph(
    graph,
    "graphify-out"
)

print("Graph exported.")