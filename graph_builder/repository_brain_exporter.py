import json

from graph_builder.repository_brain import (
    generate_repository_brain
)


def export_repository_brain(
    symbol_index,
    knowledge_graph,
    output_file,
    project_name,
    project_purpose,
    current_stage
):

    brain = (
        generate_repository_brain(
            symbol_index,
            knowledge_graph,
            project_name,
            project_purpose,
            current_stage
        )
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            brain,
            f,
            indent=4
        )

    return brain