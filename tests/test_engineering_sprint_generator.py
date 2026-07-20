from pprint import pprint

from graph_builder.planner.engineering_sprint_generator import (
    EngineeringSprintGenerator,
)

print("\n========================================")
print("Engineering Sprint Generator")
print("========================================\n")

objective_plan = {

    "strategy": "EXPANSION",

    "priority": "HIGH",

    "objectives": [

        "Analyze repository architecture",

        "Improve plugin architecture",

        "Expand runtime capabilities",

        "Increase worker intelligence",

    ],

}

generator = EngineeringSprintGenerator(

    objective_plan

)

pprint(

    generator.build()

)