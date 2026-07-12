from pprint import pprint

from graph_builder.prediction.repository_prediction_engine import (
    RepositoryPredictionEngine,
)

trend_report = {

    "health_score": 82,

    "dead_code": 11,

    "hotspots": 7,

    "graph_nodes": 324,

}

prediction = RepositoryPredictionEngine().predict(
    trend_report
)

print()

print("Repository Prediction")

print()

pprint(prediction)