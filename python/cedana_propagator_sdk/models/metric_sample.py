from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MetricSample(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The metric_name property
    metric_name: Optional[str] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The route property
    route: Optional[str] = None
    # The timestamp property
    timestamp: Optional[int] = None
    # The value property
    value: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MetricSample:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MetricSample
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MetricSample()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "metric_name": lambda n : setattr(self, 'metric_name', n.get_str_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "route": lambda n : setattr(self, 'route', n.get_str_value()),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_int_value()),
            "value": lambda n : setattr(self, 'value', n.get_float_value()),
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
        writer.write_str_value("metric_name", self.metric_name)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_str_value("route", self.route)
        writer.write_int_value("timestamp", self.timestamp)
        writer.write_float_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

