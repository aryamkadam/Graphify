from pprint import pprint

from graph_builder.executive.repository_strategy_engine import (
    RepositoryStrategyEngine,
)

from graph_builder.executive.repository_priority_engine import (
    RepositoryPriorityEngine,
)

from graph_builder.executive.repository_executive_planner import (
    RepositoryExecutivePlanner,
)

from graph_builder.executive.repository_executive_decision_engine import (
    RepositoryExecutiveDecisionEngine,
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

planner = RepositoryExecutivePlanner().build(
    strategy,
    priority,
    consciousness,
)

decision = RepositoryExecutiveDecisionEngine().build(
    planner,
    consciousness,
    knowledge,
    experience,
)

print("\n========================================")
print("Repository Executive Decision Engine")
print("========================================\n")

pprint(decision)