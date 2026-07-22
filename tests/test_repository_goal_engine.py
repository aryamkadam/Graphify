from pprint import pprint

from graph_builder.cognition.repository_mission import (
    RepositoryMission,
)

from graph_builder.reasoning.repository_goal_engine import (
    RepositoryGoalEngine,
)

print("=" * 40)
print("Repository Goal Engine")
print("=" * 40)

mission = RepositoryMission(

    repository="graphify",

    identity="Autonomous Engineering Brain",

    mission=(
        "Continuously understand, "
        "reason about, improve and "
        "autonomously evolve software repositories."
    ),

    engineering_scope="Repository Engineering",

    confidence=0.97,

)

engine = RepositoryGoalEngine()

goal = engine.build(mission)

print()

print("Goals")

print()

pprint(goal.to_dict())