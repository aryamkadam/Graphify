"""
Graphify

Phase 18

Commit 5

Graphify Boot Manager

The Boot Manager is responsible for starting
the Graphify Operating System.

Responsibilities

• Validate repository
• Build Repository Intelligence
• Build Repository Brain
• Initialize Engineering Kernel
• Update Repository Context

The Boot Manager performs orchestration only.

It never performs repository analysis itself.

Author:
Graphify Core
"""

from graph_builder.intelligence.repository_intelligence_pipeline import (
    RepositoryIntelligencePipeline,
)

from graph_builder.intelligence.repository_intelligence_engine import (
    RepositoryIntelligenceEngine,
)

from graph_builder.brain.repository_brain import (
    RepositoryBrain,
)


class GraphifyBootManager:

    VERSION = "P18.0"

    # --------------------------------------------------

    def __init__(

        self,

        context,

        engineering_kernel,

    ):

        self.context = context

        self.engineering_kernel = engineering_kernel

    # --------------------------------------------------

    def boot(self):

        """
        Boot Graphify.
        """

        #
        # Build Repository Intelligence Context
        #

        pipeline = RepositoryIntelligencePipeline()

        self.context.intelligence_context = pipeline.build(

            repository_name=self.context.project_name,

            repository_path=self.context.repository_path,

            entry_file="main.py",

        )

        #
        # Repository Intelligence
        #

        intelligence = RepositoryIntelligenceEngine(

            self.context.intelligence_context,

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
        # Engineering Runtime
        #

        self.context.engineering_runtime = (

            self.engineering_kernel

        )

        #
        # Repository Loaded
        #

        self.context.repository_loaded = True

        self.context.booted = True

        return self.context

    # --------------------------------------------------

    def shutdown(self):

        self.context.repository_brain = None

        self.context.repository_intelligence = None

        self.context.intelligence_context = None

        self.context.engineering_runtime = None

        self.context.repository_loaded = False

        self.context.booted = False