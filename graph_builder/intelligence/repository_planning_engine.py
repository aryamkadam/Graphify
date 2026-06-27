"""
Stage 15.8

Repository Planning Engine

Converts repository intelligence into
an actionable engineering roadmap.

This engine determines what should
happen next inside the repository.
"""


class RepositoryPlanningEngine:

    def generate(

        self,

        brain,

        reasoning_summary,

    ):

        plan = []

        # -----------------------------

        health = brain["health"]

        knowledge = brain["knowledge"]

        execution = brain["execution"]

        executive = brain["executive_summary"]

        # -----------------------------

        if knowledge["dead_code_count"] > 0:

            plan.append({

                "priority": 1,

                "title": "Remove Dead Code",

                "reason":

                    "Dead code reduces maintainability.",

                "impact": "High"

            })

        # -----------------------------

        if knowledge["hotspot_count"] > 0:

            plan.append({

                "priority": 2,

                "title": "Stabilize Hotspot Files",

                "reason":

                    "Frequently modified files require refactoring.",

                "impact": "High"

            })

        # -----------------------------

        if len(

            knowledge["critical_symbols"]

        ) > 0:

            plan.append({

                "priority": 3,

                "title": "Protect Critical Symbols",

                "reason":

                    "Critical repository components require additional testing.",

                "impact": "Medium"

            })

        # -----------------------------

        if execution["graph_nodes"] > 250:

            plan.append({

                "priority": 4,

                "title": "Reduce Execution Complexity",

                "reason":

                    "Execution graph continues to grow.",

                "impact": "Medium"

            })

        # -----------------------------

        if health["health_score"] < 90:

            plan.append({

                "priority": 5,

                "title": "Increase Repository Health",

                "reason":

                    "Repository health should exceed 90.",

                "impact": "Medium"

            })

        # -----------------------------

        roadmap = {

            "repository":

                brain["project_name"],

            "current_health":

                health["health_score"],

            "target_health":

                95,

            "repository_direction":

                executive["project_direction"],

            "planning_summary":

                reasoning_summary["summary"],

            "recommended_actions":

                plan

        }

        return roadmap