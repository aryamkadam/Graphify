from graph_builder.context_history import (
    save_context_commit,
    get_context_history
)

from graph_builder.context_commit import (
    create_context_commit
)

from graph_builder.universal_context import (
    build_universal_context
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

commit = create_context_commit(
    context,
    "Second Context Commit"
)

path = save_context_commit(
    commit
)

print(path)

print(
    len(
        get_context_history()
    )
)