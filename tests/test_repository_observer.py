from pprint import pprint

from graph_builder.runtime.repository_observer import RepositoryObserver


def main():

    observer = RepositoryObserver()

    snapshot = {

        "changed": True,

        "reason": "Repository structure changed.",

    }

    event = observer.observe(

        snapshot,

    )

    print("\n========================================")
    print("Repository Observer")
    print("========================================\n")

    pprint(event.to_dict())


if __name__ == "__main__":
    main()