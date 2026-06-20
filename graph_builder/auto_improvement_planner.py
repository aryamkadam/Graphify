from graph_builder.critical_symbol_ranking import (
    rank_critical_symbols
)

from graph_builder.smart_improvement_planner import (
    generate_symbol_plan
)


def generate_repository_plans(
    symbol_index,
    knowledge_graph,
    limit=5
):

    plans = []

    critical_symbols = (
        rank_critical_symbols(
            symbol_index,
            knowledge_graph
        )
    )

    for item in critical_symbols[:limit]:

        plan = generate_symbol_plan(
            item["symbol"],
            symbol_index
        )

        if plan:

            plans.append(
                plan
            )

    return plans