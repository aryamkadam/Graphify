from graph_builder.context_history import get_context_history
from graph_builder.decision_history import build_decision_history

def generate_transfer_quality():

    history = get_context_history()
    decisions = build_decision_history()

    history_score = min(len(history) * 50, 100)
    decision_score = min(len(decisions) * 25, 100)

    transfer_score = int(
        (history_score + decision_score + 100) / 3
    )

    return {
        "transfer_score": transfer_score,
        "history_coverage": history_score,
        "decision_coverage": decision_score,
        "continuation_coverage": 100,
        "recommendation":
            "Context pack is highly transferable."
    }