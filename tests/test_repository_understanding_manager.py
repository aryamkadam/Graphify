"""
Graphify

Phase 22

Stage P22.8

Repository Understanding Manager Test

Validates the Repository Understanding
Runtime Layer.

Author:
Graphify Core
"""

from graph_builder.kernel.graphify_kernel import (
    GraphifyKernel,
)

from graph_builder.understanding.repository_understanding_manager import (
    RepositoryUnderstandingManager,
)


def main():

    print("=" * 60)
    print("REPOSITORY UNDERSTANDING MANAGER TEST")
    print("=" * 60)

    #
    # Boot Graphify
    #

    kernel = GraphifyKernel(

        ".",

        "Graphify",

    )

    kernel.boot()

    #
    # Create Manager
    #

    manager = RepositoryUnderstandingManager(

        kernel.context,

    )

    print("\nInitial Manager Status")

    print(manager.status())

    #
    # Build Understanding
    #

    print("\nBuilding Repository Understanding...")

    understanding = manager.build()

    print("Repository Understanding Built")

    #
    # Latest
    #

    assert manager.latest() is understanding

    print("Latest Understanding Available")

    #
    # Summary
    #

    print("\nUnderstanding Summary")

    print(

        understanding.summary(),

    )

    #
    # Status
    #

    print("\nManager Status")

    print(

        manager.status(),

    )

    #
    # Clear
    #

    print("\nClearing Understanding Cache...")

    manager.clear()

    print(

        manager.status(),

    )

    #
    # Shutdown
    #

    kernel.shutdown()

    print("\nALL TESTS PASSED")


if __name__ == "__main__":

    main()