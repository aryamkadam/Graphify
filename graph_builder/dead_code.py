def detect_dead_code(
    symbol_index
):

    dead_symbols = []

    for symbol, data in symbol_index.items():

        if len(
            data["used_by"]
        ) == 0:

            dead_symbols.append(
                {
                    "symbol": symbol,
                    "type": data["type"],
                    "file": data["file"]
                }
            )

    return dead_symbols