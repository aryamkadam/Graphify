from pprint import pprint

from graph_builder.planner.engineering_sprint import (
    EngineeringSprint,
)

print("\n========================================")
print("Engineering Sprint")
print("========================================\n")

sprint = EngineeringSprint(

    title="Sprint 1",

    goal="Reduce Technical Debt",

)

print("Sprint\n")

pprint(

    sprint.to_dict()

)