from enum import Enum

class RestoreReason(str, Enum):
    NodeTermination = "nodeTermination",
    NodeUnschedulable = "nodeUnschedulable",
    Manual = "manual",

