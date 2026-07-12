"""
Graphify

Stage 21.9

Runtime Plugin Validator

Validates Runtime Plugins before they are
accepted into Graphify Runtime.

Author:
Graphify Core
"""

from graph_builder.runtime.runtime_service import RuntimeService


class RuntimePluginValidator:

    VERSION = "21.9.0"

    # ------------------------------------------

    def validate(self, plugin):

        if plugin is None:

            return {
                "status": "failed",
                "reason": "Plugin is None",
            }

        if not isinstance(plugin, RuntimeService):

            return {
                "status": "failed",
                "reason": "Plugin is not RuntimeService",
            }

        if not plugin.service_name:

            return {
                "status": "failed",
                "reason": "Missing service name",
            }

        return {
            "status": "success",
            "service": plugin.service_name,
            "validated": True,
        }