"""
Graphify

Phase P5.2

Unified Runtime Worker

Every engineering worker automatically receives
its own WorkerProfile containing:

- Identity
- Memory
- Goals
- Learning
- Experience
- Decision Engine

This makes every worker a persistent
autonomous engineering agent.

Author:
Graphify Core
"""

from graph_builder.runtime.runtime_inbox import RuntimeInbox
from graph_builder.workers.worker_profile import WorkerProfile


class RuntimeWorker:

    VERSION = "P5.2"

    def __init__(
        self,
        worker_name,
        role="GENERAL",
    ):

        # ------------------------------------------
        # Core Worker Identity
        # ------------------------------------------

        self.worker_name = worker_name
        self.name = worker_name

        # ------------------------------------------
        # Runtime
        # ------------------------------------------

        self.inbox = RuntimeInbox()
        self.state = "IDLE"

        # ------------------------------------------
        # Unified Worker Brain
        # ------------------------------------------

        self.profile = WorkerProfile(
            worker=worker_name,
            role=role,
        )

        # ------------------------------------------
        # Convenience References
        # ------------------------------------------

        self.identity = self.profile.identity
        self.memory = self.profile.memory
        self.goals = self.profile.goals
        self.learning = self.profile.learning
        self.experience = self.profile.experience
        self.decision = self.profile.decision

    # --------------------------------------------------

    def receive(
        self,
        message,
    ):

        self.inbox.push(message)

    # --------------------------------------------------

    def think(self):
        """
        Override inside subclasses.
        """
        return None

    # --------------------------------------------------

    def execute(
        self,
        *args,
        **kwargs,
    ):
        """
        Override inside subclasses.
        """
        return None

    # --------------------------------------------------

    def learn(
        self,
        category,
        content,
    ):
        """
        Store engineering knowledge.
        """

        self.memory.remember(
            category,
            content,
        )

    # --------------------------------------------------

    def complete_task(
        self,
        experience_points=10,
    ):
        """
        Called whenever the worker
        successfully completes work.
        """

        self.identity.complete_task()

        self.experience.gain(
            experience_points,
        )

    # --------------------------------------------------

    def status(self):

        return {

            "worker": self.worker_name,

            "role": self.identity.role,

            "state": self.state,

            "pending_messages": self.inbox.size(),

            "experience": self.identity.experience,

            "knowledge": self.identity.knowledge,

            "confidence": self.identity.confidence,

            "tasks_completed": self.identity.tasks_completed,

            "worker_level":
                self.experience.profile()["level"],

            "maturity":
                self.experience.profile()["maturity"],

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def profile_summary(self):

        return {

            "identity":
                self.identity.profile(),

            "experience":
                self.experience.profile(),

            "goals":
                self.goals.profile(),

            "memory":
                self.memory.status(),

            "version":
                self.VERSION,

        }