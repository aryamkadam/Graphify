from pprint import pprint

from graph_builder.workers.repository_architect import RepositoryArchitect


def main():

    architect = RepositoryArchitect()

    print("\n========================================")
    print("Repository Architect")
    print("========================================\n")

    assessment = architect.assess_repository(

        repository_phase="Stabilization",

        technical_direction="Positive",

    )

    pprint(assessment)


if __name__ == "__main__":
    main()