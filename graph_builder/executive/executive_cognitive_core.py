"""
Graphify

Phase 5

Stage P5.11

Executive Cognitive Core

Runs the complete executive cognition pipeline.

The Cognitive Core does not own memory.
Executive Memory is injected by the Executive Brain.

Author:
Graphify Core
"""

from graph_builder.executive.repository_strategy_engine import (
    RepositoryStrategyEngine,
)
from graph_builder.executive.executive_adaptation_engine import (
    ExecutiveAdaptationEngine,
)
from graph_builder.executive.executive_index_engine import (
    ExecutiveIndexEngine,
)
from graph_builder.executive.executive_recall_engine import (
    ExecutiveRecallEngine,
)
from graph_builder.executive.executive_prediction_engine import (
    ExecutivePredictionEngine,
)
from graph_builder.executive.executive_decision_intelligence import (
    ExecutiveDecisionIntelligence,
)


class ExecutiveCognitiveCore:

    VERSION = "P5.11"

    def __init__(

        self,

        executive_memory,

    ):

        # Shared persistent executive memory
        self.memory = executive_memory

        self.strategy_engine = RepositoryStrategyEngine()

        self.adaptation_engine = ExecutiveAdaptationEngine()

        self.index_engine = ExecutiveIndexEngine()

        self.recall_engine = ExecutiveRecallEngine()

        self.prediction_engine = ExecutivePredictionEngine()

        self.decision_engine = ExecutiveDecisionIntelligence()

    # --------------------------------------------------

    def execute(

        self,

        consciousness,

        knowledge,

        experience,

    ):

        strategy = self.strategy_engine.build(

            consciousness,

            knowledge,

            experience,

        )

        adaptation = self.adaptation_engine.build(

            strategy,

        )

        self.memory.remember(

            adaptation,

        )

        memory_export = self.memory.export()

        index = self.index_engine.build(

            memory_export,

        )

        recall = self.recall_engine.recall_by_strategy(

            memory_export,

            index,

            adaptation["adaptation_strategy"],

        )

        prediction = self.prediction_engine.build(

            recall,

            strategy,

        )

        decision = self.decision_engine.build(

            strategy,

            recall,

            prediction,

        )

        return {

            "strategy": strategy,

            "adaptation": adaptation,

            "memory": memory_export,

            "index": index,

            "recall": recall,

            "prediction": prediction,

            "decision": decision,

            "version": self.VERSION,

        }