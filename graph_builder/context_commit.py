from datetime import datetime

from graph_builder.context_intelligence import (
    generate_context_intelligence
)


def create_context_commit(
    context,
    message
):

    identity = context[
        "identity"
    ]

    quality = context[
        "quality"
    ]

    commit = {

        "context_id":
            f"ctx_{datetime.now().strftime('%Y%m%d%H%M%S%f')}",

        "timestamp":
            datetime.now().isoformat(),

        "message":
            message,

        "project_name":
            identity[
                "project_name"
            ],

        "stage":
            identity[
                "current_stage"
            ],

        "health_score":
            quality.get(
                "transfer_score",
                0
            ),

        "latest_commit":
            identity.get(
                "latest_commit",
                "unknown"
            ),

        "latest_tag":
            identity[
                "current_stage"
            ],

        "identity":
            context[
                "identity"
            ],

        "history":
            context[
                "history"
            ],

        "decisions":
            context[
                "decisions"
            ],

        "reconstruction":
            context[
                "reconstruction"
            ],

        "continuation":
            context[
                "continuation"
            ],

        "quality":
            context[
                "quality"
            ]
    }

    return commit