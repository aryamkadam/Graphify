"""
Graphify

Phase 20

Stage P20.3

Repository Context

The RepositoryContext is the central runtime
state object of the Graphify Operating System.

Every subsystem enriches this object.

Ownership:
    GraphifyKernel

Author:
Graphify Core
"""

from dataclasses import dataclass, field


@dataclass
class RepositoryContext:

    VERSION = "P20.3"

    # --------------------------------------------------
    # Repository
    # --------------------------------------------------

    repository_path: str

    project_name: str | None = None

    entry_file: str | None = None

    # --------------------------------------------------
    # Kernel
    # --------------------------------------------------

    booted: bool = False

    repository_loaded: bool = False

    # --------------------------------------------------
    # Repository Intelligence Layer
    # --------------------------------------------------

    intelligence_context = None

    repository_intelligence = None

    # --------------------------------------------------
    # Repository Brain Layer
    # --------------------------------------------------

    repository_brain = None

    # --------------------------------------------------
    # Repository Memory Layer
    # --------------------------------------------------

    repository_memory = None

    repository_evolution_memory = None

    # --------------------------------------------------
    # Repository State Layer
    # --------------------------------------------------

    repository_state = None

    # --------------------------------------------------
    # Runtime
    # --------------------------------------------------

    engineering_runtime = None

    # --------------------------------------------------
    # Legacy Modules
    # --------------------------------------------------

    repository_history = None

    repository_cognition = None

    repository_strategy = None

    repository_plan = None

    repository_prediction = None

    repository_understanding = None

    repository_insights = None

    repository_executive = None

    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------

    metadata: dict = field(default_factory=dict)

    # --------------------------------------------------

    @property
    def ready(self):

        return (

            self.booted

            and self.repository_loaded

            and self.repository_intelligence is not None

            and self.repository_brain is not None

        )

    # --------------------------------------------------

    def status(self):

        return {

            "booted": self.booted,

            "repository_loaded": self.repository_loaded,

            "project_name": self.project_name,

            "repository_path": self.repository_path,

            "ready": self.ready,

            "repository_intelligence":
                self.repository_intelligence is not None,

            "repository_brain":
                self.repository_brain is not None,

            "repository_memory":
                self.repository_memory is not None,

            "repository_evolution_memory":
                self.repository_evolution_memory is not None,

            "repository_state":
                self.repository_state is not None,

            "version": self.VERSION,

        }