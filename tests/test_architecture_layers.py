import sys
from pathlib import Path

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent
    )
)

from graph_builder.architecture_layers import (
    detect_architecture_layers
)

layers = detect_architecture_layers(
    "."
)

for layer, modules in layers.items():

    print()

    print(
        f"LAYER: {layer.upper()}"
    )

    for module in modules:

        print(
            f"  - {module}"
        )