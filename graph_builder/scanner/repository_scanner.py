"""
Graphify

Phase 11

Stage P11.2

Repository Scanner

Scans a repository and builds a RepositoryInventory.

This is Graphify's first perception engine.

Author:
Graphify Core
"""

from pathlib import Path

from graph_builder.scanner.repository_inventory import (
    RepositoryInventory,
)
IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".idea",
    ".vscode",
}

IGNORED_FILES = {
    ".coverage",
}

class RepositoryScanner:

    VERSION = "P11.2"

    def __init__(

        self,

        repository_name,

        repository_path,

    ):

        self.repository_name = repository_name

        self.repository_path = Path(repository_path)

    # --------------------------------------------------

    def scan(self):

        inventory = RepositoryInventory(

            repository_name=self.repository_name,

            repository_path=str(self.repository_path),

        )

        for path in self.repository_path.rglob("*"):

            if any(part in IGNORED_DIRECTORIES for part in path.parts):
               continue

            if path.name in IGNORED_FILES:
                continue
            relative = str(

                path.relative_to(self.repository_path)

            )

            # ---------------- Directories ----------------

            if path.is_dir():

                inventory.directories.append(relative)

                continue

            # ---------------- Files ----------------

            suffix = path.suffix.lower()
            if relative.startswith("tests") and suffix == ".py":

                inventory.test_files.append(relative)

            elif suffix == ".py":

                inventory.python_files.append(relative)

            elif suffix == ".md":

                inventory.markdown_files.append(relative)
            elif suffix == ".json":

                inventory.json_files.append(relative)

            elif suffix in [".yaml", ".yml"]:

                inventory.yaml_files.append(relative)

            elif suffix in [

                ".ini",

                ".cfg",

                ".toml",

            ]:

                inventory.configuration_files.append(relative)

            elif relative.startswith("tests"):

                inventory.test_files.append(relative)

            elif suffix in [

                ".png",

                ".jpg",

                ".jpeg",

                ".gif",

                ".svg",

            ]:

                inventory.asset_files.append(relative)

            else:

                inventory.other_files.append(relative)

        # ---------------- Metrics ----------------

        inventory.directory_count = len(

            inventory.directories

        )

        inventory.python_file_count = len(

            inventory.python_files

        )

        inventory.file_count = (

            len(inventory.python_files)

            + len(inventory.markdown_files)

            + len(inventory.json_files)

            + len(inventory.yaml_files)

            + len(inventory.configuration_files)

            + len(inventory.test_files)

            + len(inventory.asset_files)

            + len(inventory.other_files)

        )

        return inventory