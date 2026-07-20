"""
Graphify

Phase 12

Stage P12.1

Repository Responsibility Engine

Discovers engineering responsibilities
for repository components.

Author:
Graphify Core
"""

from graph_builder.intelligence.repository_responsibility import (
    RepositoryResponsibility,
)


class RepositoryResponsibilityEngine:

    VERSION = "P12.1"

    def build(

        self,

        architecture,

    ):

        responsibilities = []

        for component in architecture:

            category = component["layer"]

            responsibility = self._responsibility(category)

            owner = category

            role = self._engineering_role(category)

            importance = self._importance(category)

            responsibilities.append(

                RepositoryResponsibility(

                    component=component["name"],

                    responsibility=responsibility,

                    category=category,

                    owner=owner,

                    engineering_role=role,

                    business_importance=importance,

                    confidence=0.97,

                )

            )

        return responsibilities

    # -------------------------------------------------

    def _responsibility(

        self,

        category,

    ):

        mapping = {

            "Knowledge": "Stores repository knowledge.",

            "Learning": "Learns engineering patterns.",

            "Reasoning": "Performs engineering reasoning.",

            "Planning": "Creates engineering plans.",

            "Runtime": "Executes repository runtime.",

            "Workers": "Performs engineering work.",

            "Knowledge Graph": "Maintains repository graph.",

            "Executive": "Coordinates engineering decisions.",

            "Memory": "Stores repository memory.",

            "Infrastructure": "Provides engineering utilities.",

        }

        return mapping.get(

            category,

            "Supports repository engineering.",

        )

    # -------------------------------------------------

    def _engineering_role(

        self,

        category,

    ):

        if category in [

            "Executive",

            "Reasoning",

            "Planning",

        ]:

            return "CORE"

        if category in [

            "Knowledge",

            "Learning",

            "Memory",

        ]:

            return "INTELLIGENCE"

        return "SUPPORT"

    # -------------------------------------------------

    def _importance(

        self,

        category,

    ):

        if category in [

            "Executive",

            "Knowledge",

            "Reasoning",

        ]:

            return "HIGH"

        if category in [

            "Learning",

            "Planning",

            "Runtime",

        ]:

            return "MEDIUM"

        return "LOW"