from pprint import pprint

from graph_builder.runtime.runtime_plugin_loader import RuntimePluginLoader

loader = RuntimePluginLoader()

print("\n========================================")
print("Runtime Plugin Discovery")
print("========================================\n")

result = loader.discover_plugins()

pprint(result)