from pprint import pprint

from graph_builder.repository.repository_knowledge import RepositoryKnowledge
from graph_builder.repository.repository_metrics_engine import RepositoryMetricsEngine
from graph_builder.repository.repository_evolution_engine import RepositoryEvolutionEngine
from graph_builder.repository.repository_learning_engine import RepositoryLearningEngine
from graph_builder.repository.repository_intelligence_engine import RepositoryIntelligenceEngine

from graph_builder.executive.executive_decision import ExecutiveDecision
from graph_builder.executive.executive_planning_engine import ExecutivePlanningEngine
from graph_builder.executive.engineering_task_generator import EngineeringTaskGenerator

from graph_builder.runtime.runtime_task_dispatcher import RuntimeTaskDispatcher
from graph_builder.runtime.runtime_worker_scheduler import RuntimeWorkerScheduler
from graph_builder.runtime.runtime_execution_engine import RuntimeExecutionEngine
from graph_builder.runtime.runtime_feedback_engine import RuntimeFeedbackEngine


print("\n========================================")
print("PHASE 10 AUTONOMOUS ENGINEERING LOOP")
print("========================================\n")

# ============================================================
# PHASE 9
# ============================================================

knowledge = RepositoryKnowledge(
    repository_name="Graphify",
    repository_path="E:/Projects/graphify",
)

knowledge.modules = [
    "runtime",
    "repository",
]

knowledge.files = [
    "main.py",
    "runtime.py",
    "repository.py",
    "executive.py",
]

knowledge.directories = [
    "graph_builder",
    "tests",
]

metrics = RepositoryMetricsEngine().analyze(knowledge)

evolution = RepositoryEvolutionEngine().evolve(metrics)

learning = RepositoryLearningEngine()

# give repository at least one historical learning record
learning.learn(evolution)

repository_report = RepositoryIntelligenceEngine().analyze(
    knowledge,
    metrics,
    evolution,
    learning,
)

# ============================================================
# PHASE 10
# ============================================================

decision = ExecutiveDecision(
    decision_type="START_ENGINEERING",
    objective=evolution["objective"],
    priority=evolution["priority"],
    reasoning=repository_report.executive_summary,
    actions=["Start engineering cycle"],
)

plan = ExecutivePlanningEngine().generate_plan(decision)

tasks = EngineeringTaskGenerator().generate(plan)

queue = RuntimeTaskDispatcher().dispatch(tasks)

schedule = RuntimeWorkerScheduler().schedule(queue)

task = schedule["ready_tasks"][0]

execution = RuntimeExecutionEngine().execute(task)

feedback = RuntimeFeedbackEngine().learn(execution)

status = {
    "Repository Intelligence": repository_report is not None,
    "Executive Decision": decision is not None,
    "Planning": plan is not None,
    "Task Generation": tasks is not None,
    "Dispatcher": queue is not None,
    "Scheduler": schedule is not None,
    "Execution": execution is not None,
    "Feedback": feedback is not None,
}

pprint(status)

print("\n----------------------------------------")
print("Overall Status :", "PASS" if all(status.values()) else "FAIL")
print("----------------------------------------")

print("\nRepository Intelligence Report\n")
pprint(repository_report.to_dict())

print("\nFeedback\n")
pprint(feedback)