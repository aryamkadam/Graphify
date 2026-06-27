"""
Stage 15.7.2

Repository Reasoning Builder

Combines every reasoning module into one
Repository Reasoning object.

This becomes the central reasoning layer
used by:

- Repository Brain
- Prediction Engine
- AI Assistant
- Self Improvement Engine
- Future AGI modules
"""

from graph_builder.intelligence.repository_reasoning_rules import (
    RepositoryReasoningRules,
)


class RepositoryReasoningBuilder:

    def __init__(self):

        self.rules = RepositoryReasoningRules()

    # -------------------------------------

    def build(
        self,
        health_report,
        execution_engine,
        knowledge,
        decisions,
        insights,
    ):

        health_reasoning = self.rules.analyze_health(
            health_report
        )

        execution_reasoning = self.rules.analyze_execution(
            execution_engine
        )

        knowledge_reasoning = self.rules.analyze_knowledge(
            knowledge
        )

        decision_reasoning = self.rules.analyze_decisions(
            decisions
        )

        repository_direction = self.rules.analyze_repository_direction(
            insights
        )

        overall_reasoning = []

        overall_reasoning.extend(health_reasoning)

        overall_reasoning.extend(execution_reasoning)

        overall_reasoning.extend(knowledge_reasoning)

        overall_reasoning.extend(decision_reasoning)

        overall_reasoning.extend(repository_direction)

        return {

            "health_reasoning":
                health_reasoning,

            "execution_reasoning":
                execution_reasoning,

            "knowledge_reasoning":
                knowledge_reasoning,

            "decision_reasoning":
                decision_reasoning,

            "repository_direction":
                repository_direction,

            "overall_reasoning":
                overall_reasoning

        }