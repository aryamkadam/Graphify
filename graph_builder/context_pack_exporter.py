from graph_builder.context_pack_generator import (
    generate_context_pack
)


def export_context_pack(
    symbol_index,
    knowledge_graph,
    output_file
):

    context_pack = (
        generate_context_pack(
            symbol_index,
            knowledge_graph
        )
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            context_pack
        )

    return context_pack