"""
Graphify

Stage 20.2.1

Repository Transfer Package

Creates a fully self-contained Repository
Transfer Package.

Author:
Graphify Core
"""

import hashlib
import json
import shutil
import uuid
from datetime import datetime
from pathlib import Path

from graph_builder.context.repository_export_manifest import (
    RepositoryExportManifest,
)


class RepositoryTransferPackage:

    VERSION = "20.2.1"

    PROTOCOL = "Graphify Repository Transfer Protocol"

    def __init__(self):

        self._manifest = RepositoryExportManifest()

    # --------------------------------------------------

    def build(

        self,

        serialized_file,

        compressed_file,

        target_ai,

        output_directory="graphify_export",

    ):

        output = Path(output_directory)

        output.mkdir(

            parents=True,

            exist_ok=True,

        )

        serialized_file = Path(serialized_file)
        compressed_file = Path(compressed_file)

        # ------------------------------------------
        # Copy exported context files
        # ------------------------------------------

        packaged_graphify = output / serialized_file.name
        packaged_gctx = output / compressed_file.name

        shutil.copy2(
            serialized_file,
            packaged_graphify,
        )

        shutil.copy2(
            compressed_file,
            packaged_gctx,
        )

        # ------------------------------------------
        # Manifest
        # ------------------------------------------

        manifest = self._manifest.build(
            target_ai,
        )

        manifest_file = output / "manifest.json"

        with open(
            manifest_file,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                manifest,
                file,
                indent=4,
            )

        # ------------------------------------------
        # Metadata
        # ------------------------------------------

        metadata = self._metadata(
            target_ai,
        )

        metadata_file = output / "metadata.json"

        with open(
            metadata_file,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                metadata,
                file,
                indent=4,
            )

        # ------------------------------------------
        # README
        # ------------------------------------------

        readme_file = output / "README.md"

        readme_file.write_text(
            self._readme(),
            encoding="utf-8",
        )

        # ------------------------------------------
        # AI Instructions
        # ------------------------------------------

        instruction_file = output / "AI_INSTRUCTIONS.md"

        instruction_file.write_text(
            self._instructions(),
            encoding="utf-8",
        )

        # ------------------------------------------
        # Checksum
        # ------------------------------------------

        checksum_file = output / "checksum.sha256"

        checksum_file.write_text(
            self._checksum(
                packaged_graphify,
                packaged_gctx,
            ),
            encoding="utf-8",
        )

        return {

            "status": "success",

            "package_version": self.VERSION,

            "protocol": self.PROTOCOL,

            "package_directory": str(output),

            "repository_context": str(packaged_graphify),

            "compressed_context": str(packaged_gctx),

            "manifest": str(manifest_file),

            "metadata": str(metadata_file),

            "readme": str(readme_file),

            "instructions": str(instruction_file),

            "checksum": str(checksum_file),

        }

    # --------------------------------------------------

    def _metadata(
        self,
        target_ai,
    ):

        return {

            "package_version": self.VERSION,

            "protocol": self.PROTOCOL,

            "repository_context_version": "19.1",

            "portable": True,

            "created_by": "Graphify",

            "target_ai": target_ai,

            "package_id": str(uuid.uuid4()),

            "created_at_utc": datetime.utcnow().isoformat() + "Z",

            "export_type": "Repository AI Continuation Package",

        }

    # --------------------------------------------------

    def _readme(self):

        return (
            "# Graphify Repository Transfer Package\n\n"
            "This package contains a complete portable Repository Brain.\n\n"
            "Contents:\n\n"
            "- repository_context.graphify\n"
            "- repository_context.gctx\n"
            "- manifest.json\n"
            "- metadata.json\n"
            "- README.md\n"
            "- AI_INSTRUCTIONS.md\n"
            "- checksum.sha256\n"
        )

    # --------------------------------------------------

    def _instructions(self):

        return (
            "# AI Continuation Instructions\n\n"
            "Continue the repository exactly from this exported state.\n"
            "Do not restart repository understanding.\n"
        )

    # --------------------------------------------------

    def _checksum(

        self,

        serialized_file,

        compressed_file,

    ):

        sha = hashlib.sha256()

        for file_path in [

            serialized_file,

            compressed_file,

        ]:

            with open(

                file_path,

                "rb",

            ) as file:

                sha.update(

                    file.read(),

                )

        return sha.hexdigest()