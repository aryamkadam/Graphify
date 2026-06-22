import json

from graph_builder.github_intelligence import (
    generate_github_intelligence
)


def export_github_intelligence(
    output_file
):

    intelligence = (
        generate_github_intelligence()
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            intelligence,
            file,
            indent=4
        )

    return intelligence