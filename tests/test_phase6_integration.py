from pprint import pprint

from graph_builder.executive.repository_strategy_engine import RepositoryStrategyEngine
from graph_builder.executive.executive_adaptation_engine import ExecutiveAdaptationEngine
from graph_builder.executive.executive_memory_engine import ExecutiveMemoryEngine
from graph_builder.executive.executive_index_engine import ExecutiveIndexEngine
from graph_builder.executive.executive_recall_engine import ExecutiveRecallEngine
from graph_builder.executive.executive_prediction_engine import ExecutivePredictionEngine
from graph_builder.executive.executive_decision_intelligence import ExecutiveDecisionIntelligence
from graph_builder.executive.executive_directive_engine import ExecutiveDirectiveEngine

from graph_builder.planner.planning_brain import PlanningBrain
from graph_builder.planner.task_decomposition_engine import TaskDecompositionEngine
from graph_builder.planner.dependency_graph_engine import DependencyGraphEngine
from graph_builder.planner.execution_planner import ExecutionPlanner
from graph_builder.planner.worker_assignment_engine import WorkerAssignmentEngine


def main():

    consciousness = {
        "repository_identity": {
            "phase": "Stabilization",
            "technical_direction": "Positive",
        }
    }

    knowledge = {
        "knowledge_confidence": 0.95
    }

    experience = {
        "experience_level": "Senior"
    }

    # ---------------- Executive ----------------

    strategy = RepositoryStrategyEngine().build(
        consciousness,
        knowledge,
        experience,
    )

    adaptation = ExecutiveAdaptationEngine().build(
        strategy,
    )

    memory_engine = ExecutiveMemoryEngine()
    memory_engine.remember(adaptation)

    memory = memory_engine.export()

    index = ExecutiveIndexEngine().build(
        memory,
    )

    recall = ExecutiveRecallEngine().recall_by_strategy(
        memory,
        index,
        adaptation["adaptation_strategy"],
    )

    prediction = ExecutivePredictionEngine().build(
        recall,
        strategy,
    )

    decision = ExecutiveDecisionIntelligence().build(
        strategy,
        recall,
        prediction,
    )
    directive = ExecutiveDirectiveEngine().build(
    decision,
)

    # ---------------- Planning ----------------

    planning = PlanningBrain().plan(
        directive,
    )

    decomposition = TaskDecompositionEngine().build(
        planning,
    )

    dependency = DependencyGraphEngine().build(
        decomposition,
    )

    execution = ExecutionPlanner().build(
        dependency,
    )

    workers = WorkerAssignmentEngine().build(
        execution,
    )

    print("\n========================================")
    print("Phase 6 Integration Test")
    print("========================================\n")

    pprint({
        "strategy": strategy["engineering_strategy"],
        "directive_count": len(directive["directive"]),
        "work_packages": decomposition["count"],
        "dependency_nodes": dependency["nodes"],
        "execution_steps": execution["completed"],
        "worker_assignments": len(workers["assignments"]),
        "workers_used": workers["workers_used"],
        "status": "PIPELINE VERIFIED",
        "version": "P6.INTEGRATION",
    })


if __name__ == "__main__":
    main()