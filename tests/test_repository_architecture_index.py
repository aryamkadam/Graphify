"""
Graphify

Phase 11

Stage P11.6.1

Repository Architecture Index Test

Author:
Graphify Core
"""

from pprint import pprint

from graph_builder.architecture.repository_architecture_index import (
    RepositoryArchitectureIndex,
)

print()
print("=" * 40)
print("Repository Architecture Index")
print("=" * 40)

index = RepositoryArchitectureIndex()

result = index.build(".")

print()
print("Summary")
print()

pprint({

    "repository": result["repository"],

    "components": result["component_count"],

    "version": result["version"],

})

print()
print("Layer Summary")
print()

pprint(result["layer_summary"])

print()
print("First 10 Components")
print()

for component in result["components"][:10]:

    pprint({

        "name": component.name,

        "layer": component.layer,

        "role": component.role,

        "importance": component.importance,

        "visibility": component.visibility,

        "path": component.path,

    })