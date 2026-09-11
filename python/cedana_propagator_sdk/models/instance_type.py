from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .instance_type_availability import InstanceTypeAvailability
    from .instance_type_boot_time import InstanceTypeBootTime
    from .instance_type_configuration import InstanceTypeConfiguration

@dataclass
class InstanceType(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The availability property
    availability: Optional[list[InstanceTypeAvailability]] = None
    # The boot_time property
    boot_time: Optional[InstanceTypeBootTime] = None
    # The cloud property
    cloud: Optional[str] = None
    # The cloud_instance_type property
    cloud_instance_type: Optional[str] = None
    # The configuration property
    configuration: Optional[InstanceTypeConfiguration] = None
    # The deployment_type property
    deployment_type: Optional[str] = None
    # The hourly_price property
    hourly_price: Optional[int] = None
    # The shade_instance_type property
    shade_instance_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InstanceType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InstanceType
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InstanceType()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .instance_type_availability import InstanceTypeAvailability
        from .instance_type_boot_time import InstanceTypeBootTime
        from .instance_type_configuration import InstanceTypeConfiguration

        from .instance_type_availability import InstanceTypeAvailability
        from .instance_type_boot_time import InstanceTypeBootTime
        from .instance_type_configuration import InstanceTypeConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "availability": lambda n : setattr(self, 'availability', n.get_collection_of_object_values(InstanceTypeAvailability)),
            "boot_time": lambda n : setattr(self, 'boot_time', n.get_object_value(InstanceTypeBootTime)),
            "cloud": lambda n : setattr(self, 'cloud', n.get_str_value()),
            "cloud_instance_type": lambda n : setattr(self, 'cloud_instance_type', n.get_str_value()),
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(InstanceTypeConfiguration)),
            "deployment_type": lambda n : setattr(self, 'deployment_type', n.get_str_value()),
            "hourly_price": lambda n : setattr(self, 'hourly_price', n.get_int_value()),
            "shade_instance_type": lambda n : setattr(self, 'shade_instance_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("availability", self.availability)
        writer.write_object_value("boot_time", self.boot_time)
        writer.write_str_value("cloud", self.cloud)
        writer.write_str_value("cloud_instance_type", self.cloud_instance_type)
        writer.write_object_value("configuration", self.configuration)
        writer.write_str_value("deployment_type", self.deployment_type)
        writer.write_int_value("hourly_price", self.hourly_price)
        writer.write_str_value("shade_instance_type", self.shade_instance_type)
        writer.write_additional_data_value(self.additional_data)
    

