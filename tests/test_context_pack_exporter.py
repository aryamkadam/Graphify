from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.context_pack_exporter import (
    export_context_pack
)

symbol_index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

knowledge_graph = build_knowledge_graph(
    symbol_index
)

context_pack = (
    export_context_pack(
        symbol_index,
        knowledge_graph,
        "graphify-out/repository_context.md"
    )
)

print()

print(
    "Context Pack Generated"
)

print()

print(
    context_pack
)