import json

from graph_builder.uacs import (
    build_uacs
)


def export_uacs(
    universal_context,
    output_file
):

    uacs = build_uacs(
        universal_context
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            uacs,
            f,
            indent=4
        )

    return uacs