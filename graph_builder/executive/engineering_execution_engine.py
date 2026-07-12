"""
Graphify

Phase 3

Stage P3.6

Engineering Execution Engine

Executes an EngineeringPlan by assigning
tasks to the correct engineering workers.

Author:
Graphify Core
"""

from graph_builder.executive.engineering_plan import EngineeringPlan
from graph_builder.executive.worker_selection_engine import WorkerSelectionEngine


class EngineeringExecutionEngine:

    VERSION = "P3.6"

    def __init__(

        self,

        worker_registry,

    ):

        self.registry = worker_registry

        self.selector = WorkerSelectionEngine(

        self.registry

)
    # --------------------------------------------------

    def execute(

        self,

        plan: EngineeringPlan,

    ):

        report = []

        tasks = plan.tasks

        roles = plan.assigned_roles

        for task, role in zip(tasks, roles):

            selection = self.selector.select(role)

            if selection["status"] != "SELECTED":

                report.append({

                    "task": task,

                    "status": "FAILED",

                    "reason": "No suitable worker",

                })

                continue

            worker = self.registry.get(

                selection["worker"]

            )

            result = worker.execute(task)

            report.append(result)

        return {

            "objective": plan.objective,

            "completed_tasks": len(report),

            "report": report,

            "version": self.VERSION,

        }