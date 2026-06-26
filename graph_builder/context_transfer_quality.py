from graph_builder.context_history import (
    get_context_history
)

from graph_builder.decision_history import (
    build_decision_history
)


def generate_transfer_quality():

    history = (
        get_context_history()
    )

    decisions = (
        build_decision_history()
    )

    history_score = 100

    if len(history) == 0:

        history_score = 0

    elif len(history) < 3:

        history_score = 70

    decision_score = 100

    if len(decisions) == 0:

        decision_score = 0

    elif len(decisions) < 3:

        decision_score = 75

    continuation_score = 100

    reconstruction_score = 100

    transfer_score = int(

        (
            history_score
            + decision_score
            + continuation_score
            + reconstruction_score
        )
        / 4
    )

    if transfer_score >= 90:

        recommendation = (
            "AI handover ready."
        )

    elif transfer_score >= 70:

        recommendation = (
            "Minor context gaps detected."
        )

    else:

        recommendation = (
            "Context transfer quality is insufficient."
        )

    return {

        "transfer_score":
            transfer_score,

        "history_coverage":
            history_score,

        "decision_coverage":
            decision_score,

        "continuation_coverage":
            continuation_score,

        "reconstruction_coverage":
            reconstruction_score,

        "recommendation":
            recommendation
    }