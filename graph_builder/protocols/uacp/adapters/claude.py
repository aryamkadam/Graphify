from graph_builder.protocols.uacp.adapters.base import (
    BaseAdapter
)


class ClaudeAdapter(
    BaseAdapter
):

    AI_NAME = "Claude"

    ADAPTER_NAME = "claude"


_adapter = ClaudeAdapter()


def claude_to_uacp(
    universal_context_schema
):

    return _adapter.convert(

        universal_context_schema

    )