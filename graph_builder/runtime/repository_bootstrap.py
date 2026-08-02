"""
Graphify

Phase 20

Stage P20.4

Repository Bootstrap

Bootstraps a Repository into a fully
operational Graphify Runtime.

Responsibilities

• Discover repository entry point
• Build Repository Intelligence Context
• Build Repository Intelligence
• Build Repository Brain
• Load Repository Cognitive Memory
• Build Repository Evolution Memory
• Build Repository State
• Attach Engineering Runtime
• Update Repository Context

The Bootstrap never performs engineering.

The Bootstrap never performs reasoning.

It only assembles the Repository Runtime.

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


class RepositoryBootstrap:

    VERSION = "P20.4"

    # --------------------------------------------------

    def __init__(

        self,

        context,

        engineering_kernel,

    ):

        self.context = context

        self.engineering_kernel = engineering_kernel

        self.memory = RepositoryCognitiveMemory()

        self.evolution_memory = RepositoryEvolutionMemory()

    # --------------------------------------------------

    def boot(self):

        """
        Bootstrap one repository.
        """

        #
        # Discover Repository Entry
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

        return self.context

    # --------------------------------------------------

    def shutdown(self):

        #
        # Clear Cognitive Memory
        #

        if self.memory:

            self.memory.clear()

        #
        # Clear Evolution Memory
        #

        if self.evolution_memory:

            self.evolution_memory.clear()

        #
        # Clear Runtime Objects
        #

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

            "project":
                self.context.project_name,

            "version":
                self.VERSION,

        }