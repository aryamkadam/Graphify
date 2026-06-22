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

    return {

        "imported":
            True,

        "status":
            "SUCCESS",

        "project":
            context[
                "project"
            ][
                "project_name"
            ],

        "stage":
            context[
                "project"
            ][
                "current_stage"
            ],

        "schema_version":
            context[
                "schema_version"
            ]
    }