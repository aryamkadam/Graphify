from graph_builder.context_history import (
    get_context_history
)

from graph_builder.decision_history import (
    build_decision_history
)


def generate_structured_reconstruction():

    history = get_context_history()

    decisions = build_decision_history()

    evolution = []

    for item in history:

        evolution.append({

            "timestamp":
                item.get(
                    "timestamp"
                ),

            "event":
                item.get(
                    "message"
                )
        })

    decision_data = []

    for decision in decisions:

        decision_data.append({

            "title":
                decision.get(
                    "title"
                ),

            "reason":
                decision.get(
                    "reason"
                ),

            "impact":
                decision.get(
                    "impact"
                ),

            "stage":
                decision.get(
                    "stage"
                )
        })

    return {

        "project_evolution":
            evolution,

        "decision_narrative":
            decision_data,

        "reconstruction_summary":
            (
                "Graphify evolved from repository "
                "understanding into an AI Context "
                "Transfer Platform."
            )
    }