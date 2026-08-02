"""
Graphify

Phase 21

Stage P21.2

Repository Awareness Engine

Builds the current awareness snapshot
of the active repository.

The Awareness Engine only observes.

It never performs reasoning.
It never performs planning.
It never performs engineering.

Input:
    RepositoryContext

Output:
    RepositoryAwarenessReport

Author:
Graphify Core
"""

from datetime import datetime, UTC

from graph_builder.awareness.repository_awareness_report import (
    RepositoryAwarenessReport,
)


class RepositoryAwarenessEngine:

    VERSION = "P21.2"

    # --------------------------------------------------

    def __init__(

        self,

        repository_context,

    ):

        self.context = repository_context

    # --------------------------------------------------

    def build(self):

        """
        Build the current repository awareness report.
        """

        state = self._repository_state()

        health = self._repository_health()

        return RepositoryAwarenessReport(

            repository_name=self.context.project_name,

            repository_path=self.context.repository_path,

            timestamp=datetime.now(UTC),

            identity=self._identity(),

            capability=self._capability(),

            behavior=self._behavior(),

            state=state,

            health=health,

            runtime_ready=self.context.ready,

            memory_loaded=self.context.repository_memory is not None,

            evolution_loaded=self.context.repository_evolution_memory is not None,

            brain_loaded=self.context.repository_brain is not None,

            warnings=self._warnings(),

        )

    # --------------------------------------------------

    def _identity(self):

        intelligence = self.context.repository_intelligence

        if intelligence is None:

            return "UNKNOWN"

        return getattr(intelligence, "identity", "UNKNOWN")

    # --------------------------------------------------

    def _capability(self):

        intelligence = self.context.repository_intelligence

        if intelligence is None:

            return "UNKNOWN"

        return getattr(intelligence, "capability", "UNKNOWN")

    # --------------------------------------------------

    def _behavior(self):

        intelligence = self.context.repository_intelligence

        if intelligence is None:

            return "UNKNOWN"

        return getattr(intelligence, "behavior", "UNKNOWN")

    # --------------------------------------------------

    def _repository_state(self):

        if self.context.repository_state is None:

            return "UNKNOWN"

        state = self.context.repository_state

        if hasattr(state, "status"):

            status = state.status()

            if isinstance(status, dict):

                return status.get("state", "ACTIVE")

        return "ACTIVE"

    # --------------------------------------------------

    def _repository_health(self):

        state = self.context.repository_state

        if state is None:

            return "UNKNOWN"

        if hasattr(state, "health"):

            return state.health()

        return "HEALTHY"

    # --------------------------------------------------

    def _warnings(self):

        warnings = []

        if self.context.repository_brain is None:

            warnings.append("Repository Brain Not Loaded")

        if self.context.repository_memory is None:

            warnings.append("Repository Memory Not Loaded")

        if self.context.repository_evolution_memory is None:

            warnings.append("Repository Evolution Memory Not Loaded")

        if self.context.repository_state is None:

            warnings.append("Repository State Not Loaded")

        return warnings

    # --------------------------------------------------

    def status(self):

        return {

            "engine": "READY",

            "version": self.VERSION,

        }