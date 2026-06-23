import json


def save_context_commit(
    commit,
    output_file
):

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            commit,
            file,
            indent=4
        )

    return output_file