"""
Graphify

Phase 3

Stage P3.3

Executive Reasoning Engine

Produces explainable engineering
decisions based on repository state.

Author:
Graphify Core
"""


class ExecutiveReasoningEngine:

    VERSION = "P3.3"

    def __init__(self, experience_engine):

        self.experience = experience_engine

    # --------------------------------------------------

    def reason(self):

        health = self.experience.repository_health()

        repository_state = health["health"]

        if repository_state == "GROWING":

            strategy = "EXPANSION"

            priority = "HIGH"

            reasons = [

                "Repository architecture is stable.",

                "Engineering capacity can be expanded.",

            ]

            recommendation = (

                "Prioritize new engineering capabilities."

            )

        elif repository_state == "PRINCIPAL":

            strategy = "OPTIMIZATION"

            priority = "MEDIUM"

            reasons = [

                "Repository has reached high maturity.",

            ]

            recommendation = (

                "Focus on optimization and innovation."

            )

        else:

            strategy = "STABILIZATION"

            priority = "CRITICAL"

            reasons = [

                "Repository maturity is low.",

            ]

            recommendation = (

                "Stabilize engineering foundation."

            )

        return {

            "strategy": strategy,

            "priority": priority,

            "repository_health": repository_state,

            "reasons": reasons,

            "recommendation": recommendation,

            "version": self.VERSION,

        }