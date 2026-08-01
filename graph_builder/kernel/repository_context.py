"""
Graphify

Phase 18

Repository Context

The RepositoryContext is the central state object
for the Graphify Operating System.

Every subsystem reads from and enriches this object.

Ownership:
    GraphifyKernel

Consumers:
    Repository Brain
    Repository History
    Repository Memory
    Repository Cognition
    Executive Engine
    Planning Engine
    Engineering Kernel

Author:
Graphify Core
"""

from dataclasses import dataclass, field


@dataclass
class RepositoryContext:

    VERSION = "P18.2"

    # -----------------------------------------
    # Core Repository
    # -----------------------------------------

    repository_path: str

    project_name: str | None = None

    entry_file: str | None = None

    # -----------------------------------------
    # Kernel State
    # -----------------------------------------

    booted: bool = False

    repository_loaded: bool = False

    # -----------------------------------------
    # Intelligence
    # -----------------------------------------

    repository_brain: dict | None = None

    repository_history: dict | None = None

    repository_memory: dict | None = None

    repository_cognition: dict | None = None

    repository_strategy: dict | None = None

    repository_plan: dict | None = None

    repository_prediction: dict | None = None

    repository_understanding: dict | None = None

    repository_insights: dict | None = None

    repository_executive: dict | None = None

    # -----------------------------------------
    # Runtime
    # -----------------------------------------

    engineering_runtime: dict | None = None

    # -----------------------------------------
    # Metadata
    # -----------------------------------------

    metadata: dict = field(default_factory=dict)

    # -----------------------------------------

    def is_ready(self):

        return (

            self.booted

            and self.repository_loaded

        )

    # -----------------------------------------

    def status(self):

        return {

            "booted": self.booted,

            "repository_loaded": self.repository_loaded,

            "project_name": self.project_name,

            "repository_path": self.repository_path,

            "ready": self.is_ready(),

            "version": self.VERSION,

        }