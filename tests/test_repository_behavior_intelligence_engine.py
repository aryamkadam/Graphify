from pprint import pprint

from graph_builder.intelligence.repository_behavior_intelligence_engine import (
    RepositoryBehaviorIntelligenceEngine,
)

print()
print("=" * 40)
print("Repository Behavior Intelligence")
print("=" * 40)
print()

module = {

    "module_name": "repository_learning_engine",

}

symbols = [

    {

        "name": "learn",

        "symbol_type": "FUNCTION",

    },

    {

        "name": "record_experience",

        "symbol_type": "FUNCTION",

    },

    {

        "name": "feedback",

        "symbol_type": "FUNCTION",

    },

    {

        "name": "PythonASTParser",

        "symbol_type": "CLASS",

    },

]

engine = RepositoryBehaviorIntelligenceEngine()

report = engine.analyze(

    module,

    symbols,

)

print("Behavior")

print()

pprint(report)