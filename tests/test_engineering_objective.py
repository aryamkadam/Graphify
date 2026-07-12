from pprint import pprint

from graph_builder.planner.engineering_objective import (
    EngineeringObjective,
)

print("\n========================================")
print("Engineering Objective")
print("========================================\n")

objective = EngineeringObjective(

    title="Improve Repository Security",

    description="Increase overall repository security posture.",

    priority="HIGH",

)

print("Objective\n")

pprint(

    objective.to_dict()

)

objective.complete()

print("\nCompleted\n")

pprint(

    objective.to_dict()

)