from pprint import pprint

from graph_builder.planner.task_decomposition_engine import (
    TaskDecompositionEngine,
)


def main():

    planning = {

        "directives": [

            "Expand repository engineering capabilities.",

            "Increase architectural quality.",

            "Continue engineering improvements.",

        ]

    }

    result = TaskDecompositionEngine().build(

        planning,

    )

    print("\n========================================")

    print("Task Decomposition Engine")

    print("========================================\n")

    pprint(result)


if __name__ == "__main__":

    main()