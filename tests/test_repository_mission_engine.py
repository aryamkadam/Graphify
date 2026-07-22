from pprint import pprint

from graph_builder.intelligence.repository_identity import (
    RepositoryIdentity,
)

from graph_builder.reasoning.repository_mission_engine import (
    RepositoryMissionEngine,
)


print("=" * 40)
print("Repository Mission Engine")
print("=" * 40)

identity = RepositoryIdentity(

    repository="graphify",

    identity="Autonomous Engineering Brain",

    engineering_type="Engineering AI",

    confidence=0.82,

    capabilities=[

        "Engineering Knowledge Acquisition",

        "Persistent Engineering Memory",

        "Engineering Decision Making",

        "Engineering Planning",

    ],

)

engine = RepositoryMissionEngine()

mission = engine.build(identity)

print()

print("Mission")

print()

pprint(mission.to_dict())