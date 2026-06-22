def export_chatgpt_context(
    context
):

    repo = context[
        "repository_brain"
    ]

    return f"""
You are continuing work on Graphify.

Current Stage:
{repo['current_stage']}

Project Purpose:
{repo['project_purpose']}

Health Score:
{repo['health_score']}

Critical Symbols:
{repo['critical_symbols']}

Continue development from here.
"""