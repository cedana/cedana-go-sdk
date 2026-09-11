from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class InstanceTypePricing(AdditionalDataHolder, Parsable):
    """
    Instance type pricing configuration
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # "spot" or "on-demand"
    capacity_type: Optional[str] = None
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The id property
    id: Optional[UUID] = None
    # The instance_type property
    instance_type: Optional[str] = None
    # Hourly cost when running as on-demand
    ondemand_price_per_hour: Optional[float] = None
    # Hourly cost when running as spot
    spot_price_per_hour: Optional[float] = None
    # The updated_at property
    updated_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InstanceTypePricing:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InstanceTypePricing
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InstanceTypePricing()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "capacity_type": lambda n : setattr(self, 'capacity_type', n.get_str_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "instance_type": lambda n : setattr(self, 'instance_type', n.get_str_value()),
            "ondemand_price_per_hour": lambda n : setattr(self, 'ondemand_price_per_hour', n.get_float_value()),
            "spot_price_per_hour": lambda n : setattr(self, 'spot_price_per_hour', n.get_float_value()),
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
        writer.write_str_value("capacity_type", self.capacity_type)
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("instance_type", self.instance_type)
        writer.write_float_value("ondemand_price_per_hour", self.ondemand_price_per_hour)
        writer.write_float_value("spot_price_per_hour", self.spot_price_per_hour)
        writer.write_datetime_value("updated_at", self.updated_at)
        writer.write_additional_data_value(self.additional_data)
    

