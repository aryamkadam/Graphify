from pprint import pprint

from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.universal_context import (
    build_universal_context
)

symbol_index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

knowledge_graph = build_knowledge_graph(
    symbol_index
)

result = build_universal_context(
    symbol_index,
    knowledge_graph
)

print(
    "\nUniversal Context Generated\n"
)

pprint(result)