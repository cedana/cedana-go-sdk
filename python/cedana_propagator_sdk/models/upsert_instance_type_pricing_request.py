from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class UpsertInstanceTypePricingRequest(AdditionalDataHolder, Parsable):
    """
    Request to create or update instance type pricing
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # "spot" or "on-demand"
    capacity_type: Optional[str] = None
    # The instance_type property
    instance_type: Optional[str] = None
    # Hourly cost when running as on-demand
    ondemand_price_per_hour: Optional[float] = None
    # Hourly cost when running as spot
    spot_price_per_hour: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpsertInstanceTypePricingRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpsertInstanceTypePricingRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpsertInstanceTypePricingRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "capacity_type": lambda n : setattr(self, 'capacity_type', n.get_str_value()),
            "instance_type": lambda n : setattr(self, 'instance_type', n.get_str_value()),
            "ondemand_price_per_hour": lambda n : setattr(self, 'ondemand_price_per_hour', n.get_float_value()),
            "spot_price_per_hour": lambda n : setattr(self, 'spot_price_per_hour', n.get_float_value()),
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
        writer.write_str_value("capacity_type", self.capacity_type)
        writer.write_str_value("instance_type", self.instance_type)
        writer.write_float_value("ondemand_price_per_hour", self.ondemand_price_per_hour)
        writer.write_float_value("spot_price_per_hour", self.spot_price_per_hour)
        writer.write_additional_data_value(self.additional_data)
    

