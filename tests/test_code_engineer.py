from pprint import pprint

from graph_builder.workers.repository_architect import RepositoryArchitect
from graph_builder.workers.code_engineer import CodeEngineer


def main():

    architect = RepositoryArchitect()

    engineer = CodeEngineer()

    report = architect.assess_repository(

        repository_phase="Stabilization",

        technical_direction="Positive",

    )

    plan = engineer.create_plan(

        report,

    )

    print("\n========================================")
    print("Code Engineer")
    print("========================================\n")

    pprint(plan)


if __name__ == "__main__":
    main()