from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class LifecycleEventView(AdditionalDataHolder, Parsable):
    """
    One durably-persisted lifecycle event, across every profile in the cluster.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The event_id property
    event_id: Optional[UUID] = None
    # The generation property
    generation: Optional[int] = None
    # Lifecycle kind, e.g. model.ready, route.published, route.withdrawn.
    kind: Optional[str] = None
    # The occurred_at property
    occurred_at: Optional[datetime.datetime] = None
    # The profile the event belongs to, when known. Null for cluster-wide eventsand for rows written before the column existed.
    profile_id: Optional[str] = None
    # The sequence property
    sequence: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LifecycleEventView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LifecycleEventView
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LifecycleEventView()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "event_id": lambda n : setattr(self, 'event_id', n.get_uuid_value()),
            "generation": lambda n : setattr(self, 'generation', n.get_int_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_str_value()),
            "occurred_at": lambda n : setattr(self, 'occurred_at', n.get_datetime_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "sequence": lambda n : setattr(self, 'sequence', n.get_int_value()),
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
        writer.write_uuid_value("event_id", self.event_id)
        writer.write_int_value("generation", self.generation)
        writer.write_str_value("kind", self.kind)
        writer.write_datetime_value("occurred_at", self.occurred_at)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_int_value("sequence", self.sequence)
        writer.write_additional_data_value(self.additional_data)
    

