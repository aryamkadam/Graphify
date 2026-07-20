from pprint import pprint

from graph_builder.executive.executive_index_engine import (
    ExecutiveIndexEngine,
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

    report = (

        ExecutiveIndexEngine()

        .build(

            executive_memory

        )

    )

    print("\n========================================")
    print("Executive Index Engine")
    print("========================================\n")

    pprint(report)


if __name__ == "__main__":

    main()