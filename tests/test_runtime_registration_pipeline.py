from pprint import pprint

from graph_builder.runtime.runtime_registration_pipeline import (
    RuntimeRegistrationPipeline,
)

pipeline = RuntimeRegistrationPipeline()

print("\n========================================")
print("Runtime Registration Pipeline")
print("========================================\n")

result = pipeline.build()

pprint(result)