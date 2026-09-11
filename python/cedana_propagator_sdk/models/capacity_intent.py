from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class CapacityIntent(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # When this intent row was first created. Not when the request it currentlydescribes was made: the row is reused for a repeated ask. Use requested_at for that.
    created_at: Optional[datetime.datetime] = None
    # The deadline property
    deadline: Optional[datetime.datetime] = None
    # The desired_replicas property
    desired_replicas: Optional[int] = None
    # The desired_state property
    desired_state: Optional[str] = None
    # The generation property
    generation: Optional[int] = None
    # The id property
    id: Optional[UUID] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # When a caller last asked for this exact state and replica count, so it ordersrequests as they were made rather than as the row happened to change.
    requested_at: Optional[datetime.datetime] = None
    # The status property
    status: Optional[str] = None
    # When this row last changed for any reason, including the expiry sweep. Not anordering key for what a caller asked for.
    updated_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CapacityIntent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CapacityIntent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CapacityIntent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "deadline": lambda n : setattr(self, 'deadline', n.get_datetime_value()),
            "desired_replicas": lambda n : setattr(self, 'desired_replicas', n.get_int_value()),
            "desired_state": lambda n : setattr(self, 'desired_state', n.get_str_value()),
            "generation": lambda n : setattr(self, 'generation', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "requested_at": lambda n : setattr(self, 'requested_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "updated_at": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
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
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_datetime_value("deadline", self.deadline)
        writer.write_int_value("desired_replicas", self.desired_replicas)
        writer.write_str_value("desired_state", self.desired_state)
        writer.write_int_value("generation", self.generation)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_datetime_value("requested_at", self.requested_at)
        writer.write_str_value("status", self.status)
        writer.write_datetime_value("updated_at", self.updated_at)
        writer.write_additional_data_value(self.additional_data)
    

