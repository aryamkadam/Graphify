"""
Graphify

Stage 21.7

Runtime Plugin Loader

Discovers Graphify Runtime plugins.

Author:
Graphify Core
"""

import pkgutil
import importlib


class RuntimePluginLoader:

    VERSION = "21.7"

    def __init__(self):

        self._plugins = []

    # ------------------------------------------

    def register_plugin(self, plugin):

        self._plugins.append(plugin)

        return {
            "status": "success",
            "registered": plugin.service_name,
        }

    # ------------------------------------------

    def discover_plugins(

        self,

        package_name="graph_builder.plugins",

    ):

        package = importlib.import_module(package_name)

        discovered = []

        for module in pkgutil.iter_modules(package.__path__):

            discovered.append(module.name)

        return {
            "status": "success",
            "package": package_name,
            "plugins": discovered,
            "count": len(discovered),
        }

    # ------------------------------------------

    def plugins(self):

        return [
            plugin.service_name
            for plugin in self._plugins
        ]

    # ------------------------------------------

    def count(self):

        return len(self._plugins)

    # ------------------------------------------

    def status(self):

        return {
            "version": self.VERSION,
            "registered_plugins": self.count(),
            "plugins": self.plugins(),
        }
    
    def load_plugins(self, package_name="graph_builder.plugins"):

          package = importlib.import_module(package_name)

          loaded = []

          for module in pkgutil.iter_modules(package.__path__):

            module_name = f"{package_name}.{module.name}"

            imported = importlib.import_module(module_name)

            if hasattr(imported, "create_plugin"):

                plugin = imported.create_plugin()

                loaded.append(plugin)

          return {
            "status": "success",
            "loaded_plugins": loaded,
            "count": len(loaded),
           }