"""
Graphify

Phase 2

Worker Identity

Persistent identity for every
engineering worker.

Author:
Graphify Core
"""


class WorkerIdentity:

    VERSION = "P2.1"

    def __init__(

        self,

        name,

        role,

    ):

        self.name = name

        self.role = role

        self.experience = 0

        self.tasks_completed = 0

        self.knowledge = 0

        self.confidence = 50

        self.current_goal = None

        self.long_term_goal = None

    # ------------------------------------------

    def complete_task(self):

        self.tasks_completed += 1

        self.experience += 10

        self.knowledge += 5

        self.confidence = min(

            100,

            self.confidence + 1,

        )

    # ------------------------------------------

    def set_goal(

        self,

        goal,

    ):

        self.current_goal = goal

    # ------------------------------------------

    def set_long_term_goal(

        self,

        goal,

    ):

        self.long_term_goal = goal

    # ------------------------------------------

    def profile(self):

        return {

            "worker": self.name,

            "role": self.role,

            "experience": self.experience,

            "tasks_completed": self.tasks_completed,

            "knowledge": self.knowledge,

            "confidence": self.confidence,

            "current_goal": self.current_goal,

            "long_term_goal": self.long_term_goal,

            "version": self.VERSION,

        }