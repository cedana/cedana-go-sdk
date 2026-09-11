from enum import Enum

class SlurmCheckpointReason(str, Enum):
    Heartbeat = "heartbeat",
    Manual = "manual",
    Preemption = "preemption",

