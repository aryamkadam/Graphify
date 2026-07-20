from pprint import pprint

from graph_builder.planner.planning_brain import (
    PlanningBrain,
)


def main():

    executive_directive = {

        "strategy":

            "Continuous Quality Expansion",

        "directive": [

            "Expand repository engineering capabilities.",

            "Increase architectural quality.",

            "Continue engineering improvements.",

        ],

    }

    result = PlanningBrain().plan(

        executive_directive,

    )

    print(

        "\n========================================"

    )

    print(

        "Planning Brain"

    )

    print(

        "========================================\n"

    )

    pprint(result)


if __name__ == "__main__":

    main()