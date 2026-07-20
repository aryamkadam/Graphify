from pprint import pprint

from graph_builder.executive.executive_adaptation_engine import (
    ExecutiveAdaptationEngine,
)


def main():

    strategy = {

        "engineering_strategy":

            "Continuous Quality Expansion",

        "executive_priority":

            "HIGH",

    }

    report = (

        ExecutiveAdaptationEngine()

        .build(

            strategy

        )

    )

    print("\n========================================")
    print("Executive Adaptation Engine")
    print("========================================\n")

    pprint(report)


if __name__ == "__main__":

    main()