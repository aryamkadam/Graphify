from graph_builder.protocols.uacp.adapters.chatgpt import (
    chatgpt_to_uacp
)

from graph_builder.protocols.uacp.adapters.claude import (
    claude_to_uacp
)
from graph_builder.protocols.uacp.adapters.chatgpt import (
    chatgpt_to_uacp
)


ADAPTERS = {

    "chatgpt": chatgpt_to_uacp,
     "claude": claude_to_uacp,


}


def register_adapter(

    name,

    adapter

):

    ADAPTERS[
        name.lower()
    ] = adapter


def get_adapter(

    name

):

    return ADAPTERS.get(

        name.lower()

    )


def available_adapters():

    return sorted(

        ADAPTERS.keys()

    )