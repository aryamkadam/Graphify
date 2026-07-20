from pprint import pprint

from graph_builder.engineering.repository_refactoring_executor import (
    RepositoryRefactoringExecutor,
)

print()
print("=" * 40)
print("Repository Refactoring Executor")
print("=" * 40)
print()

plans = [

    {

        "type": "MERGE",

        "severity": "HIGH",

        "goal": "Create single engineering owner",

        "targets": [

            "learning/repository_learning_engine.py",

            "repository/repository_learning_engine.py",

        ],

        "recommended_fix": "Merge into one implementation.",

    },

    {

        "type": "SPLIT",

        "severity": "MEDIUM",

        "goal": "Reduce architectural complexity",

        "targets": [

            "Infrastructure",

        ],

        "recommended_fix": "Split infrastructure into domains.",

    },

]

executor = RepositoryRefactoringExecutor()

report = executor.create_execution_plan(plans)

print("Summary")
print()

pprint(report["summary"])

print()

print("Operations")
print()

for operation in report["operations"]:

    pprint(operation)

    print("-" * 40)