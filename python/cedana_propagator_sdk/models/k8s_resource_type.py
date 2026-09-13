from enum import Enum

class K8sResource_type(str, Enum):
    None_ = "None",
    Pod = "Pod",
    Node = "Node",
    Job = "Job",
    DynamoGraphDeployment = "DynamoGraphDeployment",
    DynamoService = "DynamoService",

