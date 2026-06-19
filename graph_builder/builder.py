def build_graph(parsed_data):

    nodes = []
    edges = []

    for func in parsed_data["functions"]:

        nodes.append(
            {
                "id": func["name"],
                "type": "function",
                "line": func["line"]
            }
        )

    for cls in parsed_data["classes"]:

        nodes.append(
            {
                "id": cls["name"],
                "type": "class",
                "line": cls["line"]
            }
        )

    for imp in parsed_data["imports"]:

        nodes.append(
            {
                "id": imp,
                "type": "module"
            }
        )

    for call in parsed_data["calls"]:

        edges.append(
            {
                "source": call["caller"],
                "target": call["callee"],
                "type": "CALLS"
            }
        )

    return {
        "nodes": nodes,
        "edges": edges
    }