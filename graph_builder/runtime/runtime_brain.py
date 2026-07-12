"""
Graphify

Stage 57.1

Runtime Brain

Central runtime controller of Graphify.

Author:
Graphify Core
"""

from graph_builder.persistence.graph_persistence_engine import (
    GraphPersistenceEngine,
)

from graph_builder.engineering.engineering_experience_engine import (
    EngineeringExperienceEngine,
)

from graph_builder.executive.executive_learning_engine import (
    ExecutiveLearningEngine,
)

from graph_builder.engineering.engineering_workflow_engine import (
    EngineeringWorkflowEngine,
)

from graph_builder.workers.worker_registry import (
    WorkerRegistry,
)


class RuntimeBrain:

    VERSION = "57.1"

    def __init__(self):

        self.persistence = GraphPersistenceEngine()

        self.graph = self.persistence.load()

        self.experience = EngineeringExperienceEngine(
            self.graph
        )

        self.executive = ExecutiveLearningEngine(
            self.experience
        )

        self.workflow = EngineeringWorkflowEngine()

        # ----------------------------
        # Boot Engineering Workers
        # ----------------------------

        self.registry = WorkerRegistry()

        boot_status = self.registry.register_default_workers()

        self.worker_status = boot_status

    # --------------------------------------------------

    def boot(self):

        return {

            "status": "ONLINE",

            "graph": self.graph.status(),

            "repository_health":
                self.experience.repository_health(),

            "workers":
                self.worker_status,

            "version":
                self.VERSION,

        }

    # --------------------------------------------------

    def shutdown(self):

        self.persistence.save(self.graph)

        return {

            "status": "OFFLINE",

            "version":
                self.VERSION,

        }