from enum import Enum

class BurstingConfigStatus(str, Enum):
    Not_configured = "not_configured",
    Configured = "configured",
    Invalid = "invalid",

