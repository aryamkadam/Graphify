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


def check(condition):
    return "PASS" if condition else "FAIL"


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

    # ---------------- Executive Layer ----------------

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

    # ---------------- Planning Layer ----------------

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

    validation = {

        "Repository Strategy":
            check(strategy["engineering_strategy"] is not None),

        "Executive Adaptation":
            check(len(adaptation["executive_adaptations"]) > 0),

        "Executive Memory":
            check(memory["summary"]["executive_decisions"] > 0),

        "Executive Recall":
            check(recall["matches"] > 0),

        "Executive Prediction":
            check(prediction["confidence"] > 0),

        "Executive Decision":
            check(decision["executive_decision"] is not None),

        "Executive Directive":
            check(len(directive["directive"]) > 0),

        "Planning Brain":
            check(planning["planning_state"] == "PLANNING"),

        "Task Decomposition":
            check(decomposition["count"] > 0),

        "Dependency Graph":
            check(dependency["nodes"] == decomposition["count"]),

        "Execution Planner":
            check(execution["completed"] == decomposition["count"]),

        "Worker Assignment":
            check(len(workers["assignments"]) == decomposition["count"]),
    }

    passed = all(v == "PASS" for v in validation.values())

    print("\n========================================")
    print("GRAPHIFY CORE VALIDATION")
    print("========================================\n")

    pprint(validation)

    print("\n----------------------------------------")

    print(f"Overall Status : {'PASS' if passed else 'FAIL'}")

    print("Core Version   : P6.STABLE")

    print("----------------------------------------")

    print("\nPipeline Summary")

    pprint({

        "strategy": strategy["engineering_strategy"],

        "directive_count": len(directive["directive"]),

        "work_packages": decomposition["count"],

        "execution_steps": execution["completed"],

        "workers": workers["workers_used"],

    })


if __name__ == "__main__":
    main()