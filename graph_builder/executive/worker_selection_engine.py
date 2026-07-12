"""
Graphify

Stage 59.3

Worker Selection Engine

Responsible for selecting the correct
engineering worker based on task type.

Author:
Graphify Core
"""

from graph_builder.workers.worker_registry import WorkerRegistry


class WorkerSelectionEngine:

    VERSION = "59.3"

    def __init__(self, registry: WorkerRegistry):

        self.registry = registry

        self.role_map = {

            "architecture": "Repository Architect",

            "implementation": "Code Engineer",

            "testing": "Testing Engineer",

        }

    # --------------------------------------------------

    def select(

        self,

        task_type,

    ):

        worker_name = self.role_map.get(task_type)

        if worker_name is None:

            return {

                "status": "NO_MATCH",

                "task_type": task_type,

                "version": self.VERSION,

            }

        worker = self.registry.get(worker_name)

        if worker is None:

            return {

                "status": "WORKER_NOT_FOUND",

                "worker": worker_name,

                "version": self.VERSION,

            }

        return {

            "status": "SELECTED",

            "task_type": task_type,

            "worker": worker.name,

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def supported_roles(self):

        return list(self.role_map.keys())

    # --------------------------------------------------

    def status(self):

        return {

            "roles": len(self.role_map),

            "supported_roles": self.supported_roles(),

            "version": self.VERSION,

        }