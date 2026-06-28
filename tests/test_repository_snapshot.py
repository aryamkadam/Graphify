"""
Stage 16.1

Repository Snapshot Test

This is a smoke test for the Repository Snapshot.

Later this test will be upgraded to use the
real Symbol Index and Knowledge Graph generated
by Graphify's parser pipeline.

Current version verifies that the Snapshot
engine can execute successfully.
"""

from pprint import pprint

from graph_builder.memory.repository_snapshot import (
    RepositorySnapshot,
)


def main():

    # Temporary placeholder objects.
    # These will later come from Graphify's parser.

    symbol_index = {}

    knowledge_graph = {}

    snapshot = RepositorySnapshot(

        symbol_index=symbol_index,

        knowledge_graph=knowledge_graph,

        project_name="Graphify",

        project_purpose="Repository Intelligence Platform",

    ).build()

    print("\n==============================")
    print("Repository Snapshot")
    print("==============================\n")

    pprint(snapshot)


if __name__ == "__main__":
    main()