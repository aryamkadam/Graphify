"""
Graphify

Stage 22.0

Runtime Registry

Stores all Runtime Services registered
inside the Graphify Runtime.

Author:
Graphify Core
"""


class RuntimeRegistry:

    VERSION = "22.0"

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

    def get(self, service_name):

        return self._services.get(service_name)

    # ------------------------------------------

    def exists(self, service_name):

        return service_name in self._services

    # ------------------------------------------

    def count(self):

        return len(self._services)

    # ------------------------------------------

    def services(self):

        return sorted(self._services.keys())

    # ------------------------------------------

    def status(self):

        return {

            "version": self.VERSION,

            "registered_services": self.count(),

            "services": self.services(),

        }