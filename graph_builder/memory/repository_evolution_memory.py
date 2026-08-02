"""
Graphify

Phase 20

Stage P20.5

Repository Evolution Memory

Maintains the runtime evolution history of the
currently loaded repository.

Unlike RepositoryEvolutionMemoryEngine,
this class is the active runtime memory.

Responsibilities

• Record repository snapshots
• Detect evolution
• Maintain timeline
• Provide evolution history

Author:
Graphify Core
"""

from copy import deepcopy
from datetime import datetime


class RepositoryEvolutionMemory:

    VERSION = "P20.5"

    # --------------------------------------------------

    def __init__(self):

        self.timeline = []

        self.last_snapshot = None

    # --------------------------------------------------

    def record(

        self,

        intelligence_context,

    ):

        snapshot = {

            "timestamp": datetime.utcnow(),

            "repository":

                intelligence_context.inventory.repository_name,

            "identity":

                intelligence_context.identity,

            "capability":

                intelligence_context.capability,

            "behavior":

                intelligence_context.behavior,

        }

        if self.last_snapshot is None:

            snapshot["event"] = "INITIAL_BOOT"

        else:

            snapshot["event"] = self._detect_change(

                self.last_snapshot,

                snapshot,

            )

        self.timeline.append(snapshot)

        self.last_snapshot = deepcopy(snapshot)

        return snapshot

    # --------------------------------------------------

    def _detect_change(

        self,

        previous,

        current,

    ):

        if previous["identity"] != current["identity"]:

            return "IDENTITY_CHANGED"

        if previous["capability"] != current["capability"]:

            return "CAPABILITY_CHANGED"

        if previous["behavior"] != current["behavior"]:

            return "BEHAVIOR_CHANGED"

        return "NO_CHANGE"

    # --------------------------------------------------

    def history(self):

        return list(self.timeline)

    # --------------------------------------------------

    def latest(self):

        return self.last_snapshot

    # --------------------------------------------------

    def clear(self):

        self.timeline.clear()

        self.last_snapshot = None

    # --------------------------------------------------

    def status(self):

        return {

            "entries": len(self.timeline),

            "loaded": self.last_snapshot is not None,

            "version": self.VERSION,

        }