from pprint import pprint

from graph_builder.intelligence.repository_planning_engine import (
    RepositoryPlanningEngine,
)

brain = {

    "project_name": "Graphify",

    "health": {

        "health_score": 82

    },

    "knowledge": {

        "dead_code_count": 11,

        "hotspot_count": 7,

        "critical_symbols": [

            "build_context",

            "build_repository_brain"

        ]

    },

    "execution": {

        "graph_nodes": 324

    },

    "executive_summary": {

        "project_direction":

            "Repository Intelligence"

    }

}

summary = {

    "summary":

        "Repository health remains stable although execution complexity continues to increase."

}

roadmap = RepositoryPlanningEngine().generate(

    brain,

    summary

)

print()

print("Repository Planning Engine")

print()

pprint(roadmap)