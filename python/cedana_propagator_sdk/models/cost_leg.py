from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CostLeg(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cost_usd property
    cost_usd: Optional[float] = None
    # The heavy_activation_count property
    heavy_activation_count: Optional[int] = None
    # The heavy_active_duration_s property
    heavy_active_duration_s: Optional[float] = None
    # The node_seconds property
    node_seconds: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostLeg:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostLeg
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CostLeg()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "cost_usd": lambda n : setattr(self, 'cost_usd', n.get_float_value()),
            "heavy_activation_count": lambda n : setattr(self, 'heavy_activation_count', n.get_int_value()),
            "heavy_active_duration_s": lambda n : setattr(self, 'heavy_active_duration_s', n.get_float_value()),
            "node_seconds": lambda n : setattr(self, 'node_seconds', n.get_float_value()),
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
        writer.write_float_value("cost_usd", self.cost_usd)
        writer.write_int_value("heavy_activation_count", self.heavy_activation_count)
        writer.write_float_value("heavy_active_duration_s", self.heavy_active_duration_s)
        writer.write_float_value("node_seconds", self.node_seconds)
        writer.write_additional_data_value(self.additional_data)
    

