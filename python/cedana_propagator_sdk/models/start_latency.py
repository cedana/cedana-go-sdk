from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class StartLatency(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The max_ms property
    max_ms: Optional[int] = None
    # The median_ms property
    median_ms: Optional[int] = None
    # The min_ms property
    min_ms: Optional[int] = None
    # The samples property
    samples: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StartLatency:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StartLatency
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StartLatency()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "max_ms": lambda n : setattr(self, 'max_ms', n.get_int_value()),
            "median_ms": lambda n : setattr(self, 'median_ms', n.get_int_value()),
            "min_ms": lambda n : setattr(self, 'min_ms', n.get_int_value()),
            "samples": lambda n : setattr(self, 'samples', n.get_int_value()),
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
        writer.write_int_value("max_ms", self.max_ms)
        writer.write_int_value("median_ms", self.median_ms)
        writer.write_int_value("min_ms", self.min_ms)
        writer.write_int_value("samples", self.samples)
        writer.write_additional_data_value(self.additional_data)
    

