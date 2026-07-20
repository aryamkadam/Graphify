from pprint import pprint

from graph_builder.executive.executive_prediction_engine import (
    ExecutivePredictionEngine,
)


def main():

    recall = {

        "matches": 2,

    }

    strategy = {

        "engineering_strategy":

            "Continuous Quality Expansion",

    }

    report = (

        ExecutivePredictionEngine()

        .build(

            recall,

            strategy,

        )

    )

    print("\n========================================")
    print("Executive Prediction Engine")
    print("========================================\n")

    pprint(report)


if __name__ == "__main__":

    main()