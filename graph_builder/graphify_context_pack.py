from graph_builder.universal_context_schema import (
    generate_universal_context_schema
)

from graph_builder.context_manifest import (
    generate_context_manifest
)

from graph_builder.context_signature import (
    generate_context_signature
)


def generate_graphify_context_pack():

    schema = (
        generate_universal_context_schema()
    )

    manifest = (
        generate_context_manifest()
    )

    signature = (
        generate_context_signature(
            schema
        )
    )

    return {

        "manifest":
            manifest,

        "signature":
            signature,

        "schema":
            schema
    }