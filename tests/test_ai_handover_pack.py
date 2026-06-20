from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.ai_handover_exporter import (
    export_ai_handover_pack
)

symbol_index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

knowledge_graph = build_knowledge_graph(
    symbol_index
)

content = (
    export_ai_handover_pack(
        symbol_index,
        knowledge_graph,
        "graphify-out/ai_handover_pack.md"
    )
)

print()
print(
    "AI Handover Pack Generated"
)
print()

print(
    content
)