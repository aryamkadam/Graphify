from pprint import pprint

from graph_builder.executive.executive_directive_engine import (
    ExecutiveDirectiveEngine,
)


def main():

    executive_decision = {

        "recommended_next_action":

            "Continuous Quality Expansion",

        "priority":

            "MEDIUM",

        "confidence":

            0.75,

    }

    report = ExecutiveDirectiveEngine().build(

        executive_decision,

    )

    print(

        "\n========================================"

    )

    print(

        "Executive Directive Engine"

    )

    print(

        "========================================\n"

    )

    pprint(report)


if __name__ == "__main__":

    main()