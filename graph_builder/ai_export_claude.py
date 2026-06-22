def export_claude_context(
    context
):

    repository = context[
        "repository_brain"
    ]

    project = context[
        "project_memory"
    ]

    decision = context[
        "decision_brain"
    ]

    return {

        "platform":
            "Claude",

        "project_summary": {

            "name":
                project["project_name"],

            "goal":
                project["goal"],

            "current_stage":
                project["current_stage"]
        },

        "architecture_context": {

            "critical_symbols":
                repository["critical_symbols"],

            "risky_symbols":
                repository["risky_symbols"],

            "health_score":
                repository["health_score"]
        },

        "reasoning_context": {

            "important_decisions":
                decision[
                    "latest_decisions"
                ],

            "decision_count":
                decision[
                    "decision_count"
                ]
        }
    }