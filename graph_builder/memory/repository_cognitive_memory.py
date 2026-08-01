"""
Graphify

Phase 19

Stage P19.5

Repository Cognitive Memory

Maintains the active cognitive memory of the
currently loaded repository.

Acts as the working memory layer between the
Repository Brain and future reasoning systems.

Author:
Graphify Core
"""

from datetime import datetime

from graph_builder.memory.repository_evolution_memory import (
    RepositoryEvolutionMemory,
)


class RepositoryCognitiveMemory:

    VERSION = "P19.5"

    def __init__(self):

        #
        # Active Working Memory
        #

        self.intelligence_context = None

        self.repository_brain = None

        self.repository_identity = None

        self.repository_capability = None

        self.repository_behavior = None

        self.boot_timestamp = None

        self.repository_name = None

        self.repository_path = None

        #
        # Long-term Cognitive Memory
        #

        self.history = []

        #
        # Repository Evolution Memory
        #

        self.evolution_memory = RepositoryEvolutionMemory()

        self.evolution_history = []

    # -----------------------------------------------------

    def load(

        self,

        intelligence_context,

        repository_brain,

    ):

        self.intelligence_context = intelligence_context

        self.repository_brain = repository_brain

        self.repository_identity = (

            intelligence_context.identity

        )

        self.repository_capability = (

            intelligence_context.capability

        )

        self.repository_behavior = (

            intelligence_context.behavior

        )

        self.repository_name = (

            intelligence_context.inventory.repository_name

        )

        self.repository_path = (

            intelligence_context.inventory.repository_path

        )

        self.boot_timestamp = datetime.utcnow()

        #
        # Build Snapshot
        #

        snapshot = self._create_snapshot()

        #
        # Compare with previous snapshot
        #

        previous_snapshot = (

            self.history[-1]

            if self.history

            else None

        )

        evolution = self.evolution_memory.compare(

            previous_snapshot,

            snapshot,

        )

        #
        # Store evolution first
        #

        self.evolution_history.append(

            evolution,

        )

        #
        # Store snapshot
        #

        self.history.append(

            snapshot,

        )

    # -----------------------------------------------------

    def _create_snapshot(self):

        return {

            "repository": self.repository_name,

            "path": self.repository_path,

            "boot_timestamp": self.boot_timestamp,

            "identity": self.repository_identity,

            "capability": self.repository_capability,

            "behavior": self.repository_behavior,

            "version": self.VERSION,

        }

    # -----------------------------------------------------

    def clear(self):

        #
        # Clear only Working Memory
        #

        self.intelligence_context = None

        self.repository_brain = None

        self.repository_identity = None

        self.repository_capability = None

        self.repository_behavior = None

        self.boot_timestamp = None

        self.repository_name = None

        self.repository_path = None

        #
        # Preserve history and evolution history
        #

    # -----------------------------------------------------

    def timeline(self):

        return list(self.history)

    # -----------------------------------------------------

    def evolution(self):

        return list(self.evolution_history)

    # -----------------------------------------------------

    def is_loaded(self):

        return (

            self.intelligence_context is not None

        )

    # -----------------------------------------------------

    def status(self):

        return {

            "loaded": self.is_loaded(),

            "repository": self.repository_name,

            "path": self.repository_path,

            "boot_timestamp": self.boot_timestamp,

            "history_entries": len(self.history),

            "evolution_entries": len(self.evolution_history),

            "version": self.VERSION,

        }