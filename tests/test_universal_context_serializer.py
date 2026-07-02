from pprint import pprint

from graph_builder.context.universal_repository_context import (
    UniversalRepositoryContext,
)

from graph_builder.context.universal_context_serializer import (
    UniversalContextSerializer,
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

            "task": "Remove Technical Debt"

        }

    },

    "planner": {

        "summary": "3 engineering sprints generated."

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

serializer = UniversalContextSerializer()

result = serializer.save(

    context,

)

loaded = serializer.load(

    result["file_path"]

)

print("\n========================================")
print("Universal Context Serializer")
print("========================================\n")

print("Save Result:\n")

pprint(result)

print("\nLoaded Context:\n")

pprint(loaded)