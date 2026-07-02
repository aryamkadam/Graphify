"""
Graphify

Stage 20.4.2

Repository AI Import Engine

Loads a complete Graphify Repository
Transfer Package.

Author:
Graphify Core
"""

from pathlib import Path

from graph_builder.context.universal_context_serializer import (
    UniversalContextSerializer,
)

from graph_builder.context.universal_context_compressor import (
    UniversalContextCompressor,
)


class RepositoryAIImportEngine:

    VERSION = "20.4.2"

    def __init__(self):

        self._serializer = UniversalContextSerializer()

        self._compressor = UniversalContextCompressor()

    # --------------------------------------------------

    def import_package(

        self,

        package_directory,

    ):

        package_directory = Path(package_directory)

        graphify_file = (
            package_directory /
            "repository_context.graphify"
        )

        compressed_file = (
            package_directory /
            "repository_context.gctx"
        )

        context = self._serializer.load(

            graphify_file,

        )

        compressed_context = None

        if compressed_file.exists():

            compressed_context = self._compressor.decompress(

                compressed_file,

            )

        return {

            "status": "success",

            "version": self.VERSION,

            "repository_context": context,

            "compressed_context": compressed_context,

            "repository_ready": True,

            "continuation_ready": True,

        }