def export_gemini_context(
    context
):

    repository = context[
        "repository_brain"
    ]

    github = context[
        "github_intelligence"
    ]

    project = context[
        "project_memory"
    ]

    return {

        "platform":
            "Gemini",

        "workspace_context": {

            "project":
                project["project_name"],

            "goal":
                project["goal"],

            "current_stage":
                project["current_stage"]
        },

        "repository_status": {

            "health":
                repository["status"],

            "health_score":
                repository["health_score"],

            "critical_symbols":
                repository["critical_symbols"]
        },

        "development_metrics": {

            "commits":
                github["activity"][
                    "total_commits"
                ],

            "repository_maturity":
                github[
                    "repository_maturity"
                ],

            "velocity":
                github[
                    "velocity"
                ]
        }
    }