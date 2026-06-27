from pprint import pprint

from graph_builder.knowledge_graph.entry_point_detector import (
    EntryPointDetector
)

detector = EntryPointDetector(".")

entries = detector.detect()

print()

print("Repository Entry Points")

print()

pprint(entries)

print()

print("Total Entry Points:", len(entries))