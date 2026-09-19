"""
Graphify

GitHub Evidence Adapter

Read-only adapter that converts GitHub repository activity into
canonical external engineering evidence.

This component does NOT:
- create decisions
- create plans
- rank evidence
- infer causality
- create outcomes
- mutate GitHub
- mutate repository state
"""

from __future__ import annotations

import json
import os
import re
import subprocess
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class GitHubEvidenceAdapter:

    VERSION = "1.1"

    API_BASE = "https://api.github.com"

    DEFAULT_LIMIT = 20

    # --------------------------------------------------
    # Integration States
    # --------------------------------------------------

    CONNECTED_WITH_EVIDENCE = (
        "CONNECTED_WITH_EVIDENCE"
    )

    CONNECTED_NO_EVIDENCE = (
        "CONNECTED_NO_EVIDENCE"
    )

    AUTHENTICATION_FAILED = (
        "AUTHENTICATION_FAILED"
    )

    PERMISSION_DENIED = (
        "PERMISSION_DENIED"
    )

    RATE_LIMITED = (
        "RATE_LIMITED"
    )

    NETWORK_ERROR = (
        "NETWORK_ERROR"
    )

    REPOSITORY_UNAVAILABLE = (
        "REPOSITORY_UNAVAILABLE"
    )

    INVALID_REPOSITORY = (
        "INVALID_REPOSITORY"
    )

    def __init__(
        self,
        token: str | None = None,
        api_base: str = API_BASE,
    ):

        self.token = (
            token
            if token is not None
            else os.getenv(
                "GITHUB_TOKEN"
            )
        )

        self.api_base = (
            api_base.rstrip("/")
        )

    # ==================================================
    # Public API
    # ==================================================

    def collect(
        self,
        repository: str | None = None,
        limit: int = DEFAULT_LIMIT,
    ) -> dict[str, Any]:
        """
        Collect read-only GitHub engineering evidence.

        The returned status distinguishes:

        - connected + evidence
        - connected + no evidence
        - authentication failure
        - permission failure
        - rate limiting
        - network failure
        - unavailable repository

        No causality is inferred.
        """

        try:

            repository = (
                self._resolve_repository(
                    repository
                )
            )

        except ValueError as exc:

            return self._error_result(
                status=self.INVALID_REPOSITORY,
                repository=None,
                message=str(exc),
            )

        limit = self._normalize_limit(
            limit
        )

        # --------------------------------------------------
        # Verify repository connectivity first
        # --------------------------------------------------

        try:

            repository_data = (
                self._get_json(
                    f"/repos/{repository}"
                )
            )

        except _GitHubRequestError as exc:

            return self._error_result(
                status=exc.status,
                repository=repository,
                message=exc.message,
            )

        # --------------------------------------------------
        # Repository metadata sanity check
        # --------------------------------------------------

        if not isinstance(
            repository_data,
            dict,
        ):

            return self._error_result(
                status=self.REPOSITORY_UNAVAILABLE,
                repository=repository,
                message=(
                    "GitHub returned an unexpected "
                    "repository response."
                ),
            )

        evidence = []

        # --------------------------------------------------
        # Pull requests
        # --------------------------------------------------

        try:

            pull_requests = (
                self._get_json(
                    f"/repos/{repository}/pulls",
                    params={
                        "state": "all",
                        "sort": "updated",
                        "direction": "desc",
                        "per_page": min(
                            limit,
                            100,
                        ),
                    },
                )
            )

        except _GitHubRequestError as exc:

            return self._error_result(
                status=exc.status,
                repository=repository,
                message=exc.message,
            )

        if not isinstance(
            pull_requests,
            list,
        ):

            pull_requests = []

        for pull_request in pull_requests:

            if not isinstance(
                pull_request,
                dict,
            ):
                continue

            pr_number = pull_request.get(
                "number"
            )

            if pr_number is None:
                continue

            evidence.append(
                self._pull_request_evidence(
                    repository,
                    pull_request,
                )
            )

            # --------------------------------------------------
            # PR commits
            # --------------------------------------------------

            try:

                commits = (
                    self._get_json(
                        (
                            f"/repos/{repository}/pulls/"
                            f"{pr_number}/commits"
                        ),
                        params={
                            "per_page": 100,
                        },
                    )
                )

            except _GitHubRequestError as exc:

                return self._error_result(
                    status=exc.status,
                    repository=repository,
                    message=exc.message,
                )

            if not isinstance(
                commits,
                list,
            ):

                commits = []

            for commit in commits:

                if not isinstance(
                    commit,
                    dict,
                ):
                    continue

                evidence.append(
                    self._commit_evidence(
                        repository,
                        pr_number,
                        commit,
                    )
                )

            # --------------------------------------------------
            # Pull request changed files
            # --------------------------------------------------

            try:

                pull_request_files = (
                    self._get_json(
                        (
                            f"/repos/{repository}/pulls/"
                            f"{pr_number}/files"
                        ),
                        params={
                            "per_page": 100,
                        },
                    )
                )

            except _GitHubRequestError as exc:

                return self._error_result(
                    status=exc.status,
                    repository=repository,
                    message=exc.message,
                )

            if not isinstance(
                pull_request_files,
                list,
            ):

                pull_request_files = []

            for pull_request_file in pull_request_files:

                if not isinstance(
                    pull_request_file,
                    dict,
                ):
                    continue

                evidence.append(
                    self._file_evidence(
                        repository,
                        pr_number,
                        pull_request_file,
                    )
                )

            # --------------------------------------------------
            # Checks
            # --------------------------------------------------

            head_sha = (
                pull_request.get(
                    "head",
                    {},
                )
                or {}
            ).get(
                "sha"
            )

            if head_sha:

                try:

                    check_runs = (
                        self._get_json(
                            (
                                f"/repos/{repository}/"
                                f"commits/{head_sha}/"
                                f"check-runs"
                            ),
                            params={
                                "per_page": 100,
                            },
                        )
                    )

                except _GitHubRequestError as exc:

                    return self._error_result(
                        status=exc.status,
                        repository=repository,
                        message=exc.message,
                    )

                for check_run in (
                    self._extract_check_runs(
                        check_runs
                    )
                ):

                    evidence.append(
                        self._check_evidence(
                            repository,
                            pr_number,
                            head_sha,
                            check_run,
                        )
                    )

        if evidence:

            status = (
                self.CONNECTED_WITH_EVIDENCE
            )

        else:

            status = (
                self.CONNECTED_NO_EVIDENCE
            )

        return {

            "source":
                "github",

            "repository":
                repository,

            "repository_metadata":
                {
                    "name":
                        repository_data.get(
                            "name"
                        ),

                    "full_name":
                        repository_data.get(
                            "full_name"
                        ),

                    "private":
                        repository_data.get(
                            "private"
                        ),

                    "default_branch":
                        repository_data.get(
                            "default_branch"
                        ),
                },

            "status":
                status,

            "connected":
                True,

            "evidence_available":
                bool(evidence),

            "evidence_count":
                len(evidence),

            "evidence":
                evidence,

            "counts": {

                "pull_requests":
                    sum(
                        1
                        for item
                        in evidence
                        if item.get(
                            "type"
                        )
                        == "github_pull_request"
                    ),

                "commits":
                    sum(
                        1
                        for item
                        in evidence
                        if item.get(
                            "type"
                        )
                        == "github_commit"
                    ),

                "files":
                    sum(
                        1
                        for item
                        in evidence
                        if item.get(
                            "type"
                        )
                        == "github_file"
                    ),

                "checks":
                    sum(
                        1
                        for item
                        in evidence
                        if item.get(
                            "type"
                        )
                        == "github_check"
                    ),

            },

            "version":
                self.VERSION,

            "read_only":
                True,

            "causality_inferred":
                False,

        }

    # ==================================================
    # Targeted Pull Request Collection
    # ==================================================

    def collect_pull_request(
        self,
        repository: str | None,
        pull_request: int,
    ) -> dict[str, Any]:
        """
        Collect evidence for one explicitly identified GitHub PR.

        This is intentionally narrower than collect(), which discovers
        recent repository PR activity.

        The method observes the requested PR, its commits, changed files,
        and head commit checks. It does not infer causality or outcomes.
        """

        try:
            repository = self._resolve_repository(repository)
        except ValueError as exc:
            return self._error_result(
                status=self.INVALID_REPOSITORY,
                repository=None,
                message=str(exc),
            )

        try:
            pull_request = int(pull_request)
        except (TypeError, ValueError):
            return self._error_result(
                status=self.INVALID_REPOSITORY,
                repository=repository,
                message="pull_request must be an integer.",
            )

        if pull_request < 1:
            return self._error_result(
                status=self.INVALID_REPOSITORY,
                repository=repository,
                message="pull_request must be greater than zero.",
            )

        try:
            repository_data = self._get_json(
                f"/repos/{repository}"
            )

            pr = self._get_json(
                f"/repos/{repository}/pulls/{pull_request}"
            )

        except _GitHubRequestError as exc:
            return self._error_result(
                status=exc.status,
                repository=repository,
                message=exc.message,
            )

        if not isinstance(repository_data, dict):
            return self._error_result(
                status=self.REPOSITORY_UNAVAILABLE,
                repository=repository,
                message="GitHub returned an unexpected repository response.",
            )

        if not isinstance(pr, dict):
            return self._error_result(
                status=self.REPOSITORY_UNAVAILABLE,
                repository=repository,
                message="GitHub returned an unexpected pull request response.",
            )

        evidence = []

        evidence.append(
            self._pull_request_evidence(
                repository,
                pr,
            )
        )

        try:
            commits = self._get_json(
                f"/repos/{repository}/pulls/{pull_request}/commits",
                params={"per_page": 100},
            )
        except _GitHubRequestError as exc:
            return self._error_result(
                status=exc.status,
                repository=repository,
                message=exc.message,
            )

        if not isinstance(commits, list):
            commits = []

        for commit in commits:
            if not isinstance(commit, dict):
                continue

            evidence.append(
                self._commit_evidence(
                    repository,
                    pull_request,
                    commit,
                )
            )

        # --------------------------------------------------
        # Pull request changed files
        # --------------------------------------------------

        try:
            pull_request_files = self._get_json(
                f"/repos/{repository}/pulls/{pull_request}/files",
                params={"per_page": 100},
            )
        except _GitHubRequestError as exc:
            return self._error_result(
                status=exc.status,
                repository=repository,
                message=exc.message,
            )

        if not isinstance(pull_request_files, list):
            pull_request_files = []

        for pull_request_file in pull_request_files:
            if not isinstance(pull_request_file, dict):
                continue

            evidence.append(
                self._file_evidence(
                    repository,
                    pull_request,
                    pull_request_file,
                )
            )

        head_sha = (
            pr.get("head", {})
            or {}
        ).get("sha")

        if head_sha:
            try:
                check_runs = self._get_json(
                    f"/repos/{repository}/commits/{head_sha}/check-runs",
                    params={"per_page": 100},
                )
            except _GitHubRequestError as exc:
                return self._error_result(
                    status=exc.status,
                    repository=repository,
                    message=exc.message,
                )

            for check_run in self._extract_check_runs(
                check_runs
            ):
                evidence.append(
                    self._check_evidence(
                        repository,
                        pull_request,
                        head_sha,
                        check_run,
                    )
                )

        return {
            "source": "github",
            "repository": repository,
            "status": self.CONNECTED_WITH_EVIDENCE,
            "connected": True,
            "evidence_available": bool(evidence),
            "evidence_count": len(evidence),
            "evidence": evidence,
            "counts": {
                "pull_requests": sum(
                    1
                    for item in evidence
                    if item.get("type") == "github_pull_request"
                ),
                "commits": sum(
                    1
                    for item in evidence
                    if item.get("type") == "github_commit"
                ),
                "files": sum(
                    1
                    for item in evidence
                    if item.get("type") == "github_file"
                ),
                "checks": sum(
                    1
                    for item in evidence
                    if item.get("type") == "github_check"
                ),
            },
            "binding": {
                "provider": "github",
                "repository": repository,
                "pull_request": pull_request,
                "binding_type": "EXPLICIT",
                "binding_status": "OBSERVED",
            },
            "version": self.VERSION,
            "read_only": True,
            "causality_inferred": False,
        }

    # ==================================================
    # Pull Request File
    # ==================================================

    @staticmethod
    def _file_evidence(
        repository: str,
        pr_number: int,
        pull_request_file: dict[str, Any],
    ) -> dict[str, Any]:

        return {
            "source": "github",
            "type": "github_file",
            "repository": repository,
            "pull_request": pr_number,
            "path": pull_request_file.get("filename"),
            "status": pull_request_file.get("status"),
            "additions": pull_request_file.get("additions", 0),
            "deletions": pull_request_file.get("deletions", 0),
            "changes": pull_request_file.get("changes", 0),
            "blob_url": pull_request_file.get("blob_url"),
            "classification": "DIRECT",
            "evidence_strength": "DIRECT",
            "causality_status": "NOT_INFERRED",
        }

    # ==================================================
    # Error Result
    # ==================================================

    @classmethod
    def _error_result(
        cls,
        status,
        repository,
        message,
    ):

        return {

            "source":
                "github",

            "repository":
                repository,

            "status":
                status,

            "connected":
                False,

            "evidence_available":
                False,

            "evidence_count":
                0,

            "evidence":
                [],

            "counts": {

                "pull_requests":
                    0,

                "commits":
                    0,

                "files":
                    0,

                "checks":
                    0,

            },

            "error":
                message,

            "version":
                cls.VERSION,

            "read_only":
                True,

            "causality_inferred":
                False,

        }

    # ==================================================
    # Pull Request
    # ==================================================

    @staticmethod
    def _pull_request_evidence(
        repository: str,
        pull_request: dict[str, Any],
    ) -> dict[str, Any]:

        return {

            "source":
                "github",

            "type":
                "github_pull_request",

            "repository":
                repository,

            "pull_request":
                pull_request.get(
                    "number"
                ),

            "title":
                pull_request.get(
                    "title"
                ),

            "state":
                pull_request.get(
                    "state"
                ),

            "merged":
                (
                    pull_request.get(
                        "merged_at"
                    )
                    is not None
                ),

            "merged_at":
                pull_request.get(
                    "merged_at"
                ),

            "author":
                (
                    pull_request.get(
                        "user",
                        {},
                    )
                    or {}
                ).get(
                    "login"
                ),

            "url":
                pull_request.get(
                    "html_url"
                ),

            "base_branch":
                (
                    pull_request.get(
                        "base",
                        {},
                    )
                    or {}
                ).get(
                    "ref"
                ),

            "head_branch":
                (
                    pull_request.get(
                        "head",
                        {},
                    )
                    or {}
                ).get(
                    "ref"
                ),

            "head_sha":
                (
                    pull_request.get(
                        "head",
                        {},
                    )
                    or {}
                ).get(
                    "sha"
                ),

            "classification":
                "DIRECT",

            "evidence_strength":
                "DIRECT",

            "causality_status":
                "NOT_INFERRED",

        }

    # ==================================================
    # Commit
    # ==================================================

    @staticmethod
    def _commit_evidence(
        repository: str,
        pr_number: int,
        commit: dict[str, Any],
    ) -> dict[str, Any]:

        commit_data = (
            commit.get(
                "commit",
                {},
            )
            or {}
        )

        author_data = (
            commit_data.get(
                "author",
                {},
            )
            or {}
        )

        files = (
            commit.get(
                "files",
                [],
            )
            or []
        )

        return {

            "source":
                "github",

            "type":
                "github_commit",

            "repository":
                repository,

            "pull_request":
                pr_number,

            "commit":
                commit.get(
                    "sha"
                ),

            "message":
                commit_data.get(
                    "message"
                ),

            "author":
                author_data.get(
                    "name"
                ),

            "timestamp":
                author_data.get(
                    "date"
                ),

            "files": [

                item.get(
                    "filename"
                )

                for item
                in files

                if isinstance(
                    item,
                    dict,
                )

                and item.get(
                    "filename"
                )

            ],

            "url":
                commit.get(
                    "html_url"
                ),

            "classification":
                "DIRECT",

            "evidence_strength":
                "DIRECT",

            "causality_status":
                "NOT_INFERRED",

        }

    # ==================================================
    # Checks
    # ==================================================

    @staticmethod
    def _extract_check_runs(
        response,
    ) -> list[dict[str, Any]]:

        if not isinstance(
            response,
            dict,
        ):
            return []

        runs = response.get(
            "check_runs",
            [],
        )

        if not isinstance(
            runs,
            list,
        ):
            return []

        return [
            item
            for item in runs
            if isinstance(
                item,
                dict,
            )
        ]

    @staticmethod
    def _check_evidence(
        repository: str,
        pr_number: int,
        commit: str,
        check_run: dict[str, Any],
    ) -> dict[str, Any]:

        return {

            "source":
                "github",

            "type":
                "github_check",

            "repository":
                repository,

            "pull_request":
                pr_number,

            "commit":
                commit,

            "check_name":
                check_run.get(
                    "name"
                ),

            "status":
                check_run.get(
                    "status"
                ),

            "conclusion":
                check_run.get(
                    "conclusion"
                ),

            "started_at":
                check_run.get(
                    "started_at"
                ),

            "completed_at":
                check_run.get(
                    "completed_at"
                ),

            "url":
                check_run.get(
                    "html_url"
                ),

            "classification":
                "VERIFICATION",

            "evidence_strength":
                "DIRECT",

            "causality_status":
                "NOT_INFERRED",

        }

    # ==================================================
    # HTTP
    # ==================================================

    def _get_json(
        self,
        path: str,
        params: dict[str, Any] | None = None,
    ):

        url = (
            f"{self.api_base}"
            f"{path}"
        )

        if params:

            url += (
                "?"
                + urlencode(
                    params
                )
            )

        headers = {

            "Accept":
                "application/vnd.github+json",

            "X-GitHub-Api-Version":
                "2026-03-10",

            "User-Agent":
                "Graphify-GitHub-Evidence",

        }

        if self.token:

            headers[
                "Authorization"
            ] = (
                f"Bearer {self.token}"
            )

        request = Request(
            url,
            headers=headers,
            method="GET",
        )

        try:

            with urlopen(
                request,
                timeout=20,
            ) as response:

                payload = response.read()

            return json.loads(
                payload.decode(
                    "utf-8"
                )
            )

        except HTTPError as exc:

            status_code = exc.code

            if status_code == 401:

                status = (
                    self.AUTHENTICATION_FAILED
                )

            elif status_code == 403:

                # GitHub uses 403 for both permission
                # failures and rate limiting. Inspect headers.
                remaining = exc.headers.get(
                    "X-RateLimit-Remaining"
                )

                if remaining == "0":

                    status = (
                        self.RATE_LIMITED
                    )

                else:

                    status = (
                        self.PERMISSION_DENIED
                    )

            elif status_code == 404:

                status = (
                    self.REPOSITORY_UNAVAILABLE
                )

            else:

                status = (
                    self.REPOSITORY_UNAVAILABLE
                )

            raise _GitHubRequestError(
                status=status,
                message=(
                    f"GitHub API request failed "
                    f"with HTTP {status_code}: "
                    f"{exc.reason}"
                ),
            ) from exc

        except URLError as exc:

            raise _GitHubRequestError(
                status=self.NETWORK_ERROR,
                message=(
                    "Unable to reach GitHub API: "
                    f"{exc.reason}"
                ),
            ) from exc

        except json.JSONDecodeError as exc:

            raise _GitHubRequestError(
                status=self.NETWORK_ERROR,
                message=(
                    "GitHub API returned invalid JSON."
                ),
            ) from exc

    # ==================================================
    # Repository Resolution
    # ==================================================

    def _resolve_repository(
        self,
        repository: str | None,
    ) -> str:

        if repository:

            return (
                self._normalize_repository(
                    repository
                )
            )

        remote = self._git_remote()

        if not remote:

            raise ValueError(
                "GitHub repository was not provided "
                "and no GitHub origin remote was found."
            )

        return (
            self._normalize_repository(
                remote
            )
        )

    @staticmethod
    def _git_remote():

        try:

            return subprocess.check_output(
                [
                    "git",
                    "config",
                    "--get",
                    "remote.origin.url",
                ],
                text=True,
                stderr=subprocess.DEVNULL,
            ).strip()

        except Exception:

            return None

    @staticmethod
    def _normalize_repository(
        value: str,
    ) -> str:

        value = (
            str(
                value
            )
            .strip()
            .rstrip("/")
        )

        match = re.search(
            r"github\.com/([^/]+)/([^/]+?)(?:\.git)?$",
            value,
            re.IGNORECASE,
        )

        if match:

            return (
                f"{match.group(1)}/"
                f"{match.group(2)}"
            )

        match = re.search(
            r"github\.com:([^/]+)/([^/]+?)(?:\.git)?$",
            value,
            re.IGNORECASE,
        )

        if match:

            return (
                f"{match.group(1)}/"
                f"{match.group(2)}"
            )

        if value.count("/") == 1:

            owner, repo = (
                value.split(
                    "/",
                    1,
                )
            )

            if owner and repo:

                return (
                    f"{owner}/"
                    f"{repo.removesuffix('.git')}"
                )

        raise ValueError(
            "Invalid GitHub repository. "
            "Expected owner/repo or a GitHub URL."
        )

    # ==================================================
    # Validation
    # ==================================================

    @staticmethod
    def _normalize_limit(
        value,
    ) -> int:

        try:

            value = int(
                value
            )

        except (
            TypeError,
            ValueError,
        ):

            value = (
                GitHubEvidenceAdapter.DEFAULT_LIMIT
            )

        return max(
            1,
            min(
                value,
                100,
            )
        )


class _GitHubRequestError(
    RuntimeError
):

    def __init__(
        self,
        status,
        message,
    ):

        super().__init__(
            message
        )

        self.status = status
        self.message = message