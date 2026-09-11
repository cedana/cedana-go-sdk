from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class Observation(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The duration_ms property
    duration_ms: Optional[int] = None
    # The event_type property
    event_type: Optional[str] = None
    # The evidence property
    evidence: Optional[str] = None
    # The experiment_id property
    experiment_id: Optional[UUID] = None
    # The id property
    id: Optional[UUID] = None
    # The observation_key property
    observation_key: Optional[str] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The source property
    source: Optional[str] = None
    # The started_at property
    started_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Observation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Observation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Observation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "duration_ms": lambda n : setattr(self, 'duration_ms', n.get_int_value()),
            "event_type": lambda n : setattr(self, 'event_type', n.get_str_value()),
            "evidence": lambda n : setattr(self, 'evidence', n.get_str_value()),
            "experiment_id": lambda n : setattr(self, 'experiment_id', n.get_uuid_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "observation_key": lambda n : setattr(self, 'observation_key', n.get_str_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "started_at": lambda n : setattr(self, 'started_at', n.get_datetime_value()),
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
        writer.write_int_value("duration_ms", self.duration_ms)
        writer.write_str_value("event_type", self.event_type)
        writer.write_str_value("evidence", self.evidence)
        writer.write_uuid_value("experiment_id", self.experiment_id)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("observation_key", self.observation_key)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_str_value("source", self.source)
        writer.write_datetime_value("started_at", self.started_at)
        writer.write_additional_data_value(self.additional_data)
    

