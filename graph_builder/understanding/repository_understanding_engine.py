"""
Graphify

Phase 22

Stage P22.6

Repository Understanding Engine

Builds the canonical semantic understanding
of the active repository.

Consumes:

• Repository Intelligence
• Repository Brain
• Repository Memory
• Repository State
• Repository Awareness

Produces:

• RepositoryUnderstanding

The engine NEVER evaluates.

The engine NEVER reasons.

The engine NEVER plans.

Author:
Graphify Core
"""

from graph_builder.understanding.repository_understanding import (
    RepositoryUnderstanding,
)


class RepositoryUnderstandingEngine:

    VERSION = "P22.6"

    # --------------------------------------------------

    def __init__(

        self,

        repository_context,

    ):

        self.context = repository_context

    # --------------------------------------------------

    def build(self):

        intelligence = self.context.repository_intelligence

        understanding = RepositoryUnderstanding(

            repository=self.context.project_name,

            identity=getattr(intelligence, "identity", None),

            capability=getattr(intelligence, "capability", None),

            behavior=getattr(intelligence, "behavior", None),

            engineering_scope=self._engineering_scope(),

            architecture_description=self._architecture_description(),

            repository_focus=self._repository_focus(),

            organization_description=self._organization_description(),

            runtime_description=self._runtime_description(),

            dependency_description=self._dependency_description(),

            confidence=self._confidence(),

        )

        return understanding

    # --------------------------------------------------
    # Understanding Builders
    # --------------------------------------------------

    def _engineering_scope(self):

        return "Repository Intelligence Platform"

    # --------------------------------------------------

    def _architecture_description(self):

        return (
            "Repository follows a layered cognitive "
            "architecture where intelligence, brain, memory, "
            "state and awareness are separated into dedicated "
            "runtime subsystems."
        )

    # --------------------------------------------------

    def _repository_focus(self):

        return (
            "Building a self-aware repository runtime capable "
            "of understanding software architecture."
        )

    # --------------------------------------------------

    def _organization_description(self):

        return (
            "Repository is organized into independent cognitive "
            "modules with clear subsystem separation."
        )

    # --------------------------------------------------

    def _runtime_description(self):

        return (
            "Repository Runtime is initialized through the "
            "Graphify Kernel and Repository Bootstrap."
        )

    # --------------------------------------------------

    def _dependency_description(self):

        return (
            "Runtime layers are initialized sequentially "
            "from Discovery to Intelligence, Brain, Memory, "
            "State, Awareness and Understanding."
        )

    # --------------------------------------------------

    def _confidence(self):

        confidence = 0.0

        if self.context.repository_intelligence:
            confidence += 0.25

        if self.context.repository_brain:
            confidence += 0.20

        if self.context.repository_memory:
            confidence += 0.20

        if self.context.repository_state:
            confidence += 0.20

        if self.context.repository_awareness:
            confidence += 0.15

        return round(confidence, 2)

    # --------------------------------------------------

    def status(self):

        return {

            "engine": "READY",

            "version": self.VERSION,

        }