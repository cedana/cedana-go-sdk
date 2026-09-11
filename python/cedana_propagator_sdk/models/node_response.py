from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class NodeResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # "spot" or "on-demand" - detected from node labels
    capacity_type: Optional[str] = None
    # The cluster_name property
    cluster_name: Optional[str] = None
    # The compute_type property
    compute_type: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # The instance_type property
    instance_type: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The region property
    region: Optional[str] = None
    # The status property
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NodeResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NodeResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NodeResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "capacity_type": lambda n : setattr(self, 'capacity_type', n.get_str_value()),
            "cluster_name": lambda n : setattr(self, 'cluster_name', n.get_str_value()),
            "compute_type": lambda n : setattr(self, 'compute_type', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
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
        writer.write_str_value("capacity_type", self.capacity_type)
        writer.write_str_value("cluster_name", self.cluster_name)
        writer.write_str_value("compute_type", self.compute_type)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("instance_type", self.instance_type)
        writer.write_str_value("name", self.name)
        writer.write_str_value("region", self.region)
        writer.write_str_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

