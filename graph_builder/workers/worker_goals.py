"""
Graphify

Phase 2

Stage P2.3

Worker Goals Engine

Stores engineering objectives for
every worker.

Author:
Graphify Core
"""


class WorkerGoals:

    VERSION = "P2.3"

    def __init__(self):

        self.current_goal = None

        self.long_term_goal = None

        self.progress = 0

    # --------------------------------------------------

    def set_current_goal(

        self,

        goal,

    ):

        self.current_goal = goal

        self.progress = 0

    # --------------------------------------------------

    def set_long_term_goal(

        self,

        goal,

    ):

        self.long_term_goal = goal

    # --------------------------------------------------

    def update_progress(

        self,

        amount,

    ):

        self.progress += amount

        self.progress = max(

            0,

            min(

                100,

                self.progress,

            ),

        )

    # --------------------------------------------------

    def completed(self):

        return self.progress >= 100

    # --------------------------------------------------

    def profile(self):

        return {

            "current_goal": self.current_goal,

            "long_term_goal": self.long_term_goal,

            "progress": self.progress,

            "completed": self.completed(),

            "version": self.VERSION,

        }