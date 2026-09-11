from enum import Enum

class Status(str, Enum):
    UNKNOWN = "UNKNOWN",
    AVAILABLE = "AVAILABLE",
    INSTALLED = "INSTALLED",
    OUTDATED = "OUTDATED",

