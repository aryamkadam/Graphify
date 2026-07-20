from pprint import pprint

from graph_builder.executive.executive_brain import (
    ExecutiveBrain,
)


def main():

    consciousness = {

        "repository_identity": {

            "phase": "Stabilization",

            "technical_direction": "Positive",

        }

    }

    knowledge = {

        "knowledge_confidence": 0.95,

    }

    experience = {

        "experience_level": "Senior",

    }

    brain = ExecutiveBrain()

    result = brain.think(

        consciousness,

        knowledge,

        experience,

    )

    print("\n========================================")

    print("Executive Brain")

    print("========================================\n")

    pprint(result)

    print("\nExecutive Memory\n")

    pprint(

        brain.executive_memory()

    )

    print("\nSummary\n")

    pprint(

        brain.summary()

    )


if __name__ == "__main__":

    main()