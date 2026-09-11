from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_checkpoint_info import PolicyCheckpointInfo

@dataclass
class PolicyActivityResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The failed_checkpoints property
    failed_checkpoints: Optional[int] = None
    # The last_checkpoint_at property
    last_checkpoint_at: Optional[str] = None
    # The policy_id property
    policy_id: Optional[str] = None
    # The recent_checkpoints property
    recent_checkpoints: Optional[list[PolicyCheckpointInfo]] = None
    # The successful_checkpoints property
    successful_checkpoints: Optional[int] = None
    # The total_checkpoints property
    total_checkpoints: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyActivityResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyActivityResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyActivityResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policy_checkpoint_info import PolicyCheckpointInfo

        from .policy_checkpoint_info import PolicyCheckpointInfo

        fields: dict[str, Callable[[Any], None]] = {
            "failed_checkpoints": lambda n : setattr(self, 'failed_checkpoints', n.get_int_value()),
            "last_checkpoint_at": lambda n : setattr(self, 'last_checkpoint_at', n.get_str_value()),
            "policy_id": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "recent_checkpoints": lambda n : setattr(self, 'recent_checkpoints', n.get_collection_of_object_values(PolicyCheckpointInfo)),
            "successful_checkpoints": lambda n : setattr(self, 'successful_checkpoints', n.get_int_value()),
            "total_checkpoints": lambda n : setattr(self, 'total_checkpoints', n.get_int_value()),
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
        writer.write_int_value("failed_checkpoints", self.failed_checkpoints)
        writer.write_str_value("last_checkpoint_at", self.last_checkpoint_at)
        writer.write_str_value("policy_id", self.policy_id)
        writer.write_collection_of_object_values("recent_checkpoints", self.recent_checkpoints)
        writer.write_int_value("successful_checkpoints", self.successful_checkpoints)
        writer.write_int_value("total_checkpoints", self.total_checkpoints)
        writer.write_additional_data_value(self.additional_data)
    

