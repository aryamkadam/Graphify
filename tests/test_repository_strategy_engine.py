from pprint import pprint

from graph_builder.executive.repository_strategy_engine import (
    RepositoryStrategyEngine,
)

consciousness = {

    "repository_identity": {

        "phase": "Stabilization",

        "technical_direction": "Positive",

    }

}

knowledge = {

    "knowledge_confidence": 0.95

}

experience = {

    "experience_level": "Junior"

}

report = RepositoryStrategyEngine().build(

    consciousness,

    knowledge,

    experience,

)

print("\n========================================")
print("Repository Strategy Engine")
print("========================================\n")

pprint(report)