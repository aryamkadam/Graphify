from enum import Enum


class RuntimeState(Enum):
    OFFLINE = "OFFLINE"
    BOOTING = "BOOTING"
    ONLINE = "ONLINE"
    SYNCING = "SYNCING"
    SUSPENDED = "SUSPENDED"
    SHUTDOWN = "SHUTDOWN"