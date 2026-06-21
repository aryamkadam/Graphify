from pprint import pprint

from graph_builder.project_decision_brain import (
    generate_project_decision_brain
)

brain = (
    generate_project_decision_brain()
)

print()
print("Project Decision Brain Generated")
print()

pprint(brain)