from pprint import pprint

from graph_builder.executive.repository_strategy_engine import RepositoryStrategyEngine
from graph_builder.executive.repository_priority_engine import RepositoryPriorityEngine
from graph_builder.executive.repository_executive_planner import RepositoryExecutivePlanner
from graph_builder.executive.repository_executive_decision_engine import RepositoryExecutiveDecisionEngine
from graph_builder.executive.repository_executive_brain import RepositoryExecutiveBrain

consciousness = {
    "repository_identity": {
        "phase": "Stabilization",
        "technical_direction": "Positive",
        "brain_state": "Growing",
    }
}

knowledge = {
    "knowledge_confidence": 0.95,
    "repository_knowledge":
        "Continuous refactoring improves repository quality."
}

experience = {
    "experience_level": "Junior"
}

strategy = RepositoryStrategyEngine().build(
    consciousness,
    knowledge,
    experience,
)

priorities = RepositoryPriorityEngine().build(
    strategy,
    consciousness,
    knowledge,
)

planner = RepositoryExecutivePlanner().build(
    strategy,
    priorities,
    consciousness,
)

decision = RepositoryExecutiveDecisionEngine().build(
    planner,
    consciousness,
    knowledge,
    experience,
)

brain = RepositoryExecutiveBrain().build(
    consciousness,
    experience,
    knowledge,
    strategy,
    priorities,
    planner,
    decision,
)

print("\n========================================")
print("Repository Executive Brain")
print("========================================\n")

pprint(brain)