def validate_context(
    context
):

    required_keys = [

        "schema_version",

        "project",

        "repository",

        "github",

        "decisions",

        "sessions"
    ]

    missing_keys = []

    for key in required_keys:

        if key not in context:

            missing_keys.append(
                key
            )

    if missing_keys:

        return {

            "valid":
                False,

            "status":
                "INVALID",

            "missing_keys":
                missing_keys
        }

    return {

        "valid":
            True,

        "status":
            "VALID",

        "missing_keys":
            []
    }