"""
Graphify

Phase 8

Stage P8.6

Runtime Engine

Coordinates one autonomous
engineering runtime.

Author:
Graphify Core
"""

from graph_builder.runtime.repository_observer import RepositoryObserver
from graph_builder.runtime.autonomous_runtime_scheduler import (
    AutonomousRuntimeScheduler,
)
from graph_builder.runtime.engineering_cycle import EngineeringCycle


class RuntimeEngine:

    VERSION = "P8.6"

    def __init__(self):

        self.observer = RepositoryObserver()

        self.scheduler = AutonomousRuntimeScheduler()

    # --------------------------------------------------

    def execute(

        self,

        repository_snapshot,

    ):

        event = self.observer.observe(

            repository_snapshot,

        )

        decision = self.scheduler.evaluate(

            event.to_dict(),

        )

        if not decision["requires_cycle"]:

            return {

                "runtime_status": "NO_ENGINEERING",

                "event": event.to_dict(),

                "version": self.VERSION,

            }

        cycle = EngineeringCycle(

            strategy="Continuous Quality Expansion",

        )

        cycle.start()

        return {

            "runtime_status": "ENGINEERING_STARTED",

            "event": event.to_dict(),

            "cycle": cycle.summary(),

            "version": self.VERSION,

        }