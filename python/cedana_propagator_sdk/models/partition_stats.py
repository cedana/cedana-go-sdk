from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PartitionStats(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cpu_load property
    cpu_load: Optional[float] = None
    # The free_memory property
    free_memory: Optional[float] = None
    # The idle_cpus property
    idle_cpus: Optional[float] = None
    # The idle_nodes property
    idle_nodes: Optional[float] = None
    # The partition_name property
    partition_name: Optional[str] = None
    # The real_memory property
    real_memory: Optional[float] = None
    # The timestamp property
    timestamp: Optional[int] = None
    # The total_cpus property
    total_cpus: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PartitionStats:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PartitionStats
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PartitionStats()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "cpu_load": lambda n : setattr(self, 'cpu_load', n.get_float_value()),
            "free_memory": lambda n : setattr(self, 'free_memory', n.get_float_value()),
            "idle_cpus": lambda n : setattr(self, 'idle_cpus', n.get_float_value()),
            "idle_nodes": lambda n : setattr(self, 'idle_nodes', n.get_float_value()),
            "partition_name": lambda n : setattr(self, 'partition_name', n.get_str_value()),
            "real_memory": lambda n : setattr(self, 'real_memory', n.get_float_value()),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_int_value()),
            "total_cpus": lambda n : setattr(self, 'total_cpus', n.get_float_value()),
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
        writer.write_float_value("free_memory", self.free_memory)
        writer.write_float_value("idle_cpus", self.idle_cpus)
        writer.write_float_value("idle_nodes", self.idle_nodes)
        writer.write_str_value("partition_name", self.partition_name)
        writer.write_float_value("real_memory", self.real_memory)
        writer.write_int_value("timestamp", self.timestamp)
        writer.write_float_value("total_cpus", self.total_cpus)
        writer.write_additional_data_value(self.additional_data)
    

