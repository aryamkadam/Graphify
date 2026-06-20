from graph_builder.symbol_context import (
    generate_symbol_context
)


def build_context_pack(
    symbol,
    symbol_index,
    knowledge_graph
):

    context = generate_symbol_context(
        symbol,
        symbol_index,
        knowledge_graph
    )

    if not context:
        return None

    symbol_data = symbol_index[
        symbol
    ]

    context_pack = {
        "symbol_context": context,
        "used_by": symbol_data[
            "used_by"
        ],
        "docstring": symbol_data.get(
            "docstring"
        )
    }

    return context_pack