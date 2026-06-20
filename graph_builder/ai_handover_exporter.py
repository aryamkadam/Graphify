from graph_builder.ai_handover_pack import (
    generate_ai_handover_pack
)


def export_ai_handover_pack(
    symbol_index,
    knowledge_graph,
    output_file
):

    content = (
        generate_ai_handover_pack(
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
            content
        )

    return content