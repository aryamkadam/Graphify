import json


def export_context_pack(
    context_pack,
    output_file
):

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            context_pack,
            file,
            indent=4
        )

    return context_pack