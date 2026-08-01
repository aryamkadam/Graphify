"""
Graphify

Phase 18

Commit 6

Repository Entry Discovery

Discovers the primary entry point of a repository.

Responsibilities

• Detect executable entry files
• Rank candidate entry points
• Return best entry point

Author:
Graphify Core
"""

from pathlib import Path


class RepositoryEntryDiscovery:

    VERSION = "P18.0"

    DEFAULT_PRIORITY = [

        "main.py",

        "app.py",

        "manage.py",

        "server.py",

        "cli.py",

        "__main__.py",

    ]

    # --------------------------------------------------

    def __init__(

        self,

        repository_path,

    ):

        self.repository_path = Path(repository_path)

    # --------------------------------------------------

    def discover(self):

        candidates = []

        for path in self.repository_path.rglob("*.py"):

            candidates.append(path)

        #
        # Priority search
        #

        for preferred in self.DEFAULT_PRIORITY:

            for file in candidates:

                if file.name == preferred:

                    return {

                        "entry_file":

                            str(

                                file.relative_to(

                                    self.repository_path

                                )

                            ),

                        "entry_type":

                            "priority",

                        "confidence":

                            1.0,

                    }

        #
        # Fallback
        #

        if candidates:

            candidates.sort()

            return {

                "entry_file":

                    str(

                        candidates[0].relative_to(

                            self.repository_path

                        )

                    ),

                "entry_type":

                    "fallback",

                "confidence":

                    0.5,

            }

        raise FileNotFoundError(

            "No Python entry file found."

        )