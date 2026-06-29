"""
Stage 18.2

Repository Priority Engine

Converts repository strategy into
ordered engineering priorities.

This engine determines WHAT should
be done FIRST.
"""


class RepositoryPriorityEngine:

    def build(

        self,

        strategy,

        consciousness,

        knowledge,

    ):

        priorities = self._generate_priorities(

            strategy,

            consciousness,

            knowledge,

        )

        return {

            "strategy":

                strategy["engineering_strategy"],

            "priorities": priorities,

            "highest_priority":

                priorities[0],

            "summary":

                f"{len(priorities)} engineering priorities generated."

        }

    # --------------------------------------

    def _generate_priorities(

        self,

        strategy,

        consciousness,

        knowledge,

    ):

        engineering_strategy = strategy[
            "engineering_strategy"
        ]

        priorities = []

        if engineering_strategy == \
            "Repository-wide Refactoring":

            priorities.extend([

                {

                    "priority": 1,

                    "task":
                        "Remove Technical Debt",

                    "reason":
                        "Improves long-term maintainability",

                },

                {

                    "priority": 2,

                    "task":
                        "Refactor Architectural Hotspots",

                    "reason":
                        "Reduces repository complexity",

                },

                {

                    "priority": 3,

                    "task":
                        "Improve Repository Documentation",

                    "reason":
                        "Improves AI understanding",

                },

                {

                    "priority": 4,

                    "task":
                        "Expand Execution Graph",

                    "reason":
                        "Improves Repository Brain",

                },

                {

                    "priority": 5,

                    "task":
                        "Prepare AI Context Pack",

                    "reason":
                        "Supports multi-AI transfer",

                }

            ])

        else:

            priorities.append(

                {

                    "priority": 1,

                    "task":
                        "Monitor Repository",

                    "reason":
                        "No immediate action required",

                }

            )

        return priorities