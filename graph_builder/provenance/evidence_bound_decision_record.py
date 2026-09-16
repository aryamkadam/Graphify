"""
Graphify

Phase 38
Stage 38.9

Evidence-Bound Engineering Decision Record

Binds an existing EngineeringDecisionRecord to an existing
EvidenceRelevanceEngine result.

This component is READ-ONLY.

It does NOT:

- create decisions
- modify decisions
- create policy
- create plans
- create memory
- execute engineering work
- mutate repositories
- infer causality
- invent rationale
- invent outcomes

Canonical authority remains upstream.

Decision:
    RepositoryDecisionEngine

Policy:
    RepositoryDecisionPolicy

Planning:
    RepositoryExecutionPlanningEngine

Experience:
    EngineeringMemory

Evidence discovery:
    DecisionEvidenceCollector

Evidence relevance:
    EvidenceRelevanceEngine
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any


class EvidenceBoundDecisionRecord:

    VERSION = "38.9"
    STATUS = "READ_ONLY_EVIDENCE_BOUND_RECORD"

    def build(
        self,
        decision_record: dict[str, Any],
        relevance_result: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Bind an existing EngineeringDecisionRecord to an existing
        EvidenceRelevanceEngine result.

        No new engineering meaning is created here.
        """

        if not isinstance(
            decision_record,
            dict,
        ):
            raise TypeError(
                "decision_record must be a dictionary."
            )

        if not isinstance(
            relevance_result,
            dict,
        ):
            raise TypeError(
                "relevance_result must be a dictionary."
            )

        record = deepcopy(
            decision_record
        )

        ranked_evidence = (
            relevance_result.get(
                "ranked_evidence",
                [],
            )
            or []
        )

        if not isinstance(
            ranked_evidence,
            list,
        ):
            ranked_evidence = []

        summary = (
            relevance_result.get(
                "summary",
                {},
            )
            or {}
        )

        provenance = (
            record.get(
                "provenance",
                {},
            )
            or {}
        )

        bound_provenance = deepcopy(
            provenance
        )

        bound_provenance.update({

            "evidence_relevance_owner":
                "EvidenceRelevanceEngine",

            "read_only":
                True,

            "creates_decision":
                False,

            "creates_policy":
                False,

            "creates_strategy":
                False,

            "creates_plan":
                False,

            "creates_memory":
                False,

            "executes_work":
                False,

            "mutates_repository":
                False,

            "infers_causality":
                False,

        })

        trust_policy = (
            record.get(
                "trust_policy",
                {},
            )
            or {}
        )

        bound_trust = deepcopy(
            trust_policy
        )

        bound_trust.update({

            "relevance_is_explanatory":
                True,

            "evidence_strength_is_explanatory":
                True,

            "causality_is_not_inferred":
                True,

        })

        record.update({

            "record_version":
                self.VERSION,

            "status":
                self.STATUS,

            "record_type":
                "Evidence-Bound Engineering Decision Record",

            "base_record_version":
                decision_record.get(
                    "record_version"
                ),

            "evidence_relevance_version":
                relevance_result.get(
                    "version"
                ),

            "evidence_binding": {

                "available":
                    True,

                "ranked_evidence":
                    deepcopy(
                        ranked_evidence
                    ),

                "summary": {

                    "high":
                        summary.get(
                            "high",
                            0,
                        ),

                    "medium":
                        summary.get(
                            "medium",
                            0,
                        ),

                    "low":
                        summary.get(
                            "low",
                            0,
                        ),

                },

                "evidence_count":
                    len(
                        ranked_evidence
                    ),

                "causality_status":
                    "NOT_INFERRED",

                "binding_owner":
                    "EvidenceBoundDecisionRecord",

            },

            "provenance":
                bound_provenance,

            "trust_policy":
                bound_trust,

        })

        return record