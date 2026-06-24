def extract_project_history(
    timeline
):

    milestones = []

    for item in timeline:

        stage = item.get(
            "stage",
            "unknown"
        )

        message = item.get(
            "message",
            ""
        )

        milestones.append({

            "stage":
                stage,

            "message":
                message
        })

    return milestones