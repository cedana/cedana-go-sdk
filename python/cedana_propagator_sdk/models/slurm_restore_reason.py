from enum import Enum

class SlurmRestoreReason(str, Enum):
    NodeTermination = "nodeTermination",
    NodeUnschedulable = "nodeUnschedulable",
    Manual = "manual",

