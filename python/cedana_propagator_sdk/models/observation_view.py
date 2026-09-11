from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class ObservationView(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The completion_tokens property
    completion_tokens: Optional[int] = None
    # The deadline_missed property
    deadline_missed: Optional[bool] = None
    # The duration_ms property
    duration_ms: Optional[int] = None
    # The event_type property
    event_type: Optional[str] = None
    # The evidence property
    evidence: Optional[str] = None
    # The experiment_id property
    experiment_id: Optional[UUID] = None
    # The fallback_used property
    fallback_used: Optional[bool] = None
    # The id property
    id: Optional[UUID] = None
    # The logical_bytes property
    logical_bytes: Optional[int] = None
    # The observation_key property
    observation_key: Optional[str] = None
    # The physical_bytes property
    physical_bytes: Optional[int] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The prompt_tokens property
    prompt_tokens: Optional[int] = None
    # The source property
    source: Optional[str] = None
    # The started_at property
    started_at: Optional[datetime.datetime] = None
    # The success property
    success: Optional[bool] = None
    # The ttft_ms property
    ttft_ms: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ObservationView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ObservationView
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ObservationView()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "completion_tokens": lambda n : setattr(self, 'completion_tokens', n.get_int_value()),
            "deadline_missed": lambda n : setattr(self, 'deadline_missed', n.get_bool_value()),
            "duration_ms": lambda n : setattr(self, 'duration_ms', n.get_int_value()),
            "event_type": lambda n : setattr(self, 'event_type', n.get_str_value()),
            "evidence": lambda n : setattr(self, 'evidence', n.get_str_value()),
            "experiment_id": lambda n : setattr(self, 'experiment_id', n.get_uuid_value()),
            "fallback_used": lambda n : setattr(self, 'fallback_used', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "logical_bytes": lambda n : setattr(self, 'logical_bytes', n.get_int_value()),
            "observation_key": lambda n : setattr(self, 'observation_key', n.get_str_value()),
            "physical_bytes": lambda n : setattr(self, 'physical_bytes', n.get_int_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "prompt_tokens": lambda n : setattr(self, 'prompt_tokens', n.get_int_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "started_at": lambda n : setattr(self, 'started_at', n.get_datetime_value()),
            "success": lambda n : setattr(self, 'success', n.get_bool_value()),
            "ttft_ms": lambda n : setattr(self, 'ttft_ms', n.get_int_value()),
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
        writer.write_int_value("completion_tokens", self.completion_tokens)
        writer.write_bool_value("deadline_missed", self.deadline_missed)
        writer.write_int_value("duration_ms", self.duration_ms)
        writer.write_str_value("event_type", self.event_type)
        writer.write_str_value("evidence", self.evidence)
        writer.write_uuid_value("experiment_id", self.experiment_id)
        writer.write_bool_value("fallback_used", self.fallback_used)
        writer.write_uuid_value("id", self.id)
        writer.write_int_value("logical_bytes", self.logical_bytes)
        writer.write_str_value("observation_key", self.observation_key)
        writer.write_int_value("physical_bytes", self.physical_bytes)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_int_value("prompt_tokens", self.prompt_tokens)
        writer.write_str_value("source", self.source)
        writer.write_datetime_value("started_at", self.started_at)
        writer.write_bool_value("success", self.success)
        writer.write_int_value("ttft_ms", self.ttft_ms)
        writer.write_additional_data_value(self.additional_data)
    

