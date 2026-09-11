from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class NodeMetricItem(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The collector property
    collector: Optional[str] = None
    # The cpu_core property
    cpu_core: Optional[str] = None
    # The cpu_mode property
    cpu_mode: Optional[str] = None
    # The filesystem property
    filesystem: Optional[str] = None
    # The metric_name property
    metric_name: Optional[str] = None
    # The mountpoint property
    mountpoint: Optional[str] = None
    # The resource property
    resource: Optional[str] = None
    # The timestamp property
    timestamp: Optional[str] = None
    # The value property
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NodeMetricItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NodeMetricItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NodeMetricItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "collector": lambda n : setattr(self, 'collector', n.get_str_value()),
            "cpu_core": lambda n : setattr(self, 'cpu_core', n.get_str_value()),
            "cpu_mode": lambda n : setattr(self, 'cpu_mode', n.get_str_value()),
            "filesystem": lambda n : setattr(self, 'filesystem', n.get_str_value()),
            "metric_name": lambda n : setattr(self, 'metric_name', n.get_str_value()),
            "mountpoint": lambda n : setattr(self, 'mountpoint', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_str_value()),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_str_value("collector", self.collector)
        writer.write_str_value("cpu_core", self.cpu_core)
        writer.write_str_value("cpu_mode", self.cpu_mode)
        writer.write_str_value("filesystem", self.filesystem)
        writer.write_str_value("metric_name", self.metric_name)
        writer.write_str_value("mountpoint", self.mountpoint)
        writer.write_str_value("resource", self.resource)
        writer.write_str_value("timestamp", self.timestamp)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

