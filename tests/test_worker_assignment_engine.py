from pprint import pprint

from graph_builder.planner.worker_assignment_engine import (
    WorkerAssignmentEngine,
)


def main():

    execution = {

        "execution_order": [

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

    result = WorkerAssignmentEngine().build(

        execution,

    )

    print("\n========================================")
    print("Worker Assignment Engine")
    print("========================================\n")

    pprint(result)


if __name__ == "__main__":
    main()