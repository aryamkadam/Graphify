import json


def import_context_pack(
    file_path
):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        context = json.load(
            file
        )

    return context