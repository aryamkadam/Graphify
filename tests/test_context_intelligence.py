from pprint import pprint

from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.repository_brain import (
    generate_repository_brain
)

from graph_builder.context_intelligence import (
    generate_context_intelligence
)

symbol_index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

knowledge_graph = build_knowledge_graph(
    symbol_index
)

brain = generate_repository_brain(
    symbol_index,
    knowledge_graph,
    project_name="Graphify",
    project_purpose="AI Context Transfer Engine"
)

result = generate_context_intelligence(
    brain
)

print(
    "\nContext Intelligence Generated\n"
)

pprint(result)