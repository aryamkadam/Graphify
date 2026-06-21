from graph_builder.decision_reasoning_pack import (
    generate_decision_reasoning_pack
)


def export_decision_reasoning_pack(
    output_file
):

    content = (
        generate_decision_reasoning_pack()
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            content
        )

    return content