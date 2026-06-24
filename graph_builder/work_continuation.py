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

            "Design universal AI context schema",

            "Create Claude context adapter",

            "Create Gemini context adapter",

            "Create Local LLM adapter"

        ]
    }