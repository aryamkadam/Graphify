"""
Graphify

Phase 21

Repository Awareness Manager Tests

Validates the Repository Awareness Runtime.

Author:
Graphify Core
"""

from graph_builder.kernel.graphify_kernel import GraphifyKernel
from graph_builder.awareness.repository_awareness_manager import (
    RepositoryAwarenessManager,
)


def main():

    print("=" * 60)
    print("REPOSITORY AWARENESS MANAGER TEST")
    print("=" * 60)

    #
    # Boot Graphify
    #

    kernel = GraphifyKernel(".", "Graphify")

    kernel.boot()

    manager = RepositoryAwarenessManager(
        kernel.context
    )

    #
    # Initial Status
    #

    print("\nInitial Manager Status")

    print(manager.status())

    assert manager.latest() is None

    #
    # Build Awareness
    #

    print("\nBuilding Awareness Report...")

    report = manager.build()

    assert report is not None

    print("Report Built")

    #
    # Latest Report
    #

    latest = manager.latest()

    assert latest is report

    print("Latest Report Available")

    #
    # Status
    #

    status = manager.status()

    print(status)

    assert status["report_available"]

    #
    # Clear Cache
    #

    print("\nClearing Awareness Cache...")

    manager.clear()

    assert manager.latest() is None

    status = manager.status()

    print(status)

    assert not status["report_available"]

    #
    # Shutdown
    #

    kernel.shutdown()

    print("\nALL TESTS PASSED")


if __name__ == "__main__":

    main()