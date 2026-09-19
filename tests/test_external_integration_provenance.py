from __future__ import annotations

from graph_builder.provenance.engineering_decision_record import (
    EngineeringDecisionRecord,
)
from graph_builder.provenance.engineering_review import (
    EngineeringReview,
)


class FakeEvidenceCollector:
    def __init__(self, external_integration):
        self.external_integration = external_integration

    def collect(
        self,
        repository_path,
        decision,
        repository_plan=None,
        external_evidence=None,
    ):
        return {
            "repository": str(repository_path),
            "evidence": {
                "direct": [
                    {
                        "type": "repository_document",
                        "path": "docs/ARCHITECTURE.md",
                        "text": "Repository architecture",
                        "classification": "DIRECT",
                        "evidence_strength": "EXPLICIT",
                    }
                ],
                "related": [],
                "context": [],
                "external": [],
            },
            "counts": {
                "direct": 1,
                "related": 0,
                "context": 0,
                "external": 0,
                "total": 1,
            },
            "external_counts": {
                "total": 0,
            },
            "external_integration": self.external_integration,
            "provenance": {
                "read_only": True,
                "external_integration": self.external_integration,
                "external_providers": self.external_integration.get(
                    "providers",
                    [],
                ),
                "external_statuses": [
                    self.external_integration.get(
                        "status",
                        "UNKNOWN",
                    )
                ],
                "external_evidence": False,
            },
            "version": "38.5",
        }


def _build_record(tmp_path, external_integration):
    collector = FakeEvidenceCollector(
        external_integration
    )

    record_builder = EngineeringDecisionRecord(
        evidence_collector=collector
    )

    decision = {
        "decision": "Prioritize Architectural Improvement",
        "selected_goal": "Strengthen Repository Architecture",
        "strategy": "Repository Architecture",
        "decision_reason": "Architecture evidence supports the change.",
        "confidence": "HIGH",
    }

    plan = {
        "objective": "Strengthen Repository Architecture",
        "expected_result": (
            "Improved repository architecture"
        ),
    }

    return record_builder.build(
        repository_path=tmp_path,
        decision=decision,
        repository_plan=plan,
        external_evidence={
            "source": "github",
            "status": external_integration["status"],
            "connected": external_integration["connected"],
            "evidence_count": external_integration[
                "evidence_count"
            ],
            "evidence": [],
        }
        if external_integration["requested"]
        else None,
    )


def test_external_integration_not_requested(tmp_path):
    integration = {
        "requested": False,
        "connected": False,
        "status": "NOT_REQUESTED",
        "providers": [],
        "evidence_count": 0,
    }

    record = _build_record(
        tmp_path,
        integration,
    )

    assert record["provenance"]["external_integration"] == integration
    assert record["knowledge"]["external_integration"] == integration

    review = EngineeringReview().build(record)

    assert review["external_integration"] == integration


def test_external_integration_connected_no_evidence(
    tmp_path,
):
    integration = {
        "requested": True,
        "connected": True,
        "status": "CONNECTED_NO_EVIDENCE",
        "providers": ["github"],
        "evidence_count": 0,
    }

    record = _build_record(
        tmp_path,
        integration,
    )

    assert (
        record["provenance"]["external_integration"]
        == integration
    )

    review = EngineeringReview().build(record)

    assert review["external_integration"] == integration

    # Critical contract:
    # connected + zero evidence is still a successful connection.
    assert (
        review["external_integration"]["connected"]
        is True
    )

    assert (
        review["external_integration"]["status"]
        == "CONNECTED_NO_EVIDENCE"
    )

    assert (
        review["external_integration"]["evidence_count"]
        == 0
    )


def test_external_integration_connected_with_evidence(
    tmp_path,
):
    integration = {
        "requested": True,
        "connected": True,
        "status": "CONNECTED_WITH_EVIDENCE",
        "providers": ["github"],
        "evidence_count": 3,
    }

    record = _build_record(
        tmp_path,
        integration,
    )

    review = EngineeringReview().build(record)

    assert review["external_integration"] == integration


def test_external_integration_authentication_failed(
    tmp_path,
):
    integration = {
        "requested": True,
        "connected": False,
        "status": "AUTHENTICATION_FAILED",
        "providers": ["github"],
        "evidence_count": 0,
    }

    record = _build_record(
        tmp_path,
        integration,
    )

    review = EngineeringReview().build(record)

    assert (
        review["external_integration"]["requested"]
        is True
    )

    assert (
        review["external_integration"]["connected"]
        is False
    )

    assert (
        review["external_integration"]["status"]
        == "AUTHENTICATION_FAILED"
    )

    assert (
        review["external_integration"]["evidence_count"]
        == 0
    )


def test_external_integration_does_not_change_local_evidence(
    tmp_path,
):
    integration = {
        "requested": True,
        "connected": True,
        "status": "CONNECTED_NO_EVIDENCE",
        "providers": ["github"],
        "evidence_count": 0,
    }

    record = _build_record(
        tmp_path,
        integration,
    )

    review = EngineeringReview().build(record)

    # External integration metadata must not replace
    # the canonical local evidence stream.
    assert review["evidence_shown"] >= 1
    assert review["evidence_available"] >= 1

    assert (
        review["external_integration"]["evidence_count"]
        == 0
    )