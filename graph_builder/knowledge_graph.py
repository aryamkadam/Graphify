def build_knowledge_graph(
    symbol_index
):

    graph = {}

    for symbol, data in symbol_index.items():

        graph[symbol] = []

        for usage in data["used_by"]:

            caller = usage["caller"]

            # Ignore recursive self-calls
            if caller == symbol:
                continue

            graph[
                symbol
            ].append(
                caller
            )

    return graph