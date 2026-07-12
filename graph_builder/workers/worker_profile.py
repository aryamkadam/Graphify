"""
Graphify

Phase 2

Stage P2.8

Worker Profile

Centralized engineering profile
for every Graphify worker.

Author:
Graphify Core
"""

from graph_builder.workers.worker_identity import WorkerIdentity
from graph_builder.workers.worker_memory import WorkerMemory
from graph_builder.workers.worker_goals import WorkerGoals
from graph_builder.workers.worker_learning import WorkerLearning
from graph_builder.workers.worker_experience import WorkerExperience
from graph_builder.workers.worker_decision_engine import WorkerDecisionEngine


class WorkerProfile:

    VERSION = "P2.8"

    def __init__(

        self,

        worker,

        role,

    ):

        self.identity = WorkerIdentity(

            worker,

            role,

        )

        self.memory = WorkerMemory()

        self.goals = WorkerGoals()

        self.learning = WorkerLearning()

        self.experience = WorkerExperience()

        self.decision = WorkerDecisionEngine(

            self.identity,

            self.memory,

            self.goals,

            self.learning,

            self.experience,

        )

    # --------------------------------------------------

    def status(self):

        return {

            "worker": self.identity.profile()["worker"],

            "role": self.identity.profile()["role"],

            "version": self.VERSION,

        }