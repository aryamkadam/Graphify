from pprint import pprint

from graph_builder.planner.engineering_planner import (
    EngineeringPlanner,
)

planner = EngineeringPlanner()

repository_brain = {

    "priorities": {

        "highest_priority": {

            "task": "Remove Technical Debt",

        }

    },

    "strategy": {

        "engineering_strategy": "Repository-wide Refactoring",

    },

}

print("\n========================================")
print("Engineering Planner")
print("========================================\n")

print("Generate Plan\n")

result = planner.generate_plan(

    repository_brain,

)

pprint(result)

print("\nBacklog\n")

pprint(

    planner.backlog_status()

)

print("\nNext Task\n")

pprint(

    planner.next_task()

)