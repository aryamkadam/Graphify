"""
Graphify

Phase 6

Stage P6.5

Worker Assignment Engine

Assigns engineering ownership for
planned work packages.

Author:
Graphify Core
"""


class WorkerAssignmentEngine:

    VERSION = "P6.5"

    # --------------------------------------------------

    def build(

        self,

        execution_report,

    ):

        assignments = []

        execution_order = execution_report.get(

            "execution_order",

            [],

        )

        for package in execution_order:

            assignments.append(

                {

                    "work_package": package,

                    "assigned_worker":

                        self._assign_worker(

                            package,

                        ),

                }

            )

        return {

            "assignments":

                assignments,

            "workers_used":

                len(

                    {

                        a["assigned_worker"]

                        for a in assignments

                    }

                ),

            "summary":

                (

                    f"{len(assignments)} work packages "

                    f"assigned."

                ),

            "version":

                self.VERSION,

        }

    # --------------------------------------------------

    def _assign_worker(

        self,

        package,

    ):

        if "Assessment" in package:

            return "Repository Architect"

        if "Architecture" in package:

            return "Repository Architect"

        if "Technical Debt" in package:

            return "Code Engineer"

        if "Roadmap" in package:

            return "Planning Worker"

        if "Planning" in package:

            return "Planning Worker"

        if "Prioritization" in package:

            return "Planning Worker"

        return "Engineering Worker"