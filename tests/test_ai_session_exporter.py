from graph_builder.ai_session_exporter import (
    generate_ai_session_report
)

report = (
    generate_ai_session_report()
)

print(
    "\nAI Session Report Generated\n"
)

print(
    report
)