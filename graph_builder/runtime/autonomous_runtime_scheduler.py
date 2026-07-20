"""
Graphify

Phase 8

Stage P8.3

Autonomous Runtime Scheduler

Determines whether a new engineering
cycle should begin based on
repository events.

Author:
Graphify Core
"""


class AutonomousRuntimeScheduler:

    VERSION = "P8.3"

    def __init__(self):

        self.last_event = None

    # --------------------------------------------------

    def evaluate(

        self,

        repository_event,

    ):

        self.last_event = repository_event

        requires_cycle = repository_event.get(

            "requires_engineering",

            False,

        )

        return {

            "requires_cycle": requires_cycle,

            "reason": repository_event.get(

                "reason",

                "Unknown",

            ),

            "version": self.VERSION,

        }