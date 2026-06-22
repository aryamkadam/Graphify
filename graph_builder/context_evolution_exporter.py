import json

from graph_builder.context_evolution import (
    generate_context_evolution
)


def export_context_evolution(
    old_context,
    new_context,
    output_file
):

    evolution = (
        generate_context_evolution(
            old_context,
            new_context
        )
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            evolution,
            f,
            indent=4
        )

    return evolution