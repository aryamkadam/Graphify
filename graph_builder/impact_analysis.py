def analyze_impact(
    symbol_name,
    symbol_index,
    visited=None
):

    if visited is None:

        visited = set()

    if symbol_name in visited:

        return None

    visited.add(
        symbol_name
    )

    symbol = symbol_index.get(
        symbol_name
    )

    if not symbol:

        return None

    result = {
        "symbol": symbol_name,
        "file": symbol["file"],
        "line": symbol["line"],
        "used_by": []
    }

    for usage in symbol["used_by"]:

        caller = usage["caller"]

        child = analyze_impact(
            caller,
            symbol_index,
            visited
        )

        result["used_by"].append(
            {
                "file": usage["file"],
                "caller": caller,
                "count": usage["count"],
                "impact_chain": child
            }
        )

    return result