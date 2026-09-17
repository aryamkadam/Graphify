from __future__ import annotations

from graph_builder.provenance.github_evidence_adapter import (
    GitHubEvidenceAdapter,
    _GitHubRequestError,
)


def test_connected_no_evidence_status(monkeypatch):
    adapter = GitHubEvidenceAdapter(
        token="test-token"
    )

    monkeypatch.setattr(
        adapter,
        "_git_remote",
        lambda: "https://github.com/acme/example.git",
    )

    def fake_get_json(path, params=None):
        if path == "/repos/acme/example":
            return {
                "name": "example",
                "full_name": "acme/example",
                "private": False,
                "default_branch": "main",
            }

        if path == "/repos/acme/example/pulls":
            return []

        raise AssertionError(
            f"Unexpected GitHub API path: {path}"
        )

    monkeypatch.setattr(
        adapter,
        "_get_json",
        fake_get_json,
    )

    result = adapter.collect()

    assert (
        result["status"]
        == GitHubEvidenceAdapter.CONNECTED_NO_EVIDENCE
    )
    assert result["connected"] is True
    assert result["evidence_available"] is False
    assert result["evidence_count"] == 0


def test_connected_with_evidence_status(monkeypatch):
    adapter = GitHubEvidenceAdapter(
        token="test-token"
    )

    monkeypatch.setattr(
        adapter,
        "_git_remote",
        lambda: "https://github.com/acme/example.git",
    )

    def fake_get_json(path, params=None):
        if path == "/repos/acme/example":
            return {
                "name": "example",
                "full_name": "acme/example",
                "private": False,
                "default_branch": "main",
            }

        if path == "/repos/acme/example/pulls":
            return [
                {
                    "number": 42,
                    "title": "Improve architecture",
                    "state": "closed",
                    "merged_at": "2026-09-01T10:00:00Z",
                    "user": {
                        "login": "developer",
                    },
                    "html_url": (
                        "https://github.com/acme/example/pull/42"
                    ),
                    "base": {
                        "ref": "main",
                    },
                    "head": {
                        "ref": "architecture",
                        "sha": "abc123",
                    },
                }
            ]

        if path == "/repos/acme/example/pulls/42/commits":
            return []

        if (
            path
            == "/repos/acme/example/commits/abc123/check-runs"
        ):
            return {
                "check_runs": [
                    {
                        "name": "pytest",
                        "status": "completed",
                        "conclusion": "success",
                    }
                ]
            }

        raise AssertionError(
            f"Unexpected GitHub API path: {path}"
        )

    monkeypatch.setattr(
        adapter,
        "_get_json",
        fake_get_json,
    )

    result = adapter.collect()

    assert (
        result["status"]
        == GitHubEvidenceAdapter.CONNECTED_WITH_EVIDENCE
    )
    assert result["connected"] is True
    assert result["evidence_available"] is True
    assert result["evidence_count"] == 2
    assert result["counts"]["pull_requests"] == 1
    assert result["counts"]["checks"] == 1


def test_authentication_failure_status(monkeypatch):
    adapter = GitHubEvidenceAdapter(
        token="bad-token"
    )

    monkeypatch.setattr(
        adapter,
        "_git_remote",
        lambda: "https://github.com/acme/example.git",
    )

    def fake_get_json(path, params=None):
        raise _GitHubRequestError(
            GitHubEvidenceAdapter.AUTHENTICATION_FAILED,
            "Authentication failed.",
        )

    monkeypatch.setattr(
        adapter,
        "_get_json",
        fake_get_json,
    )

    result = adapter.collect()

    assert (
        result["status"]
        == GitHubEvidenceAdapter.AUTHENTICATION_FAILED
    )
    assert result["connected"] is False
    assert result["evidence_count"] == 0
    assert result["evidence"] == []


def test_permission_denied_status(monkeypatch):
    adapter = GitHubEvidenceAdapter(
        token="test-token"
    )

    monkeypatch.setattr(
        adapter,
        "_git_remote",
        lambda: "https://github.com/acme/example.git",
    )

    def fake_get_json(path, params=None):
        raise _GitHubRequestError(
            GitHubEvidenceAdapter.PERMISSION_DENIED,
            "Permission denied.",
        )

    monkeypatch.setattr(
        adapter,
        "_get_json",
        fake_get_json,
    )

    result = adapter.collect()

    assert (
        result["status"]
        == GitHubEvidenceAdapter.PERMISSION_DENIED
    )
    assert result["connected"] is False
    assert result["evidence_count"] == 0


def test_repository_normalization():
    adapter = GitHubEvidenceAdapter()

    assert (
        adapter._normalize_repository(
            "https://github.com/acme/example.git"
        )
        == "acme/example"
    )

    assert (
        adapter._normalize_repository(
            "git@github.com:acme/example.git"
        )
        == "acme/example"
    )

    assert (
        adapter._normalize_repository(
            "acme/example"
        )
        == "acme/example"
    )


