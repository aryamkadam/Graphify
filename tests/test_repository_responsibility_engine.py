from pprint import pprint

from graph_builder.intelligence.repository_responsibility_engine import (
    RepositoryResponsibilityEngine,
)

print()
print("=" * 40)
print("Repository Responsibility Engine")
print("=" * 40)
print()

architecture = [

    {

        "name": "repository_learning_engine",

        "layer": "Learning",

    },

    {

        "name": "repository_reasoning_engine",

        "layer": "Reasoning",

    },

    {

        "name": "runtime_engine",

        "layer": "Runtime",

    },

]

engine = RepositoryResponsibilityEngine()

responsibilities = engine.build(architecture)

print("Responsibilities")
print()

for item in responsibilities:

    pprint(item.to_dict())

    print("-" * 40)