from pprint import pprint

from graph_builder.intelligence.repository_reasoning_builder import (
    RepositoryReasoningBuilder,
)

builder = RepositoryReasoningBuilder()

health_report = {

    "health_score": 82,

    "status": "Healthy",

    "dead_code": 5,

    "god_files": 1,

    "high_risk_symbols": [

        "build_context",

        "build_repository_brain"

    ]

}

execution = {

    "statistics": {

        "graph_nodes": 620,

        "execution_paths": 390,

        "reverse_call_entries": 270

    }

}

knowledge = {

    "critical_symbols": [

        "repository_brain",

        "execution_engine"

    ],

    "dead_code_count": 5,

    "hotspot_count": 10

}

decisions = {

    "decision_count": 18

}

insights = {

    "dominant_area": "Repository Intelligence"

}

reasoning = builder.build(

    health_report,

    execution,

    knowledge,

    decisions,

    insights

)

print()

print("Repository Reasoning")

print()

pprint(reasoning)