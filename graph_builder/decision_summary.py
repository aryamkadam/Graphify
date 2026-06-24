# graph_builder/decision_summary.py

from graph_builder.decision_history import (
    build_decision_history
)


def generate_decision_summary():

    decisions = (
        build_decision_history()
    )

    summary = []

    for decision in decisions:

        summary.append(

            f"{decision['title']} "
            f"({decision['stage']})"

        )

    return summary