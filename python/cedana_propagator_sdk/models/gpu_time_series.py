from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .gpu_time_series_point import GpuTimeSeriesPoint

@dataclass
class GpuTimeSeries(AdditionalDataHolder, Parsable):
    """
    Time-series data for a single GPU
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The data property
    data: Optional[list[GpuTimeSeriesPoint]] = None
    # The gpu_index property
    gpu_index: Optional[str] = None
    # The gpu_uuid property
    gpu_uuid: Optional[str] = None
    # The model_name property
    model_name: Optional[str] = None
    # The node_name property
    node_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GpuTimeSeries:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GpuTimeSeries
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GpuTimeSeries()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .gpu_time_series_point import GpuTimeSeriesPoint

        from .gpu_time_series_point import GpuTimeSeriesPoint

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_collection_of_object_values(GpuTimeSeriesPoint)),
            "gpu_index": lambda n : setattr(self, 'gpu_index', n.get_str_value()),
            "gpu_uuid": lambda n : setattr(self, 'gpu_uuid', n.get_str_value()),
            "model_name": lambda n : setattr(self, 'model_name', n.get_str_value()),
            "node_name": lambda n : setattr(self, 'node_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("data", self.data)
        writer.write_str_value("gpu_index", self.gpu_index)
        writer.write_str_value("gpu_uuid", self.gpu_uuid)
        writer.write_str_value("model_name", self.model_name)
        writer.write_str_value("node_name", self.node_name)
        writer.write_additional_data_value(self.additional_data)
    

