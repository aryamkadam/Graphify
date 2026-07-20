"""
Graphify

Phase 9

Stage P9.1

Repository Knowledge Model

Canonical engineering representation
of a repository.

This object is the single source of truth
for repository intelligence.

Author:
Graphify Core
"""

from datetime import datetime


class RepositoryKnowledge:

    VERSION = "P9.1"

    def __init__(
        self,
        repository_name,
        repository_path,
        language="Unknown",
        framework="Unknown",
        build_system="Unknown",
    ):

        # --------------------------------------------------
        # Identity
        # --------------------------------------------------

        self.repository_name = repository_name
        self.repository_path = repository_path
        self.language = language
        self.framework = framework
        self.build_system = build_system

        # --------------------------------------------------
        # Repository Structure
        # --------------------------------------------------

        self.directories = []
        self.modules = []
        self.files = []
        self.entry_points = []

        # --------------------------------------------------
        # Architecture
        # --------------------------------------------------

        self.layers = []
        self.services = []
        self.patterns = []

        # --------------------------------------------------
        # Components
        # --------------------------------------------------

        self.classes = []
        self.functions = []
        self.interfaces = []
        self.enums = []

        # --------------------------------------------------
        # Relationships
        # --------------------------------------------------

        self.dependencies = []
        self.imports = []
        self.inheritance = []
        self.composition = []

        # --------------------------------------------------
        # Engineering Metrics
        # --------------------------------------------------

        self.metrics = {
            "complexity": None,
            "technical_debt": None,
            "maintainability": None,
            "coverage": None,
        }

        # --------------------------------------------------
        # Engineering Intelligence
        # --------------------------------------------------

        self.known_risks = []
        self.opportunities = []
        self.strengths = []

        # --------------------------------------------------
        # Metadata
        # --------------------------------------------------

        timestamp = datetime.utcnow().isoformat() + "Z"

        self.created_at = timestamp
        self.updated_at = timestamp

    # --------------------------------------------------

    def summary(self):

        return {

            "repository": self.repository_name,

            "language": self.language,

            "framework": self.framework,

            "modules": len(self.modules),

            "files": len(self.files),

            "classes": len(self.classes),

            "functions": len(self.functions),

            "known_risks": len(self.known_risks),

            "opportunities": len(self.opportunities),

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def to_dict(self):

        return {

            "identity": {

                "repository_name": self.repository_name,

                "repository_path": self.repository_path,

                "language": self.language,

                "framework": self.framework,

                "build_system": self.build_system,

            },

            "structure": {

                "directories": self.directories,

                "modules": self.modules,

                "files": self.files,

                "entry_points": self.entry_points,

            },

            "architecture": {

                "layers": self.layers,

                "services": self.services,

                "patterns": self.patterns,

            },

            "components": {

                "classes": self.classes,

                "functions": self.functions,

                "interfaces": self.interfaces,

                "enums": self.enums,

            },

            "relationships": {

                "dependencies": self.dependencies,

                "imports": self.imports,

                "inheritance": self.inheritance,

                "composition": self.composition,

            },

            "metrics": self.metrics,

            "engineering_intelligence": {

                "known_risks": self.known_risks,

                "opportunities": self.opportunities,

                "strengths": self.strengths,

            },

            "metadata": {

                "created_at": self.created_at,

                "updated_at": self.updated_at,

                "version": self.VERSION,

            },

        }