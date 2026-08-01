"""
Graphify

Phase 17

Stage P17.2

Repository Intelligence Engine

Builds the canonical Repository Intelligence object
from a Repository Intelligence Context.

The Engine performs no repository scanning.

It converts Repository Context into the unified
Repository Intelligence representation.

Pipeline
    ↓
Context
    ↓
Repository Intelligence Engine
    ↓
RepositoryIntelligence
    ↓
Repository Brain

Author:
Graphify Core
"""

from graph_builder.intelligence.repository_intelligence_context import (
    RepositoryIntelligenceContext,
)

from graph_builder.intelligence.repository_intelligence import (
    RepositoryIntelligence,
)


class RepositoryIntelligenceEngine:

    VERSION = "P17.2"

    # --------------------------------------------------

    def __init__(

        self,

        context: RepositoryIntelligenceContext,

    ):

        self.context = context

    # --------------------------------------------------

    def build(self):

        intelligence = RepositoryIntelligence(

            inventory=self.context.inventory,

            module=self.context.module,

            symbols=self.context.symbols,

            relationships=self.context.relationships,

            repository_graph=self.context.repository_graph,

            symbol_graph=self.context.symbol_graph,

            behavior=self.context.behavior,

            capability=self.context.capability,

            identity=self.context.identity,

            health=self.context.health,

            knowledge=self.context.knowledge,

            execution=self.context.execution,

            evolution=self.context.evolution,

            decisions=self.context.decisions,

            insights=self.context.insights,

            metadata=self.context.metadata,

            extra=self.context.extra,

        )

        return intelligence

    # --------------------------------------------------

    def summary(self):

        intelligence = self.build()

        return intelligence.summary()