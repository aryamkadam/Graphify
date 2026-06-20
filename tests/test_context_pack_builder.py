from pprint import pprint

from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.context_pack_builder import (
    build_context_pack
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

graph = build_knowledge_graph(
    index
)

pack = build_context_pack(
    "parse_python_file",
    index,
    graph
)

pprint(pack)