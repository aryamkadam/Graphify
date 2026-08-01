"""
Graphify

Phase 19

Stage P19.2

Repository Bootstrap

Bootstraps a Repository into a fully
operational Graphify Runtime.

Responsibilities

• Discover repository entry point
• Build Repository Intelligence Context
• Build Repository Intelligence
• Build Repository Brain
• Load Repository Cognitive Memory
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


class RepositoryBootstrap:

    VERSION = "P19.2"

    # --------------------------------------------------

    def __init__(

        self,

        context,

        engineering_kernel,

    ):

        self.context = context

        self.engineering_kernel = engineering_kernel

        self.memory = RepositoryCognitiveMemory()

    # --------------------------------------------------

    def boot(self):

        """
        Bootstrap one repository.
        """

        #
        # Discover repository entry point
        #

        discovery = RepositoryEntryDiscovery(

            self.context.repository_path,

        )

        entry = discovery.discover()

        #
        # Build Repository Intelligence Context
        #

        pipeline = RepositoryIntelligencePipeline()

        intelligence_context = pipeline.build(

            repository_name=self.context.project_name,

            repository_path=self.context.repository_path,

            entry_file=entry["entry_file"],

        )

        self.context.intelligence_context = intelligence_context

        #
        # Build Repository Intelligence
        #

        intelligence = RepositoryIntelligenceEngine(

            intelligence_context,

        ).build()

        self.context.repository_intelligence = intelligence

        #
        # Build Repository Brain
        #

        brain = RepositoryBrain(

            intelligence,

        )

        self.context.repository_brain = brain

        #
        # Load Repository Cognitive Memory
        #

        self.memory.load(

            intelligence_context,

            brain,

        )

        self.context.repository_memory = self.memory

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

        if self.memory:

            self.memory.clear()

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

            "project":
                self.context.project_name,

            "version":
                self.VERSION,

        }