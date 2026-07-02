from pprint import pprint

from graph_builder.context.repository_reconstruction_engine import (
    RepositoryReconstructionEngine,
)

engine = RepositoryReconstructionEngine()

context = {

    "repository_identity": {
        "brain_state": "Growing",
        "phase": "Stabilization",
        "technical_direction": "Positive",
    },

    "repository_strategy": {
        "engineering_strategy": "Repository-wide Refactoring",
    },

    "repository_priorities": {
        "highest_priority": {
            "task": "Remove Technical Debt",
        }
    },

    "repository_planner": {
        "summary": "3 engineering sprints generated.",
    },

    "repository_decision": {
        "next_engineering_action": "Remove Technical Debt",
    },

    "repository_memory": {
        "memory_strength": 0.6,
    },

    "repository_story": {
        "summary": "Repository has evolved positively.",
    },

}

print("\n========================================")
print("Repository Reconstruction Engine")
print("========================================\n")

repository = engine.reconstruct(

    context,

)

pprint(repository)