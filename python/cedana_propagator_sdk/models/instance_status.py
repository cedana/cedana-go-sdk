from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class InstanceStatus(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The created_at property
    created_at: Optional[str] = None
    # The instance_id property
    instance_id: Optional[str] = None
    # The ip_address property
    ip_address: Optional[str] = None
    # The ssh_port property
    ssh_port: Optional[int] = None
    # The ssh_user property
    ssh_user: Optional[str] = None
    # The status property
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InstanceStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InstanceStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InstanceStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "created_at": lambda n : setattr(self, 'created_at', n.get_str_value()),
            "instance_id": lambda n : setattr(self, 'instance_id', n.get_str_value()),
            "ip_address": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "ssh_port": lambda n : setattr(self, 'ssh_port', n.get_int_value()),
            "ssh_user": lambda n : setattr(self, 'ssh_user', n.get_str_value()),
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
        writer.write_str_value("created_at", self.created_at)
        writer.write_str_value("instance_id", self.instance_id)
        writer.write_str_value("ip_address", self.ip_address)
        writer.write_int_value("ssh_port", self.ssh_port)
        writer.write_str_value("ssh_user", self.ssh_user)
        writer.write_str_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

