from graph_builder.decision_history import (
    build_decision_history
)


def generate_decision_replay():

    decisions = (
        build_decision_history()
    )

    replay = []

    for decision in decisions:

        replay.append({

            "decision":
                decision["title"],

            "reason":
                decision["reason"],

            "impact":
                decision["impact"],

            "stage":
                decision["stage"]
        })

    return replay