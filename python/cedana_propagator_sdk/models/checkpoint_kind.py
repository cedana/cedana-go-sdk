from enum import Enum

class CheckpointKind(str, Enum):
    Simple = "simple",
    Rootfs = "rootfs",
    Rootfsonly = "rootfsonly",

