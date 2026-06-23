from graph_builder.context_forecast import (
    generate_forecast
)

from graph_builder.context_goal import (
    generate_goal_plan
)


def generate_roadmap(
    context,
    target_health=95
):

    forecast = generate_forecast(
        context
    )

    goal = generate_goal_plan(
        context,
        target_health
    )

    phases = [

        {
            "phase": 1,
            "title": "Remove Dead Symbols",
            "expected_health":
                forecast[
                    "after_dead_code_removal"
                ]
        },

        {
            "phase": 2,
            "title": "Refactor Critical Symbols",
            "expected_health":
                forecast[
                    "after_refactoring"
                ]
        },

        {
            "phase": 3,
            "title": "Reduce Hotspots",
            "expected_health":
                forecast[
                    "after_hotspot_reduction"
                ]
        },

        {
            "phase": 4,
            "title": "Improve Architecture",
            "expected_health":
                target_health
        }
    ]

    return {

        "current_health":
            goal[
                "current_health"
            ],

        "target_health":
            target_health,

        "confidence":
            goal[
                "success_probability"
            ],

        "estimated_duration":
            "2 Weeks",

        "phases":
            phases
    }