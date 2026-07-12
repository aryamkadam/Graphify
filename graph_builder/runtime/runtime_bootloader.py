"""
Graphify

Stage 22.2

Runtime Bootloader

Responsible for reconstructing a Repository
and preparing a Runtime.

The Bootloader NEVER owns the Runtime.

It prepares everything and returns it to
RepositoryRuntime, which becomes the Runtime
Orchestrator.

Boot Sequence

Verify
    ↓
Import
    ↓
Reconstruct Repository
    ↓
Discover Plugins
    ↓
Return Boot Package

Author:
Graphify Core
"""

from graph_builder.context.repository_package_verifier import (
    RepositoryPackageVerifier,
)

from graph_builder.context.repository_ai_import_engine import (
    RepositoryAIImportEngine,
)

from graph_builder.context.repository_reconstruction_engine import (
    RepositoryReconstructionEngine,
)

from graph_builder.runtime.runtime_registration_pipeline import (
    RuntimeRegistrationPipeline,
)


class RuntimeBootloader:

    VERSION = "22.2"

    def __init__(self):

        self._verifier = RepositoryPackageVerifier()

        self._importer = RepositoryAIImportEngine()

        self._reconstructor = RepositoryReconstructionEngine()

        self._pipeline = RuntimeRegistrationPipeline()

    # --------------------------------------------------

    def boot(

        self,

        package_directory,

    ):

        # ------------------------------------------
        # Verify Transfer Package
        # ------------------------------------------

        verification = self._verifier.verify(

            package_directory,

        )

        if not verification["verified"]:

            return {

                "status": "failed",

                "reason": "Package verification failed",

                "verification": verification,

                "version": self.VERSION,

            }

        # ------------------------------------------
        # Import Repository Context
        # ------------------------------------------

        imported = self._importer.import_package(

            package_directory,

        )

        # ------------------------------------------
        # Reconstruct Repository Brain
        # ------------------------------------------

        repository = self._reconstructor.reconstruct(

            imported["repository_context"],

        )

        # ------------------------------------------
        # Prepare Runtime Plugins
        # ------------------------------------------

        runtime = self._pipeline.build()

        # ------------------------------------------
        # Boot Package
        # ------------------------------------------

        return {

            "status": "success",

            "version": self.VERSION,

            "verification": verification,

            "repository": repository,

            "plugins": runtime["plugins"],

            "runtime_metrics": runtime["metrics"],

            "runtime_ready": True,

        }