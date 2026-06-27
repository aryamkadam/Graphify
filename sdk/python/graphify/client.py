"""
Official Graphify SDK
"""

from graph_builder.context.builder import (
    build_context
)

from graph_builder.protocols.uacp.builder import (
    build_uacp
)


class GraphifyClient:

    """
    Official SDK client.
    """

    def __init__(self):
        print("Graphify SDK Initialized 🚀")


    def context(self):
        """
        Return the canonical Graphify Context.
        """

        return build_context()


    def uacp(self):
        """
        Export Graphify Context as UACP.
        """

        context = build_context()

        return build_uacp(context)