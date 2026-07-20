from pprint import pprint

from graph_builder.executive.executive_directive_validator import (
    ExecutiveDirectiveValidator,
)


def main():

    registry = {

        "executive_directives": [

            {

                "directive_id": "DIR-0001",

                "strategy": "Continuous Quality Expansion",

                "directive": [

                    "Improve repository quality."

                ],

            },

            {

                "directive_id": "DIR-0002",

                "strategy": "Continuous Quality Expansion",

                "directive": [

                    "Improve repository quality."

                ],

            },

            {

                "directive_id": "DIR-0003",

                "strategy": "Repository-wide Refactoring",

                "directive": [

                    "Refactor repository."

                ],

            },

            {

                "directive_id": None,

                "strategy": "Broken",

                "directive": [],

            },

        ]

    }

    result = ExecutiveDirectiveValidator().build(

        registry,

    )

    print(

        "\n========================================"

    )

    print(

        "Executive Directive Validator"

    )

    print(

        "========================================\n"

    )

    pprint(result)


if __name__ == "__main__":

    main()