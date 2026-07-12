"""
Graphify

Stage 40.0

Executive Decision Engine

Author:
Graphify Core
"""


class ExecutiveDecisionEngine:

    VERSION = "40.0"

    def decide(self, prioritized_items):

        decisions = []

        for item in prioritized_items:

            severity = item["severity"]

            recommendation = item["recommendation"]

            if severity == "HIGH":

                action = "ESCALATE"

                worker = "Repository Architect"

            elif severity == "MEDIUM":

                action = "PLAN"

                worker = "Planner"

            else:

                action = "ASSIGN"

                worker = "Testing Engineer"

            decisions.append(

                {

                    "node": item["node"],

                    "severity": severity,

                    "priority_score": item["priority_score"],

                    "action": action,

                    "assigned_worker": worker,

                    "reason": recommendation,

                }

            )

        return decisions