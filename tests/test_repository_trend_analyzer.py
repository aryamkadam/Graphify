from pprint import pprint

from graph_builder.intelligence.repository_trend_analyzer import (
    RepositoryTrendAnalyzer,
)

brain = {

    "health": {

        "health_score": 82

    },

    "knowledge": {

        "dead_code_count": 11,

        "hotspot_count": 7

    },

    "execution": {

        "graph_nodes": 324

    }

}

analysis = RepositoryTrendAnalyzer().analyze(brain)

print()

print("Repository Trend Analysis")

print()

pprint(analysis)