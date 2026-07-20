from pprint import pprint

from graph_builder.planner.execution_planner import (
    ExecutionPlanner,
)


def main():

    dependency = {

        "dependency_graph": {

            "Repository Assessment": {

                "depends_on": []

            },

            "Architecture Analysis": {

                "depends_on": [

                    "Repository Assessment"

                ]

            },

            "Capability Expansion Planning": {

                "depends_on": [

                    "Architecture Analysis"

                ]

            },

            "Architecture Review": {

                "depends_on": [

                    "Capability Expansion Planning"

                ]

            },

            "Technical Debt Analysis": {

                "depends_on": [

                    "Architecture Review"

                ]

            },

            "Architecture Improvement Planning": {

                "depends_on": [

                    "Technical Debt Analysis"

                ]

            },

            "Engineering Opportunity Discovery": {

                "depends_on": [

                    "Architecture Improvement Planning"

                ]

            },

            "Improvement Prioritization": {

                "depends_on": [

                    "Engineering Opportunity Discovery"

                ]

            },

            "Engineering Roadmap Preparation": {

                "depends_on": [

                    "Improvement Prioritization"

                ]

            },

        }

    }

    result = ExecutionPlanner().build(

        dependency,

    )

    print("\n========================================")
    print("Execution Planner")
    print("========================================\n")

    pprint(result)


if __name__ == "__main__":
    main()