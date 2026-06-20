from pprint import pprint

from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.symbol_context import (
    generate_symbol_context
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

graph = build_knowledge_graph(
    index
)

context = generate_symbol_context(
    "parse_python_file",
    index,
    graph
)

pprint(context)