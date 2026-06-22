from collections import Counter

from graph_builder.ai_session_history import (
    load_ai_sessions
)


def generate_ai_session_memory():

    sessions = (
        load_ai_sessions()
    )

    topics = []

    for session in sessions:

        topics.append(
            session["title"]
        )

    topic_counter = Counter(
        topics
    )

    major_topics = []

    for topic, _ in topic_counter.most_common(5):

        major_topics.append(
            topic
        )

    latest_focus = None

    if sessions:

        latest_focus = (
            sessions[-1]["title"]
        )

    memory = {

        "total_sessions":
            len(sessions),

        "major_topics":
            major_topics,

        "latest_focus":
            latest_focus
    }

    return memory