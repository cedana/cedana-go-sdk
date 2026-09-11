from enum import Enum

class CheckpointStatus(str, Enum):
    Initializing = "initializing",
    Updated_info = "updated_info",
    Possibly_uploaded = "possibly_uploaded",
    Ready = "ready",
    Deprecated = "deprecated",

