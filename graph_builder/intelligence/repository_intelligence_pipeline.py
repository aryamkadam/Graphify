"""
Graphify

Phase 12

Stage P12.6.1

Repository Intelligence Pipeline

Bootstraps the complete Repository Brain.

Author:
Graphify Core
"""

from pathlib import Path

from graph_builder.scanner.repository_scanner import RepositoryScanner

from graph_builder.parser.python_ast_parser import PythonASTParser
from graph_builder.symbols.symbol_extractor import SymbolExtractor
from graph_builder.relationships.relationship_extractor import RelationshipExtractor

from graph_builder.intelligence.repository_behavior_intelligence_engine import (
    RepositoryBehaviorIntelligenceEngine,
)

from graph_builder.intelligence.repository_capability_engine import (
    RepositoryCapabilityEngine,
)

from graph_builder.intelligence.repository_identity_engine import (
    RepositoryIdentityEngine,
)


class RepositoryIntelligencePipeline:

    VERSION = "P12.6.1"

    def build(

        self,

        repository_name,

        repository_path,

        entry_file,

    ):

        scanner = RepositoryScanner(

            repository_name,

            repository_path,

        )

        inventory = scanner.scan()

        parser = PythonASTParser()

        module = parser.parse(

            Path(repository_path) / entry_file

        )

        symbols = SymbolExtractor().extract(

            module,

        )

        relationships = RelationshipExtractor().extract(

            module,

        )

        behavior = RepositoryBehaviorIntelligenceEngine().analyze(

            module,

            symbols,

        )

        capability = RepositoryCapabilityEngine().build(

            behavior,

        )

        identity = RepositoryIdentityEngine().build(

            repository=inventory.repository_name,

            capabilities=[

                capability.to_dict()

            ],

        )

        return {

            "inventory": inventory,

            "module": module,

            "symbols": symbols,

            "relationships": relationships,

            "behavior": behavior,

            "capability": capability,

            "identity": identity,

        }