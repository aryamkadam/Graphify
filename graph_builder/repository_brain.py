from graph_builder.repository_brain_builder import (
    RepositoryBrainBuilder
)


def generate_repository_brain(
    symbol_index,
    knowledge_graph,
    project_name="Unknown Project",
    project_purpose="Not Specified"
):

    builder = RepositoryBrainBuilder(

        symbol_index,

        knowledge_graph,

        project_name,

        project_purpose

    )

    return builder.build()