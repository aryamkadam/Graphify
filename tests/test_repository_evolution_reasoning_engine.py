from pprint import pprint

from graph_builder.reasoning.repository_evolution_reasoning_engine import (
    RepositoryEvolutionReasoningEngine,
)


def main():

    evolution = {

        "health": {
            "status": "improved",
            "delta": 6
        },

        "execution": {
            "status": "expanded",
            "delta": 60
        },

        "knowledge": {

            "dead_code": {
                "delta": -3
            },

            "hotspots": {
                "delta": -2
            }

        }

    }

    reasoning = RepositoryEvolutionReasoningEngine(
        evolution
    ).build()

    print("\nRepository Evolution Reasoning\n")

    pprint(reasoning)


if __name__ == "__main__":
    main()