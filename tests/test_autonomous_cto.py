from pprint import pprint

from graph_builder.executive.autonomous_cto import (
    AutonomousCTO,
)

print("\n========================================")
print("Autonomous CTO")
print("========================================\n")

reasoning = {

    "executive_priority":

        "EXPANSION",

    "executive_recommendation":

        "Expand repository engineering capabilities."

}

cto = AutonomousCTO(

    reasoning

)

pprint(

    cto.think()

)