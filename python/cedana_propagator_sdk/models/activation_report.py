from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ActivationReport(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The desired_state property
    desired_state: Optional[str] = None
    # The endpoint property
    endpoint: Optional[str] = None
    # The observed_generation property
    observed_generation: Optional[int] = None
    # The phase property
    phase: Optional[str] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The ready property
    ready: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ActivationReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActivationReport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ActivationReport()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "desired_state": lambda n : setattr(self, 'desired_state', n.get_str_value()),
            "endpoint": lambda n : setattr(self, 'endpoint', n.get_str_value()),
            "observed_generation": lambda n : setattr(self, 'observed_generation', n.get_int_value()),
            "phase": lambda n : setattr(self, 'phase', n.get_str_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "ready": lambda n : setattr(self, 'ready', n.get_bool_value()),
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
        writer.write_str_value("desired_state", self.desired_state)
        writer.write_str_value("endpoint", self.endpoint)
        writer.write_int_value("observed_generation", self.observed_generation)
        writer.write_str_value("phase", self.phase)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_bool_value("ready", self.ready)
        writer.write_additional_data_value(self.additional_data)
    

