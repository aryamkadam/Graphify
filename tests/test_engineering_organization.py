from pprint import pprint

from graph_builder.workers.repository_architect import RepositoryArchitect
from graph_builder.workers.code_engineer import CodeEngineer
from graph_builder.workers.engineering_worker import EngineeringWorker

from graph_builder.workers.engineering_organization import (
    EngineeringOrganization,
)


def main():

    workers = [

        RepositoryArchitect(),

        CodeEngineer(),

        EngineeringWorker(

            "Planning Worker",

            "Planning",

        ),

        EngineeringWorker(

            "Engineering Worker",

            "Engineering",

        ),

    ]

    organization = EngineeringOrganization(

        workers,

    )

    print("\n========================================")
    print("Engineering Organization")
    print("========================================\n")

    pprint(

        organization.summary()

    )

    print("\nAvailable Workers\n")

    pprint(

        [

            worker.worker_name

            for worker in organization.available_workers()

        ]

    )

    print("\nWorker Roles\n")

    pprint(

        organization.worker_roles()

    )


if __name__ == "__main__":

    main()