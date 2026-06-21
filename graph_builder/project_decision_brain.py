from graph_builder.decision_history import (
    build_decision_history
)


def generate_project_decision_brain():

    decisions = (
        build_decision_history()
    )

    brain = {

        "decision_count":
            len(decisions),

        "latest_decisions":
            decisions[-3:],

        "most_important_decisions":
            decisions
    }

    return brain