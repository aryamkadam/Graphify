import json


def export_graphify_pack(
    pack,
    output_file="graphify_pack.json"
):

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            pack,
            file,
            indent=4
        )

    return output_file