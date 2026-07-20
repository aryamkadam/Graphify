"""
Graphify

Phase 10

Stage P10.4

Engineering Task Generator

Transforms Engineering Plans into
atomic executable tasks.

Author:
Graphify Core
"""

from datetime import datetime
import uuid


class EngineeringTaskGenerator:

    VERSION = "P10.4"

    def generate(self, plan):

        tasks = []

        previous_task = None

        for index, worker in enumerate(plan["execution_order"], start=1):

            task_id = f"TASK-{index:03d}"

            task = {

                "task_id": task_id,

                "worker": worker,

                "objective": plan["objective"],

                "priority": plan["priority"],

                "status": "PENDING",

                "created_at": datetime.utcnow().isoformat() + "Z",

                "depends_on": previous_task,

            }

            tasks.append(task)

            previous_task = task_id

        return {

            "plan_id": plan["plan_id"],

            "repository_objective": plan["objective"],

            "tasks": tasks,

            "task_count": len(tasks),

            "version": self.VERSION,

        }