from pprint import pprint

from graph_builder.runtime.runtime_plugin_validator import RuntimePluginValidator
from graph_builder.runtime.runtime_service import RuntimeService

validator = RuntimePluginValidator()

plugin = RuntimeService("Memory Plugin")

print("\n========================================")
print("Runtime Plugin Validator")
print("========================================\n")

result = validator.validate(plugin)

pprint(result)