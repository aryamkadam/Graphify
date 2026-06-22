from graph_builder.ai_session_history import (
    load_ai_sessions
)


def generate_ai_session_report():

    sessions = (
        load_ai_sessions()
    )

    lines = []

    lines.append(
        "# AI Session Memory"
    )

    lines.append("")

    for index, session in enumerate(
        sessions,
        start=1
    ):

        lines.append(
            f"## Session {index}"
        )

        lines.append("")

        lines.append(
            f"Title: {session['title']}"
        )

        lines.append(
            f"Stage: {session['stage']}"
        )

        lines.append(
            f"Topic: {session['topic']}"
        )

        lines.append(
            f"Date: {session['timestamp']}"
        )

        lines.append("")

        lines.append(
            f"Summary: {session['summary']}"
        )

        lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(
        lines
    )