CURRENT_SCHEMA_VERSION = "1.0"


def get_schema_version():

    return CURRENT_SCHEMA_VERSION


def check_schema_compatibility(
    schema_version
):

    if schema_version == CURRENT_SCHEMA_VERSION:

        return {

            "compatible": True,

            "message":
                "Fully compatible."
        }

    major_current = (
        CURRENT_SCHEMA_VERSION.split(".")[0]
    )

    major_target = (
        schema_version.split(".")[0]
    )

    if major_current == major_target:

        return {

            "compatible": True,

            "message":
                "Compatible with minor differences."
        }

    return {

        "compatible": False,

        "message":
            "Major version mismatch."
    }