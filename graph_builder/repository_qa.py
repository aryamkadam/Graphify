from graph_builder.query_router import (
    route_query
)

from graph_builder.query_intent import (
    detect_query_intent
)


def answer_query(
    query,
    symbol_index,
    knowledge_graph
):

    intent = detect_query_intent(
        query
    )

    result = route_query(
        query,
        symbol_index,
        knowledge_graph
    )

    if intent == "critical_symbols":

        top = result[0]

        return (
            f"Most critical symbol: "
            f"{top['symbol']} "
            f"(score={top['critical_score']}) "
            f"in {top['file']}"
        )

    if intent == "risky_symbols":

        top = result[0]

        return (
            f"Highest risk symbol: "
            f"{top['symbol']} "
            f"(severity={top['severity']})"
        )

    if intent == "hotspots":

        top = result[0]

        return (
            f"Hottest file: "
            f"{top['file']} "
            f"(usage_count={top['usage_count']})"
        )

    if intent == "dead_code":

        return (
            f"Dead code symbols found: "
            f"{len(result)}"
        )

    return str(result)