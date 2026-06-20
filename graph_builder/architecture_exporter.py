from graph_builder.architecture_summary import (
    generate_architecture_summary
)


def export_architecture_summary(
    symbol_index,
    output_file
):

    summary = (
        generate_architecture_summary(
            symbol_index
        )
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            summary
        )

    return summary