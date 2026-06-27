from graph_builder.protocols.uacp.adapters.base import (
    BaseAdapter
)


class GeminiAdapter(
    BaseAdapter
):

    AI_NAME = "Gemini"

    ADAPTER_NAME = "gemini"


_adapter = GeminiAdapter()


def gemini_to_uacp(
    universal_context_schema
):

    return _adapter.convert(

        universal_context_schema

    )