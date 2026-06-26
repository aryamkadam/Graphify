REQUIRED_SECTIONS = [

    "identity",

    "history",

    "decisions",

    "reconstruction",

    "continuation",

    "quality"
]


def validate_context(
    context
):

    missing_keys = []

    for section in REQUIRED_SECTIONS:

        if section not in context:

            missing_keys.append(
                section
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

    identity = context.get(
        "identity",
        {}
    )

    required_identity = [

        "project_name",

        "goal",

        "current_stage"
    ]

    missing_identity = []

    for field in required_identity:

        if field not in identity:

            missing_identity.append(
                field
            )

    if missing_identity:

        return {

            "valid":
                False,

            "status":
                "INVALID_IDENTITY",

            "missing_keys":
                missing_identity
        }

    return {

        "valid":
            True,

        "status":
            "VALID",

        "missing_keys":
            []
    }