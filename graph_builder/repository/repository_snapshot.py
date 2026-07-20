"""
Graphify

Phase 9

Stage P9.2

Repository Snapshot

Represents the observable state
of a repository at a specific time.

This object contains facts only.

It never performs reasoning.

Author:
Graphify Core
"""

from datetime import datetime
import uuid


class RepositorySnapshot:

    VERSION = "P9.2"

    def __init__(
        self,
        repository_name,
        repository_path,
    ):

        self.snapshot_id = str(uuid.uuid4())

        # --------------------------------------------------
        # Repository Identity
        # --------------------------------------------------

        self.repository_name = repository_name
        self.repository_path = repository_path

        # --------------------------------------------------
        # Observable Repository Structure
        # --------------------------------------------------

        self.directories = []
        self.files = []
        self.modules = []
        self.packages = []

        # --------------------------------------------------
        # Repository Metadata
        # --------------------------------------------------

        self.file_count = 0
        self.directory_count = 0
        self.module_count = 0

        # --------------------------------------------------
        # Scan Information
        # --------------------------------------------------

        self.scan_hash = None
        self.scan_time = datetime.utcnow().isoformat() + "Z"

    # --------------------------------------------------

    def summary(self):

        return {

            "repository": self.repository_name,

            "directories": self.directory_count,

            "files": self.file_count,

            "modules": self.module_count,

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def to_dict(self):

        return {

            "snapshot_id": self.snapshot_id,

            "repository_name": self.repository_name,

            "repository_path": self.repository_path,

            "directories": self.directories,

            "files": self.files,

            "modules": self.modules,

            "packages": self.packages,

            "directory_count": self.directory_count,

            "file_count": self.file_count,

            "module_count": self.module_count,

            "scan_hash": self.scan_hash,

            "scan_time": self.scan_time,

            "version": self.VERSION,

        }