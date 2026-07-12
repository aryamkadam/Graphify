"""
Graphify

Stage 22.2

Repository Runtime

Graphify Runtime Kernel.

Owns:

- Runtime Registry
- Runtime Service Manager
- Runtime Bootloader
- Runtime Lifecycle

This is the single Runtime Orchestrator.

Author:
Graphify Core
"""

from graph_builder.runtime.runtime_registry import RuntimeRegistry
from graph_builder.runtime.runtime_state import RuntimeState
from graph_builder.runtime.runtime_bootloader import RuntimeBootloader
from graph_builder.runtime.runtime_service_manager import RuntimeServiceManager


class RepositoryRuntime:

    VERSION = "22.2"

    def __init__(self):

        self.registry = RuntimeRegistry()

        self.service_manager = RuntimeServiceManager()

        self.bootloader = RuntimeBootloader()

        self.state = RuntimeState.OFFLINE

    # --------------------------------------------------

    def boot(self):

        self.state = RuntimeState.BOOTING

    # --------------------------------------------------

    def online(self):

        self.state = RuntimeState.ONLINE

    # --------------------------------------------------

    def shutdown(self):

        self.service_manager.stop_all()

        self.state = RuntimeState.SHUTDOWN

    # --------------------------------------------------

    def register_plugin(

        self,

        plugin,

    ):

        # Runtime Registry owns metadata

        self.registry.register(

            plugin.service_name,

            plugin,

        )

        # Runtime Service Manager owns lifecycle

        self.service_manager.register(

            plugin,

        )

    # --------------------------------------------------

    def boot_repository(

        self,

        package_directory,

    ):

        self.boot()

        boot_result = self.bootloader.boot(

            package_directory,

        )

        if boot_result["status"] != "success":

            return boot_result

        # ------------------------------------------
        # Register Plugins
        # ------------------------------------------

        for plugin in boot_result["plugins"]:

            self.register_plugin(

                plugin,

            )

        # ------------------------------------------
        # Start Runtime
        # ------------------------------------------

        self.service_manager.start_all()

        self.online()

        # ------------------------------------------
        # Final Runtime Package
        # ------------------------------------------

        return {

            "status": "success",

            "version": self.VERSION,

            "repository": boot_result["repository"],

            "runtime": {

                "services": self.registry.services(),

                "metrics": boot_result["runtime_metrics"],

            },

            "runtime_ready": True,

        }

    # --------------------------------------------------

    def status(self):

        return {

            "version": self.VERSION,

            "state": self.state.value,

            "services": self.registry.services(),

            "runtime_services": self.service_manager.status(),

        }