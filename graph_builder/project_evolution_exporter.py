import json

from graph_builder.project_evolution import (
    get_project_evolution
)


def export_project_evolution(
    output_file
):

    evolution = {

        "stages":
            get_project_evolution()
    }

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            evolution,
            file,
            indent=4
        )

    return evolution