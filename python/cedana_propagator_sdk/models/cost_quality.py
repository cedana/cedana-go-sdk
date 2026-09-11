from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CostQuality(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The avg_ttft_ms property
    avg_ttft_ms: Optional[float] = None
    # The refusal_rate property
    refusal_rate: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostQuality:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostQuality
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CostQuality()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "avg_ttft_ms": lambda n : setattr(self, 'avg_ttft_ms', n.get_float_value()),
            "refusal_rate": lambda n : setattr(self, 'refusal_rate', n.get_float_value()),
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
        writer.write_float_value("avg_ttft_ms", self.avg_ttft_ms)
        writer.write_float_value("refusal_rate", self.refusal_rate)
        writer.write_additional_data_value(self.additional_data)
    

