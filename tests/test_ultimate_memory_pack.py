from graph_builder.ultimate_memory_pack_exporter import (
    export_ultimate_memory_pack
)

content = (
    export_ultimate_memory_pack()
)

print()
print(
    "Ultimate Memory Pack Generated"
)
print()

print(
    content[:3000]
)