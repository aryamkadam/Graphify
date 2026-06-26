from graph_builder.context_forecast import (
    generate_forecast
)

from graph_builder.context_goal import (
    generate_goal_plan
)


def generate_roadmap(
    context,
    target_transfer_score=100
):

    forecast = generate_forecast(
        context
    )

    goal = generate_goal_plan(
        context,
        target_transfer_score
    )

    phases = [

        {
            "phase": 1,
            "title":
                "Universal Context Schema",

            "expected_score":
                forecast[
                    "after_context_growth"
                ]
        },

        {
            "phase": 2,
            "title":
                "Claude Context Adapter",

            "expected_score":
                forecast[
                    "after_decision_growth"
                ]
        },

        {
            "phase": 3,
            "title":
                "Gemini Context Adapter",

            "expected_score":
                forecast[
                    "predicted_ai_readiness"
                ]
        },

        {
            "phase": 4,
            "title":
                "Local LLM Adapter",

            "expected_score":
                target_transfer_score
        }
    ]

    return {

        "current_transfer_score":
            goal[
                "current_transfer_score"
            ],

        "target_transfer_score":
            target_transfer_score,

        "confidence":
            goal[
                "success_probability"
            ],

        "estimated_duration":
            "4 Stages",

        "phases":
            phases
    }