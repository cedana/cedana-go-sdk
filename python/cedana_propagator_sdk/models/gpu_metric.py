from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class GpuMetric(AdditionalDataHolder, Parsable):
    """
    GPU metrics for a single GPU
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The gpu_index property
    gpu_index: Optional[str] = None
    # GPU utilization percentage (0-100)
    gpu_utilization: Optional[float] = None
    # The gpu_uuid property
    gpu_uuid: Optional[str] = None
    # Framebuffer memory free in MiB
    memory_free_mib: Optional[float] = None
    # Framebuffer memory used in MiB
    memory_used_mib: Optional[float] = None
    # Memory bandwidth utilization percentage (0-100)
    memory_utilization: Optional[float] = None
    # GPU model name (e.g., "NVIDIA H100 80GB HBM3")
    model_name: Optional[str] = None
    # Namespace of the pod (if any)
    namespace: Optional[str] = None
    # The node_name property
    node_name: Optional[str] = None
    # Pod currently using this GPU (if any)
    pod_name: Optional[str] = None
    # Power usage in Watts
    power_watts: Optional[float] = None
    # GPU temperature in Celsius
    temperature_celsius: Optional[float] = None
    # The timestamp property
    timestamp: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GpuMetric:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GpuMetric
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GpuMetric()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "gpu_index": lambda n : setattr(self, 'gpu_index', n.get_str_value()),
            "gpu_utilization": lambda n : setattr(self, 'gpu_utilization', n.get_float_value()),
            "gpu_uuid": lambda n : setattr(self, 'gpu_uuid', n.get_str_value()),
            "memory_free_mib": lambda n : setattr(self, 'memory_free_mib', n.get_float_value()),
            "memory_used_mib": lambda n : setattr(self, 'memory_used_mib', n.get_float_value()),
            "memory_utilization": lambda n : setattr(self, 'memory_utilization', n.get_float_value()),
            "model_name": lambda n : setattr(self, 'model_name', n.get_str_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "node_name": lambda n : setattr(self, 'node_name', n.get_str_value()),
            "pod_name": lambda n : setattr(self, 'pod_name', n.get_str_value()),
            "power_watts": lambda n : setattr(self, 'power_watts', n.get_float_value()),
            "temperature_celsius": lambda n : setattr(self, 'temperature_celsius', n.get_float_value()),
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
        writer.write_str_value("gpu_index", self.gpu_index)
        writer.write_float_value("gpu_utilization", self.gpu_utilization)
        writer.write_str_value("gpu_uuid", self.gpu_uuid)
        writer.write_float_value("memory_free_mib", self.memory_free_mib)
        writer.write_float_value("memory_used_mib", self.memory_used_mib)
        writer.write_float_value("memory_utilization", self.memory_utilization)
        writer.write_str_value("model_name", self.model_name)
        writer.write_str_value("namespace", self.namespace)
        writer.write_str_value("node_name", self.node_name)
        writer.write_str_value("pod_name", self.pod_name)
        writer.write_float_value("power_watts", self.power_watts)
        writer.write_float_value("temperature_celsius", self.temperature_celsius)
        writer.write_str_value("timestamp", self.timestamp)
        writer.write_additional_data_value(self.additional_data)
    

