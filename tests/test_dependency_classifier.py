from pprint import pprint

from graph_builder.knowledge_graph.import_parser import ImportParser
from graph_builder.knowledge_graph.dependency_resolver import DependencyResolver
from graph_builder.knowledge_graph.dependency_classifier import (
    DependencyClassifier
)

parser = ImportParser(".")

edges = parser.parse_imports()

resolver = DependencyResolver(".")

resolved = resolver.resolve(edges)

classifier = DependencyClassifier()

classified = classifier.classify(resolved)

print("\nDependency Classification\n")

pprint(classified[:40])

print()

internal = sum(
    e["category"] == "internal"
    for e in classified
)

stdlib = sum(
    e["category"] == "stdlib"
    for e in classified
)

third = sum(
    e["category"] == "third_party"
    for e in classified
)

unknown = sum(
    e["category"] == "unknown"
    for e in classified
)

print("Internal     :", internal)
print("Std Library  :", stdlib)
print("Third Party  :", third)
print("Unknown      :", unknown)