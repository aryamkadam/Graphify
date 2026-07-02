from pprint import pprint

from graph_builder.context.universal_repository_context import (
    UniversalRepositoryContext,
)

executive_brain = {

    "identity": {
        "phase": "Stabilization",
        "technical_direction": "Positive",
        "brain_state": "Growing",
    },

    "strategy": {
        "engineering_strategy":
            "Repository-wide Refactoring",
    },

    "priorities": {

        "highest_priority": {

            "task":
                "Remove Technical Debt"

        }

    },

    "planner": {

        "summary":
            "3 engineering sprints generated."

    },

    "decision": {

        "next_engineering_action":
            "Remove Technical Debt"

    },

    "future_direction":
        "Remove Technical Debt",

    "summary":
        "Repository Executive Brain ready."

}

repository_memory = {

    "memory_strength": 0.60

}

repository_story = {

    "summary":
        "Repository has evolved positively."

}

repository_consciousness = {

    "phase":
        "Stabilization"

}

context = UniversalRepositoryContext().build(

    executive_brain,

    repository_memory,

    repository_story,

    repository_consciousness,

)

print("\n========================================")
print("Universal Repository Context")
print("========================================\n")

pprint(context)