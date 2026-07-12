from pprint import pprint

from graph_builder.runtime.runtime_plugin_loader import RuntimePluginLoader

loader = RuntimePluginLoader()

print("\n========================================")
print("Runtime Plugin Loader")
print("========================================\n")

result = loader.load_plugins()

print("Loaded Plugins\n")

pprint(
    [
        plugin.service_name
        for plugin in result["loaded_plugins"]
    ]
)

print()

pprint(result)