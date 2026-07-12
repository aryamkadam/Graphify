from pprint import pprint

from graph_builder.engineering.engineering_dependency_graph import (
    EngineeringDependencyGraph,
)

print("\n========================================")
print("Engineering Dependency Graph")
print("========================================\n")

graph = EngineeringDependencyGraph()

graph.add_dependency(

    "Task_B",

    "Task_A",

)

graph.add_dependency(

    "Task_C",

    "Task_B",

)

graph.add_task(

    "Task_D",

)

print("Status\n")

pprint(graph.status())

print("\nReady Tasks\n")

pprint(graph.ready_tasks())

print("\nDependencies of Task_C\n")

pprint(graph.dependencies("Task_C"))