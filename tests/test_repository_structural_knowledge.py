from pathlib import Path
from pprint import pprint

from graph_builder.tools.repository_scanner import RepositoryScanner

from graph_builder.symbols.symbol_extractor import (
    SymbolExtractor,
)

from graph_builder.relationships.relationship_extractor import (
    RelationshipExtractor,
)

from graph_builder.metrics.repository_metrics_engine import (
    RepositoryMetricsEngine,
)

from graph_builder.learning.repository_learning_engine import (
    RepositoryLearningEngine,
)

from graph_builder.knowledge.repository_knowledge_engine import (
    RepositoryKnowledgeEngine,
)

print("\n========================================")
print("Repository Structural Knowledge")
print("========================================\n")

# --------------------------------------------------
# Repository Inventory
# --------------------------------------------------

scanner = RepositoryScanner()

inventory = scanner.scan(".")

# --------------------------------------------------
# Parse one engineering file
# --------------------------------------------------

target = (

    Path(__file__).resolve().parent.parent

    / "graph_builder"

    / "parser"

    / "python_ast_parser.py"

)

symbols = SymbolExtractor().extract(

    target

)

relationships = RelationshipExtractor().extract(

    target

)

metrics = RepositoryMetricsEngine().analyze(

    inventory

)

learning = RepositoryLearningEngine().summary()

# --------------------------------------------------
# Build Repository Knowledge
# --------------------------------------------------

knowledge = RepositoryKnowledgeEngine().build_repository_knowledge(

    repository="Graphify",

    inventory=inventory,

    symbols=symbols,

    relationships=relationships,

    metrics=metrics,

    learning=learning,

)

print("Summary\n")

pprint(

    knowledge["repository_summary"]

)

print("\nRepository Knowledge\n")

pprint(

    knowledge

)