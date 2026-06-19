from graph_builder.query_engine import (
    load_symbol_index
)


def build_repository_flow(
    symbol_name,
    symbol_index,
    visited=None
):

    if visited is None:
        visited = set()

    if symbol_name in visited:
        return None

    visited.add(symbol_name)

    symbol = symbol_index.get(
        symbol_name
    )

    if not symbol:
        return None

    flow = {
        "symbol": symbol_name,
        "children": []
    }

    for usage in symbol["used_by"]:

        caller = usage["caller"]

        child = build_repository_flow(
            caller,
            symbol_index,
            visited
        )

        if child:

            flow["children"].append(
                child
            )

    return flow