"""
Graphify

Phase 17

Stage P17.1

Repository Intelligence

The canonical intelligence representation of a repository.

This object represents everything Graphify knows about
a repository.

It contains no scanning logic, no reasoning logic,
and no analysis logic.

Every higher-level Graphify component consumes this object.

Pipeline
    ↓
Context
    ↓
Repository Intelligence Engine
    ↓
RepositoryIntelligence
    ↓
Repository Brain
    ↓
Graphify Kernel

Author:
Graphify Core
"""


class RepositoryIntelligence:

    VERSION = "P17.1"

    def __init__(

        self,

        inventory=None,
        module=None,
        symbols=None,
        relationships=None,

        repository_graph=None,
        symbol_graph=None,

        behavior=None,
        capability=None,
        identity=None,

        health=None,
        knowledge=None,
        execution=None,

        evolution=None,

        decisions=None,
        insights=None,

        metadata=None,
        extra=None,

    ):

        # ------------------------------------------
        # Repository Structure
        # ------------------------------------------

        self.inventory = inventory

        self.module = module

        self.symbols = symbols

        self.relationships = relationships

        # ------------------------------------------
        # Graph Layer
        # ------------------------------------------

        self.repository_graph = repository_graph

        self.symbol_graph = symbol_graph

        # ------------------------------------------
        # Repository Intelligence
        # ------------------------------------------

        self.behavior = behavior

        self.capability = capability

        self.identity = identity

        self.health = health

        self.knowledge = knowledge

        self.execution = execution

        self.evolution = evolution

        # ------------------------------------------
        # AI Reasoning
        # ------------------------------------------

        self.decisions = decisions

        self.insights = insights

        # ------------------------------------------
        # Metadata
        # ------------------------------------------

        self.metadata = metadata

        self.extra = extra

    # --------------------------------------------------

    def to_dict(self):

        return {

            "inventory":
                self.inventory,

            "module":
                self.module,

            "symbols":
                self.symbols,

            "relationships":
                self.relationships,

            "repository_graph":
                self.repository_graph,

            "symbol_graph":
                self.symbol_graph,

            "behavior":
                self.behavior,

            "capability":
                self.capability,

            "identity":
                self.identity,

            "health":
                self.health,

            "knowledge":
                self.knowledge,

            "execution":
                self.execution,

            "evolution":
                self.evolution,

            "decisions":
                self.decisions,

            "insights":
                self.insights,

            "metadata":
                self.metadata,

            "extra":
                self.extra,

            "version":
                self.VERSION,

        }

    # --------------------------------------------------

    def summary(self):

        return {

            "version":
                self.VERSION,

            "total_symbols":
                len(self.symbols)
                if self.symbols
                else 0,

            "repository_loaded":
                self.inventory is not None,

            "health_available":
                self.health is not None,

            "execution_available":
                self.execution is not None,

            "knowledge_available":
                self.knowledge is not None,

        }

    # --------------------------------------------------

    def __repr__(self):

        return (

            f"RepositoryIntelligence("

            f"version={self.VERSION}, "

            f"symbols={len(self.symbols) if self.symbols else 0}"

            f")"

        )