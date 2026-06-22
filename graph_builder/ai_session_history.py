import json
import os


MEMORY_FILE = (
    "graphify-out/ai_sessions.json"
)


def load_ai_sessions():

    if not os.path.exists(
        MEMORY_FILE
    ):

        return []

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(
            file
        )


def save_ai_session(
    session
):

    sessions = (
        load_ai_sessions()
    )

    sessions.append(
        session
    )

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            sessions,
            file,
            indent=4
        )

    return sessions