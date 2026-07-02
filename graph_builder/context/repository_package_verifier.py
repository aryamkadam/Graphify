"""
Graphify

Stage 20.2

Repository Package Verifier

Verifies that a Graphify Repository Transfer
Package is complete and compatible before
Repository AI Continuation begins.

Author:
Graphify Core
"""

import hashlib
from pathlib import Path


class RepositoryPackageVerifier:

    VERSION = "20.2"

    REQUIRED_FILES = [

        "metadata.json",

        "manifest.json",

        "README.md",

        "AI_INSTRUCTIONS.md",

        "checksum.sha256",

    ]

    # --------------------------------------------------

    def verify(

        self,

        package_directory,

    ):

        package = Path(package_directory)

        missing = []

        for file_name in self.REQUIRED_FILES:

            if not (package / file_name).exists():

                missing.append(file_name)

        return {

            "status": "success" if not missing else "failed",

            "version": self.VERSION,

            "package_exists": package.exists(),

            "verified": len(missing) == 0,

            "missing_files": missing,

        }

    # --------------------------------------------------

    def verify_checksum(

        self,

        file_path,

        expected_checksum,

    ):

        sha = hashlib.sha256()

        with open(

            file_path,

            "rb",

        ) as file:

            sha.update(

                file.read(),

            )

        actual = sha.hexdigest()

        return {

            "verified": actual == expected_checksum,

            "expected": expected_checksum,

            "actual": actual,

        }