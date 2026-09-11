from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PodStartupTime(AdditionalDataHolder, Parsable):
    """
    Startup time for a single worker pod.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether this pod was started via a Cedana restore (true) or cold-started (false)
    cedana_restore: Optional[bool] = None
    # Pod name
    pod_name: Optional[str] = None
    # Time from PodScheduled → Ready in milliseconds
    start_time_ms: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PodStartupTime:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PodStartupTime
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PodStartupTime()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "cedana_restore": lambda n : setattr(self, 'cedana_restore', n.get_bool_value()),
            "pod_name": lambda n : setattr(self, 'pod_name', n.get_str_value()),
            "start_time_ms": lambda n : setattr(self, 'start_time_ms', n.get_int_value()),
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
        writer.write_bool_value("cedana_restore", self.cedana_restore)
        writer.write_str_value("pod_name", self.pod_name)
        writer.write_int_value("start_time_ms", self.start_time_ms)
        writer.write_additional_data_value(self.additional_data)
    

