from pprint import pprint

from graph_builder.planner.dependency_graph_engine import (
    DependencyGraphEngine,
)


def main():

    decomposition = {

        "work_packages": [

            "Repository Assessment",

            "Architecture Analysis",

            "Capability Expansion Planning",

            "Architecture Review",

            "Technical Debt Analysis",

            "Architecture Improvement Planning",

            "Engineering Opportunity Discovery",

            "Improvement Prioritization",

            "Engineering Roadmap Preparation",

        ]

    }

    result = DependencyGraphEngine().build(

        decomposition,

    )

    print("\n========================================")
    print("Dependency Graph Engine")
    print("========================================\n")

    pprint(result)


if __name__ == "__main__":
    main()