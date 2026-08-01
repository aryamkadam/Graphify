"""
Graphify

Kernel Integration Test

Tests the complete Kernel boot lifecycle.
"""

from graph_builder.kernel.graphify_kernel import GraphifyKernel


def main():

    print("=" * 60)
    print("GRAPHIFY KERNEL TEST")
    print("=" * 60)

    kernel = GraphifyKernel(

        repository_path=".",

        project_name="Graphify",

    )

    print("\nInitial Status")
    print(kernel.status())

    print("\nBooting Kernel...")

    kernel.boot()

    print("\nKernel Status")
    print(kernel.status())

    assert kernel.context.booted is True

    assert kernel.context.repository_loaded is True

    assert kernel.context.repository_brain is not None

    assert kernel.context.repository_intelligence is not None

    assert kernel.context.engineering_runtime is not None

    print("\nRepository Boot Successful")

    print("\nShutting Down...")

    kernel.shutdown()

    print(kernel.status())

    assert kernel.context.booted is False

    print("\nShutdown Successful")

    print("\nALL TESTS PASSED")


if __name__ == "__main__":
    main()