from pprint import pprint

from graph_builder.planner.engineering_risk_analyzer import (
    EngineeringRiskAnalyzer,
)

print("\n========================================")
print("Engineering Risk Analyzer")
print("========================================\n")

sprint = {

    "strategy": "EXPANSION",

    "priority": "HIGH",

    "tasks": [

        {

            "id": 1,

            "title": "Analyze repository architecture",

            "role": "architecture",

        },

        {

            "id": 2,

            "title": "Improve plugin architecture",

            "role": "implementation",

        },

        {

            "id": 3,

            "title": "Expand runtime capabilities",

            "role": "implementation",

        },

        {

            "id": 4,

            "title": "Increase worker intelligence",

            "role": "testing",

        }

    ]

}

analyzer = EngineeringRiskAnalyzer(

    sprint

)

pprint(

    analyzer.build()

)