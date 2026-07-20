from pprint import pprint

from graph_builder.intelligence.repository_capability_engine import (
    RepositoryCapabilityEngine,
)

print()
print("=" * 40)
print("Repository Capability Engine")
print("=" * 40)
print()

behavior = {

    "module": "repository_learning_engine",

    "primary_behavior": "Repository Learning",

    "behavior_confidence": 0.90,

    "behavior_keywords": [

        "learn",

        "record_experience",

        "feedback",

    ],

}

engine = RepositoryCapabilityEngine()

capability = engine.build(

    behavior,

)

print("Capability")
print()

pprint(capability.to_dict())