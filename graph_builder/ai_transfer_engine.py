from graph_builder.ai_context_pack import (
    build_ai_context_pack
)

from graph_builder.ai_platform_adapter import (
    adapt_context_pack
)


def transfer_context(

    symbol_index,
    knowledge_graph,
    target_ai

):

    pack = (
        build_ai_context_pack(
            symbol_index,
            knowledge_graph
        )
    )

    return adapt_context_pack(
        pack,
        target_ai
    )