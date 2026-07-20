from pprint import pprint

from graph_builder.executive.executive_recall_engine import (
    ExecutiveRecallEngine,
)


def main():

    executive_memory = {

        "executive_memory": [

            {

                "adaptation_strategy":
                    "Continuous Quality Expansion",

                "priority":
                    "HIGH",

            },

            {

                "adaptation_strategy":
                    "Continuous Quality Expansion",

                "priority":
                    "HIGH",

            },

            {

                "adaptation_strategy":
                    "Repository-wide Refactoring",

                "priority":
                    "MEDIUM",

            },

        ]

    }

    executive_index = {

        "index": {

            "strategy": {

                "Continuous Quality Expansion": [0, 1],

                "Repository-wide Refactoring": [2],

            }

        }

    }

    engine = ExecutiveRecallEngine()

    report = engine.recall_by_strategy(

        executive_memory,

        executive_index,

        "Continuous Quality Expansion",

    )

    print("\n========================================")
    print("Executive Recall Engine")
    print("========================================\n")

    pprint(report)

    print("\nLatest Executive Memory\n")

    pprint(

        engine.latest(

            executive_memory

        )

    )


if __name__ == "__main__":

    main()