from pprint import pprint

from graph_builder.executive.executive_memory_engine import (
    ExecutiveMemoryEngine,
)


def main():

    memory = ExecutiveMemoryEngine()

    report = {

        "adaptation_strategy":

            "Continuous Quality Expansion",

        "priority":

            "HIGH",

        "executive_adaptations": [

            "Increase investment in repository quality.",

            "Favor architectural improvements.",

        ],

    }

    memory.remember(

        report

    )

    print("\n========================================")
    print("Executive Memory Engine")
    print("========================================\n")

    print("Latest Decision\n")

    pprint(

        memory.latest()

    )

    print("\nSummary\n")

    pprint(

        memory.summary()

    )

    print("\nExport\n")

    pprint(

        memory.export()

    )


if __name__ == "__main__":

    main()