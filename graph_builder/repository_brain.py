from graph_builder.repository_health_report import (
    generate_health_report
)

from graph_builder.repository_knowledge_pack import (
    build_repository_knowledge_pack
)

from graph_builder.repository_metadata import (
    get_repository_metadata
)


def generate_repository_brain(
    symbol_index,
    knowledge_graph,
    project_name="Unknown Project",
    project_purpose="Not Specified"
):

    metadata = (
        get_repository_metadata()
    )

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

    critical_symbols = []

    for item in knowledge_pack[
        "critical_symbols"
    ][:5]:

        critical_symbols.append(
            item["symbol"]
        )

    risky_symbols = []

    for item in knowledge_pack[
        "risky_symbols"
    ][:5]:

        risky_symbols.append(
            item["symbol"]
        )

    brain = {

        "project_name":
            project_name,

        "project_purpose":
            project_purpose,

        "current_stage":
            metadata[
                "current_stage"
            ],

        "latest_commit":
            metadata[
                "latest_commit"
            ],

        "total_commits":
            metadata[
                "total_commits"
            ],

        "latest_tag":
            metadata.get(
                "latest_tag",
                "unknown"
            ),

        "current_branch":
            metadata.get(
                "current_branch",
                "unknown"
            ),

        "health_score":
            health_report[
                "health_score"
            ],

        "status":
            health_report[
                "status"
            ],

        "critical_symbols":
            critical_symbols,

        "risky_symbols":
            risky_symbols,

        "dead_code_count":
            len(
                knowledge_pack[
                    "dead_code"
                ]
            ),

        "hotspot_count":
            len(
                knowledge_pack[
                    "hotspots"
                ]
            ),

        "top_recommendations":
            health_report[
                "top_recommendations"
            ]
    }

    return brain