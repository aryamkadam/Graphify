from pprint import pprint

from graph_builder.project_memory_exporter import (
    export_project_memory
)

memory = export_project_memory(
    "graphify-out/project_memory.json"
)

print()
print(
    "Project Memory Generated"
)
print()

pprint(memory)