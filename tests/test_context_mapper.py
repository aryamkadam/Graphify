from pprint import pprint

from graph_builder.protocols.uacp.context_mapper import (
    map_universal_context
)

sample = {

    "schema_version": "1.0",

    "project": {
        "project_name": "Graphify",
        "goal": "Universal AI Context Infrastructure",
        "current_stage": "Stage 13"
    },

    "repository": {
        "current_stage": "Stage 13",
        "latest_commit": "abc123",
        "total_commits": 412,
        "latest_tag": "stage-13",
        "current_branch": "master"
    },

    "decisions": {

        "decision_count": 3,

        "latest_decisions": [
            "Created UACP",
            "Implemented SDK",
            "Added Context Mapper"
        ],

        "most_important_decisions": [
            "UACP Architecture",
            "Universal Context",
            "Protocol Independence"
        ]
    }
}
result = map_universal_context(sample)

print("\nMapped Context\n")

pprint(result)