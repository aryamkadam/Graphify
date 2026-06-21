from graph_builder.decision_reasoning_exporter import (
    export_decision_reasoning_pack
)

content = export_decision_reasoning_pack(
    "graphify-out/decision_reasoning_pack.md"
)

print()
print("Decision Reasoning Pack Generated")
print()

print(content)