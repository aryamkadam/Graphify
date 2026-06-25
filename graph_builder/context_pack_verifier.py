from graph_builder.context_signature import (
    generate_context_signature
)

from graph_builder.context_schema_validator import (
    validate_context_schema
)


def verify_context_pack(
    pack
):

    schema = pack["schema"]

    stored_signature = (
        pack["signature"]
    )

    generated_signature = (
        generate_context_signature(
            schema
        )
    )

    signature_valid = (

        stored_signature
        ==
        generated_signature
    )

    schema_result = (
        validate_context_schema(
            schema
        )
    )

    schema_valid = (
        schema_result["valid"]
    )

    verified = (
        signature_valid
        and
        schema_valid
    )

    return {

        "verified":
            verified,

        "signature_valid":
            signature_valid,

        "schema_valid":
            schema_valid,

        "status":
            (
                "SAFE"
                if verified
                else
                "CORRUPTED"
            )
    }