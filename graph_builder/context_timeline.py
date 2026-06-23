from graph_builder.context_history import (
    get_context_history
)


def generate_context_timeline():

    history = (
        get_context_history()
    )

    timeline = []

    for version, item in enumerate(
        history,
        start=1
    ):

        timeline.append(

            {
                "version":
                    version,

                "context_id":
                    item[
                        "context_id"
                    ],

                "stage":
                    item[
                        "stage"
                    ],

                "health_score":
                    item[
                        "health_score"
                    ],

                "timestamp":
                    item[
                        "timestamp"
                    ],

                "message":
                    item[
                        "message"
                    ]
            }
        )

    return timeline