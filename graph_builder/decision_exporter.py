import json

from graph_builder.decision_history import (
    build_decision_history
)


def export_decision_history(
    output_file
):

    decisions = (
        build_decision_history()
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            decisions,
            file,
            indent=4
        )

    return decisions