from graph_builder.ultimate_memory_pack import (
    build_ultimate_memory_pack
)


def export_ultimate_memory_pack():

    content = (
        build_ultimate_memory_pack()
    )

    output_file = (
        "graphify-out/ultimate_memory_pack.md"
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