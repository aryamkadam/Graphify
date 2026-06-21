from graph_builder.prediction_engine import (
    generate_prediction
)


def generate_future_roadmap(
    repository_brain
):

    prediction = (
        generate_prediction(
            repository_brain
        )
    )

    roadmap = {

        "current_stage":
            repository_brain[
                "current_stage"
            ],

        "next_stage":
            prediction[
                "recommended_next_stage"
            ],

        "recommended_feature":
            prediction[
                "recommended_feature"
            ],

        "future_stages": [

            "Stage 6.4 - Prediction Engine",

            "Stage 6.5 - GitHub Intelligence",

            "Stage 6.6 - VS Code Extension",

            "Stage 7 - Multi-AI Context Transfer",

            "Stage 8 - Autonomous Repository Architect"
        ]
    }

    return roadmap