from pprint import pprint

from graph_builder.executive.engineering_learning_engine import (
    EngineeringLearningEngine,
)


def main():

    execution = {

        "completed_tasks": 4,

        "report": [

            {

                "worker":

                    "Repository Architect",

                "task":

                    "Analyze repository architecture",

            },

            {

                "worker":

                    "Repository Architect",

                "task":

                    "Improve plugin architecture",

            },

            {

                "worker":

                    "Code Engineer",

                "task":

                    "Expand runtime capabilities",

            },

            {

                "worker":

                    "Testing Engineer",

                "task":

                    "Increase worker intelligence",

            },

        ],

    }

    learning = EngineeringLearningEngine(

        execution,

    ).build()

    print()

    print(

        "========================================"

    )

    print(

        "Engineering Learning Engine"

    )

    print(

        "========================================"

    )

    print()

    pprint(

        learning,

    )


if __name__ == "__main__":

    main()