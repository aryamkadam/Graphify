from graph_builder.query_intent import (
    detect_query_intent
)

queries = [
    "Which function is most critical?",
    "Show dead code",
    "Show risky symbols",
    "Show repository hotspots",
    "What happens if parse_python_file changes?",
    "Find hashing functions"
]

for query in queries:

    print(
        query,
        "->",
        detect_query_intent(
            query
        )
    )