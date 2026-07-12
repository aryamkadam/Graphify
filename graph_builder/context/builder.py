"""
Graphify Context Builder

High-level orchestration entry point.

Responsible for generating the complete
Graphify Context Schema.
"""

from .schema import (
    generate_context_schema
)


def build_context():

    """
    Build the complete
    Graphify Context.
    """

    return generate_context_schema()