"""
Graphify

Phase 8

Stage P8.5

Repository Observer

Observes repository state and generates
Repository Events.

Author:
Graphify Core
"""

from graph_builder.runtime.repository_event import RepositoryEvent


class RepositoryObserver:

    VERSION = "P8.5"

    def observe(

        self,

        repository_snapshot,

    ):

        changed = repository_snapshot.get(

            "changed",

            False,

        )

        if changed:

            return RepositoryEvent(

                event_type="REPOSITORY_MODIFIED",

                reason=repository_snapshot.get(

                    "reason",

                    "Repository modified.",

                ),

                requires_engineering=True,

            )

        return RepositoryEvent(

            event_type="NO_CHANGE",

            reason="Repository unchanged.",

            requires_engineering=False,

        )