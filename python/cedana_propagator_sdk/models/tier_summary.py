from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TierSummary(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The attempts property
    attempts: Optional[int] = None
    # The bytes_total property
    bytes_total: Optional[int] = None
    # The operation property
    operation: Optional[str] = None
    # The p50_ns property
    p50_ns: Optional[float] = None
    # The storage_tier property
    storage_tier: Optional[str] = None
    # The succeeded property
    succeeded: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TierSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TierSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TierSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "attempts": lambda n : setattr(self, 'attempts', n.get_int_value()),
            "bytes_total": lambda n : setattr(self, 'bytes_total', n.get_int_value()),
            "operation": lambda n : setattr(self, 'operation', n.get_str_value()),
            "p50_ns": lambda n : setattr(self, 'p50_ns', n.get_float_value()),
            "storage_tier": lambda n : setattr(self, 'storage_tier', n.get_str_value()),
            "succeeded": lambda n : setattr(self, 'succeeded', n.get_int_value()),
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
        writer.write_int_value("attempts", self.attempts)
        writer.write_int_value("bytes_total", self.bytes_total)
        writer.write_str_value("operation", self.operation)
        writer.write_float_value("p50_ns", self.p50_ns)
        writer.write_str_value("storage_tier", self.storage_tier)
        writer.write_int_value("succeeded", self.succeeded)
        writer.write_additional_data_value(self.additional_data)
    

