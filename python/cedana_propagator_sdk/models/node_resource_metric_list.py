from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .node_metric_item import NodeMetricItem

@dataclass
class NodeResourceMetricList(AdditionalDataHolder, Parsable):
    """
    New structured event state
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The details property
    details: Optional[list[NodeMetricItem]] = None
    # The name property
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NodeResourceMetricList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NodeResourceMetricList
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NodeResourceMetricList()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .node_metric_item import NodeMetricItem

        from .node_metric_item import NodeMetricItem

        fields: dict[str, Callable[[Any], None]] = {
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(NodeMetricItem)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_collection_of_object_values("details", self.details)
        writer.write_str_value("name", self.name)
        writer.write_additional_data_value(self.additional_data)
    

