from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class InstanceTypeConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The gpu_type property
    gpu_type: Optional[str] = None
    # The interconnect property
    interconnect: Optional[str] = None
    # The memory_in_gb property
    memory_in_gb: Optional[int] = None
    # The num_gpus property
    num_gpus: Optional[int] = None
    # The nvlink property
    nvlink: Optional[bool] = None
    # The os_options property
    os_options: Optional[list[str]] = None
    # The storage_in_gb property
    storage_in_gb: Optional[int] = None
    # The vcpus property
    vcpus: Optional[int] = None
    # The vram_per_gpu_in_gb property
    vram_per_gpu_in_gb: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InstanceTypeConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InstanceTypeConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InstanceTypeConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "gpu_type": lambda n : setattr(self, 'gpu_type', n.get_str_value()),
            "interconnect": lambda n : setattr(self, 'interconnect', n.get_str_value()),
            "memory_in_gb": lambda n : setattr(self, 'memory_in_gb', n.get_int_value()),
            "num_gpus": lambda n : setattr(self, 'num_gpus', n.get_int_value()),
            "nvlink": lambda n : setattr(self, 'nvlink', n.get_bool_value()),
            "os_options": lambda n : setattr(self, 'os_options', n.get_collection_of_primitive_values(str)),
            "storage_in_gb": lambda n : setattr(self, 'storage_in_gb', n.get_int_value()),
            "vcpus": lambda n : setattr(self, 'vcpus', n.get_int_value()),
            "vram_per_gpu_in_gb": lambda n : setattr(self, 'vram_per_gpu_in_gb', n.get_int_value()),
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
        writer.write_str_value("gpu_type", self.gpu_type)
        writer.write_str_value("interconnect", self.interconnect)
        writer.write_int_value("memory_in_gb", self.memory_in_gb)
        writer.write_int_value("num_gpus", self.num_gpus)
        writer.write_bool_value("nvlink", self.nvlink)
        writer.write_collection_of_primitive_values("os_options", self.os_options)
        writer.write_int_value("storage_in_gb", self.storage_in_gb)
        writer.write_int_value("vcpus", self.vcpus)
        writer.write_int_value("vram_per_gpu_in_gb", self.vram_per_gpu_in_gb)
        writer.write_additional_data_value(self.additional_data)
    

