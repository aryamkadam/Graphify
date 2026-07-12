"""
Graphify

Phase 3

Stage P3.9

Worker Bootstrap Engine

Responsible for assembling fully
intelligent engineering workers.

Author:
Graphify Core
"""

from graph_builder.workers.worker_identity import WorkerIdentity
from graph_builder.workers.worker_memory import WorkerMemory
from graph_builder.workers.worker_learning import WorkerLearning
from graph_builder.workers.worker_experience import WorkerExperience
from graph_builder.workers.worker_goals import WorkerGoals
from graph_builder.workers.worker_decision_engine import (
    WorkerDecisionEngine,
)


class WorkerBootstrapEngine:

    VERSION = "P3.9"

    # --------------------------------------------------

    def bootstrap(

        self,

        worker,

        role,

    ):

        worker.identity = WorkerIdentity(

            worker.name,

            role,

        )

        worker.memory = WorkerMemory()

        worker.learning = WorkerLearning()

        worker.experience = WorkerExperience()

        worker.goals = WorkerGoals()

        worker.decision = WorkerDecisionEngine(

            worker.identity,

            worker.memory,

            worker.learning,

            worker.experience,

            worker.goals,

        )

        return worker