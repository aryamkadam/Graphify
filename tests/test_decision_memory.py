from graph_builder.decision_memory_exporter import (
    export_decision_memory
)

content = (
    export_decision_memory(
        "graphify-out/decision_memory.md"
    )
)

print()
print(
    "Decision Memory Generated"
)
print()

print(
    content
)