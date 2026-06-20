from pprint import pprint

from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.repository_brain_exporter import (
    export_repository_brain
)

symbol_index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

knowledge_graph = build_knowledge_graph(
    symbol_index
)

brain = export_repository_brain(

    symbol_index,

    knowledge_graph,

    "graphify-out/repository_brain.json",

    project_name="Graphify",

    project_purpose=
    "AI Context Transfer Engine",

    current_stage=
    "Stage 5 Complete"
)

pprint(
    brain
)