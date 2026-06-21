from graph_builder.repository_brain import (
    generate_repository_brain
)


def generate_prediction(
    repository_brain
):

    direction = (
        repository_brain[
            "project_direction"
        ]
    )

    health_score = (
        repository_brain[
            "health_score"
        ]
    )

    if direction == "architecture":

        feature = (
            "GitHub Integration"
        )

        confidence = 90

        reason = (
            "Project direction is architecture focused."
        )

    elif direction == "memory":

        feature = (
            "AI Session Export"
        )

        confidence = 85

        reason = (
            "Project is focused on memory systems."
        )

    else:

        feature = (
            "VS Code Extension"
        )

        confidence = 75

        reason = (
            "General platform expansion."
        )

    prediction = {

        "recommended_next_stage":
            "Stage 6.4",

        "recommended_feature":
            feature,

        "confidence":
            confidence,

        "reason":
            reason,

        "health_score":
            health_score
    }

    return prediction