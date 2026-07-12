"""
Graphify

Stage 22.2

Runtime Registration Pipeline

Responsible for discovering, loading and
validating Runtime plugins.

This pipeline is intentionally stateless.

It NEVER owns:

- Runtime Registry
- Runtime Service Manager
- Runtime State

Those responsibilities belong to
RepositoryRuntime.

Author:
Graphify Core
"""

from graph_builder.runtime.runtime_plugin_loader import RuntimePluginLoader
from graph_builder.runtime.runtime_plugin_validator import RuntimePluginValidator


class RuntimeRegistrationPipeline:

    VERSION = "22.2"

    def __init__(self):

        self.loader = RuntimePluginLoader()
        self.validator = RuntimePluginValidator()

    # --------------------------------------------------

    def build(self):

        discovery = self.loader.discover_plugins()

        loaded = self.loader.load_plugins()

        validated_plugins = []

        for plugin in loaded["loaded_plugins"]:

            result = self.validator.validate(plugin)

            if result["status"] == "success":

                validated_plugins.append(plugin)

        return {

            "status": "success",

            "version": self.VERSION,

            "plugins": validated_plugins,

            "metrics": {

                "discovered": discovery["count"],

                "loaded": loaded["count"],

                "validated": len(validated_plugins),

            }

        }