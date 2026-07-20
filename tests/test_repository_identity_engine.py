from pprint import pprint

from graph_builder.intelligence.repository_identity_engine import (
    RepositoryIdentityEngine,
)

print()
print("=" * 40)
print("Repository Identity Engine")
print("=" * 40)
print()

capabilities = [

    {

        "capability":

            "Engineering Knowledge Acquisition",

    },

    {

        "capability":

            "Persistent Engineering Memory",

    },

    {

        "capability":

            "Engineering Decision Making",

    },

    {

        "capability":

            "Engineering Planning",

    },

]

engine = RepositoryIdentityEngine()

identity = engine.build(

    repository="graphify",

    capabilities=capabilities,

)

print("Identity")
print()

pprint(identity.to_dict())