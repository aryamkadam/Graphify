import json

from graph_builder.future_roadmap import (
    generate_future_roadmap
)


def export_future_roadmap(
    repository_brain,
    output_file
):

    roadmap = (
        generate_future_roadmap(
            repository_brain
        )
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            roadmap,
            file,
            indent=4
        )

    return roadmap