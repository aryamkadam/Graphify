from pprint import pprint

from graph_builder.runtime.repository_event import RepositoryEvent


def main():

    event = RepositoryEvent(

        event_type="REPOSITORY_MODIFIED",

        reason="Repository structure changed.",

        requires_engineering=True,

    )

    print("\n========================================")
    print("Repository Event")
    print("========================================\n")

    pprint(event.to_dict())


if __name__ == "__main__":

    main()