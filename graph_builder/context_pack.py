def generate_context_pack(
    symbol_index
):

    context = []

    for name, data in symbol_index.items():

        context.append(
            {
                "symbol": name,
                "file": data["file"],
                "type": data["type"],
                "line": data["line"],
                "used_by": len(
                    data["used_by"]
                ),
                "parameters": data.get(
                    "parameters",
                    []
                ),
                "docstring": data.get(
                    "docstring"
                )
            }
        )

    return context