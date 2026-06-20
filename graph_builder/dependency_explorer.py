def explore_dependencies(
    symbol,
    reverse_graph,
    visited=None
):

    if visited is None:
        visited = set()

    if symbol in visited:
        return None

    visited.add(symbol)

    tree = {
        "symbol": symbol,
        "dependencies": []
    }

    for dependency in reverse_graph.get(
        symbol,
        []
    ):

        child = explore_dependencies(
            dependency,
            reverse_graph,
            visited.copy()
        )

        if child:

            tree[
                "dependencies"
            ].append(
                child
            )

    return tree