from graph_builder.repository_qa import (
    answer_query
)


def ask_repository(
    query,
    symbol_index,
    knowledge_graph
):

    return answer_query(
        query,
        symbol_index,
        knowledge_graph
    )