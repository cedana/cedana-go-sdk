from enum import Enum

class CheckpointOperationStatus(str, Enum):
    Initialized = "initialized",
    Processing = "processing",
    Checkpoint_created = "checkpoint_created",
    Ready = "ready",
    Error = "error",
    Not_found = "not_found",

