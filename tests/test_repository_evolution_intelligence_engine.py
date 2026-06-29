from pprint import pprint

from graph_builder.history.repository_timeline_engine import (
    RepositoryTimelineEngine,
)

from graph_builder.learning.repository_learning_engine import (
    RepositoryLearningEngine,
)

from graph_builder.history.repository_change_explanation_engine import (
    RepositoryChangeExplanationEngine,
)

from graph_builder.history.repository_cause_effect_engine import (
    RepositoryCauseEffectEngine,
)

from graph_builder.intelligence.repository_decision_graph_engine import (
    RepositoryDecisionGraphEngine,
)

from graph_builder.intelligence.repository_evolution_intelligence_engine import (
    RepositoryEvolutionIntelligenceEngine,
)

history = [

    {
        "timestamp": "2026-06-01",

        "health": {
            "old": 90,
            "new": 93,
            "delta": 3,
        },

        "execution": {
            "old": 200,
            "new": 220,
            "delta": 20,
        },

        "knowledge": {

            "dead_code": {
                "old": 4,
                "new": 2,
                "delta": -2,
            },

            "hotspots": {
                "old": 8,
                "new": 6,
                "delta": -2,
            }

        }

    },

    {
        "timestamp": "2026-06-20",

        "health": {
            "old": 93,
            "new": 96,
            "delta": 3,
        },

        "execution": {
            "old": 220,
            "new": 260,
            "delta": 40,
        },

        "knowledge": {

            "dead_code": {
                "old": 2,
                "new": 1,
                "delta": -1,
            },

            "hotspots": {
                "old": 6,
                "new": 5,
                "delta": -1,
            }

        }

    }

]

timeline = RepositoryTimelineEngine().build(history)

learning = RepositoryLearningEngine().build(history)

explanations = RepositoryChangeExplanationEngine().build(
    timeline,
    history,
    learning,
)

cause_effect = RepositoryCauseEffectEngine().build(
    explanations,
    learning,
)

decision_graph = RepositoryDecisionGraphEngine().build(
    cause_effect
)

report = RepositoryEvolutionIntelligenceEngine().build(
    timeline,
    learning,
    decision_graph,
)

print("\nRepository Evolution Intelligence\n")

pprint(report)