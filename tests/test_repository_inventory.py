"""
Graphify

Phase 11

Stage P11.1

Repository Inventory Test

Smoke test for RepositoryInventory.

Author:
Graphify Core
"""

from pprint import pprint

from graph_builder.scanner.repository_inventory import (
    RepositoryInventory,
)


def main():

    inventory = RepositoryInventory(

        repository_name="Graphify",

        repository_path="E:/Projects/graphify",

    )

    inventory.directories = [

        "graph_builder",
        "tests",
        "docs",

    ]

    inventory.python_files = [

        "main.py",
        "runtime.py",

    ]

    inventory.markdown_files = [

        "README.md",
        "VISION.md",

    ]

    inventory.directory_count = len(

        inventory.directories

    )

    inventory.file_count = (

        len(inventory.python_files)

        + len(inventory.markdown_files)

    )

    inventory.python_file_count = len(

        inventory.python_files

    )

    print("\n========================================")
    print("Repository Inventory")
    print("========================================\n")

    print("Summary\n")

    pprint(

        inventory.summary()

    )

    print("\nInventory\n")

    pprint(

        inventory.to_dict()

    )


if __name__ == "__main__":
    main()