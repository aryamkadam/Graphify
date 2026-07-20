"""
Graphify

Phase 10

Stage P10.3

Executive Planning Engine

Transforms Executive Decisions
into executable Engineering Plans.

Author:
Graphify Core
"""

from datetime import datetime
import uuid


class ExecutivePlanningEngine:

    VERSION = "P10.3"

    def generate_plan(self, decision):

        plan = {

            "plan_id": str(uuid.uuid4()),

            "decision_id": decision.decision_id,

            "objective": decision.objective,

            "priority": decision.priority,

            "created_at": datetime.utcnow().isoformat() + "Z",

            "workers": [],

            "execution_order": [],

            "status": "PLANNED",

            "version": self.VERSION,

        }

        # --------------------------------------

        if decision.decision_type == "START_ENGINEERING":

            workers = [

                "Planning Worker",

                "Architecture Worker",

                "Implementation Worker",

                "Testing Worker",

                "Documentation Worker",

            ]

        elif decision.decision_type == "START_REFACTOR":

            workers = [

                "Architecture Worker",

                "Implementation Worker",

                "Testing Worker",

            ]

        elif decision.decision_type == "OPTIMIZE_ENGINEERING":

            workers = [

                "Optimization Worker",

                "Testing Worker",

            ]

        else:

            workers = [

                "Observer",

            ]

        plan["workers"] = workers

        plan["execution_order"] = list(workers)

        return plan