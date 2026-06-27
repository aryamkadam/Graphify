"""
Stage 15.6 Test

Repository Consciousness Engine
"""

from pprint import pprint

from graph_builder.intelligence.repository_intelligence_engine import (
    RepositoryIntelligenceEngine,
)

from graph_builder.reasoning.repository_consciousness_engine import (
    RepositoryConsciousnessEngine,
)

from graph_builder.symbol_index import (
    build_symbol_index,
)

from graph_builder.repository_graph import (
    build_repository_graph,
)


symbol_index = build_symbol_index(".")

knowledge_graph = build_repository_graph(".")

intelligence = RepositoryIntelligenceEngine(

    symbol_index,

    knowledge_graph,

    "."

).build()

engine = RepositoryConsciousnessEngine(

    intelligence

)

print()

print("Repository Consciousness")

print()

pprint(

    engine.build(),

    sort_dicts=False

)