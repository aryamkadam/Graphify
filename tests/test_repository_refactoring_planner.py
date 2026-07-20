from pprint import pprint

from graph_builder.architecture.repository_refactoring_planner import (
    RepositoryRefactoringPlanner,
)

print()
print("=" * 40)
print("Repository Refactoring Planner")
print("=" * 40)
print()

planner = RepositoryRefactoringPlanner()

diagnostics = [

    {
        "category": "Duplicate Responsibility",
        "severity": "HIGH",
        "affected_components": [
            "learning/repository_learning_engine.py",
            "repository/repository_learning_engine.py",
        ],
        "recommended_fix":
        "Merge into one implementation.",
    },

    {
        "category": "Oversized Layer",
        "severity": "MEDIUM",
        "affected_components": [
            "Infrastructure"
        ],
        "recommended_fix":
        "Split infrastructure into domains.",
    }

]

plan = planner.build_plan(diagnostics)

print("Summary")
print()

pprint({

    "migration_count": plan["migration_count"],

    "overall_priority": plan["overall_priority"],

    "version": plan["version"],

})

print()

print("Plans")
print()

for p in plan["plans"]:

    pprint(p)

    print("-" * 40)