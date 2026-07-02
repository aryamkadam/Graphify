from graph_builder.runtime.runtime_registry import RuntimeRegistry
from graph_builder.runtime.runtime_state import RuntimeState

from graph_builder.runtime.runtime_bootloader import RuntimeBootloader
class RepositoryRuntime:

    VERSION = "20.4.1"

    def __init__(self):

        self.bootloader = RuntimeBootloader()
        self.state = RuntimeState.OFFLINE

        self.registry = RuntimeRegistry()

    # ---------------------------------

    def boot(self):

        self.state = RuntimeState.BOOTING

    # ---------------------------------

    def online(self):

        self.state = RuntimeState.ONLINE

    # ---------------------------------

    def shutdown(self):

        self.state = RuntimeState.SHUTDOWN

    # ---------------------------------

    def status(self):

        return {
            "version": self.VERSION,
            "state": self.state.value,
            "services": self.registry.services(),
        }
    def boot_repository(

    self,

    package_directory,

):

     self.boot()

     result = self.bootloader.boot(
  
        package_directory,

    )

     if result["status"] == "success":

        self.online()

     return result