"""
Graphify

Phase 20

Stage P20.4

Repository State Engine

Builds the current Repository State.

The State Engine never performs reasoning.

It assembles state from specialized state engines.

Author:
Graphify Core
"""

from graph_builder.state.repository_state import (
    RepositoryState,
)

from graph_builder.state.repository_health_engine import (
    RepositoryHealthEngine,
)


class RepositoryStateEngine:

    VERSION = "P20.4"

    # --------------------------------------------------

    def build(

        self,

        repository_context,

    ):

        #
        # Health
        #

        health_score = RepositoryHealthEngine().build(

            repository_context,

        )

        #
        # Temporary placeholders
        # (Future commits replace these engines.)
        #

        maturity_score = 0.0

        stability_score = 0.0

        confidence = health_score

        #
        # Build Repository State
        #

        state = RepositoryState(

            repository=repository_context.project_name,

            repository_path=repository_context.repository_path,

            identity=repository_context.intelligence_context.identity,

            capability=repository_context.intelligence_context.capability,

            behavior=repository_context.intelligence_context.behavior,

            health_score=health_score,

            maturity_score=maturity_score,

            stability_score=stability_score,

            confidence=confidence,

        )

        #
        # Attach to Runtime Context
        #

        repository_context.repository_state = state

        return state

    # --------------------------------------------------

    def status(self):

        return {

            "engine": "Repository State Engine",

            "version": self.VERSION,

        }