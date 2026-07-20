"""
Graphify

Phase 6

Stage P6.2

Task Decomposition Engine

Transforms executive directives into
engineering work packages.

Author:
Graphify Core
"""


class TaskDecompositionEngine:

    VERSION = "P6.2"

    # --------------------------------------------

    def build(

        self,

        planning_report,

    ):

        work_packages = []

        directives = planning_report.get(

            "directives",

            [],

        )

        for directive in directives:

            work_packages.extend(

                self._expand(

                    directive,

                )

            )

        return {

            "work_packages":

                work_packages,

            "count":

                len(

                    work_packages,

                ),

            "summary":

                (

                    f"{len(work_packages)} engineering "

                    f"work packages generated."

                ),

            "version":

                self.VERSION,

        }

    # --------------------------------------------

    def _expand(

        self,

        directive,

    ):

        mapping = {

            "Expand repository engineering capabilities.": [

                "Repository Assessment",

                "Architecture Analysis",

                "Capability Expansion Planning",

            ],

            "Increase architectural quality.": [

                "Architecture Review",

                "Technical Debt Analysis",

                "Architecture Improvement Planning",

            ],

            "Continue engineering improvements.": [

                "Engineering Opportunity Discovery",

                "Improvement Prioritization",

                "Engineering Roadmap Preparation",

            ],

        }

        return mapping.get(

            directive,

            [

                "General Engineering Planning",

            ],

        )