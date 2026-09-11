from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PolicyCheckpointInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The action_id property
    action_id: Optional[str] = None
    # The checkpoint_id property
    checkpoint_id: Optional[str] = None
    # The completed_at property
    completed_at: Optional[str] = None
    # The duration_ms property
    duration_ms: Optional[int] = None
    # The namespace property
    namespace: Optional[str] = None
    # The pod_name property
    pod_name: Optional[str] = None
    # The size_bytes property
    size_bytes: Optional[int] = None
    # The status property
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyCheckpointInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyCheckpointInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyCheckpointInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "action_id": lambda n : setattr(self, 'action_id', n.get_str_value()),
            "checkpoint_id": lambda n : setattr(self, 'checkpoint_id', n.get_str_value()),
            "completed_at": lambda n : setattr(self, 'completed_at', n.get_str_value()),
            "duration_ms": lambda n : setattr(self, 'duration_ms', n.get_int_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "pod_name": lambda n : setattr(self, 'pod_name', n.get_str_value()),
            "size_bytes": lambda n : setattr(self, 'size_bytes', n.get_int_value()),
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
        writer.write_str_value("action_id", self.action_id)
        writer.write_str_value("checkpoint_id", self.checkpoint_id)
        writer.write_str_value("completed_at", self.completed_at)
        writer.write_int_value("duration_ms", self.duration_ms)
        writer.write_str_value("namespace", self.namespace)
        writer.write_str_value("pod_name", self.pod_name)
        writer.write_int_value("size_bytes", self.size_bytes)
        writer.write_str_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

