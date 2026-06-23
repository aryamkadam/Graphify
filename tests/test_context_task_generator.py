from pprint import pprint

from graph_builder.universal_context import (
    build_universal_context
)

from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.context_task_generator import (
    generate_tasks
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

result = generate_tasks(
    context
)

print(
    "\nContext Tasks Generated\n"
)

pprint(
    result
)