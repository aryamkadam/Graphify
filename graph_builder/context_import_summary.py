def generate_import_summary(
    context
):

    return {

        "project_name":
            context[
                "project_name"
            ],

        "stage":
            context[
                "stage"
            ],

        "health_score":
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

        "context_id":
            context[
                "context_id"
            ]
    }