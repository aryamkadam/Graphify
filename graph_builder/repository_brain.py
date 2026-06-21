from graph_builder.repository_health_report import (
    generate_health_report
)

from graph_builder.repository_knowledge_pack import (
    build_repository_knowledge_pack
)

from graph_builder.repository_metadata import (
    get_repository_metadata
)

from graph_builder.project_decision_brain import (
    generate_project_decision_brain
)

from graph_builder.decision_insights import (
    generate_decision_insights
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

    decision_brain = (
        generate_project_decision_brain()
    )

    decision_insights = (
        generate_decision_insights()
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

        "decision_count":
            decision_brain[
                "decision_count"
            ],

        "latest_decisions":
            decision_brain[
                "latest_decisions"
            ],

        "most_important_decision":
            decision_brain[
                "most_important_decisions"
            ][0],

        "decision_insights":
            decision_insights,

        "project_direction":
            decision_insights[
                "dominant_area"
            ],

        "top_recommendations":
            health_report[
                "top_recommendations"
            ]
    }

    return brain