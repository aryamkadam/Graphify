"""
Graphify

Stage 33.0

Engineering Dependency Graph

Represents engineering tasks as
a directed graph.

Author:
Graphify Core
"""


class EngineeringDependencyGraph:

    VERSION = "33.0"

    def __init__(self):

        self._graph = {}

    # ------------------------------------------

    def add_task(self, task_id):

        self._graph.setdefault(

            task_id,

            set(),

        )

    # ------------------------------------------

    def add_dependency(

        self,

        task_id,

        depends_on,

    ):

        self.add_task(task_id)

        self.add_task(depends_on)

        self._graph[task_id].add(depends_on)

    # ------------------------------------------

    def dependencies(

        self,

        task_id,

    ):

        return list(

            self._graph.get(

                task_id,

                set(),

            )

        )

    # ------------------------------------------

    def ready_tasks(self):

        ready = []

        for task, deps in self._graph.items():

            if len(deps) == 0:

                ready.append(task)

        return ready

    # ------------------------------------------

    def status(self):

        edges = sum(

            len(v)

            for v in self._graph.values()

        )

        return {

            "version": self.VERSION,

            "tasks": len(self._graph),

            "dependencies": edges,

        }