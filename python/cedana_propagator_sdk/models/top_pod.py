from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TopPod(AdditionalDataHolder, Parsable):
    """
    Top pods by resource usage
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cpu_usage_seconds property
    cpu_usage_seconds: Optional[float] = None
    # The memory_bytes property
    memory_bytes: Optional[float] = None
    # The namespace property
    namespace: Optional[str] = None
    # The node_name property
    node_name: Optional[str] = None
    # The pod_name property
    pod_name: Optional[str] = None
    # The pod_uid property
    pod_uid: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TopPod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TopPod
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TopPod()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "cpu_usage_seconds": lambda n : setattr(self, 'cpu_usage_seconds', n.get_float_value()),
            "memory_bytes": lambda n : setattr(self, 'memory_bytes', n.get_float_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "node_name": lambda n : setattr(self, 'node_name', n.get_str_value()),
            "pod_name": lambda n : setattr(self, 'pod_name', n.get_str_value()),
            "pod_uid": lambda n : setattr(self, 'pod_uid', n.get_str_value()),
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
        writer.write_float_value("cpu_usage_seconds", self.cpu_usage_seconds)
        writer.write_float_value("memory_bytes", self.memory_bytes)
        writer.write_str_value("namespace", self.namespace)
        writer.write_str_value("node_name", self.node_name)
        writer.write_str_value("pod_name", self.pod_name)
        writer.write_str_value("pod_uid", self.pod_uid)
        writer.write_additional_data_value(self.additional_data)
    

