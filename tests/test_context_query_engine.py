from graph_builder.universal_context import (
    build_universal_context
)

from graph_builder.context_query_engine import (
    query_context
)

from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

symbol_index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

knowledge_graph = build_knowledge_graph(
    symbol_index
)

context = build_universal_context(
    symbol_index,
    knowledge_graph
)

print()

print(
    query_context(
        context,
        "How healthy is the repository?"
    )
)

print()

print(
    query_context(
        context,
        "What is the current project stage?"
    )
)

print()

print(
    query_context(
        context,
        "What are the critical symbols?"
    )
)

print()

print(
    query_context(
        context,
        "Where is the project heading?"
    )
)

print()

print(
    query_context(
        context,
        "Show risky symbols"
    )
)