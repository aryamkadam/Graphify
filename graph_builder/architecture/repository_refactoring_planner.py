"""
Graphify

Phase 11

Stage P11.8

Repository Refactoring Planner

Converts architecture diagnostics into
engineering migration plans.

Author:
Graphify Core
"""

from datetime import datetime


class RepositoryRefactoringPlanner:

    VERSION = "P11.8"

    def build_plan(self, diagnostics):

        migrations = []

        priorities = []

        for issue in diagnostics:

            category = issue["category"]

            if category == "Duplicate Responsibility":

                migrations.append(

                    self._duplicate_plan(issue)

                )

                priorities.append("HIGH")

            elif category == "Oversized Layer":

                migrations.append(

                    self._layer_plan(issue)

                )

                priorities.append("MEDIUM")

        return {

            "created_at": datetime.utcnow().isoformat() + "Z",

            "version": self.VERSION,

            "migration_count": len(migrations),

            "overall_priority": self._overall_priority(priorities),

            "plans": migrations,

        }

    # -------------------------------------------------

    def _duplicate_plan(self, issue):

        component = issue["affected_components"]

        return {

            "type": "MERGE",

            "severity": issue["severity"],

            "goal": "Create single engineering owner",

            "targets": component,

            "recommended_fix": issue["recommended_fix"],

        }

    # -------------------------------------------------

    def _layer_plan(self, issue):

        return {

            "type": "SPLIT",

            "severity": issue["severity"],

            "goal": "Reduce architectural complexity",

            "targets": issue["affected_components"],

            "recommended_fix": issue["recommended_fix"],

        }

    # -------------------------------------------------

    def _overall_priority(self, priorities):

        if "HIGH" in priorities:

            return "HIGH"

        if "MEDIUM" in priorities:

            return "MEDIUM"

        return "LOW"