from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SetProfileState(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The deadline_ms property
    deadline_ms: Optional[int] = None
    # The desired_replicas property
    desired_replicas: Optional[int] = None
    # The desired_state property
    desired_state: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SetProfileState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SetProfileState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SetProfileState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "deadline_ms": lambda n : setattr(self, 'deadline_ms', n.get_int_value()),
            "desired_replicas": lambda n : setattr(self, 'desired_replicas', n.get_int_value()),
            "desired_state": lambda n : setattr(self, 'desired_state', n.get_str_value()),
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
        writer.write_int_value("deadline_ms", self.deadline_ms)
        writer.write_int_value("desired_replicas", self.desired_replicas)
        writer.write_str_value("desired_state", self.desired_state)
        writer.write_additional_data_value(self.additional_data)
    

