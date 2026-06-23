import json
import os


EXPORT_DIR = (
    "graphify-export"
)


def export_context_pack(
    context_commit
):

    os.makedirs(
        EXPORT_DIR,
        exist_ok=True
    )

    file_path = os.path.join(

        EXPORT_DIR,

        f"{context_commit['context_id']}.json"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            context_commit,
            file,
            indent=4
        )

    return file_path