"""
Graphify

Phase 15

Stage P15.1

Repository Understanding Engine Test

Author:
Graphify Core
"""

from pprint import pprint

from graph_builder.intelligence.repository_identity import (
    RepositoryIdentity,
)

from graph_builder.reasoning.repository_goal_engine import (
    RepositoryGoalEngine,
)

from graph_builder.reasoning.repository_mission_engine import (
    RepositoryMissionEngine,
)

from graph_builder.understanding.repository_understanding_engine import (
    RepositoryUnderstandingEngine,
)


print("=" * 40)
print("Repository Understanding Engine")
print("=" * 40)

# --------------------------------------------------

identity = RepositoryIdentity(

    repository="graphify",

    identity="Autonomous Engineering Brain",

    engineering_type="Engineering AI",

    confidence=0.99,

    capabilities=[

        "Knowledge",

        "Memory",

        "Decision",

    ],

)

# --------------------------------------------------

mission_engine = RepositoryMissionEngine()

mission = mission_engine.build(identity)

# --------------------------------------------------

goal_engine = RepositoryGoalEngine()

goals = goal_engine.build(mission)

# --------------------------------------------------

engine = RepositoryUnderstandingEngine()

understanding = engine.build_understanding(

    repository="graphify",

    identity=identity,

    mission=mission,

    goals=goals,

)

# --------------------------------------------------

print("\nUnderstanding Summary\n")

pprint(

    understanding.summary()

)

# --------------------------------------------------

print("\nRepository Understanding\n")

pprint(

    vars(understanding)

)

# --------------------------------------------------

print("\nEngine Status\n")

pprint(

    engine.status()

)