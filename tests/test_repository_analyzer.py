from graph_builder.engine import GraphifyEngine

engine = GraphifyEngine()

result = engine.analyze_repository(".")

print("\nRepository Analysis\n")

print(result)