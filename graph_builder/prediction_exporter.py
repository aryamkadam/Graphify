import json

from graph_builder.prediction_engine import (
    generate_prediction
)


def export_prediction(
    repository_brain,
    output_file
):

    prediction = (
        generate_prediction(
            repository_brain
        )
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            prediction,
            file,
            indent=4
        )

    return prediction