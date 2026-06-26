from graph_builder.decision_replay import (
    generate_decision_replay
)

from graph_builder.context_history import (
    get_context_history
)

from graph_builder.stage_resolver import (
    resolve_current_stage
)


def generate_context_continuation():

    history = (
        get_context_history()
    )

    decisions = (
        generate_decision_replay()
    )

    current_stage = (
        resolve_current_stage()
    )

    if current_stage.startswith(
        "stage-11"
    ):

        next_objective = (
            "Cross-AI Context Transfer"
        )

        current_maturity = (
            "AI Memory Infrastructure"
        )

        reason = (
            "Graphify already captures, "
            "stores, reconstructs and verifies "
            "AI context. The next logical step "
            "is transferring context across "
            "different AI systems."
        )

    else:

        next_objective = (
            "Autonomous AI Handover"
        )

        current_maturity = (
            "AI Context Platform"
        )

        reason = (
            "Graphify should evolve toward "
            "fully autonomous AI-to-AI "
            "continuity and handover."
        )

    return {

        "current_maturity":
            current_maturity,

        "completed_context_commits":
            len(history),

        "completed_decisions":
            len(decisions),

        "recommended_next_stage":
            next_objective,

        "reason":
            reason
    }