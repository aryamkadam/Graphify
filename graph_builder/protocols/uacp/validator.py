from graph_builder.protocols.uacp.protocol import (
    UACP_VERSION
)


REQUIRED_SECTIONS = [

    "protocol",

    "identity",

    "repository",

    "reasoning",

    "decisions",

    "continuation",

    "transfer",

    "integrity",

    "metadata"

]


def validate_uacp(
    protocol
):

    missing = []

    for section in REQUIRED_SECTIONS:

        if section not in protocol:

            missing.append(
                section
            )

    if missing:

        return {

            "valid": False,

            "status": "INVALID_PROTOCOL",

            "missing_sections": missing
        }

    protocol_info = protocol.get(
        "protocol",
        {}
    )

    version = protocol_info.get(
        "version"
    )

    if version != UACP_VERSION:

        return {

            "valid": False,

            "status": "VERSION_MISMATCH",

            "expected": UACP_VERSION,

            "received": version
        }

    return {

        "valid": True,

        "status": "VALID",

        "protocol": protocol_info.get(
            "name",
            "Unknown"
        ),

        "version": version
    }