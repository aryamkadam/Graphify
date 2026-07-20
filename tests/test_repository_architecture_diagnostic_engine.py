from pprint import pprint

from graph_builder.repository.repository_architecture_diagnostic_engine import (
    RepositoryArchitectureDiagnosticEngine,
)

validation_report = {
    "repository": "graphify",
    "duplicate_responsibilities": [
        {
            "component": "repository_learning_engine",
            "occurrences": 3,
            "paths": [
                "learning/repository_learning_engine.py",
                "repository/repository_learning_engine.py",
                "intelligence/repository_learning_engine.py",
            ],
        }
    ],
    "oversized_layers": [
        {
            "layer": "Infrastructure",
            "components": 244,
        }
    ],
    "architecture_cycles": [],
}

engine = RepositoryArchitectureDiagnosticEngine()

report = engine.diagnose(validation_report)

print("\n========================================")
print("Repository Architecture Diagnostic Engine")
print("========================================\n")

print("Summary\n")
pprint(
    {
        "repository": report["repository"],
        "total_issues": report["total_issues"],
        "engineering_risk": report["engineering_risk"],
        "version": report["version"],
    }
)

print("\nDiagnostics\n")

for issue in report["diagnostics"]:
    pprint(issue)
    print("-" * 40)