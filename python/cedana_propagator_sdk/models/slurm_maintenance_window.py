from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SlurmMaintenanceWindow(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The end_time property
    end_time: Optional[datetime.datetime] = None
    # The id property
    id: Optional[str] = None
    # The nodes property
    nodes: Optional[list[str]] = None
    # The partitions property
    partitions: Optional[list[str]] = None
    # The reason property
    reason: Optional[str] = None
    # The start_time property
    start_time: Optional[datetime.datetime] = None
    # The status property
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SlurmMaintenanceWindow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SlurmMaintenanceWindow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SlurmMaintenanceWindow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "end_time": lambda n : setattr(self, 'end_time', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "nodes": lambda n : setattr(self, 'nodes', n.get_collection_of_primitive_values(str)),
            "partitions": lambda n : setattr(self, 'partitions', n.get_collection_of_primitive_values(str)),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "start_time": lambda n : setattr(self, 'start_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_datetime_value("end_time", self.end_time)
        writer.write_str_value("id", self.id)
        writer.write_collection_of_primitive_values("nodes", self.nodes)
        writer.write_collection_of_primitive_values("partitions", self.partitions)
        writer.write_str_value("reason", self.reason)
        writer.write_datetime_value("start_time", self.start_time)
        writer.write_str_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

