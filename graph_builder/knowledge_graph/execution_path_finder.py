class ExecutionPathFinder:

    """
    Finds execution paths starting
    from repository entry points.
    """

    def __init__(self, execution_graph):

        self.graph = execution_graph

    def build_paths(self):

        paths = []

        for source in self.graph:

            paths.append({

                "entry": source,

                "path": self.graph[source]

            })

        return paths