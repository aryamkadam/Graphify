from graph_builder.protocols.uacp.protocol import (
    create_protocol
)


def build_uacp(
    context_schema
):

    protocol = create_protocol()

    protocol["identity"] = (
        context_schema.get(
            "identity",
            {}
        )
    )

    protocol["repository"] = (
        context_schema.get(
            "history",
            {}
        )
    )

    protocol["reasoning"] = (
        context_schema.get(
            "reconstruction",
            {}
        )
    )

    protocol["decisions"] = (
        context_schema.get(
            "decisions",
            {}
        )
    )

    protocol["continuation"] = (
        context_schema.get(
            "continuation",
            {}
        )
    )

    protocol["transfer"] = (
        context_schema.get(
            "quality",
            {}
        )
    )

    protocol["integrity"] = {

        "verified": True,

        "signature":

            context_schema.get(
                "signature",
                None
            )
    }

    protocol["metadata"] = {

        "generated_by":

            "Graphify",

        "schema_version":

            context_schema.get(
                "schema_version",
                "1.0"
            )
    }

    return protocol