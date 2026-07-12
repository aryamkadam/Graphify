"""
Graphify

Stage 58.1

Worker Registry

Responsible for registering every
engineering worker during Runtime boot.

Author:
Graphify Core
"""

from graph_builder.workers.base_worker import BaseWorker

from graph_builder.workers.repository_architect_worker import (
    RepositoryArchitectWorker,
)

from graph_builder.workers.code_engineer_worker import (
    CodeEngineerWorker,
)

from graph_builder.workers.testing_engineer_worker import (
    TestingEngineerWorker,
)

from graph_builder.workers.worker_bootstrap_engine import (
    WorkerBootstrapEngine,
)


class WorkerRegistry:

    VERSION = "58.1"

    def __init__(self):

        self._workers = {}

    # --------------------------------------------------

    def register(self, worker: BaseWorker):

        if worker is None:
            raise ValueError("Cannot register a None worker.")

        if not hasattr(worker, "name"):
            raise AttributeError(
                f"Worker {type(worker).__name__} has no 'name' attribute."
            )

        self._workers[worker.name] = worker

        return worker

    # --------------------------------------------------

    def register_default_workers(self):

        """
        Automatically register every
        built-in engineering worker.
        """

        bootstrap = WorkerBootstrapEngine()

        self.register(
            bootstrap.bootstrap(
                RepositoryArchitectWorker(),
                "Architecture",
            )
        )

        self.register(
            bootstrap.bootstrap(
                CodeEngineerWorker(),
                "Implementation",
            )
        )

        self.register(
            bootstrap.bootstrap(
                TestingEngineerWorker(),
                "Testing",
            )
        )

        return self.status()

    # --------------------------------------------------

    def get(self, worker_name):

        return self._workers.get(worker_name)

    # --------------------------------------------------

    def exists(self, worker_name):

        return worker_name in self._workers

    # --------------------------------------------------

    def unregister(self, worker_name):

        return self._workers.pop(worker_name, None)

    # --------------------------------------------------

    def clear(self):

        self._workers.clear()

    # --------------------------------------------------

    def all_workers(self):

        return list(self._workers.keys())

    # --------------------------------------------------

    def all_instances(self):

        return list(self._workers.values())

    # --------------------------------------------------

    def count(self):

        return len(self._workers)

    # --------------------------------------------------

    def status(self):

        return {
            "workers": self.count(),
            "registered_workers": self.all_workers(),
            "version": self.VERSION,
        }