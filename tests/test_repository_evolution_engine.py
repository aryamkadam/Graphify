from pprint import pprint

from graph_builder.history.repository_evolution_engine import (
    RepositoryEvolutionEngine,
)

old_snapshot = {

    "health": {

        "health_score": 90

    },

    "execution": {

        "graph_nodes": 200

    },

    "knowledge": {

        "dead_code_count": 4,

        "hotspot_count": 8

    }

}

new_snapshot = {

    "health": {

        "health_score": 96

    },

    "execution": {

        "graph_nodes": 260

    },

    "knowledge": {

        "dead_code_count": 1,

        "hotspot_count": 5

    }

}

report = RepositoryEvolutionEngine(

    old_snapshot,

    new_snapshot

).build()

print("\nRepository Evolution Report\n")

pprint(report)