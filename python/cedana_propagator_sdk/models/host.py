from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .host_cpu import HostCpu
    from .host_memory import HostMemory

@dataclass
class Host(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The CPU property
    c_p_u: Optional[HostCpu] = None
    # The Hostname property
    hostname: Optional[str] = None
    # The ID property
    i_d: Optional[str] = None
    # The KernelArch property
    kernel_arch: Optional[str] = None
    # The KernelVersion property
    kernel_version: Optional[str] = None
    # The MAC property
    m_a_c: Optional[str] = None
    # The Memory property
    memory: Optional[HostMemory] = None
    # The OS property
    o_s: Optional[str] = None
    # The Platform property
    platform: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Host:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Host
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Host()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .host_cpu import HostCpu
        from .host_memory import HostMemory

        from .host_cpu import HostCpu
        from .host_memory import HostMemory

        fields: dict[str, Callable[[Any], None]] = {
            "CPU": lambda n : setattr(self, 'c_p_u', n.get_object_value(HostCpu)),
            "Hostname": lambda n : setattr(self, 'hostname', n.get_str_value()),
            "ID": lambda n : setattr(self, 'i_d', n.get_str_value()),
            "KernelArch": lambda n : setattr(self, 'kernel_arch', n.get_str_value()),
            "KernelVersion": lambda n : setattr(self, 'kernel_version', n.get_str_value()),
            "MAC": lambda n : setattr(self, 'm_a_c', n.get_str_value()),
            "Memory": lambda n : setattr(self, 'memory', n.get_object_value(HostMemory)),
            "OS": lambda n : setattr(self, 'o_s', n.get_str_value()),
            "Platform": lambda n : setattr(self, 'platform', n.get_str_value()),
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
        writer.write_object_value("CPU", self.c_p_u)
        writer.write_str_value("Hostname", self.hostname)
        writer.write_str_value("ID", self.i_d)
        writer.write_str_value("KernelArch", self.kernel_arch)
        writer.write_str_value("KernelVersion", self.kernel_version)
        writer.write_str_value("MAC", self.m_a_c)
        writer.write_object_value("Memory", self.memory)
        writer.write_str_value("OS", self.o_s)
        writer.write_str_value("Platform", self.platform)
        writer.write_additional_data_value(self.additional_data)
    

