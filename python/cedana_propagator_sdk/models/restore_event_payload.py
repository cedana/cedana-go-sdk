from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RestoreEventPayload(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The action_id property
    action_id: Optional[str] = None
    # The action_ids property
    action_ids: Optional[list[str]] = None
    # The action_scope property
    action_scope: Optional[str] = None
    # The checkpoint_action_id property
    checkpoint_action_id: Optional[str] = None
    # The checkpoint_id property
    checkpoint_id: Optional[str] = None
    # The cluster_id property
    cluster_id: Optional[str] = None
    # The completed_at property
    completed_at: Optional[datetime.datetime] = None
    # The error_message property
    error_message: Optional[str] = None
    # The kind property
    kind: Optional[str] = None
    # The path_id property
    path_id: Optional[str] = None
    # The profile_available_on_error property
    profile_available_on_error: Optional[bool] = None
    # The profile_object_path property
    profile_object_path: Optional[str] = None
    # The reason property
    reason: Optional[str] = None
    # The restore_path property
    restore_path: Optional[str] = None
    # The restore_uuid property
    restore_uuid: Optional[str] = None
    # The started_at property
    started_at: Optional[datetime.datetime] = None
    # The status property
    status: Optional[str] = None
    # The storage_provider property
    storage_provider: Optional[str] = None
    # The workload_type property
    workload_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RestoreEventPayload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RestoreEventPayload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RestoreEventPayload()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "action_id": lambda n : setattr(self, 'action_id', n.get_str_value()),
            "action_ids": lambda n : setattr(self, 'action_ids', n.get_collection_of_primitive_values(str)),
            "action_scope": lambda n : setattr(self, 'action_scope', n.get_str_value()),
            "checkpoint_action_id": lambda n : setattr(self, 'checkpoint_action_id', n.get_str_value()),
            "checkpoint_id": lambda n : setattr(self, 'checkpoint_id', n.get_str_value()),
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_str_value()),
            "completed_at": lambda n : setattr(self, 'completed_at', n.get_datetime_value()),
            "error_message": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_str_value()),
            "path_id": lambda n : setattr(self, 'path_id', n.get_str_value()),
            "profile_available_on_error": lambda n : setattr(self, 'profile_available_on_error', n.get_bool_value()),
            "profile_object_path": lambda n : setattr(self, 'profile_object_path', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "restore_path": lambda n : setattr(self, 'restore_path', n.get_str_value()),
            "restore_uuid": lambda n : setattr(self, 'restore_uuid', n.get_str_value()),
            "started_at": lambda n : setattr(self, 'started_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "storage_provider": lambda n : setattr(self, 'storage_provider', n.get_str_value()),
            "workload_type": lambda n : setattr(self, 'workload_type', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("action_ids", self.action_ids)
        writer.write_str_value("action_scope", self.action_scope)
        writer.write_str_value("checkpoint_action_id", self.checkpoint_action_id)
        writer.write_str_value("checkpoint_id", self.checkpoint_id)
        writer.write_str_value("cluster_id", self.cluster_id)
        writer.write_datetime_value("completed_at", self.completed_at)
        writer.write_str_value("error_message", self.error_message)
        writer.write_str_value("kind", self.kind)
        writer.write_str_value("path_id", self.path_id)
        writer.write_bool_value("profile_available_on_error", self.profile_available_on_error)
        writer.write_str_value("profile_object_path", self.profile_object_path)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("restore_path", self.restore_path)
        writer.write_str_value("restore_uuid", self.restore_uuid)
        writer.write_datetime_value("started_at", self.started_at)
        writer.write_str_value("status", self.status)
        writer.write_str_value("storage_provider", self.storage_provider)
        writer.write_str_value("workload_type", self.workload_type)
        writer.write_additional_data_value(self.additional_data)
    

