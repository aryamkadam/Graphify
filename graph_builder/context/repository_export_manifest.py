"""
Graphify

Stage 19.5.5

Repository Export Manifest

Builds the master manifest for every
Graphify Repository Transfer Package.

The manifest describes every exported file,
protocol version, and package metadata.

Author:
Graphify Core
"""


class RepositoryExportManifest:

    VERSION = "19.5.5"

    PROTOCOL = "Graphify Repository Transfer Protocol"

    def build(

        self,

        target_ai,

    ):

        return {

            "graphify_version": self.VERSION,

            "protocol": self.PROTOCOL,

            "package_type": "Repository AI Continuation",

            "target_ai": target_ai,

            "portable": True,

            "verified": True,

            "files": [

                "repository_context.graphify",

                "repository_context.gctx",

                "metadata.json",

                "README.md",

                "AI_INSTRUCTIONS.md",

                "checksum.sha256",

                "manifest.json",

            ],

        }