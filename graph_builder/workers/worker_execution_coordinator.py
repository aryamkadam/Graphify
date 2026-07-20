"""
Graphify

Phase 7

Stage P7.5

Worker Execution Coordinator

Coordinates EngineeringTask execution.

Responsibilities
----------------
- Assign EngineeringTask to a worker
- Control worker lifecycle
- Collect execution results
- Return updated EngineeringTask

Author:
Graphify Core
"""


class WorkerExecutionCoordinator:

    VERSION = "P7.5"

    # --------------------------------------------------

    def execute(

        self,

        task,

        worker,

    ):

        # ------------------------------------------
        # Assign Engineering Task
        # ------------------------------------------

        task.assign(

            worker.worker_name,

        )

        worker.assign(

            task.title,

        )

        # ------------------------------------------
        # Begin Execution
        # ------------------------------------------

        task.start()

        worker.start()

        # ------------------------------------------
        # Execute Worker Logic
        # ------------------------------------------

        result = self._execute_worker(

            task,

            worker,

        )

        # ------------------------------------------
        # Complete Task
        # ------------------------------------------

        task.complete(

            result,

        )

        worker.complete(

            result,

        )

        return task

    # --------------------------------------------------

    def _execute_worker(

        self,

        task,

        worker,

    ):

        """
        Temporary execution simulator.

        Future versions (Phase 8+) will
        invoke the worker's real engineering
        implementation.

        Current purpose is to validate
        the execution pipeline.
        """

        role = worker.role.lower()

        if role == "architecture":

            return (

                f"{worker.worker_name} completed "

                f"'{task.title}'."

            )

        elif role == "implementation":

            return (

                f"{worker.worker_name} prepared "

                f"implementation for "

                f"'{task.title}'."

            )

        elif role == "planning":

            return (

                f"{worker.worker_name} planned "

                f"'{task.title}'."

            )

        elif role == "engineering":

            return (

                f"{worker.worker_name} finished "

                f"engineering work for "

                f"'{task.title}'."

            )

        return (

            f"{worker.worker_name} executed "

            f"'{task.title}'."

        )