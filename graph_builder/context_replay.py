from graph_builder.context_history import (
    get_context_history
)


def generate_context_replay():

    history = (
        get_context_history()
    )

    replay = []

    for index, item in enumerate(
        history,
        start=1
    ):

        replay.append(

            {
                "version":
                    index,

                "context_id":
                    item[
                        "context_id"
                    ],

                "timestamp":
                    item[
                        "timestamp"
                    ],

                "stage":
                    item[
                        "stage"
                    ],

                "health_score":
                    item[
                        "health_score"
                    ],

                "message":
                    item[
                        "message"
                    ]
            }
        )

    return replay