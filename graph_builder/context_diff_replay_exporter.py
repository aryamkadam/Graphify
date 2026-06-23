from graph_builder.context_history import (
    get_context_history
)


def generate_context_diff_replay():

    history = (
        get_context_history()
    )

    print(
        "History Length:",
        len(history)
    )

    if len(history) < 2:

        return {

            "status":
                "INSUFFICIENT_HISTORY",

            "message":
                "Need at least 2 context commits."
        }

    old_context = history[-2]

    new_context = history[-1]

    return {

        "old_context":
            old_context[
                "context_id"
            ],

        "new_context":
            new_context[
                "context_id"
            ],

        "old_stage":
            old_context[
                "stage"
            ],

        "new_stage":
            new_context[
                "stage"
            ],

        "health_change":
            new_context[
                "health_score"
            ]
            -
            old_context[
                "health_score"
            ],

        "old_message":
            old_context[
                "message"
            ],

        "new_message":
            new_context[
                "message"
            ]
    }