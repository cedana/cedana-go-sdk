from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .histogram_bucket import HistogramBucket

@dataclass
class OperationTotals(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The attempts property
    attempts: Optional[int] = None
    # The bytes_total property
    bytes_total: Optional[int] = None
    # The duration_buckets property
    duration_buckets: Optional[list[HistogramBucket]] = None
    # The failed property
    failed: Optional[int] = None
    # The fallbacks property
    fallbacks: Optional[int] = None
    # The operation property
    operation: Optional[str] = None
    # The p50_ns property
    p50_ns: Optional[float] = None
    # The p95_ns property
    p95_ns: Optional[float] = None
    # Checkpoints: pause percentiles over attempts with a pause recorded (0 otherwise).
    pause_p50_ns: Optional[float] = None
    # The pause_p95_ns property
    pause_p95_ns: Optional[float] = None
    # The succeeded property
    succeeded: Optional[int] = None
    # The to_ready_count property
    to_ready_count: Optional[int] = None
    # Restores: PodScheduled→Ready percentiles over attempts whose pod reached Ready (0 otherwise).
    to_ready_p50_ns: Optional[float] = None
    # The to_ready_p95_ns property
    to_ready_p95_ns: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OperationTotals:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OperationTotals
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OperationTotals()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .histogram_bucket import HistogramBucket

        from .histogram_bucket import HistogramBucket

        fields: dict[str, Callable[[Any], None]] = {
            "attempts": lambda n : setattr(self, 'attempts', n.get_int_value()),
            "bytes_total": lambda n : setattr(self, 'bytes_total', n.get_int_value()),
            "duration_buckets": lambda n : setattr(self, 'duration_buckets', n.get_collection_of_object_values(HistogramBucket)),
            "failed": lambda n : setattr(self, 'failed', n.get_int_value()),
            "fallbacks": lambda n : setattr(self, 'fallbacks', n.get_int_value()),
            "operation": lambda n : setattr(self, 'operation', n.get_str_value()),
            "p50_ns": lambda n : setattr(self, 'p50_ns', n.get_float_value()),
            "p95_ns": lambda n : setattr(self, 'p95_ns', n.get_float_value()),
            "pause_p50_ns": lambda n : setattr(self, 'pause_p50_ns', n.get_float_value()),
            "pause_p95_ns": lambda n : setattr(self, 'pause_p95_ns', n.get_float_value()),
            "succeeded": lambda n : setattr(self, 'succeeded', n.get_int_value()),
            "to_ready_count": lambda n : setattr(self, 'to_ready_count', n.get_int_value()),
            "to_ready_p50_ns": lambda n : setattr(self, 'to_ready_p50_ns', n.get_float_value()),
            "to_ready_p95_ns": lambda n : setattr(self, 'to_ready_p95_ns', n.get_float_value()),
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
        writer.write_collection_of_object_values("duration_buckets", self.duration_buckets)
        writer.write_int_value("failed", self.failed)
        writer.write_int_value("fallbacks", self.fallbacks)
        writer.write_str_value("operation", self.operation)
        writer.write_float_value("p50_ns", self.p50_ns)
        writer.write_float_value("p95_ns", self.p95_ns)
        writer.write_float_value("pause_p50_ns", self.pause_p50_ns)
        writer.write_float_value("pause_p95_ns", self.pause_p95_ns)
        writer.write_int_value("succeeded", self.succeeded)
        writer.write_int_value("to_ready_count", self.to_ready_count)
        writer.write_float_value("to_ready_p50_ns", self.to_ready_p50_ns)
        writer.write_float_value("to_ready_p95_ns", self.to_ready_p95_ns)
        writer.write_additional_data_value(self.additional_data)
    

