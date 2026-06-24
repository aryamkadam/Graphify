from graph_builder.decision_replay import (
    generate_decision_replay
)

from graph_builder.context_history import (
    get_context_history
)


def generate_context_continuation():

    history = get_context_history()

    decisions = generate_decision_replay()

    return {

        "current_maturity":
            "AI Memory Infrastructure",

        "completed_context_commits":
            len(history),

        "completed_decisions":
            len(decisions),

        "recommended_next_stage":
            "Cross-AI Context Transfer",

        "reason":
            (
                "Graphify already preserves "
                "and reconstructs AI context. "
                "The next logical step is "
                "transferring context between "
                "different AI systems."
            )
    }