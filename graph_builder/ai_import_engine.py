from graph_builder.context_validator import (
    validate_context
)


def import_ai_context(
    context
):

    validation = validate_context(
        context
    )

    if not validation[
        "valid"
    ]:

        return {

            "imported":
                False,

            "status":
                "REJECTED",

            "reason":
                validation
        }

    identity = context.get(
        "identity",
        {}
    )

    quality = context.get(
        "quality",
        {}
    )

    continuation = context.get(
        "continuation",
        {}
    )

    history = context.get(
        "history",
        {}
    )

    decisions = context.get(
        "decisions",
        {}
    )

    return {

        "imported":
            True,

        "status":
            "SUCCESS",

        "project":
            identity.get(
                "project_name",
                "Unknown"
            ),

        "stage":
            identity.get(
                "current_stage",
                "unknown"
            ),

        "goal":
            identity.get(
                "goal",
                "Unknown"
            ),

        "transfer_score":
            quality.get(
                "transfer_score",
                0
            ),

        "next_objective":
            continuation.get(
                "next_objective",
                "Unknown"
            ),

        "decision_count":
            len(
                decisions.get(
                    "decision_history",
                    []
                )
            ),

        "context_commit_count":
            len(
                history.get(
                    "context_commits",
                    []
                )
            ),

        "schema_version":
            context.get(
                "schema_version",
                "1.0"
            )
    }