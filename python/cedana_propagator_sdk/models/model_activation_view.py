from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ModelActivationView(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The activation_started_at property
    activation_started_at: Optional[datetime.datetime] = None
    # The compatibility_key property
    compatibility_key: Optional[str] = None
    # The desired_state property
    desired_state: Optional[str] = None
    # The endpoint property
    endpoint: Optional[str] = None
    # The estimated_cold_start_ms property
    estimated_cold_start_ms: Optional[int] = None
    # The exact_model property
    exact_model: Optional[str] = None
    # The hosting_mode property
    hosting_mode: Optional[str] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # The observed_generation property
    observed_generation: Optional[int] = None
    # The phase property
    phase: Optional[str] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The profile_revision property
    profile_revision: Optional[str] = None
    # The ready property
    ready: Optional[bool] = None
    # The ready_at property
    ready_at: Optional[datetime.datetime] = None
    # The updated_at property
    updated_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ModelActivationView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModelActivationView
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ModelActivationView()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "activation_started_at": lambda n : setattr(self, 'activation_started_at', n.get_datetime_value()),
            "compatibility_key": lambda n : setattr(self, 'compatibility_key', n.get_str_value()),
            "desired_state": lambda n : setattr(self, 'desired_state', n.get_str_value()),
            "endpoint": lambda n : setattr(self, 'endpoint', n.get_str_value()),
            "estimated_cold_start_ms": lambda n : setattr(self, 'estimated_cold_start_ms', n.get_int_value()),
            "exact_model": lambda n : setattr(self, 'exact_model', n.get_str_value()),
            "hosting_mode": lambda n : setattr(self, 'hosting_mode', n.get_str_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "observed_generation": lambda n : setattr(self, 'observed_generation', n.get_int_value()),
            "phase": lambda n : setattr(self, 'phase', n.get_str_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "profile_revision": lambda n : setattr(self, 'profile_revision', n.get_str_value()),
            "ready": lambda n : setattr(self, 'ready', n.get_bool_value()),
            "ready_at": lambda n : setattr(self, 'ready_at', n.get_datetime_value()),
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
        writer.write_datetime_value("activation_started_at", self.activation_started_at)
        writer.write_str_value("compatibility_key", self.compatibility_key)
        writer.write_str_value("desired_state", self.desired_state)
        writer.write_str_value("endpoint", self.endpoint)
        writer.write_int_value("estimated_cold_start_ms", self.estimated_cold_start_ms)
        writer.write_str_value("exact_model", self.exact_model)
        writer.write_str_value("hosting_mode", self.hosting_mode)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_int_value("observed_generation", self.observed_generation)
        writer.write_str_value("phase", self.phase)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_str_value("profile_revision", self.profile_revision)
        writer.write_bool_value("ready", self.ready)
        writer.write_datetime_value("ready_at", self.ready_at)
        writer.write_datetime_value("updated_at", self.updated_at)
        writer.write_additional_data_value(self.additional_data)
    

