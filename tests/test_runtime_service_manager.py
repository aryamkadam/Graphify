"""
Stage 21.2

Runtime Service Manager Test
"""

from pprint import pprint

from graph_builder.runtime.runtime_service import RuntimeService
from graph_builder.runtime.runtime_service_manager import RuntimeServiceManager

manager = RuntimeServiceManager()

memory = RuntimeService("Memory Service")
brain = RuntimeService("Executive Brain")
planner = RuntimeService("Planner")

print("\n========================================")
print("Runtime Service Manager")
print("========================================\n")

print("Register Services\n")

pprint(manager.register(memory))
pprint(manager.register(brain))
pprint(manager.register(planner))

print("\nManager Status\n")

pprint(manager.status())

print("\nAvailable Services\n")

pprint(manager.list_services())

print("\nStart All\n")

pprint(manager.start_all())

print("\nStop All\n")

pprint(manager.stop_all())