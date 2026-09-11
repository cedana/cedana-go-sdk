from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SlurmClusterOverview(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cpu_load property
    cpu_load: Optional[float] = None
    # The cpus_idle property
    cpus_idle: Optional[float] = None
    # The cpus_total property
    cpus_total: Optional[float] = None
    # The mem_alloc property
    mem_alloc: Optional[float] = None
    # The mem_free property
    mem_free: Optional[float] = None
    # The mem_real property
    mem_real: Optional[float] = None
    # The timestamp property
    timestamp: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SlurmClusterOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SlurmClusterOverview
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SlurmClusterOverview()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "cpu_load": lambda n : setattr(self, 'cpu_load', n.get_float_value()),
            "cpus_idle": lambda n : setattr(self, 'cpus_idle', n.get_float_value()),
            "cpus_total": lambda n : setattr(self, 'cpus_total', n.get_float_value()),
            "mem_alloc": lambda n : setattr(self, 'mem_alloc', n.get_float_value()),
            "mem_free": lambda n : setattr(self, 'mem_free', n.get_float_value()),
            "mem_real": lambda n : setattr(self, 'mem_real', n.get_float_value()),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_int_value()),
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
        writer.write_float_value("cpu_load", self.cpu_load)
        writer.write_float_value("cpus_idle", self.cpus_idle)
        writer.write_float_value("cpus_total", self.cpus_total)
        writer.write_float_value("mem_alloc", self.mem_alloc)
        writer.write_float_value("mem_free", self.mem_free)
        writer.write_float_value("mem_real", self.mem_real)
        writer.write_int_value("timestamp", self.timestamp)
        writer.write_additional_data_value(self.additional_data)
    

