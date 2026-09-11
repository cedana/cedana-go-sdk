from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .state_item import StateItem

@dataclass
class SlurmStateBreakdown(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cpus_by_state property
    cpus_by_state: Optional[list[StateItem]] = None
    # The nodes_by_state property
    nodes_by_state: Optional[list[StateItem]] = None
    # The timestamp property
    timestamp: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SlurmStateBreakdown:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SlurmStateBreakdown
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SlurmStateBreakdown()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .state_item import StateItem

        from .state_item import StateItem

        fields: dict[str, Callable[[Any], None]] = {
            "cpus_by_state": lambda n : setattr(self, 'cpus_by_state', n.get_collection_of_object_values(StateItem)),
            "nodes_by_state": lambda n : setattr(self, 'nodes_by_state', n.get_collection_of_object_values(StateItem)),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_int_value()),
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
        writer.write_collection_of_object_values("cpus_by_state", self.cpus_by_state)
        writer.write_collection_of_object_values("nodes_by_state", self.nodes_by_state)
        writer.write_int_value("timestamp", self.timestamp)
        writer.write_additional_data_value(self.additional_data)
    

