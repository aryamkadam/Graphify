from graph_builder.context_continuation import (
    generate_context_continuation
)


def generate_work_continuation_pack():

    continuation = (
        generate_context_continuation()
    )

    return {

        "current_state":
            continuation[
                "current_maturity"
            ],

        "next_objective":
            continuation[
                "recommended_next_stage"
            ],

        "reason":
            continuation[
                "reason"
            ],

        "recommended_actions": [

            "Improve cross-AI context compatibility",

            "Build Claude transfer workflow",

            "Build Gemini transfer workflow",

            "Build Local LLM transfer workflow",

            "Improve context quality scoring",

            "Prepare autonomous AI handover system"
        ]
    }