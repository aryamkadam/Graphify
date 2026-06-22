from pprint import pprint

from graph_builder.context_diff_exporter import (
    export_context_diff
)

old_context = {

    "project": {

        "current_stage":
            "stage-6.5-stable",

        "total_commits":
            10,

        "future_features": [

            "GitHub Integration",

            "VS Code Extension"
        ]
    },

    "repository": {

        "health_score":
            65
    }
}

new_context = {

    "project": {

        "current_stage":
            "stage-6.7-stable",

        "total_commits":
            15,

        "future_features": [

            "GitHub Integration",

            "VS Code Extension",

            "UACS",

            "Context Diff Engine"
        ]
    },

    "repository": {

        "health_score":
            75
    }
}

result = export_context_diff(

    old_context,

    new_context
)

print(
    "\nContext Diff Generated\n"
)

pprint(result)