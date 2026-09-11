from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .time_series_data_point import TimeSeriesDataPoint

@dataclass
class MemoryTimeSeries(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The allocated_memory property
    allocated_memory: Optional[list[TimeSeriesDataPoint]] = None
    # The free_memory property
    free_memory: Optional[list[TimeSeriesDataPoint]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemoryTimeSeries:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemoryTimeSeries
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemoryTimeSeries()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .time_series_data_point import TimeSeriesDataPoint

        from .time_series_data_point import TimeSeriesDataPoint

        fields: dict[str, Callable[[Any], None]] = {
            "allocated_memory": lambda n : setattr(self, 'allocated_memory', n.get_collection_of_object_values(TimeSeriesDataPoint)),
            "free_memory": lambda n : setattr(self, 'free_memory', n.get_collection_of_object_values(TimeSeriesDataPoint)),
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
        writer.write_collection_of_object_values("allocated_memory", self.allocated_memory)
        writer.write_collection_of_object_values("free_memory", self.free_memory)
        writer.write_additional_data_value(self.additional_data)
    

