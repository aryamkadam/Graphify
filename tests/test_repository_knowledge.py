from pprint import pprint

from graph_builder.repository.repository_knowledge import RepositoryKnowledge


def main():

    print("\n========================================")
    print("Repository Knowledge")
    print("========================================\n")

    knowledge = RepositoryKnowledge(

        repository_name="Graphify",

        repository_path="E:/Projects/graphify",

        language="Python",

        framework="Custom",

        build_system="Poetry",

    )

    print("Summary\n")

    pprint(knowledge.summary())

    print("\nKnowledge Model\n")

    pprint(knowledge.to_dict())


if __name__ == "__main__":
    main()