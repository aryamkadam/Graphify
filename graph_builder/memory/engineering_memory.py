"""
Graphify

Stage 28.1

Engineering Memory

Indexed engineering experience storage.

Author:
Graphify Core
"""


class EngineeringMemory:

    VERSION = "28.1"

    def __init__(self):

        self._history = []

        self._title_index = {}

        self._status_index = {}

        self._worker_index = {}

    # --------------------------------------------------

    def remember(

        self,

        review,

    ):

        self._history.append(review)

        task = review["task"]

        title = task["title"]

        status = task["status"]

        workers = [

            step["worker"]

            for step in review["history"]

        ]

        # ------------------------------
        # Title Index
        # ------------------------------

        self._title_index.setdefault(

            title,

            [],

        ).append(review)

        # ------------------------------
        # Status Index
        # ------------------------------

        self._status_index.setdefault(

            status,

            [],

        ).append(review)

        # ------------------------------
        # Worker Index
        # ------------------------------

        for worker in workers:

            self._worker_index.setdefault(

                worker,

                [],

            ).append(review)

        return {

            "status": "success",

            "stored": len(self._history),

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def history(self):

        return self._history

    # --------------------------------------------------

    def latest(self):

        if not self._history:

            return None

        return self._history[-1]

    # --------------------------------------------------

    def find_by_title(

        self,

        title,

    ):

        return self._title_index.get(

            title,

            [],

        )

    # --------------------------------------------------

    def find_by_status(

        self,

        status,

    ):

        return self._status_index.get(

            status,

            [],

        )

    # --------------------------------------------------

    def find_by_worker(

        self,

        worker,

    ):

        return self._worker_index.get(

            worker,

            [],

        )

    # --------------------------------------------------

    def status(self):

        return {

            "entries": len(self._history),

            "titles": len(self._title_index),

            "statuses": len(self._status_index),

            "workers": len(self._worker_index),

            "version": self.VERSION,

        }