from pprint import pprint

from graph_builder.intelligence.repository_learning_engine import (
    RepositoryLearningEngine,
)


def main():

    history = [

        {

            "health": {"delta": 5},

            "execution": {"delta": 20},

            "knowledge": {

                "dead_code": {"delta": -2},

                "hotspots": {"delta": -1}

            }

        },

        {

            "health": {"delta": 4},

            "execution": {"delta": 15},

            "knowledge": {

                "dead_code": {"delta": -1},

                "hotspots": {"delta": -2}

            }

        },

        {

            "health": {"delta": 3},

            "execution": {"delta": 18},

            "knowledge": {

                "dead_code": {"delta": -1},

                "hotspots": {"delta": -1}

            }

        }

    ]

    learning = (

        RepositoryLearningEngine()

        .build(history)

    )

    print("\nRepository Learning\n")

    pprint(learning)


if __name__ == "__main__":

    main()