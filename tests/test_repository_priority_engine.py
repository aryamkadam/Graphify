from pprint import pprint

from graph_builder.executive.repository_strategy_engine import (
    RepositoryStrategyEngine,
)

from graph_builder.executive.repository_priority_engine import (
    RepositoryPriorityEngine,
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

strategy = RepositoryStrategyEngine().build(

    consciousness,

    knowledge,

    experience,

)

priority = RepositoryPriorityEngine().build(

    strategy,

    consciousness,

    knowledge,

)

print("\n========================================")
print("Repository Priority Engine")
print("========================================\n")

pprint(priority)