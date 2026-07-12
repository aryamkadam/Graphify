"""
Graphify

Phase 2

Stage P2.4

Worker Learning Engine

Allows workers to improve after every
completed engineering task.

Author:
Graphify Core
"""


class WorkerLearning:

    VERSION = "P2.4"

    def __init__(self):

        self.learning_score = 0

        self.lessons = []

    # --------------------------------------------------

    def learn(

        self,

        lesson,

        score=5,

    ):

        self.lessons.append(lesson)

        self.learning_score += score

    # --------------------------------------------------

    def knowledge_level(self):

        if self.learning_score < 20:
            return "BEGINNER"

        if self.learning_score < 50:
            return "INTERMEDIATE"

        if self.learning_score < 100:
            return "ADVANCED"

        return "EXPERT"

    # --------------------------------------------------

    def profile(self):

        return {

            "learning_score": self.learning_score,

            "knowledge_level": self.knowledge_level(),

            "lessons": len(self.lessons),

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def history(self):

        return list(self.lessons)