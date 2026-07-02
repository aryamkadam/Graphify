from pprint import pprint

from graph_builder.context.universal_repository_context import (
    UniversalRepositoryContext,
)

from graph_builder.context.adapters.claude_adapter import (
    ClaudeAdapter,
)

executive_brain = {

    "identity": {

        "phase": "Stabilization",

        "technical_direction": "Positive",

        "brain_state": "Growing",

    },

    "strategy": {

        "engineering_strategy":
        "Repository-wide Refactoring"

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

memory = {

    "memory_strength": 0.60

}

story = {

    "summary":
    "Repository has evolved positively."

}

consciousness = {

    "phase":
    "Stabilization"

}

context = UniversalRepositoryContext().build(

    executive_brain,

    memory,

    story,

    consciousness,

)

adapter = ClaudeAdapter()

print("\n========================================")
print("Claude Adapter")
print("========================================\n")

pprint(

    adapter.adapt(

        context

    )

)