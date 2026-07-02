"""
Stage 19.5.3

Repository AI Export Engine
Integration Test
"""

from pprint import pprint

from graph_builder.context.repository_ai_export_engine import (
    RepositoryAIExportEngine,
)

engine = RepositoryAIExportEngine()

executive_brain = {

    "identity": {

        "brain_state": "Growing",

        "phase": "Stabilization",

        "technical_direction": "Positive",

    },

    "strategy": {

        "engineering_strategy": "Repository-wide Refactoring",

    },

    "priorities": {

        "highest_priority": {

            "task": "Remove Technical Debt",

        }

    },

    "planner": {

        "summary": "3 engineering sprints generated.",

    },

    "decision": {

        "next_engineering_action": "Remove Technical Debt",

    },

    "future_direction": "Remove Technical Debt",

    "summary": "Repository Executive Brain ready.",

}

repository_memory = {

    "memory_strength": 0.6,

}

repository_story = {

    "summary": "Repository has evolved positively.",

}

repository_consciousness = {

    "phase": "Stabilization",

}

print("\n========================================")
print("Repository AI Export Engine")
print("========================================\n")

result = engine.export(

    executive_brain,

    repository_memory,

    repository_story,

    repository_consciousness,

    target_ai="chatgpt",

)

pprint(result)

print("\n========================================")
print("Transfer Package")
print("========================================\n")

pprint(result["package"])