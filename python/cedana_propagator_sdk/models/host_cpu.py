from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class HostCpu(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The Count property
    count: Optional[int] = None
    # The Family property
    family: Optional[str] = None
    # The PhysicalID property
    physical_i_d: Optional[str] = None
    # The VendorID property
    vendor_i_d: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HostCpu:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HostCpu
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HostCpu()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "Count": lambda n : setattr(self, 'count', n.get_int_value()),
            "Family": lambda n : setattr(self, 'family', n.get_str_value()),
            "PhysicalID": lambda n : setattr(self, 'physical_i_d', n.get_str_value()),
            "VendorID": lambda n : setattr(self, 'vendor_i_d', n.get_str_value()),
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
        writer.write_int_value("Count", self.count)
        writer.write_str_value("Family", self.family)
        writer.write_str_value("PhysicalID", self.physical_i_d)
        writer.write_str_value("VendorID", self.vendor_i_d)
        writer.write_additional_data_value(self.additional_data)
    

