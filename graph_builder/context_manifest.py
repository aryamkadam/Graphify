from graph_builder.schema_versioning import (
    get_schema_version
)

from graph_builder.context_transfer_quality import (
    generate_transfer_quality
)

from graph_builder.context_history import (
    get_context_history
)

from graph_builder.decision_history import (
    build_decision_history
)


def generate_context_manifest():

    history = (
        get_context_history()
    )

    decisions = (
        build_decision_history()
    )

    quality = (
        generate_transfer_quality()
    )

    manifest = {

        "schema_version":
            get_schema_version(),

        "context_commits":
            len(history),

        "decisions":
            len(decisions),

        "transfer_score":
            quality[
                "transfer_score"
            ],

        "recommendation":
            quality[
                "recommendation"
            ]
    }

    return manifest