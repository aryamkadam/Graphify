from graph_builder.protocols.uacp.builder import (
    build_uacp
)


def claude_to_uacp(
    universal_context_schema
):

    uacp = build_uacp(
        universal_context_schema
    )

    uacp["metadata"]["source_ai"] = "Claude"

    uacp["metadata"]["adapter"] = "claude"

    return uacp