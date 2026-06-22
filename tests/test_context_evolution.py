from pprint import pprint

from graph_builder.context_evolution import (
    generate_context_evolution
)

old_context = {

    "project": {

        "current_stage":
            "stage-6.5-stable",

        "total_commits":
            7,

        "future_features": [

            "GitHub Integration"
        ]
    },

    "repository": {

        "health_score":
            61
    }
}

new_context = {

    "project": {

        "current_stage":
            "stage-6.7-stable",

        "total_commits":
            12,

        "future_features": [

            "GitHub Integration",
            "UACS",
            "Context Diff Engine"
        ]
    },

    "repository": {

        "health_score":
            71
    }
}

result = generate_context_evolution(
    old_context,
    new_context
)

print(
    "\nContext Evolution Generated\n"
)

pprint(result)