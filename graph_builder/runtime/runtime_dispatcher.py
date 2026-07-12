"""
Graphify

Stage 23.2

Runtime Dispatcher

Routes RuntimeMessages between
Runtime Services.

The Dispatcher owns NO business logic.

Responsibilities

Receive Message
        ↓
Locate Target
        ↓
Deliver

Author:
Graphify Core
"""

from graph_builder.runtime.runtime_message import RuntimeMessage


class RuntimeDispatcher:

    VERSION = "23.2"

    def __init__(self):

        self._services = {}

    # ------------------------------------------

    def register(

        self,

        service,

    ):

        self._services[service.service_name] = service

    # ------------------------------------------

    def unregister(

        self,

        service_name,

    ):

        self._services.pop(

            service_name,

            None,

        )

    # ------------------------------------------

    def dispatch(

        self,

        message: RuntimeMessage,

    ):

        target = self._services.get(

            message.target,

        )

        if target is None:

            return {

                "status": "failed",

                "reason": "Target service not found",

                "target": message.target,

                "version": self.VERSION,

            }

        if not hasattr(

            target,

            "receive_message",

        ):

            return {

                "status": "failed",

                "reason": "Target cannot receive RuntimeMessages",

                "target": message.target,

                "version": self.VERSION,

            }

        target.receive_message(

            message,

        )

        return {

            "status": "success",

            "source": message.source,

            "target": message.target,

            "event": message.event,

            "version": self.VERSION,

        }

    # ------------------------------------------

    def status(self):

        return {

            "registered_services": len(

                self._services,

            ),

            "services": sorted(

                self._services.keys(),

            ),

            "version": self.VERSION,

        }