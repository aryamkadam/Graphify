from graph_builder.context_bootstrap import (
    generate_context_bootstrap
)

from graph_builder.session_reconstruction import (
    generate_session_reconstruction
)

from graph_builder.context_importer import (
    import_context_pack
)


def generate_cross_ai_transfer_pack(
    context_file
):

    context = import_context_pack(
        context_file
    )

    return {

        "target":
            "Any AI System",

        "project":
            context["project_name"],

        "bootstrap":
            generate_context_bootstrap(
                context
            ),

        "session_reconstruction":
            generate_session_reconstruction(),

        "goal":
            "Continue project understanding"
    }