from pprint import pprint

from graph_builder.executive.executive_decision_intelligence import (
    ExecutiveDecisionIntelligence,
)


def main():

    strategy = {

        "engineering_strategy":

            "Continuous Quality Expansion",

    }

    recall = {

        "matches": 2,

    }

    prediction = {

        "confidence": 0.75,

        "predicted_outcome":

            "Likely Repository Improvement",

    }

    report = (

        ExecutiveDecisionIntelligence()

        .build(

            strategy,

            recall,

            prediction,

        )

    )

    print("\n========================================")
    print("Executive Decision Intelligence")
    print("========================================\n")

    pprint(report)


if __name__ == "__main__":

    main()