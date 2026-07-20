"""
Graphify

Phase 11

Stage P11.2

Repository Scanner Test

Author:
Graphify Core
"""

from pprint import pprint

from graph_builder.scanner.repository_scanner import (
    RepositoryScanner,
)


def main():

    scanner = RepositoryScanner(

        repository_name="Graphify",

        repository_path=".",

    )

    inventory = scanner.scan()

    print("\n========================================")
    print("Repository Scanner")
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