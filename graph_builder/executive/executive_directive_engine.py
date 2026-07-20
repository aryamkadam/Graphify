"""
Graphify

Phase 5

Stage P5.13

Executive Directive Engine

Transforms executive decisions into
high-level engineering directives.

The Directive Engine does NOT execute
work.

It communicates executive intent.

Author:
Graphify Core
"""


class ExecutiveDirectiveEngine:

    VERSION = "P5.13"

    # --------------------------------------------

    def build(

        self,

        executive_decision,

    ):

        strategy = executive_decision.get(

            "recommended_next_action",

            "Unknown",

        )

        priority = executive_decision.get(

            "priority",

            "MEDIUM",

        )

        confidence = executive_decision.get(

            "confidence",

            0.5,

        )

        directive = self._generate_directive(

            strategy,

        )

        return {

            "directive": directive,

            "strategy": strategy,

            "priority": priority,

            "confidence": confidence,

            "status": "READY",

            "summary": (

                f"Executive directive generated for "

                f"'{strategy}'."

            ),

            "version": self.VERSION,

        }

    # --------------------------------------------

    def _generate_directive(

        self,

        strategy,

    ):

        mapping = {

            "Continuous Quality Expansion": [

                "Expand repository engineering capabilities.",

                "Increase architectural quality.",

                "Continue engineering improvements.",

            ],

            "Repository-wide Refactoring": [

                "Refactor critical repository modules.",

                "Reduce architectural complexity.",

                "Improve maintainability.",

            ],

            "Controlled Feature Expansion": [

                "Expand repository features carefully.",

                "Protect repository stability.",

            ],

            "Aggressive Technical Debt Reduction": [

                "Reduce technical debt.",

                "Prioritize repository cleanup.",

            ],

        }

        return mapping.get(

            strategy,

            [

                "Monitor repository evolution."

            ],

        )