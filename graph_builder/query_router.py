from graph_builder.query_intent import (
    detect_query_intent
)

from graph_builder.dead_code import (
    detect_dead_code
)

from graph_builder.hotspot_analysis import (
    detect_hotspots
)

from graph_builder.risk_ranking import (
    rank_repository_risks
)

from graph_builder.critical_symbol_ranking import (
    rank_critical_symbols
)

from graph_builder.search_ranker import (
    rank_search_results
)


def route_query(
    query,
    symbol_index,
    knowledge_graph
):

    intent = detect_query_intent(
        query
    )

    if intent == "dead_code":

        return detect_dead_code(
            symbol_index
        )

    if intent == "hotspots":

        return detect_hotspots(
            symbol_index
        )

    if intent == "risky_symbols":

        return rank_repository_risks(
            symbol_index,
            knowledge_graph
        )

    if intent == "critical_symbols":

        return rank_critical_symbols(
            symbol_index,
            knowledge_graph
        )

    if intent == "search":

        return rank_search_results(
            query,
            symbol_index
        )

    return {
        "message":
        "Unknown query."
    }