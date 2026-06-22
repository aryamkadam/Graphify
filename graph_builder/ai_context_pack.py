from graph_builder.repository_brain import (
    generate_repository_brain
)

from graph_builder.project_memory import (
    generate_project_memory
)

from graph_builder.project_decision_brain import (
    generate_project_decision_brain
)

from graph_builder.github_intelligence import (
    generate_github_intelligence
)

from graph_builder.ai_session_memory import (
    generate_ai_session_memory
)


def build_ai_context_pack(
    symbol_index,
    knowledge_graph
):

    return {

        "repository_brain":
            generate_repository_brain(
                symbol_index,
                knowledge_graph,
                "Graphify",
                "AI Context Transfer Engine"
            ),

        "project_memory":
            generate_project_memory(),

        "decision_brain":
            generate_project_decision_brain(),

        "github_intelligence":
            generate_github_intelligence(),

        "session_memory":
            generate_ai_session_memory()
    }