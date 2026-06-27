"""
Stage 15.7.1

Test Repository Reasoning Rules
"""

from pprint import pprint

from graph_builder.intelligence.repository_reasoning_rules import (
    RepositoryReasoningRules,
)


rules = RepositoryReasoningRules()


health_report = {

    "health_score": 82,

    "status": "Healthy",

    "dead_code": 6,

    "god_files": 2,

    "high_risk_symbols": [

        "build_context",

        "build_knowledge_graph"

    ]

}


execution = {

    "statistics": {

        "graph_nodes": 540,

        "execution_paths": 335,

        "reverse_call_entries": 248

    }

}


knowledge = {

    "critical_symbols": [

        "build_context",

        "repository_brain"

    ],

    "dead_code_count": 6,

    "hotspot_count": 12

}


decisions = {

    "decision_count": 17

}


insights = {

    "dominant_area": "Repository Intelligence"

}


print()

print("Health Reasoning")

print()

pprint(

    rules.analyze_health(

        health_report

    )

)

print()

print("Execution Reasoning")

print()

pprint(

    rules.analyze_execution(

        execution

    )

)

print()

print("Knowledge Reasoning")

print()

pprint(

    rules.analyze_knowledge(

        knowledge

    )

)

print()

print("Decision Reasoning")

print()

pprint(

    rules.analyze_decisions(

        decisions

    )

)

print()

print("Repository Direction")

print()

pprint(

    rules.analyze_repository_direction(

        insights

    )

)