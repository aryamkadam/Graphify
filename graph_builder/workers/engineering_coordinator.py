"""
Graphify

Stage 25.2

Engineering Coordinator

Coordinates Engineering Tasks
between workers.

Author:
Graphify Core
"""

from graph_builder.workers.repository_architect_worker import RepositoryArchitectWorker
from graph_builder.workers.code_engineer_worker import CodeEngineerWorker


class EngineeringCoordinator:

    VERSION = "25.2"

    def __init__(self):

        self.architect = RepositoryArchitectWorker()

        self.engineer = CodeEngineerWorker()

    # --------------------------------------------------

    def assign(self, task):

        task.assign(

            self.architect.worker_name,

        )

        architecture = self.architect.think()

        task.assign(

            self.engineer.worker_name,

        )

        task.start()

        implementation = self.engineer.execute(

            task.title,

        )

        task.complete()

        return {

            "status": "success",

            "task": task.to_dict(),

            "architect": architecture,

            "implementation": implementation,

            "workers": [

                self.architect.worker_name,

                self.engineer.worker_name,

            ],

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def status(self):

        return {

            "workers": [

                self.architect.worker_name,

                self.engineer.worker_name,

            ],

            "version": self.VERSION,

        }