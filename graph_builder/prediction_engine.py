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
            "Context Evolution Engine"
        )

        confidence = 95

        reason = (
            "Architecture foundation is complete. "
            "Next logical step is context evolution."
        )

    elif direction == "memory":

        feature = (
            "AI Session Export"
        )

        confidence = 90

        reason = (
            "Project is focused on memory systems."
        )

    else:

        feature = (
            "VS Code Extension"
        )

        confidence = 80

        reason = (
            "General platform expansion."
        )

    prediction = {

        "recommended_next_stage":
            "Stage 6.8",

        "recommended_feature":
            feature,

        "confidence":
            confidence,

        "reason":
            reason,

        "health_score":
            health_score,

        "project_status":
            "ACTIVE"
    }

    return prediction