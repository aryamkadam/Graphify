from datetime import datetime

from graph_builder.project_memory import (
    generate_project_memory
)

from graph_builder.repository_brain import (
    generate_repository_brain
)

from graph_builder.project_decision_brain import (
    generate_project_decision_brain
)

from graph_builder.context_intelligence import (
    generate_context_intelligence
)


def create_context_commit(
    context,
    message
):

    repository = context[
        "repository"
    ]

    project = context[
        "project"
    ]

    commit = {

        "context_id":
            f"ctx_{datetime.now().strftime('%Y%m%d%H%M%S%f')}",

        "timestamp":
            datetime.now().isoformat(),

        "message":
            message,

        "project_name":
            project[
                "project_name"
            ],

        "stage":
            project[
                "current_stage"
            ],

        "health_score":
            repository[
                "health_score"
            ],

        "latest_commit":
            repository[
                "latest_commit"
            ],

        "latest_tag":
            repository[
                "latest_tag"
            ],

        "project_memory":
            context[
                "project"
            ],

        "repository_brain":
            context[
                "repository"
            ],

        "decision_brain":
            context[
                "decisions"
            ],

        "context_intelligence":
            generate_context_intelligence(
                context[
                    "repository"
                ]
            )
    }

    return commit