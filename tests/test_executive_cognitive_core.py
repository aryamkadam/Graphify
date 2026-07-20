from pprint import pprint

from graph_builder.executive.executive_cognitive_core import (
    ExecutiveCognitiveCore,
)

from graph_builder.executive.executive_memory_engine import (
    ExecutiveMemoryEngine,
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

    memory = ExecutiveMemoryEngine()

    core = ExecutiveCognitiveCore(

        memory,

    )

    result = core.execute(

        consciousness,

        knowledge,

        experience,

    )

    print("\n========================================")

    print("Executive Cognitive Core")

    print("========================================\n")

    pprint(result)


if __name__ == "__main__":

    main()