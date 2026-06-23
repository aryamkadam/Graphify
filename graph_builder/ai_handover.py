def generate_ai_handover(
    context
):

    return {

        "project_name":
            context[
                "project_name"
            ],

        "current_stage":
            context[
                "stage"
            ],

        "repository_health":
            context[
                "health_score"
            ],

        "latest_commit":
            context[
                "latest_commit"
            ],

        "latest_tag":
            context[
                "latest_tag"
            ],

        "project_goal":
            "Graphify = Git for AI Context",

        "current_focus":
            "AI Memory Infrastructure",

        "summary":
            (
                "Graphify captures, stores, "
                "transfers and restores "
                "AI understanding."
            )
    }