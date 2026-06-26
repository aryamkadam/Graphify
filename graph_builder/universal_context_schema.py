from graph_builder.context_history import (
    get_context_history
)

from graph_builder.decision_history import (
    build_decision_history
)

from graph_builder.structured_reconstruction import (
    generate_structured_reconstruction
)

from graph_builder.work_continuation import (
    generate_work_continuation_pack
)

from graph_builder.context_transfer_quality import (
    generate_transfer_quality
)

from graph_builder.stage_resolver import (
    resolve_current_stage
)


def generate_universal_context_schema():

    history = get_context_history()

    decisions = build_decision_history()

    continuation = (
        generate_work_continuation_pack()
    )

    quality = (
        generate_transfer_quality()
    )

    return {

        "identity": {

            "project_name":
                "Graphify",

            "goal":
                "Git for AI Context",

            "current_stage":
                resolve_current_stage()
        },

        "history": {

            "context_commits":
                history
        },

        "decisions": {

            "decision_history":
                decisions
        },

        "reconstruction":
            generate_structured_reconstruction(),

        "continuation":
            continuation,

        "quality":
            quality
    }