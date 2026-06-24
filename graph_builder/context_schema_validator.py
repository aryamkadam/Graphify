REQUIRED_SECTIONS = [

    "identity",

    "history",

    "decisions",

    "reconstruction",

    "continuation",

    "quality"
]


def validate_context_schema(
    schema
):

    missing = []

    for section in REQUIRED_SECTIONS:

        if section not in schema:

            missing.append(
                section
            )

    valid = (
        len(missing) == 0
    )

    return {

        "valid":
            valid,

        "schema_version":
            "1.0",

        "missing_sections":
            missing,

        "quality":
            (
                "PASS"
                if valid
                else "FAIL"
            )
    }