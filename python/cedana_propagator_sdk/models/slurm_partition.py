from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class SlurmPartition(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The default_time property
    default_time: Optional[int] = None
    # The id property
    id: Optional[UUID] = None
    # The is_default property
    is_default: Optional[bool] = None
    # The max_time property
    max_time: Optional[int] = None
    # The name property
    name: Optional[str] = None
    # The nodes property
    nodes: Optional[str] = None
    # The priority_tier property
    priority_tier: Optional[int] = None
    # The state property
    state: Optional[str] = None
    # The total_cpus property
    total_cpus: Optional[int] = None
    # The total_nodes property
    total_nodes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SlurmPartition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SlurmPartition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SlurmPartition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "default_time": lambda n : setattr(self, 'default_time', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "max_time": lambda n : setattr(self, 'max_time', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "nodes": lambda n : setattr(self, 'nodes', n.get_str_value()),
            "priority_tier": lambda n : setattr(self, 'priority_tier', n.get_int_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "total_cpus": lambda n : setattr(self, 'total_cpus', n.get_int_value()),
            "total_nodes": lambda n : setattr(self, 'total_nodes', n.get_int_value()),
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
        writer.write_int_value("default_time", self.default_time)
        writer.write_uuid_value("id", self.id)
        writer.write_bool_value("is_default", self.is_default)
        writer.write_int_value("max_time", self.max_time)
        writer.write_str_value("name", self.name)
        writer.write_str_value("nodes", self.nodes)
        writer.write_int_value("priority_tier", self.priority_tier)
        writer.write_str_value("state", self.state)
        writer.write_int_value("total_cpus", self.total_cpus)
        writer.write_int_value("total_nodes", self.total_nodes)
        writer.write_additional_data_value(self.additional_data)
    

