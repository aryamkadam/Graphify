def predict_impact(
    symbol,
    knowledge_graph,
    visited=None
):

    if visited is None:
        visited = set()

    if symbol in visited:
        return []

    visited.add(symbol)

    impacted = []

    for dependent in knowledge_graph.get(
        symbol,
        []
    ):

        impacted.append(
            dependent
        )

        impacted.extend(
            predict_impact(
                dependent,
                knowledge_graph,
                visited.copy()
            )
        )

    return impacted