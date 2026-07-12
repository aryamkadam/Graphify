from pprint import pprint

from graph_builder.workers.collaboration_engine import (
    CollaborationEngine,
)

print("\n========================================")
print("Collaboration Engine")
print("========================================\n")

engine = CollaborationEngine()

print("Architecture Proposal\n")

pprint(

    engine.send(

        "Repository Architect",

        "Code Engineer",

        "ARCHITECTURE_PROPOSAL",

        "Use Plugin Architecture"

    )

)

print("\nImplementation Reply\n")

pprint(

    engine.send(

        "Code Engineer",

        "Testing Engineer",

        "IMPLEMENTATION_COMPLETE",

        "Feature implemented."

    )

)

print("\nTesting Reply\n")

pprint(

    engine.send(

        "Testing Engineer",

        "Repository Architect",

        "TEST_REPORT",

        "No regression detected."

    )

)

print("\nConversation\n")

pprint(

    engine.conversation()

)

print("\nStatus\n")

pprint(

    engine.status()

)