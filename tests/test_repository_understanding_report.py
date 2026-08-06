"""
Graphify

Phase 22

Repository Understanding Report Test

Validates the Repository Understanding Report.

Author:
Graphify Core
"""

from graph_builder.understanding import (
    RepositoryUnderstandingReport,
)


def main():

    print("=" * 60)
    print("REPOSITORY UNDERSTANDING REPORT TEST")
    print("=" * 60)

    #
    # Build Report
    #

    report = RepositoryUnderstandingReport(

        repository_name="Graphify",

        repository_path=".",

    )

    #
    # Verify Repository
    #

    assert report.repository_name == "Graphify"

    assert report.repository_path == "."

    #
    # Verify Default Understanding
    #

    assert report.architecture_style == "UNKNOWN"

    assert report.module_organization == "UNKNOWN"

    assert report.dependency_summary == "UNKNOWN"

    assert report.structural_complexity == "UNKNOWN"

    #
    # Verify Lists
    #

    assert report.architectural_strengths == []

    assert report.architectural_weaknesses == []

    #
    # Verify Confidence
    #

    assert report.confidence == 0.0

    #
    # Verify Status
    #

    status = report.status()

    print(status)

    assert status["repository"] == "Graphify"

    assert status["architecture_style"] == "UNKNOWN"

    assert status["confidence"] == 0.0

    assert status["version"] == "P22.1"

    print()

    print("ALL TESTS PASSED")


if __name__ == "__main__":

    main()