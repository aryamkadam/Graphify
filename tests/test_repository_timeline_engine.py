from pprint import pprint

from graph_builder.intelligence.repository_timeline_engine import (
    RepositoryTimelineEngine,
)

snapshots = [

    {

        "metadata": {

            "created_at": "2026-06-01"

        },

        "health": {

            "health_score": 90

        },

        "execution": {

            "graph_nodes": 200

        },

        "repository_learning": {

            "engineering_maturity": "Growing",

            "long_term_direction": "Positive"

        }

    },

    {

        "metadata": {

            "created_at": "2026-06-10"

        },

        "health": {

            "health_score": 93

        },

        "execution": {

            "graph_nodes": 220

        },

        "repository_learning": {

            "engineering_maturity": "Growing",

            "long_term_direction": "Positive"

        }

    },

    {

        "metadata": {

            "created_at": "2026-06-20"

        },

        "health": {

            "health_score": 96

        },

        "execution": {

            "graph_nodes": 260

        },

        "repository_learning": {

            "engineering_maturity": "Growing",

            "long_term_direction": "Positive"

        }

    }

]

timeline = RepositoryTimelineEngine().build(
    snapshots
)

print("\nRepository Timeline\n")

pprint(timeline)