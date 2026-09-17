from __future__ import annotations

from graph_builder.provenance.engineering_proof import (
    EngineeringProof,
)


def test_engineering_proof_is_read_only_projection():

    record = {
        "repository": "graphify",
        "repository_path": ".",

        "decision": {
            "decision":
                "Prioritize Architectural Improvement",

            "selected_goal":
                "Strengthen Repository Architecture",

            "strategy":
                "Repository Architecture",
        },

        "plan": {
            "objective":
                "Strengthen Repository Architecture",
        },

        "evidence": {
            "direct": [
                {
                    "type":
                        "repository_document",

                    "path":
                        "docs/ARCHITECTURE.md",

                    "classification":
                        "DIRECT",

                    "evidence_strength":
                        "EXPLICIT",

                    "text":
                        "Repository architecture",
                }
            ],

            "related": [],

            "context": [],

            "external": [],
        },

        "knowledge": {
            "decision_rationale":
                "Architecture evidence supports the change.",
        },

        "provenance": {
            "read_only": True,

            "creates_decision":
                False,

            "creates_plan":
                False,

            "mutates_repository":
                False,

            "causality_inference":
                False,

            "external_integration": {
                "requested":
                    False,

                "connected":
                    False,

                "status":
                    "NOT_REQUESTED",

                "providers": [],

                "evidence_count":
                    0,
            },
        },
    }

    review = {
        "evidence": [
            {
                "type":
                    "repository_document",

                "path":
                    "docs/ARCHITECTURE.md",

                "strength":
                    "EXPLICIT",

                "score":
                    16,
            }
        ],

        "execution": {
            "performed":
                False,

            "status":
                "NOT_EXECUTED",

            "validation":
                "NOT_AVAILABLE",

            "review":
                "NOT_AVAILABLE",

            "outcome":
                "UNKNOWN",
        },

        "external_integration": {
            "requested":
                False,

            "connected":
                False,

            "status":
                "NOT_REQUESTED",

            "providers": [],

            "evidence_count":
                0,
        },
    }

    proof = EngineeringProof().build(
        record=record,
        review=review,
    )

    assert proof["proof_version"] == "39.1"

    assert proof["repository"] == "graphify"

    assert (
        proof["decision"]["statement"]
        == "Prioritize Architectural Improvement"
    )

    assert (
        proof["decision"]["goal"]
        == "Strengthen Repository Architecture"
    )

    assert (
        len(proof["why"]["evidence"])
        == 1
    )

    assert (
        proof["outcome"]["status"]
        == "UNKNOWN"
    )

    assert (
        proof["trust"]["read_only"]
        is True
    )

    assert (
        proof["trust"]["work_executed"]
        is False
    )

    assert (
        proof["trust"]["causality_inferred"]
        is False
    )

    assert (
        proof["external_integration"]["status"]
        == "NOT_REQUESTED"
    )

    assert (
        proof["status"]
        == "INCOMPLETE"
    )


def test_connected_no_evidence_remains_truthful():

    record = {
        "repository": "graphify",

        "decision": {
            "decision":
                "Improve architecture",

            "selected_goal":
                "Strengthen architecture",
        },

        "plan": {
            "objective":
                "Strengthen architecture",
        },

        "evidence": {
            "direct": [],
            "related": [],
            "context": [],
            "external": [],
        },

        "knowledge": {},

        "provenance": {
            "external_integration": {
                "requested":
                    True,

                "connected":
                    True,

                "status":
                    "CONNECTED_NO_EVIDENCE",

                "providers":
                    ["github"],

                "evidence_count":
                    0,
            }
        },
    }

    proof = EngineeringProof().build(
        record=record,
        review={
            "external_integration": {
                "requested":
                    True,

                "connected":
                    True,

                "status":
                    "CONNECTED_NO_EVIDENCE",

                "providers":
                    ["github"],

                "evidence_count":
                    0,
            },

            "execution": {
                "performed":
                    False,

                "outcome":
                    "UNKNOWN",
            },
        },
    )

    assert (
        proof["external_integration"]["requested"]
        is True
    )

    assert (
        proof["external_integration"]["connected"]
        is True
    )

    assert (
        proof["external_integration"]["status"]
        == "CONNECTED_NO_EVIDENCE"
    )

    assert (
        proof["external_integration"]["evidence_count"]
        == 0
    )

    assert (
        proof["outcome"]["causality"]
        == "UNKNOWN"
    )


def test_successful_execution_produces_proven(tmp_path):

    record = {
        "repository":
            "graphify",

        "decision": {
            "decision":
                "Improve architecture",

            "selected_goal":
                "Strengthen architecture",
        },

        "plan": {
            "objective":
                "Strengthen architecture",
        },

        "evidence": {
            "direct": [],
            "related": [],
            "context": [],
            "external": [],
        },

        "knowledge": {},

        "provenance": {
            "read_only":
                True,

            "mutates_repository":
                False,

            "causality_inference":
                False,
        },
    }

    review = {
        "evidence": [],

        "execution": {
            "performed":
                True,

            "status":
                "success",

            "validation":
                "VERIFIED",

            "review":
                "COMPLETED",

            "accountability":
                "ACCOUNTED",

            "alignment":
                "ALIGNED",

            "outcome":
                "SUCCESSFUL",
        },
    }

    proof = EngineeringProof().build(
        record=record,
        review=review,
    )

    assert proof["status"] == "PROVEN"

    assert (
        proof["outcome"]["status"]
        == "SUCCESSFUL"
    )

    assert (
        proof["verification"]["status"]
        == "VERIFIED"
    )

    assert (
        proof["trust"]["work_executed"]
        is True
    )

    assert (
        proof["trust"]["outcome_verified"]
        is True
    )

    assert (
        proof["trust"]["causality_inferred"]
        is False
    )

    assert (
        proof["trust"]["read_only"]
        is True
    )
def test_external_binding_is_projected_without_claiming_causality():

    record = {
        "repository": "graphify",

        "decision": {
            "decision": "Improve engineering traceability",
            "selected_goal": "Bind engineering work to evidence",
        },

        "plan": {
            "objective": "Observe a real GitHub pull request",
        },

        "evidence": {
            "direct": [],
            "related": [],
            "context": [],
            "external": [],
        },

        "knowledge": {},

        "provenance": {
            "external_binding": {
                "provider": "github",
                "repository": "aryamkadam/Graphify",
                "pull_request": 123,
                "binding_type": "EXPLICIT",
                "binding_status": "OBSERVED",
            }
        },
    }

    proof = EngineeringProof().build(
        record=record,
        review={},
    )

    assert proof["external_binding"] == {
        "provider": "github",
        "repository": "aryamkadam/Graphify",
        "pull_request": 123,
        "binding_type": "EXPLICIT",
        "binding_status": "OBSERVED",
    }

    assert proof["outcome"]["causality"] == "UNKNOWN"
    assert proof["trust"]["causality_inferred"] is False
def test_decision_observed_requires_real_decision():
    proof = EngineeringProof()

    real_decision = {
        "decision": "Use GitHub pull request evidence"
    }

    unknown_decision = {
        "decision": "UNKNOWN"
    }

    trust_real = proof._trust(
        decision=real_decision,
        provenance={},
        execution={},
        outcome={},
    )

    trust_unknown = proof._trust(
        decision=unknown_decision,
        provenance={},
        execution={},
        outcome={},
    )

    assert trust_real["decision_observed"] is True
    assert trust_unknown["decision_observed"] is False