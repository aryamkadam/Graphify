from datetime import datetime


def create_ai_session(
    title,
    topic,
    summary,
    stage
):

    session = {

        "session_id":
            datetime.now().strftime(
                "%Y%m%d%H%M%S"
            ),

        "timestamp":
            datetime.now().isoformat(),

        "title":
            title,

        "topic":
            topic,

        "summary":
            summary,

        "stage":
            stage
    }

    return session