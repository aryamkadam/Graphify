from pprint import pprint

from graph_builder.history.repository_evolution_story_engine import (
    RepositoryEvolutionStoryEngine,
)


def main():

    evolution = {

        "summary":

            "Repository health improved. "

            "Execution graph expanded. "

            "Dead code decreased.",

        "health": {

            "delta": 6

        }

    }

    reasoning = {

        "engineering_direction":

            "Engineering effort is improving quality "

            "while expanding repository capabilities.",

        "repository_momentum":

            "Positive"

    }

    story = (

        RepositoryEvolutionStoryEngine()

        .build(

            evolution,

            reasoning

        )

    )

    print("\nRepository Evolution Story\n")

    pprint(story)


if __name__ == "__main__":

    main()