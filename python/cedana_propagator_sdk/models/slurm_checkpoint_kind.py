from enum import Enum

class SlurmCheckpointKind(str, Enum):
    Simple = "simple",
    Rootfs = "rootfs",
    Rootfsonly = "rootfsonly",

