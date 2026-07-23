from pprint import pprint

from graph_builder.intelligence.repository_identity import RepositoryIdentity
from graph_builder.reasoning.repository_mission_engine import RepositoryMissionEngine
from graph_builder.reasoning.repository_goal_engine import RepositoryGoalEngine
from graph_builder.understanding.repository_understanding_engine import RepositoryUnderstandingEngine
from graph_builder.understanding.repository_insight_engine import RepositoryInsightEngine
from graph_builder.reasoning.repository_cognitive_reasoning_engine import RepositoryCognitiveReasoningEngine
from graph_builder.decision.repository_decision_engine import RepositoryDecisionEngine


print("=" * 40)
print("Repository Decision Engine")
print("=" * 40)

identity = RepositoryIdentity(

    repository="graphify",

    identity="Autonomous Engineering Brain",

    engineering_type="Engineering AI",

    confidence=0.99,

    capabilities=[

        "Knowledge",

        "Memory",

        "Decision",

    ],

)

mission = RepositoryMissionEngine().build(identity)

goals = RepositoryGoalEngine().build(mission)

understanding = RepositoryUnderstandingEngine().build_understanding(

    repository="graphify",

    identity=identity,

    mission=mission,

    goals=goals,

)

insight = RepositoryInsightEngine().build(

    understanding

)

reasoning = RepositoryCognitiveReasoningEngine().build(

    insight

)

decision = RepositoryDecisionEngine().build(

    reasoning

)

print("\nDecision Summary\n")

pprint(

    decision.summary()

)

print("\nDecision Object\n")

pprint(

    vars(decision)

)

print("\nEngine Status\n")

pprint(

    RepositoryDecisionEngine().status()

)