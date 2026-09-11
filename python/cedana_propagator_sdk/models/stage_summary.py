from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class StageSummary(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The count property
    count: Optional[int] = None
    # The operation property
    operation: Optional[str] = None
    # The p50_ns property
    p50_ns: Optional[float] = None
    # The p95_ns property
    p95_ns: Optional[float] = None
    # The stage property
    stage: Optional[str] = None
    # The total_ns property
    total_ns: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StageSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StageSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StageSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "operation": lambda n : setattr(self, 'operation', n.get_str_value()),
            "p50_ns": lambda n : setattr(self, 'p50_ns', n.get_float_value()),
            "p95_ns": lambda n : setattr(self, 'p95_ns', n.get_float_value()),
            "stage": lambda n : setattr(self, 'stage', n.get_str_value()),
            "total_ns": lambda n : setattr(self, 'total_ns', n.get_int_value()),
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
        writer.write_int_value("count", self.count)
        writer.write_str_value("operation", self.operation)
        writer.write_float_value("p50_ns", self.p50_ns)
        writer.write_float_value("p95_ns", self.p95_ns)
        writer.write_str_value("stage", self.stage)
        writer.write_int_value("total_ns", self.total_ns)
        writer.write_additional_data_value(self.additional_data)
    

