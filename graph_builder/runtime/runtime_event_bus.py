"""
Graphify

Stage 21.4

Runtime Event Bus

Central event communication system.

Author:
Graphify Core
"""


class RuntimeEventBus:

    VERSION = "21.4"

    def __init__(self):

        self._listeners = {}

    # ------------------------------------------

    def subscribe(self, event_name, callback):

        self._listeners.setdefault(event_name, [])

        self._listeners[event_name].append(callback)

    # ------------------------------------------

    def emit(self, event_name, payload=None):

        listeners = self._listeners.get(event_name, [])

        results = []

        for callback in listeners:

            results.append(callback(payload))

        return results

    # ------------------------------------------

    def listeners(self):

        return {

            event: len(callbacks)

            for event, callbacks in self._listeners.items()

        }