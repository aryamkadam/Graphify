import json
import os


HISTORY_DIR = "graphify-context"


def ensure_history_dir():

    os.makedirs(
        HISTORY_DIR,
        exist_ok=True
    )


def save_context_commit(
    commit
):

    ensure_history_dir()

    file_path = os.path.join(

        HISTORY_DIR,

        f"{commit['context_id']}.json"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            commit,
            file,
            indent=4
        )

    return file_path


def get_context_history():

    ensure_history_dir()

    history = []

    for filename in os.listdir(
        HISTORY_DIR
    ):

        if not filename.endswith(
            ".json"
        ):
            continue

        path = os.path.join(
            HISTORY_DIR,
            filename
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            history.append(
                json.load(file)
            )

    history.sort(

        key=lambda x:
        x["timestamp"]
    )

    return history


def load_context_commit(
    context_id
):

    path = os.path.join(

        HISTORY_DIR,

        f"{context_id}.json"
    )

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(
            file
        )