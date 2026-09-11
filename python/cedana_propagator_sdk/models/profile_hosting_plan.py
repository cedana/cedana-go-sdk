from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .checkpoint_request_view import CheckpointRequestView

@dataclass
class ProfileHostingPlan(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The checkpoint_owner property
    checkpoint_owner: Optional[str] = None
    # The checkpoint_request property
    checkpoint_request: Optional[CheckpointRequestView] = None
    # The compatibility_key property
    compatibility_key: Optional[str] = None
    # The cpu_fixture property
    cpu_fixture: Optional[bool] = None
    # The hosting_mode property
    hosting_mode: Optional[str] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The profile_revision property
    profile_revision: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProfileHostingPlan:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProfileHostingPlan
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProfileHostingPlan()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .checkpoint_request_view import CheckpointRequestView

        from .checkpoint_request_view import CheckpointRequestView

        fields: dict[str, Callable[[Any], None]] = {
            "checkpoint_owner": lambda n : setattr(self, 'checkpoint_owner', n.get_str_value()),
            "checkpoint_request": lambda n : setattr(self, 'checkpoint_request', n.get_object_value(CheckpointRequestView)),
            "compatibility_key": lambda n : setattr(self, 'compatibility_key', n.get_str_value()),
            "cpu_fixture": lambda n : setattr(self, 'cpu_fixture', n.get_bool_value()),
            "hosting_mode": lambda n : setattr(self, 'hosting_mode', n.get_str_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "profile_revision": lambda n : setattr(self, 'profile_revision', n.get_str_value()),
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
        writer.write_str_value("checkpoint_owner", self.checkpoint_owner)
        writer.write_object_value("checkpoint_request", self.checkpoint_request)
        writer.write_str_value("compatibility_key", self.compatibility_key)
        writer.write_bool_value("cpu_fixture", self.cpu_fixture)
        writer.write_str_value("hosting_mode", self.hosting_mode)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_str_value("profile_revision", self.profile_revision)
        writer.write_additional_data_value(self.additional_data)
    

