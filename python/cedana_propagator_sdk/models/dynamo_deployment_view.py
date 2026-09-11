from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dynamo_deployment import DynamoDeployment

from .dynamo_deployment import DynamoDeployment

@dataclass
class DynamoDeploymentView(DynamoDeployment, Parsable):
    """
    Combined view returned by the list endpoint
    """
    # CEDANA_CHECKPOINT name of the first worker service, if checkpointing isenabled. This is the stable key a worker restores from. None if unset.
    checkpoint_name: Optional[str] = None
    # Resolved frontend endpoint: external_ip:port or cluster_ip:port
    frontend_endpoint: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DynamoDeploymentView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DynamoDeploymentView
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DynamoDeploymentView()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dynamo_deployment import DynamoDeployment

        from .dynamo_deployment import DynamoDeployment

        fields: dict[str, Callable[[Any], None]] = {
            "checkpoint_name": lambda n : setattr(self, 'checkpoint_name', n.get_str_value()),
            "frontend_endpoint": lambda n : setattr(self, 'frontend_endpoint', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("checkpoint_name", self.checkpoint_name)
        writer.write_str_value("frontend_endpoint", self.frontend_endpoint)
    

