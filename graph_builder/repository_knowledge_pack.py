from graph_builder.critical_symbol_ranking import (
    rank_critical_symbols
)

from graph_builder.risk_ranking import (
    rank_repository_risks
)

from graph_builder.dead_code import (
    detect_dead_code
)

from graph_builder.hotspot_analysis import (
    detect_hotspots
)


def build_repository_knowledge_pack(
    symbol_index,
    knowledge_graph
):

    critical_symbols = (
        rank_critical_symbols(
            symbol_index,
            knowledge_graph
        )[:10]
    )

    risky_symbols = (
        rank_repository_risks(
            symbol_index,
            knowledge_graph
        )[:10]
    )

    dead_code = (
        detect_dead_code(
            symbol_index
        )
    )

    hotspots = (
        detect_hotspots(
            symbol_index
        )[:10]
    )

    return {
        "total_symbols": len(
            symbol_index
        ),
        "critical_symbols":
            critical_symbols,
        "risky_symbols":
            risky_symbols,
        "dead_code":
            dead_code,
        "hotspots":
            hotspots
    }