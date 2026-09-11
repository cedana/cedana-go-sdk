from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AutoRestorePolicyInfo(AdditionalDataHolder, Parsable):
    """
    Auto-restore policy info - represents pods/jobs with CEDANA_CHECKPOINT env var
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The CEDANA_CHECKPOINT value (checkpoint name)
    checkpoint_id: Optional[str] = None
    # Cluster ID
    cluster_id: Optional[str] = None
    # When the resource was created
    created_at: Optional[str] = None
    # Virtual ID based on the job/pod ID
    id: Optional[str] = None
    # The job or pod name
    name: Optional[str] = None
    # Namespace of the resource
    namespace: Optional[str] = None
    # Number of pods (1 for pods, count for jobs)
    pod_count: Optional[int] = None
    # Mapped policy status: "active", "completed", or "disabled"
    policy_status: Optional[str] = None
    # Type of resource: "job" or "pod"
    resource_type: Optional[str] = None
    # Original job/pod status
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutoRestorePolicyInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutoRestorePolicyInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutoRestorePolicyInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "checkpoint_id": lambda n : setattr(self, 'checkpoint_id', n.get_str_value()),
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_str_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "pod_count": lambda n : setattr(self, 'pod_count', n.get_int_value()),
            "policy_status": lambda n : setattr(self, 'policy_status', n.get_str_value()),
            "resource_type": lambda n : setattr(self, 'resource_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("checkpoint_id", self.checkpoint_id)
        writer.write_str_value("cluster_id", self.cluster_id)
        writer.write_str_value("created_at", self.created_at)
        writer.write_str_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("namespace", self.namespace)
        writer.write_int_value("pod_count", self.pod_count)
        writer.write_str_value("policy_status", self.policy_status)
        writer.write_str_value("resource_type", self.resource_type)
        writer.write_str_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

