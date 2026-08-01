"""
Graphify

Phase 19

Repository Evolution Memory Test

Author:
Graphify Core
"""

from graph_builder.memory.repository_evolution_memory import (
    RepositoryEvolutionMemory,
)


def print_header(title):

    print("=" * 60)
    print(title)
    print("=" * 60)


def main():

    evolution = RepositoryEvolutionMemory()

    # -------------------------------------------------
    print_header("TEST 1 : First Snapshot")

    current = {
        "repository": "Graphify",
        "identity": "Repository Intelligence Platform",
        "capability": "Knowledge",
        "behavior": "Repository Learning",
    }

    result = evolution.compare(None, current)

    print(result)

    assert result["first_snapshot"] is True
    assert result["identity_changed"] is False
    assert result["capability_changed"] is False
    assert result["behavior_changed"] is False

    # -------------------------------------------------
    print_header("TEST 2 : No Changes")

    previous = current.copy()

    result = evolution.compare(previous, current)

    print(result)

    assert result["first_snapshot"] is False
    assert result["identity_changed"] is False
    assert result["capability_changed"] is False
    assert result["behavior_changed"] is False

    # -------------------------------------------------
    print_header("TEST 3 : Behavior Changed")

    changed = current.copy()

    changed["behavior"] = "Engineering Planning"

    result = evolution.compare(current, changed)

    print(result)

    assert result["behavior_changed"] is True
    assert result["identity_changed"] is False
    assert result["capability_changed"] is False

    # -------------------------------------------------
    print_header("TEST 4 : Capability Changed")

    changed = current.copy()

    changed["capability"] = "Persistent Engineering Memory"

    result = evolution.compare(current, changed)

    print(result)

    assert result["capability_changed"] is True
    assert result["identity_changed"] is False

    # -------------------------------------------------
    print_header("TEST 5 : Identity Changed")

    changed = current.copy()

    changed["identity"] = "Autonomous Engineering Brain"

    result = evolution.compare(current, changed)

    print(result)

    assert result["identity_changed"] is True

    # -------------------------------------------------

    print()
    print("ALL RepositoryEvolutionMemory TESTS PASSED")


if __name__ == "__main__":

    main()