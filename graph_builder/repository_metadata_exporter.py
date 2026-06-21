import json

from graph_builder.repository_metadata import (
    get_repository_metadata
)


def export_repository_metadata():

    metadata = (
        get_repository_metadata()
    )

    output_file = (
        "graphify-out/repository_metadata.json"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            metadata,
            file,
            indent=4
        )

    return metadata