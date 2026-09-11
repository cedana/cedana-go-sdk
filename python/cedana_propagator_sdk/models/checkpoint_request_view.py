from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class CheckpointRequestView(AdditionalDataHolder, Parsable):
    """
    An on-demand checkpoint request and how far it has got.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The artifact the checkpoint produced, once it succeeded.
    artifact_id: Optional[str] = None
    # The completed_at property
    completed_at: Optional[datetime.datetime] = None
    # Why it failed, in the controller's words.
    error: Optional[str] = None
    # checkpoint or restart. One row per profile, so asking twice returns the open one.
    kind: Optional[str] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The reason property
    reason: Optional[str] = None
    # The replace_existing property
    replace_existing: Optional[bool] = None
    # Identifies this attempt. A caller polling with the id it was givencannot be shown a later request's outcome as though it were its own.
    request_id: Optional[UUID] = None
    # The requested_at property
    requested_at: Optional[datetime.datetime] = None
    # The started_at property
    started_at: Optional[datetime.datetime] = None
    # pending → running → succeeded | failed
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckpointRequestView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckpointRequestView
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckpointRequestView()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "artifact_id": lambda n : setattr(self, 'artifact_id', n.get_str_value()),
            "completed_at": lambda n : setattr(self, 'completed_at', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_str_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "replace_existing": lambda n : setattr(self, 'replace_existing', n.get_bool_value()),
            "request_id": lambda n : setattr(self, 'request_id', n.get_uuid_value()),
            "requested_at": lambda n : setattr(self, 'requested_at', n.get_datetime_value()),
            "started_at": lambda n : setattr(self, 'started_at', n.get_datetime_value()),
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
        writer.write_str_value("artifact_id", self.artifact_id)
        writer.write_datetime_value("completed_at", self.completed_at)
        writer.write_str_value("error", self.error)
        writer.write_str_value("kind", self.kind)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_str_value("reason", self.reason)
        writer.write_bool_value("replace_existing", self.replace_existing)
        writer.write_uuid_value("request_id", self.request_id)
        writer.write_datetime_value("requested_at", self.requested_at)
        writer.write_datetime_value("started_at", self.started_at)
        writer.write_str_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