def test_pull_request_evidence_is_observational():
    adapter = GitHubEvidenceAdapter()

    evidence = adapter._pull_request_evidence(
        "acme/example",
        {
            "number": 42,
            "title": "Improve architecture",
            "state": "open",
            "merged_at": None,
            "user": {
                "login": "developer",
            },
            "html_url": (
                "https://github.com/acme/example/pull/42"
            ),
            "base": {
                "ref": "main",
            },
            "head": {
                "ref": "feature",
                "sha": "abc123",
            },
        },
    )

    assert evidence["type"] == "github_pull_request"
    assert evidence["classification"] == "DIRECT"
    assert evidence["evidence_strength"] == "DIRECT"
    assert evidence["causality_status"] == "NOT_INFERRED"


def test_check_evidence_is_verification():
    adapter = GitHubEvidenceAdapter()

    evidence = adapter._check_evidence(
        "acme/example",
        42,
        "abc123",
        {
            "name": "pytest",
            "status": "completed",
            "conclusion": "success",
        },
    )

    assert evidence["type"] == "github_check"
    assert evidence["classification"] == "VERIFICATION"
    assert evidence["evidence_strength"] == "DIRECT"
    assert evidence["causality_status"] == "NOT_INFERRED"


def test_collect_pull_request_returns_targeted_binding():
    adapter = GitHubEvidenceAdapter(
        token="test-token",
        api_base="https://example.test",
    )

    def fake_get_json(path, params=None):
        if path == "/repos/aryamkadam/Graphify":
            return {
                "name": "Graphify",
                "full_name": "aryamkadam/Graphify",
                "private": False,
                "default_branch": "develop",
            }

        if path == "/repos/aryamkadam/Graphify/pulls/123":
            return {
                "number": 123,
                "title": "Add engineering proof binding",
                "state": "open",
                "merged_at": None,
                "html_url": (
                    "https://github.com/aryamkadam/Graphify/pull/123"
                ),
                "user": {
                    "login": "aryamkadam"
                },
                "base": {
                    "ref": "develop"
                },
                "head": {
                    "ref": "feature/proof",
                    "sha": "abc123",
                },
            }

        if path == "/repos/aryamkadam/Graphify/pulls/123/commits":
            return [
                {
                    "sha": "abc123",
                    "commit": {
                        "message": "Add proof binding",
                        "author": {
                            "name": "Arya",
                            "date": "2026-09-16T10:00:00Z",
                        },
                    },
                    "files": [
                        {
                            "filename":
                                "graph_builder/provenance/engineering_proof.py"
                        }
                    ],
                }
            ]

        if path == "/repos/aryamkadam/Graphify/pulls/123/files":
            return [
                {
                    "filename":
                        "graph_builder/provenance/engineering_proof.py",
                    "status": "modified",
                    "additions": 10,
                    "deletions": 2,
                    "changes": 12,
                    "blob_url": (
                        "https://github.com/aryamkadam/Graphify/"
                        "blob/abc123/"
                        "graph_builder/provenance/engineering_proof.py"
                    ),
                }
            ]

        if (
            path
            == "/repos/aryamkadam/Graphify/commits/abc123/check-runs"
        ):
            return {
                "check_runs": [
                    {
                        "id": 1,
                        "name": "tests",
                        "status": "completed",
                        "conclusion": "success",
                    }
                ]
            }

        raise AssertionError(
            f"Unexpected GitHub path: {path}"
        )

    adapter._get_json = fake_get_json

    result = adapter.collect_pull_request(
        "aryamkadam/Graphify",
        123,
    )

    assert result["connected"] is True
    assert (
        result["status"]
        == "CONNECTED_WITH_EVIDENCE"
    )

    assert result["binding"] == {
        "provider": "github",
        "repository": "aryamkadam/Graphify",
        "pull_request": 123,
        "binding_type": "EXPLICIT",
        "binding_status": "OBSERVED",
    }

    assert result["counts"]["pull_requests"] == 1
    assert result["counts"]["commits"] == 1
    assert result["counts"]["files"] == 1
    assert result["counts"]["checks"] == 1

    assert result["causality_inferred"] is False
    assert result["read_only"] is True


def test_file_evidence_is_observational():
    adapter = GitHubEvidenceAdapter()

    evidence = adapter._file_evidence(
        "acme/example",
        42,
        {
            "filename": "src/example.py",
            "status": "modified",
            "additions": 10,
            "deletions": 2,
            "changes": 12,
            "blob_url": (
                "https://github.com/acme/example/blob/abc123/src/example.py"
            ),
        },
    )

    assert evidence["type"] == "github_file"
    assert evidence["repository"] == "acme/example"
    assert evidence["pull_request"] == 42
    assert evidence["path"] == "src/example.py"
    assert evidence["status"] == "modified"
    assert evidence["additions"] == 10
    assert evidence["deletions"] == 2
    assert evidence["changes"] == 12
    assert evidence["classification"] == "DIRECT"
    assert evidence["evidence_strength"] == "DIRECT"
    assert evidence["causality_status"] == "NOT_INFERRED"