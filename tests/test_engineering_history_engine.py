from pprint import pprint

from graph_builder.executive.engineering_history_engine import (
    EngineeringHistoryEngine,
)

from graph_builder.executive.engineering_sprint import (
    EngineeringSprint,
)

print("\n========================================")
print("Engineering History Engine")
print("========================================\n")

history = EngineeringHistoryEngine()

report = {

    "completed_tasks": 3,

    "report": [],

}

sprint = EngineeringSprint(

    objective="Improve Runtime",

    strategy="EXPANSION",

    report=report,

)

history.archive(

    sprint

)

print("Status\n")

pprint(

    history.status()

)

print("\nLatest Sprint\n")

pprint(

    history.latest().summary()

)