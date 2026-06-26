import json


def serialize_uacp_json(
    protocol
):

    return json.dumps(

        protocol,

        indent=4,

        ensure_ascii=False

    )


def save_uacp_json(

    protocol,

    filepath

):

    with open(

        filepath,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            protocol,

            file,

            indent=4,

            ensure_ascii=False

        )

    return filepath


def load_uacp_json(

    filepath

):

    with open(

        filepath,

        "r",

        encoding="utf-8"

    ) as file:

        return json.load(file)