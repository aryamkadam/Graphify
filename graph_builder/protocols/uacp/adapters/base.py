from graph_builder.protocols.uacp.builder import (
    build_uacp
)


class BaseAdapter:

    AI_NAME = "Unknown"

    ADAPTER_NAME = "base"

    def convert(

        self,

        universal_context_schema

    ):

        uacp = build_uacp(

            universal_context_schema

        )

        uacp["metadata"]["source_ai"] = (

            self.AI_NAME

        )

        uacp["metadata"]["adapter"] = (

            self.ADAPTER_NAME

        )

        return uacp