"""
Graphify

Stage 21.2

Runtime Service Manager

Responsible for managing every runtime service.

Author:
Graphify Core
"""


class RuntimeServiceManager:

    VERSION = "21.2"

    def __init__(self):

        self._services = {}

    # ------------------------------------------

    def register(self, service):

        self._services[service.service_name] = service

        return {
            "status": "success",
            "registered": service.service_name,
        }

    # ------------------------------------------

    def unregister(self, service_name):

        if service_name in self._services:

            del self._services[service_name]

            return {
                "status": "success",
                "removed": service_name,
            }

        return {
            "status": "failed",
            "reason": "Service not found",
        }

    # ------------------------------------------

    def get_service(self, service_name):

        return self._services.get(service_name)

    # ------------------------------------------

    def list_services(self):

        return list(self._services.keys())

    # ------------------------------------------

    def start_all(self):

        results = []

        for service in self._services.values():

            results.append(service.start())

        return results

    # ------------------------------------------

    def stop_all(self):

        results = []

        for service in self._services.values():

            results.append(service.stop())

        return results

    # ------------------------------------------

    def status(self):

        return {

            "version": self.VERSION,

            "registered_services": len(self._services),

            "services": self.list_services(),

        }