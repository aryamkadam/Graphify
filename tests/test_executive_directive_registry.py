from pprint import pprint

from graph_builder.executive.executive_directive_registry import (
    ExecutiveDirectiveRegistry,
)


def main():

    registry = ExecutiveDirectiveRegistry()

    report = {

        "strategy":

            "Continuous Quality Expansion",

        "priority":

            "MEDIUM",

        "confidence":

            0.75,

        "directive": [

            "Expand repository engineering capabilities.",

            "Increase architectural quality.",

            "Continue engineering improvements.",

        ],

    }

    registry.register(report)

    registry.register(report)

    print("\n========================================")

    print("Executive Directive Registry")

    print("========================================\n")

    pprint(registry.directives())

    print("\nSummary\n")

    pprint(registry.summary())


if __name__ == "__main__":

    main()