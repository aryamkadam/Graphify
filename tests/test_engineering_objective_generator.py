from pprint import pprint

from graph_builder.planner.engineering_objective_generator import (
    EngineeringObjectiveGenerator,
)


print("\n========================================")
print("Engineering Objective Generator")
print("========================================\n")

reasoning = {

    "executive_priority": "EXPANSION",

    "executive_recommendation":
        "Expand repository engineering capabilities."

}

generator = EngineeringObjectiveGenerator(

    reasoning

)

pprint(

    generator.build()

)