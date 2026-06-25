import json


def import_graphify_pack(
    file_path="graphify_pack.json"
):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        pack = json.load(
            file
        )

    return pack