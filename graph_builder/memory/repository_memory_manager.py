"""
Stage 16.2

Repository Memory Manager

Stores and retrieves Repository Snapshots.

This is the long-term memory layer of Graphify.

Future stages will use it for:

- Repository evolution
- Snapshot comparison
- Architectural drift detection
- AI memory
"""

from copy import deepcopy


class RepositoryMemoryManager:

    def __init__(self):

        self.snapshots = []

    # ------------------------------------------

    def save_snapshot(self, snapshot):

        self.snapshots.append(
            deepcopy(snapshot)
        )

    # ------------------------------------------

    def latest_snapshot(self):

        if not self.snapshots:

            return None

        return deepcopy(
            self.snapshots[-1]
        )

    # ------------------------------------------

    def snapshot_history(self):

        return deepcopy(
            self.snapshots
        )

    # ------------------------------------------

    def snapshot_count(self):

        return len(
            self.snapshots
        )

    # ------------------------------------------

    def clear(self):

        self.snapshots.clear()