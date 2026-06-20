def build_reverse_graph(
    knowledge_graph
):

    reverse_graph = {}

    for source, targets in knowledge_graph.items():

        for target in targets:

            if target not in reverse_graph:

                reverse_graph[
                    target
                ] = []

            reverse_graph[
                target
            ].append(
                source
            )

    return reverse_graph