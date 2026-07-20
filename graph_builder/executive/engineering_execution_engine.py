"""
Graphify

Phase 5

Stage P5.0

Engineering Execution Engine

Universal execution engine capable of executing:

- EngineeringPlan objects
- Sprint dictionaries

Author:
Graphify Core
"""

from graph_builder.executive.worker_selection_engine import (
    WorkerSelectionEngine,
)


class EngineeringExecutionEngine:

    VERSION = "P5.0"

    def __init__(
        self,
        worker_registry,
    ):

        self.registry = worker_registry

        self.selector = WorkerSelectionEngine(
            self.registry
        )

    # --------------------------------------------------

    def _extract_plan(self, plan):

        """
        Supports both:

        EngineeringPlan

        and

        Sprint dictionaries.
        """

        # Dictionary Sprint
        if isinstance(plan, dict):

            objective = plan.get(
                "objective",
                "Engineering Sprint",
            )

            tasks = plan.get(
                "tasks",
                [],
            )

            assigned_roles = []

            for task in tasks:

                assigned_roles.append(

                    task.get(
                        "role",
                        "implementation",
                    )

                )

            return objective, tasks, assigned_roles

        # EngineeringPlan Object

        return (

            plan.objective,

            plan.tasks,

            plan.assigned_roles,

        )

    # --------------------------------------------------

    def execute(
        self,
        plan,
    ):

        objective, tasks, roles = self._extract_plan(
            plan
        )

        report = []

        for task, role in zip(tasks, roles):

            # Sprint dictionaries contain task dictionaries
            if isinstance(task, dict):

                task_title = task.get(
                    "title",
                    "Unnamed Task",
                )

            else:

                task_title = task

            selection = self.selector.select(
                role
            )

            if selection["status"] != "SELECTED":

                report.append(

                    {

                        "task": task_title,

                        "status": "FAILED",

                        "reason": "No suitable worker",

                    }

                )

                continue

            worker = self.registry.get(

                selection["worker"]

            )

            result = worker.execute(

                task_title

            )

            report.append(

                result

            )

        return {

            "objective": objective,

            "completed_tasks": len(report),

            "report": report,

            "version": self.VERSION,

        }