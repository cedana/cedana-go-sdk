from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class ActionDetails(AdditionalDataHolder, Parsable):
    """
    Action details response for a single action
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The action ID
    action_id: Optional[UUID] = None
    # When the action was created
    action_timestamp: Optional[datetime.datetime] = None
    # When checkpoint completed (if any)
    checkpoint_completed_timestamp: Optional[datetime.datetime] = None
    # Associated checkpoint ID (if any)
    checkpoint_id: Optional[UUID] = None
    # Checkpoint name/image
    checkpoint_name: Optional[str] = None
    # Checkpoint size in bytes
    checkpoint_size: Optional[int] = None
    # GPU type used
    gpu: Optional[str] = None
    # Node where the pod was running
    node_name: Optional[str] = None
    # Platform (e.g., containerd)
    platform: Optional[str] = None
    # Reason for the action (heartbeat, manual, nodeTermination, etc.)
    reason: Optional[str] = None
    # Restore path for the checkpoint
    restore_path: Optional[str] = None
    # Current status of the action
    status: Optional[str] = None
    # Checkpoint duration in nanoseconds (from profiling)
    total_duration: Optional[int] = None
    # Total I/O in bytes (from profiling)
    total_io: Optional[int] = None
    # Action type (checkpoint_pod, restore_pod, heartbeat)
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ActionDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActionDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ActionDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "action_id": lambda n : setattr(self, 'action_id', n.get_uuid_value()),
            "action_timestamp": lambda n : setattr(self, 'action_timestamp', n.get_datetime_value()),
            "checkpoint_completed_timestamp": lambda n : setattr(self, 'checkpoint_completed_timestamp', n.get_datetime_value()),
            "checkpoint_id": lambda n : setattr(self, 'checkpoint_id', n.get_uuid_value()),
            "checkpoint_name": lambda n : setattr(self, 'checkpoint_name', n.get_str_value()),
            "checkpoint_size": lambda n : setattr(self, 'checkpoint_size', n.get_int_value()),
            "gpu": lambda n : setattr(self, 'gpu', n.get_str_value()),
            "node_name": lambda n : setattr(self, 'node_name', n.get_str_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "restore_path": lambda n : setattr(self, 'restore_path', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "total_duration": lambda n : setattr(self, 'total_duration', n.get_int_value()),
            "total_io": lambda n : setattr(self, 'total_io', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_uuid_value("action_id", self.action_id)
        writer.write_datetime_value("action_timestamp", self.action_timestamp)
        writer.write_datetime_value("checkpoint_completed_timestamp", self.checkpoint_completed_timestamp)
        writer.write_uuid_value("checkpoint_id", self.checkpoint_id)
        writer.write_str_value("checkpoint_name", self.checkpoint_name)
        writer.write_int_value("checkpoint_size", self.checkpoint_size)
        writer.write_str_value("gpu", self.gpu)
        writer.write_str_value("node_name", self.node_name)
        writer.write_str_value("platform", self.platform)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("restore_path", self.restore_path)
        writer.write_str_value("status", self.status)
        writer.write_int_value("total_duration", self.total_duration)
        writer.write_int_value("total_io", self.total_io)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

