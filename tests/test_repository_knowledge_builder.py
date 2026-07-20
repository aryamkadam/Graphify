from pprint import pprint

from graph_builder.repository.repository_snapshot import RepositorySnapshot
from graph_builder.repository.repository_knowledge_builder import (
    RepositoryKnowledgeBuilder,
)


def main():

    print("\n========================================")
    print("Repository Knowledge Builder")
    print("========================================\n")

    snapshot = RepositorySnapshot(

        repository_name="Graphify",

        repository_path="E:/Projects/graphify",

    )

    snapshot.directories = [

        "graph_builder",

        "tests",

    ]

    snapshot.files = [

        "main.py",

        "runtime.py",

    ]

    snapshot.modules = [

        "runtime",

        "repository",

    ]

    snapshot.directory_count = len(snapshot.directories)
    snapshot.file_count = len(snapshot.files)
    snapshot.module_count = len(snapshot.modules)

    builder = RepositoryKnowledgeBuilder()

    knowledge = builder.build(snapshot)

    print("Knowledge Summary\n")

    pprint(knowledge.summary())

    print("\nKnowledge\n")

    pprint(knowledge.to_dict())


if __name__ == "__main__":
    main()