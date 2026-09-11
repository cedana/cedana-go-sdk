from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PartitionNodeCount(AdditionalDataHolder, Parsable):
    """
    Node count per state for a partition
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The count property
    count: Optional[float] = None
    # The partition_name property
    partition_name: Optional[str] = None
    # The state property
    state: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PartitionNodeCount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PartitionNodeCount
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PartitionNodeCount()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "count": lambda n : setattr(self, 'count', n.get_float_value()),
            "partition_name": lambda n : setattr(self, 'partition_name', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
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
        writer.write_float_value("count", self.count)
        writer.write_str_value("partition_name", self.partition_name)
        writer.write_str_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

