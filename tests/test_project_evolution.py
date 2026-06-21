from pprint import pprint

from graph_builder.project_evolution_exporter import (
    export_project_evolution
)

evolution = export_project_evolution(
    "graphify-out/project_evolution.json"
)

print()
print(
    "Project Evolution Generated"
)
print()

pprint(
    evolution
)