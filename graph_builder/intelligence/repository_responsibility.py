"""
Graphify

Phase 12

Stage P12.1

Repository Responsibility

Represents semantic responsibility
of one repository component.

Author:
Graphify Core
"""


class RepositoryResponsibility:

    VERSION = "P12.1"

    def __init__(

        self,

        component,

        responsibility,

        category,

        owner,

        engineering_role,

        business_importance,

        confidence,

    ):

        self.component = component

        self.responsibility = responsibility

        self.category = category

        self.owner = owner

        self.engineering_role = engineering_role

        self.business_importance = business_importance

        self.confidence = confidence

    def to_dict(self):

        return {

            "component": self.component,

            "responsibility": self.responsibility,

            "category": self.category,

            "owner": self.owner,

            "engineering_role": self.engineering_role,

            "business_importance": self.business_importance,

            "confidence": self.confidence,

            "version": self.VERSION,

        }