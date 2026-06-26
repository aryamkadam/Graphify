from graph_builder.protocols.uacp.adapters.base import (
    BaseAdapter
)


class ChatGPTAdapter(
    BaseAdapter
):

    AI_NAME = "ChatGPT"

    ADAPTER_NAME = "chatgpt"


_adapter = ChatGPTAdapter()


def chatgpt_to_uacp(
    universal_context_schema
):

    return _adapter.convert(

        universal_context_schema

    )