from graph_builder.context_history import (
    load_context_commit
)


def restore_context(
    context_id
):

    commit = (
        load_context_commit(
            context_id
        )
    )

    restored = {

        "status":
            "RESTORED",

        "context_id":
            commit[
                "context_id"
            ],

        "project_name":
            commit[
                "project_name"
            ],

        "stage":
            commit[
                "stage"
            ],

        "health_score":
            commit[
                "health_score"
            ],

        "latest_commit":
            commit[
                "latest_commit"
            ],

        "latest_tag":
            commit[
                "latest_tag"
            ],

        "timestamp":
            commit[
                "timestamp"
            ]
    }

    return restored