import json

from graph_builder.repository_metadata import (
    get_repository_metadata
)

from graph_builder.project_evolution import (
    get_project_evolution
)


def generate_project_memory():

    metadata = (
        get_repository_metadata()
    )

    evolution = (
        get_project_evolution()
    )

    completed_stages = []

    for stage in evolution:

        completed_stages.append(
            stage["tag"]
        )

    memory = {

        "project_name":
            "Graphify",

        "goal":
            "AI Context Transfer Engine",

        "completed_stages":
            completed_stages,

        "current_stage":
            metadata[
                "current_stage"
            ],

        "latest_commit":
            metadata[
                "latest_commit"
            ],

        "latest_tag":
            metadata[
                "latest_tag"
            ],

        "current_branch":
            metadata[
                "current_branch"
            ],

        "total_commits":
            metadata[
                "total_commits"
            ],

        "next_stage":
            "Stage 6.8",

        "future_features": [

            "Project Memory Engine",
            "Decision Tracking",
            "GitHub Integration",
            "VS Code Extension",
            "AI Session Export",
            "Multi-AI Context Transfer",
            "Context Evolution Engine"
        ]
    }

    return memory