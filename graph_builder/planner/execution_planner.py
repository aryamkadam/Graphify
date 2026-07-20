"""
Graphify

Phase 6

Stage P6.4

Execution Planner

Builds an executable engineering roadmap
from dependency relationships.

Author:
Graphify Core
"""


class ExecutionPlanner:

    VERSION = "P6.4"

    # --------------------------------------------------

    def build(

        self,

        dependency_report,

    ):

        graph = dependency_report.get(

            "dependency_graph",

            {},

        )

        execution_order = []

        visited = set()

        while len(visited) < len(graph):

            progress = False

            for node, info in graph.items():

                if node in visited:

                    continue

                deps = info.get(

                    "depends_on",

                    [],

                )

                if all(

                    dep in visited

                    for dep in deps

                ):

                    execution_order.append(

                        node

                    )

                    visited.add(

                        node

                    )

                    progress = True

            if not progress:

                break

        return {

            "execution_order":

                execution_order,

            "completed":

                len(execution_order),

            "summary":

                (

                    f"{len(execution_order)} work packages "

                    f"scheduled for execution."

                ),

            "version":

                self.VERSION,

        }