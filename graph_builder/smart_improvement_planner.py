def generate_symbol_plan(
    symbol_name,
    symbol_index
):

    symbol = symbol_index.get(
        symbol_name
    )

    if not symbol:

        return None

    callers = []

    for usage in symbol["used_by"]:

        callers.append(
            usage["caller"]
        )

    return {
        "symbol":
        symbol_name,

        "file":
        symbol["file"],

        "dependent_count":
        len(callers),

        "dependents":
        callers,

        "recommendation":
        (
            "Extract responsibilities "
            "into smaller modules."
        )
    }