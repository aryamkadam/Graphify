from graph_builder.repository_summary import (
    generate_repository_summary
)

summary = generate_repository_summary(
    "."
)

print(summary)