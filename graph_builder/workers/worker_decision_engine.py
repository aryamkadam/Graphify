"""
Graphify

Phase 2

Stage P2.6

Worker Decision Engine

Uses worker identity, memory,
goals, learning and experience
to make engineering decisions.

Author:
Graphify Core
"""


class WorkerDecisionEngine:

    VERSION = "P2.6"

    def __init__(

        self,

        identity,

        memory,

        goals,

        learning,

        experience,

    ):

        self.identity = identity

        self.memory = memory

        self.goals = goals

        self.learning = learning

        self.experience = experience

    # --------------------------------------------------

    def decide(

        self,

        task,

    ):

        return {

            "worker": self.identity.name,

            "task": task,

            "current_goal": self.goals.current_goal,

            "knowledge_level":

                self.learning.knowledge_level(),

            "experience_level":

                self.experience.maturity(),

            "confidence":

                self.experience.confidence,

            "memory_used":

                len(

                    self.memory.recall()

                ),

            "decision":

                f"Proceed with '{task}' using accumulated engineering knowledge.",

            "version":

                self.VERSION,

        }