from pprint import pprint

from graph_builder.decision_insights_exporter import (
    export_decision_insights
)

insights = (
    export_decision_insights(
        "graphify-out/decision_insights.json"
    )
)

print(
    "\nDecision Insights Generated\n"
)

pprint(
    insights
)