"""
Stage 21.1

Runtime Service Test
"""

from pprint import pprint

from graph_builder.runtime.runtime_service import RuntimeService

service = RuntimeService(

    "Memory Service",

)

print("\n========================================")
print("Runtime Service")
print("========================================\n")

pprint(service.status())

print("\nStart Service\n")

pprint(service.start())

print("\nCurrent Status\n")

pprint(service.status())

print("\nRestart\n")

pprint(service.restart())

print("\nStop\n")

pprint(service.stop())

print("\nFinal Status\n")

pprint(service.status())