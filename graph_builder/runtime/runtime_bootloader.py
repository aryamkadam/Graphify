"""
Graphify

Stage 20.4.2

Runtime Bootloader

Responsible for bringing a repository
package into a running Runtime.

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


class RuntimeBootloader:

    VERSION = "20.4.2"

    def __init__(self):

        self._verifier = RepositoryPackageVerifier()

        self._importer = RepositoryAIImportEngine()

        self._reconstructor = RepositoryReconstructionEngine()

    # --------------------------------------------

    def boot(

        self,

        package_directory,

    ):

        verification = self._verifier.verify(

            package_directory,

        )

        if not verification["verified"]:

            return {

                "status": "failed",

                "reason": "Package verification failed",

                "verification": verification,

            }

        imported = self._importer.import_package(

            package_directory,

        )

        reconstructed = self._reconstructor.reconstruct(

            imported["repository_context"],

        )

        return {

            "status": "success",

            "runtime_ready": True,

            "verification": verification,

            "repository": reconstructed,

            "version": self.VERSION,

        }