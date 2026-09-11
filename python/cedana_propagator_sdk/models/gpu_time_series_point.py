from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class GpuTimeSeriesPoint(AdditionalDataHolder, Parsable):
    """
    Time-series data point for GPU metrics
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The gpu_utilization property
    gpu_utilization: Optional[float] = None
    # The memory_free_mib property
    memory_free_mib: Optional[float] = None
    # The memory_used_mib property
    memory_used_mib: Optional[float] = None
    # The memory_utilization property
    memory_utilization: Optional[float] = None
    # The namespace property
    namespace: Optional[str] = None
    # The pod_name property
    pod_name: Optional[str] = None
    # The timestamp property
    timestamp: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GpuTimeSeriesPoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GpuTimeSeriesPoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GpuTimeSeriesPoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "gpu_utilization": lambda n : setattr(self, 'gpu_utilization', n.get_float_value()),
            "memory_free_mib": lambda n : setattr(self, 'memory_free_mib', n.get_float_value()),
            "memory_used_mib": lambda n : setattr(self, 'memory_used_mib', n.get_float_value()),
            "memory_utilization": lambda n : setattr(self, 'memory_utilization', n.get_float_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "pod_name": lambda n : setattr(self, 'pod_name', n.get_str_value()),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_str_value()),
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
        writer.write_float_value("gpu_utilization", self.gpu_utilization)
        writer.write_float_value("memory_free_mib", self.memory_free_mib)
        writer.write_float_value("memory_used_mib", self.memory_used_mib)
        writer.write_float_value("memory_utilization", self.memory_utilization)
        writer.write_str_value("namespace", self.namespace)
        writer.write_str_value("pod_name", self.pod_name)
        writer.write_str_value("timestamp", self.timestamp)
        writer.write_additional_data_value(self.additional_data)
    

