import json


def load_symbol_index(path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def find_symbol(
    symbol_name,
    symbol_index
):

    return symbol_index.get(
        symbol_name
    )