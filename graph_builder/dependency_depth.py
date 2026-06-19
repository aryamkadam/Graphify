def calculate_depth(
    symbol_name,
    symbol_index,
    visited=None
):

    if visited is None:
        visited = set()

    if symbol_name in visited:
        return 0

    visited.add(symbol_name)

    symbol = symbol_index.get(
        symbol_name
    )

    if not symbol:
        return 0

    if not symbol["used_by"]:
        return 0

    depths = []

    for usage in symbol["used_by"]:

        depths.append(
            1 +
            calculate_depth(
                usage["caller"],
                symbol_index,
                visited.copy()
            )
        )

    return max(depths)