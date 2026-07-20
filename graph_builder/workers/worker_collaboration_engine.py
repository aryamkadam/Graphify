"""
Graphify

Phase 7

Stage P7.6

Worker Collaboration Engine

Coordinates multiple engineering workers
to collaboratively complete one
EngineeringTask.

Author:
Graphify Core
"""


class WorkerCollaborationEngine:

    VERSION = "P7.6"

    def __init__(

        self,

        coordinator,

    ):

        self.coordinator = coordinator

    # --------------------------------------------------

    def execute(

        self,

        task,

        workers,

    ):

        collaboration_log = []

        for worker in workers:

            updated_task = self.coordinator.execute(

                task,

                worker,

            )

            collaboration_log.append(

                {

                    "worker": worker.worker_name,

                    "role": worker.role,

                    "result": updated_task.actual_output,

                }

            )

        return {

            "task": task,

            "workers": len(workers),

            "collaboration_log": collaboration_log,

            "status": "COMPLETED",

            "version": self.VERSION,

        }