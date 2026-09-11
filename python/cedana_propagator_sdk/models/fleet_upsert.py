from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class FleetUpsert(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The availability property
    availability: Optional[str] = None
    # The fleet_id property
    fleet_id: Optional[str] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The profile_ids property
    profile_ids: Optional[list[str]] = None
    # The residency property
    residency: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FleetUpsert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FleetUpsert
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FleetUpsert()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "availability": lambda n : setattr(self, 'availability', n.get_str_value()),
            "fleet_id": lambda n : setattr(self, 'fleet_id', n.get_str_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "profile_ids": lambda n : setattr(self, 'profile_ids', n.get_collection_of_primitive_values(str)),
            "residency": lambda n : setattr(self, 'residency', n.get_str_value()),
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
        writer.write_str_value("availability", self.availability)
        writer.write_str_value("fleet_id", self.fleet_id)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_primitive_values("profile_ids", self.profile_ids)
        writer.write_str_value("residency", self.residency)
        writer.write_additional_data_value(self.additional_data)
    

