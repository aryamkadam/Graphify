"""
Graphify

Phase 11

Stage P11.1

Repository Inventory

Represents the observable contents of a repository.

This object contains facts only.

It performs no reasoning.

It is the foundation of Graphify's perception system.

Author:
Graphify Core
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class RepositoryInventory:

    VERSION = "P11.1"

    # --------------------------------------------------
    # Repository Identity
    # --------------------------------------------------

    repository_name: str
    repository_path: str

    # --------------------------------------------------
    # Directory Structure
    # --------------------------------------------------

    directories: list = field(default_factory=list)

    # --------------------------------------------------
    # File Categories
    # --------------------------------------------------

    python_files: list = field(default_factory=list)

    markdown_files: list = field(default_factory=list)

    json_files: list = field(default_factory=list)

    yaml_files: list = field(default_factory=list)

    configuration_files: list = field(default_factory=list)

    test_files: list = field(default_factory=list)

    asset_files: list = field(default_factory=list)

    other_files: list = field(default_factory=list)

    # --------------------------------------------------
    # Metrics
    # --------------------------------------------------

    directory_count: int = 0

    file_count: int = 0

    python_file_count: int = 0

    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------

    created_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat() + "Z"
    )

    # --------------------------------------------------

    def summary(self):

        return {

            "repository": self.repository_name,

            "directories": self.directory_count,

            "files": self.file_count,

            "python_files": self.python_file_count,

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def to_dict(self):

        return {

            "repository": {

                "name": self.repository_name,

                "path": self.repository_path,

            },

            "directories": self.directories,

            "files": {

                "python": self.python_files,

                "markdown": self.markdown_files,

                "json": self.json_files,

                "yaml": self.yaml_files,

                "configuration": self.configuration_files,

                "tests": self.test_files,

                "assets": self.asset_files,

                "other": self.other_files,

            },

            "metrics": {

                "directory_count": self.directory_count,

                "file_count": self.file_count,

                "python_file_count": self.python_file_count,

            },

            "metadata": {

                "created_at": self.created_at,

                "version": self.VERSION,

            },

        }