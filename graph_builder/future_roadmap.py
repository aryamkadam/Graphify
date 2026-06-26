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

            "Stage 12 - AI Context Recovery",

            "Stage 13 - Context Merge Engine",

            "Stage 14 - Multi-Repository Memory",

            "Stage 15 - Context Diff Visualization",

            "Stage 16 - Universal AI Memory Protocol"
        ]
    }

    return roadmap