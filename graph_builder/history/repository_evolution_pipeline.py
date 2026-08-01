"""
Graphify

Phase 17

Repository Intelligence Pipeline

Builds the complete Repository Intelligence Context.

Responsibilities

• Scan repository
• Parse repository
• Build repository intelligence
• Populate Repository Intelligence Context

Author:
Graphify Core
"""

from pathlib import Path

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

from graph_builder.intelligence.repository_intelligence_context import (
    RepositoryIntelligenceContext,
)


class RepositoryIntelligencePipeline:

    VERSION = "P17.1"

    # --------------------------------------------------

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

        # ----------------------------------------------
        # Build Repository Intelligence Context
        # ----------------------------------------------

        context = RepositoryIntelligenceContext()

        context.inventory = inventory

        context.module = module

        context.symbols = symbols

        context.relationships = relationships

        context.behavior = behavior

        context.capability = capability

        context.identity = identity

        return context