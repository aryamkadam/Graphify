from graph_builder.provenance.engineering_proof import EngineeringProof


def test_github_file_evidence_is_projected_into_change():

    record = {
        "repository": "graphify",
        "decision": {
            "decision": "Improve engineering traceability",
            "selected_goal": "Bind engineering work to evidence",
        },
        "plan": {
            "objective": "Observe the implementation",
        },
        "evidence": {
            "direct": [],
            "related": [],
            "context": [],
            "external": [
                {
                    "type": "github_pull_request",
                    "pull_request": 1,
                    "head_sha": "32d8e31",
                },
                {
                    "type": "github_commit",
                    "pull_request": 1,
                    "commit": "32d8e31",
                    "files": [],
                },
                {
                    "type": "github_file",
                    "pull_request": 1,
                    "path": "graph_builder/provenance/engineering_proof.py",
                    "classification": "DIRECT",
                    "evidence_strength": "DIRECT",
                },
                {
                    "type": "github_file",
                    "pull_request": 1,
                    "path": "graph_builder/provenance/github_evidence_adapter.py",
                    "classification": "DIRECT",
                    "evidence_strength": "DIRECT",
                },
            ],
        },
        "knowledge": {},
        "provenance": {
            "read_only": True,
            "causality_inference": False,
        },
    }

    proof = EngineeringProof().build(
        record=record,
        review={},
    )

    assert proof["change"]["status"] == "OBSERVED"

    assert (
        "graph_builder/provenance/engineering_proof.py"
        in proof["change"]["files_changed"]
    )

    assert (
        "graph_builder/provenance/github_evidence_adapter.py"
        in proof["change"]["files_changed"]
    )

    assert proof["outcome"]["causality"] == "UNKNOWN"
    assert proof["trust"]["causality_inferred"] is False
