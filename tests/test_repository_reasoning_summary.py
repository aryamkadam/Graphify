from pprint import pprint

from graph_builder.intelligence.repository_reasoning_summary import (
    RepositoryReasoningSummary,
)

reasoning = {

    "health_reasoning": [

        "Repository is generally healthy but requires monitoring.",

        "Dead code is reducing maintainability."

    ],

    "execution_reasoning": [

        "Execution graph is becoming large.",

        "Execution complexity is increasing."

    ],

    "knowledge_reasoning": [

        "Repository contains unused implementation."

    ],

    "decision_reasoning": [

        "Repository preserves architectural knowledge."

    ],

    "repository_direction": [

        "Current development direction focuses on Repository Intelligence."

    ]

}

summary = RepositoryReasoningSummary().generate(reasoning)

print()

print("Repository Reasoning Summary")

print()

pprint(summary)