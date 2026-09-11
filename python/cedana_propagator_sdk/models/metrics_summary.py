from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MetricsSummary(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The average_backend_latency_ms property
    average_backend_latency_ms: Optional[float] = None
    # The average_routing_latency_ms property
    average_routing_latency_ms: Optional[float] = None
    # The estimated_cold_start_avoided_ms property
    estimated_cold_start_avoided_ms: Optional[int] = None
    # The fallbacks property
    fallbacks: Optional[int] = None
    # The requests property
    requests: Optional[int] = None
    # The successful_requests property
    successful_requests: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MetricsSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MetricsSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MetricsSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "average_backend_latency_ms": lambda n : setattr(self, 'average_backend_latency_ms', n.get_float_value()),
            "average_routing_latency_ms": lambda n : setattr(self, 'average_routing_latency_ms', n.get_float_value()),
            "estimated_cold_start_avoided_ms": lambda n : setattr(self, 'estimated_cold_start_avoided_ms', n.get_int_value()),
            "fallbacks": lambda n : setattr(self, 'fallbacks', n.get_int_value()),
            "requests": lambda n : setattr(self, 'requests', n.get_int_value()),
            "successful_requests": lambda n : setattr(self, 'successful_requests', n.get_int_value()),
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
        writer.write_float_value("average_backend_latency_ms", self.average_backend_latency_ms)
        writer.write_float_value("average_routing_latency_ms", self.average_routing_latency_ms)
        writer.write_int_value("estimated_cold_start_avoided_ms", self.estimated_cold_start_avoided_ms)
        writer.write_int_value("fallbacks", self.fallbacks)
        writer.write_int_value("requests", self.requests)
        writer.write_int_value("successful_requests", self.successful_requests)
        writer.write_additional_data_value(self.additional_data)
    

