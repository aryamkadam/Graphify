from pprint import pprint

from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.ai_context_pack import (
    build_ai_context_pack
)

from graph_builder.ai_export_router import (
    export_for_ai
)

symbol_index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

knowledge_graph = build_knowledge_graph(
    symbol_index
)

context = build_ai_context_pack(
    symbol_index,
    knowledge_graph
)

result = export_for_ai(
    context,
    "ChatGPT"
)

pprint(result)