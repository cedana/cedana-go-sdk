from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PodCheckpointCpu(AdditionalDataHolder, Parsable):
    """
    Per-pod checkpoint resource data for efficiency calculations
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Total number of checkpoints for this pod
    checkpoint_count: Optional[int] = None
    # Timestamp of the last checkpoint
    checkpoint_timestamp: Optional[str] = None
    # CPU usage (seconds) at the time of the last checkpointThis represents the work preserved by the checkpoint
    cpu_at_checkpoint: Optional[float] = None
    # GPU memory used (MiB) at checkpoint time, if GPU was used
    gpu_memory_used_mib: Optional[float] = None
    # GPU model name (e.g., "NVIDIA H100 80GB HBM3"), if GPU was used
    gpu_model: Optional[str] = None
    # GPU utilization at checkpoint time (percentage 0-100), if GPU was usedDerived from DCGM_FI_DEV_GPU_UTIL metric
    gpu_utilization_at_checkpoint: Optional[float] = None
    # Namespace
    namespace: Optional[str] = None
    # Pod name
    pod_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PodCheckpointCpu:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PodCheckpointCpu
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PodCheckpointCpu()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "checkpoint_count": lambda n : setattr(self, 'checkpoint_count', n.get_int_value()),
            "checkpoint_timestamp": lambda n : setattr(self, 'checkpoint_timestamp', n.get_str_value()),
            "cpu_at_checkpoint": lambda n : setattr(self, 'cpu_at_checkpoint', n.get_float_value()),
            "gpu_memory_used_mib": lambda n : setattr(self, 'gpu_memory_used_mib', n.get_float_value()),
            "gpu_model": lambda n : setattr(self, 'gpu_model', n.get_str_value()),
            "gpu_utilization_at_checkpoint": lambda n : setattr(self, 'gpu_utilization_at_checkpoint', n.get_float_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "pod_name": lambda n : setattr(self, 'pod_name', n.get_str_value()),
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
        writer.write_int_value("checkpoint_count", self.checkpoint_count)
        writer.write_str_value("checkpoint_timestamp", self.checkpoint_timestamp)
        writer.write_float_value("cpu_at_checkpoint", self.cpu_at_checkpoint)
        writer.write_float_value("gpu_memory_used_mib", self.gpu_memory_used_mib)
        writer.write_str_value("gpu_model", self.gpu_model)
        writer.write_float_value("gpu_utilization_at_checkpoint", self.gpu_utilization_at_checkpoint)
        writer.write_str_value("namespace", self.namespace)
        writer.write_str_value("pod_name", self.pod_name)
        writer.write_additional_data_value(self.additional_data)
    

