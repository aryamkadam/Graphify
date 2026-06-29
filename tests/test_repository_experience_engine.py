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

from graph_builder.reasoning.repository_decision_graph_engine import (
    RepositoryDecisionGraphEngine,
)

from graph_builder.intelligence.repository_evolution_intelligence_engine import (
    RepositoryEvolutionIntelligenceEngine,
)

from graph_builder.history.repository_evolution_story_engine import (
    RepositoryEvolutionStoryEngine,
)

from graph_builder.memory.repository_evolution_memory_engine import (
    RepositoryEvolutionMemoryEngine,
)

from graph_builder.reasoning.repository_memory_reasoning_engine import (
    RepositoryMemoryReasoningEngine,
)

from graph_builder.experience.repository_experience_engine import (
    RepositoryExperienceEngine,
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


def main():

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

        cause_effect,

    )

    intelligence = RepositoryEvolutionIntelligenceEngine().build(

        timeline,

        learning,

        decision_graph,

    )

    story = RepositoryEvolutionStoryEngine().build(

        {

            "summary": timeline["timeline_summary"],

            "health": history[-1]["health"],

        },

        {

            "engineering_direction":
                intelligence["technical_direction"],

            "repository_momentum":
                intelligence["technical_direction"],

        },

    )

    memory = RepositoryEvolutionMemoryEngine().build(

        timeline,

        learning,

        explanations,

        cause_effect,

        decision_graph,

        intelligence,

        story,

    )

    reasoning = RepositoryMemoryReasoningEngine().build(

        memory,

    )

    experience = RepositoryExperienceEngine().build(

        reasoning,

    )

    print("\n========================================")
    print("Repository Experience Engine")
    print("========================================\n")

    pprint(experience)


if __name__ == "__main__":

    main()