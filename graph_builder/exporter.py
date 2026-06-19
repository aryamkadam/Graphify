import json
from pathlib import Path


def export_graph(graph, output_dir):

    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    with open(
        output_dir / "graph.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            graph,
            f,
            indent=4
        )