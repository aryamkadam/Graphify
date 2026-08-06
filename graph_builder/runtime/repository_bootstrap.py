"""
Graphify

Phase 22

Stage P22.6

Repository Bootstrap

Bootstraps a Repository into a fully
operational Graphify Runtime.

Runtime Order

Repository
    ↓
Repository Intelligence
    ↓
Repository Brain
    ↓
Repository Memory
    ↓
Repository Evolution Memory
    ↓
Repository State
    ↓
Engineering Runtime
    ↓
Repository Ready
    ↓
Repository Awareness
    ↓
Repository Understanding

Author:
Graphify Core
"""

from graph_builder.discovery.repository_entry_discovery import (
    RepositoryEntryDiscovery,
)

from graph_builder.intelligence.repository_intelligence_pipeline import (
    RepositoryIntelligencePipeline,
)

from graph_builder.intelligence.repository_intelligence_engine import (
    RepositoryIntelligenceEngine,
)

from graph_builder.brain.repository_brain import (
    RepositoryBrain,
)

from graph_builder.memory.repository_cognitive_memory import (
    RepositoryCognitiveMemory,
)

from graph_builder.memory.repository_evolution_memory import (
    RepositoryEvolutionMemory,
)

from graph_builder.state.repository_state_engine import (
    RepositoryStateEngine,
)

from graph_builder.awareness.repository_awareness_manager import (
    RepositoryAwarenessManager,
)

from graph_builder.understanding.repository_understanding_manager import (
    RepositoryUnderstandingManager,
)


class RepositoryBootstrap:

    VERSION = "P22.6"

    # --------------------------------------------------

    def __init__(
        self,
        context,
        engineering_kernel,
    ):

        self.context = context
        self.engineering_kernel = engineering_kernel

        #
        # Runtime Components
        #

        self.memory = RepositoryCognitiveMemory()

        self.evolution_memory = RepositoryEvolutionMemory()

        self.awareness_manager = RepositoryAwarenessManager(
            self.context,
        )

        self.understanding_manager = RepositoryUnderstandingManager(
            self.context,
        )

    # --------------------------------------------------

    def boot(self):

        #
        # Repository Entry Discovery
        #

        discovery = RepositoryEntryDiscovery(
            self.context.repository_path,
        )

        entry = discovery.discover()

        #
        # Repository Intelligence Context
        #

        pipeline = RepositoryIntelligencePipeline()

        intelligence_context = pipeline.build(
            repository_name=self.context.project_name,
            repository_path=self.context.repository_path,
            entry_file=entry["entry_file"],
        )

        self.context.intelligence_context = intelligence_context

        #
        # Repository Intelligence
        #

        intelligence = RepositoryIntelligenceEngine(
            intelligence_context,
        ).build()

        self.context.repository_intelligence = intelligence

        #
        # Repository Brain
        #

        brain = RepositoryBrain(
            intelligence,
        )

        self.context.repository_brain = brain

        #
        # Repository Cognitive Memory
        #

        self.memory.load(
            intelligence_context,
            brain,
        )

        self.context.repository_memory = self.memory

        #
        # Repository Evolution Memory
        #

        self.evolution_memory.record(
            intelligence_context,
        )

        self.context.repository_evolution_memory = (
            self.evolution_memory
        )

        #
        # Repository State
        #

        repository_state = RepositoryStateEngine().build(
            self.context,
        )

        self.context.repository_state = repository_state

        #
        # Attach Engineering Runtime
        #

        self.context.engineering_runtime = (
            self.engineering_kernel
        )

        #
        # Repository Ready
        #

        self.context.repository_loaded = True

        #
        # Repository Awareness
        #

        awareness = self.awareness_manager.build()

        self.context.repository_awareness = awareness

        #
        # Repository Understanding
        #

        understanding = self.understanding_manager.build()

        self.context.repository_understanding = understanding

        return self.context

    # --------------------------------------------------

    def shutdown(self):

        #
        # Managers
        #

        if self.understanding_manager:
            self.understanding_manager.clear()

        if self.awareness_manager:
            self.awareness_manager.clear()

        #
        # Memory
        #

        if self.memory:
            self.memory.clear()

        if self.evolution_memory:
            self.evolution_memory.clear()

        #
        # Runtime Context
        #

        self.context.repository_understanding = None
        self.context.repository_awareness = None
        self.context.repository_state = None
        self.context.repository_evolution_memory = None
        self.context.repository_memory = None
        self.context.repository_brain = None
        self.context.repository_intelligence = None
        self.context.intelligence_context = None
        self.context.engineering_runtime = None

        self.context.repository_loaded = False

    # --------------------------------------------------

    def status(self):

        return {

            "bootstrap": "READY",

            "repository_loaded":
                self.context.repository_loaded,

            "memory_loaded":
                self.memory.is_loaded(),

            "evolution_memory_loaded":
                self.context.repository_evolution_memory
                is not None,

            "repository_state_loaded":
                self.context.repository_state
                is not None,

            "repository_awareness_loaded":
                self.context.repository_awareness
                is not None,

            "repository_understanding_loaded":
                self.context.repository_understanding
                is not None,

            "project":
                self.context.project_name,

            "version":
                self.VERSION,

        }