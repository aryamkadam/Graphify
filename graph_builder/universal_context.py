from graph_builder.ai_context_pack import (
    build_ai_context_pack
)


def build_universal_context(
    symbol_index,
    knowledge_graph
):

    context = (
        build_ai_context_pack(
            symbol_index,
            knowledge_graph
        )
    )

    return {

        "schema_version":
            "1.0",

        "project":
            context["project_memory"],

        "repository":
            context["repository_brain"],

        "github":
            context["github_intelligence"],

        "decisions":
            context["decision_brain"],

        "sessions":
            context["session_memory"]
    }