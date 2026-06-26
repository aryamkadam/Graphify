from graph_builder.context_bootstrap import (
    generate_context_bootstrap
)


def export_context_bootstrap(
        
    context,
    output_file
):

    content = (
        generate_context_bootstrap(
            context
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