from pprint import pprint

from graph_builder.memory.repository_evolution_memory_engine import (
    RepositoryEvolutionMemoryEngine,
)

from graph_builder.reasoning.repository_memory_reasoning_engine import (
    RepositoryMemoryReasoningEngine,
)

from graph_builder.experience.repository_experience_engine import (
    RepositoryExperienceEngine,
)

from graph_builder.knowledge.repository_knowledge_engine import (
    RepositoryKnowledgeEngine,
)

from graph_builder.consciousness.repository_consciousness_engine import (
    RepositoryConsciousnessEngine,
)

memory = {

    "repository_identity": {

        "phase": "Stabilization",

        "technical_direction": "Positive",

        "engineering_velocity": "Healthy",

        "future_risk": "Low",

    },

    "long_term_lessons": [

        {

            "lesson":

                "This engineering decision should be remembered for future repository improvements.",

            "confidence": 0.95,

            "impact": "High",

        }

    ]

}

reasoning = RepositoryMemoryReasoningEngine().build(memory)

experience = RepositoryExperienceEngine().build(reasoning)

knowledge = RepositoryKnowledgeEngine().build(experience)

consciousness = RepositoryConsciousnessEngine().build(

    {},

    {},

    memory,

    reasoning,

    experience,

    knowledge,

)

print("\n========================================")
print("Repository Consciousness")
print("========================================\n")

pprint(consciousness)