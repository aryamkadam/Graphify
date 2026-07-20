"""
Graphify

Phase 12

Repository Intelligence Pipeline

Integration Test

Author:
Graphify Core
"""

from pathlib import Path
from pprint import pprint

from graph_builder.scanner.repository_scanner import (
    RepositoryScanner,
)

from graph_builder.parser.python_ast_parser import (
    PythonASTParser,
)

from graph_builder.symbols.symbol_extractor import (
    SymbolExtractor,
)

from graph_builder.relationships.relationship_extractor import (
    RelationshipExtractor,
)

from graph_builder.intelligence.repository_behavior_intelligence_engine import (
    RepositoryBehaviorIntelligenceEngine,
)

from graph_builder.intelligence.repository_capability_engine import (
    RepositoryCapabilityEngine,
)

from graph_builder.intelligence.repository_identity_engine import (
    RepositoryIdentityEngine,
)


print()
print("=" * 50)
print("Graphify Repository Intelligence Pipeline")
print("=" * 50)
print()

# ======================================================
# Stage 1
# Repository Scanner
# ======================================================

repo_path = Path(".").resolve()

scanner = RepositoryScanner(

    repository_name=repo_path.name,

    repository_path=repo_path,

)

inventory = scanner.scan()

print("[PASS] Repository Scanner")

pprint(

    inventory.summary()

)

# ======================================================
# Stage 2
# AST Parser
# ======================================================

parser = PythonASTParser()

target = Path(

    "graph_builder/parser/python_ast_parser.py"

)

module = parser.parse(target)

print()

print("[PASS] Python AST Parser")

# ======================================================
# Stage 3
# Symbol Extraction
# ======================================================

symbol_extractor = SymbolExtractor()

symbols = symbol_extractor.extract(

    module

)

print("[PASS] Symbol Extraction")

# ======================================================
# Stage 4
# Relationship Extraction
# ======================================================

relationship_extractor = RelationshipExtractor()

relationships = relationship_extractor.extract(

    module

)

print("[PASS] Relationship Extraction")

# ======================================================
# Stage 5
# Repository Behavior Intelligence
# ======================================================

behavior_engine = RepositoryBehaviorIntelligenceEngine()

behavior = behavior_engine.analyze(

    module,

    symbols,

)

print("[PASS] Repository Behavior Intelligence")

# ======================================================
# Stage 6
# Repository Capability Engine
# ======================================================

capability_engine = RepositoryCapabilityEngine()

capability = capability_engine.build(

    behavior,

)

print("[PASS] Repository Capability Engine")

# ======================================================
# Stage 7
# Repository Identity Engine
# ======================================================

identity_engine = RepositoryIdentityEngine()

identity = identity_engine.build(

    inventory.repository_name,

    [

        capability

    ],

)

print("[PASS] Repository Identity Engine")

# ======================================================
# Final Report
# ======================================================

print()
print("=" * 50)
print("FINAL REPOSITORY IDENTITY")
print("=" * 50)
print()

pprint(identity)

print()
print("=" * 50)
print("PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 50)