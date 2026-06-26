from graph_builder.protocols.uacp.builder import (
    build_uacp
)


def chatgpt_to_uacp(
    universal_context_schema
):

    uacp = build_uacp(
        universal_context_schema
    )

    uacp["metadata"]["source_ai"] = "ChatGPT"

    uacp["metadata"]["adapter"] = "chatgpt"

    return uacp