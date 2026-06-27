"""
Graphify Context Schema

Canonical internal representation of all
Graphify knowledge.

Every protocol translator consumes this model.

No protocol is allowed to bypass it.
"""

from graph_builder.universal_context_schema import (
    generate_universal_context_schema
)


def generate_context_schema():
    """
    Return the canonical Graphify Context Schema.
    """

    return generate_universal_context_schema()