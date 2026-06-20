import json

from graph_builder.repository_health_report import (
    generate_health_report
)

from graph_builder.repository_knowledge_pack import (
    build_repository_knowledge_pack
)


def export_dashboard(
    symbol_index,
    knowledge_graph,
    output_file
):

    health_report = (
        generate_health_report(
            symbol_index,
            knowledge_graph
        )
    )

    knowledge_pack = (
        build_repository_knowledge_pack(
            symbol_index,
            knowledge_graph
        )
    )

    dashboard = {
        "health_report":
            health_report,

        "knowledge_pack":
            knowledge_pack
    }

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            dashboard,
            f,
            indent=4
        )

    return dashboard