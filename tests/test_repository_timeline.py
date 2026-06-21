from graph_builder.timeline_exporter import (
    export_repository_timeline
)

timeline = (
    export_repository_timeline(
        "graphify-out/repository_timeline.md"
    )
)

print()
print(
    "Repository Timeline Generated"
)
print()

print(
    timeline
)