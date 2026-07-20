from pprint import pprint

from graph_builder.intelligence.repository_responsibility_inference_engine import (
    RepositoryResponsibilityInferenceEngine,
)

print()
print("=" * 40)
print("Repository Responsibility Inference Engine")
print("=" * 40)
print()

engine = RepositoryResponsibilityInferenceEngine()

module = {

    "module_name": "repository_learning_engine",

}

symbols = [

    {

        "name": "learn",

    },

    {

        "name": "experience",

    },

    {

        "name": "feedback",

    },

]

relationships = [

    {

        "target": "engineering_memory",

    },

    {

        "target": "knowledge_graph",

    },

]

report = engine.infer(

    module,

    symbols,

    relationships,

)

print("Inference")
print()

pprint(report)