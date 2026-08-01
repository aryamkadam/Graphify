"""
Graphify

Phase 18

Stage P18.4

Graphify Kernel

The central operating system of Graphify.

Responsibilities

• Boot Graphify
• Manage repository lifecycle
• Own Repository Context
• Delegate engineering work
• Expose a single public API

Author:
Graphify Core
"""

from pathlib import Path
from graph_builder.runtime.repository_bootstrap import (
    RepositoryBootstrap,
)

from graph_builder.kernel.engineering_kernel import (
    EngineeringKernel,
)

from graph_builder.kernel.repository_context import (
    RepositoryContext,
)

from graph_builder.kernel.graphify_boot_pipeline import (
    GraphifyBootPipeline,
)


class GraphifyKernel:

    VERSION = "P18.4"

    # --------------------------------------------------

    def __init__(

        self,

        repository_path,

        project_name=None,

    ):

        self.repository_path = Path(repository_path)

        self.context = RepositoryContext(

            repository_path=str(self.repository_path),

            project_name=project_name,

        )

        self.engineering_kernel = EngineeringKernel()
        self.bootstrap = RepositoryBootstrap(

            self.context,

            self.engineering_kernel,

)

        self.boot_pipeline = GraphifyBootPipeline()

    # --------------------------------------------------
    def boot(self):

        if self.context.booted:

            return self.context

        self.bootstrap.boot()

        self.context.booted = True

        return self.context
        # --------------------------------------------------
    # --------------------------------------------------

    def shutdown(self):

        """
        Shutdown the active repository runtime.

        RepositoryBootstrap clears repository-level
        intelligence, brain, and runtime state.
        """

        if not self.context.booted:

            return self.context

        self.bootstrap.shutdown()

        self.context.booted = False

        return self.context
    # --------------------------------------------------

    def reboot(self):

        """
        Cold reboot Graphify.

        Destroy all runtime state and rebuild the
        Repository Context.
        """

        self.shutdown()

        return self.boot()

    # --------------------------------------------------

    def execute_engineering_task(

        self,

        task,

    ):

        if not self.context.is_ready():

            raise RuntimeError(

                "Graphify Kernel has not been booted."

            )

        return self.engineering_kernel.execute(

            task,

        )

    # --------------------------------------------------

    def status(self):

        return {

            "kernel": (

                "ONLINE"

                if self.context.booted

                else "OFFLINE"

            ),

            **self.context.status(),

            "engineering_kernel":

                self.engineering_kernel.status(),

            "version":

                self.VERSION,

        }