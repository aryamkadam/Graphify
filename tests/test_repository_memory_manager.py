from pprint import pprint

from graph_builder.memory.repository_memory_manager import (
    RepositoryMemoryManager,
)

from graph_builder.memory.repository_snapshot import (
    RepositorySnapshot,
)


def build_snapshot():

    symbol_index = {}

    knowledge_graph = {}

    return RepositorySnapshot(

        symbol_index,

        knowledge_graph,

        "Graphify",

        "Repository Intelligence Platform"

    ).build()


def main():

    manager = RepositoryMemoryManager()

    snapshot1 = build_snapshot()

    snapshot2 = build_snapshot()

    manager.save_snapshot(snapshot1)

    manager.save_snapshot(snapshot2)

    print("\nRepository Memory Manager\n")

    print("Snapshots Stored:")

    print(manager.snapshot_count())

    print("\nLatest Snapshot Metadata:\n")

    pprint(
        manager.latest_snapshot()["metadata"]
    )


if __name__ == "__main__":

    main()