from pprint import pprint

from graph_builder.runtime.runtime_brain import (
    RuntimeBrain,
)

print("\n========================================")
print("Runtime Brain")
print("========================================\n")

brain = RuntimeBrain()

print("Boot\n")

pprint(

    brain.boot()

)

print("\nShutdown\n")

pprint(

    brain.shutdown()

)