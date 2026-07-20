"""
Graphify

Phase 8

Stage P8.2

Runtime Session

Tracks the current autonomous
engineering session.

Author:
Graphify Core
"""


class RuntimeSession:

    VERSION = "P8.2"

    def __init__(self):

        self.current_cycle = None

        self.completed_cycles = 0

        self.current_strategy = None

        self.session_status = "IDLE"

    # --------------------------------------------------

    def begin(

        self,

        engineering_cycle,

    ):

        self.current_cycle = engineering_cycle

        self.current_strategy = engineering_cycle.strategy

        self.session_status = "RUNNING"

    # --------------------------------------------------

    def complete(self):

        if self.current_cycle is None:

            return

        self.completed_cycles += 1

        self.current_cycle = None

        self.current_strategy = None

        self.session_status = "IDLE"

    # --------------------------------------------------

    def summary(self):

        return {

            "session_status": self.session_status,

            "completed_cycles": self.completed_cycles,

            "current_strategy": self.current_strategy,

            "current_cycle": (

                self.current_cycle.cycle_id

                if self.current_cycle

                else None

            ),

            "version": self.VERSION,

        }