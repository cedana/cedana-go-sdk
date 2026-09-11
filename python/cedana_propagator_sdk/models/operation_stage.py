from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class OperationStage(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The bytes_in property
    bytes_in: Optional[int] = None
    # The bytes_out property
    bytes_out: Optional[int] = None
    # The duration_ns property
    duration_ns: Optional[int] = None
    # The reason property
    reason: Optional[str] = None
    # The result property
    result: Optional[str] = None
    # The seq property
    seq: Optional[int] = None
    # The stage property
    stage: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OperationStage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OperationStage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OperationStage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "bytes_in": lambda n : setattr(self, 'bytes_in', n.get_int_value()),
            "bytes_out": lambda n : setattr(self, 'bytes_out', n.get_int_value()),
            "duration_ns": lambda n : setattr(self, 'duration_ns', n.get_int_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "result": lambda n : setattr(self, 'result', n.get_str_value()),
            "seq": lambda n : setattr(self, 'seq', n.get_int_value()),
            "stage": lambda n : setattr(self, 'stage', n.get_str_value()),
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
        writer.write_int_value("bytes_in", self.bytes_in)
        writer.write_int_value("bytes_out", self.bytes_out)
        writer.write_int_value("duration_ns", self.duration_ns)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("result", self.result)
        writer.write_int_value("seq", self.seq)
        writer.write_str_value("stage", self.stage)
        writer.write_additional_data_value(self.additional_data)
    

