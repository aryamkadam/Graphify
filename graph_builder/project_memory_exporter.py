import json

from graph_builder.project_memory import (
    generate_project_memory
)


def export_project_memory(
    output_file
):

    memory = (
        generate_project_memory()
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            memory,
            file,
            indent=4
        )

    return memory