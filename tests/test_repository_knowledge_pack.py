from pprint import pprint

from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.repository_knowledge_pack import (
    build_repository_knowledge_pack
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

graph = build_knowledge_graph(
    index
)

pack = build_repository_knowledge_pack(
    index,
    graph
)

pprint(pack)