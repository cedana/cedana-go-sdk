from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class InstanceInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cloud_provider property
    cloud_provider: Optional[str] = None
    # The created_at property
    created_at: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The instance_type property
    instance_type: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The region property
    region: Optional[str] = None
    # The status property
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InstanceInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InstanceInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InstanceInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "cloud_provider": lambda n : setattr(self, 'cloud_provider', n.get_str_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "instance_type": lambda n : setattr(self, 'instance_type', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_str_value("cloud_provider", self.cloud_provider)
        writer.write_str_value("created_at", self.created_at)
        writer.write_str_value("id", self.id)
        writer.write_str_value("instance_type", self.instance_type)
        writer.write_str_value("name", self.name)
        writer.write_str_value("region", self.region)
        writer.write_str_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

